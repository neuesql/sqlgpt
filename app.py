import torch
from metaflow import FlowSpec, step


class TrainingFlow(FlowSpec):

    @step
    def start(self):
        print("Start building model job")
        self.next(self.preparing)

    @step
    def end(self):
        print("End building job")

    @step
    def preparing(self):
        self.next(self.training)

    @step
    def training(self):
        self.next(self.validation)

    @step
    def validation(self):
        self.next(self.end)

    def train_process(self, epoch, tokenizer, model, device, loader, optimizer):
        model.train()
        for _, data in enumerate(loader, 0):
            y = data['target_ids'].to(device, dtype=torch.long)
            ids = data['source_ids'].to(device, dtype=torch.long)
            mask = data['source_mask'].to(device, dtype=torch.long)

            outputs = model(input_ids=ids, attention_mask=mask, labels=y)
            loss = outputs[0]

            if _ % 500 == 0:
                print(f'Epoch: {epoch}, Loss:  {loss.item()}')

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    def validate_process(self, epoch, tokenizer, model, device, loader):
        model.eval()
        predictions = []
        actuals = []
        with torch.no_grad():
            for _, data in enumerate(loader, 0):
                y = data['target_ids'].to(device, dtype=torch.long)
                ids = data['source_ids'].to(device, dtype=torch.long)
                mask = data['source_mask'].to(device, dtype=torch.long)

                generated_ids = model.generate(
                    input_ids=ids,
                    attention_mask=mask,
                    max_length=150,
                    num_beams=2,
                    repetition_penalty=2.5,
                    length_penalty=1.0,
                    early_stopping=True
                )
                preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in
                         generated_ids]
                target = [tokenizer.decode(t, skip_special_tokens=True, clean_up_tokenization_spaces=True) for t in y]
                if _ % 100 == 0:
                    print(f'Completed {_}')

                predictions.extend(preds)
                actuals.extend(target)
        return predictions, actuals


if __name__ == "__main__":
    flow = TrainingFlow()
