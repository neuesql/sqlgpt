import torch
from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co


class OraclePostgresqlDataSet(Dataset):

    def __init__(self, dataframe, tokenizer, source_len, label_len):
        self.tokenizer = tokenizer
        self.data = dataframe
        self.source_len = source_len
        self.label_len = label_len
        self.sentence = self.data.sentence
        self.label = self.data.label

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index) -> T_co:
        sentence = ' '.join(self.data.sentence[index].split())
        label = ' '.join(self.data.label[index].split(","))

        source = self.tokenizer.batch_encode_plus([sentence],
                                                  max_length=self.source_len,
                                                  pad_to_max_length=True,
                                                  return_tensors='pt')
        target = self.tokenizer.batch_encode_plus([label],
                                                  max_length=self.label_len,
                                                  pad_to_max_length=True,
                                                  return_tensors='pt')

        source_ids = source['input_ids'].squeeze()
        source_mask = source['attention_mask'].squeeze()
        target_ids = target['input_ids'].squeeze()
        target_mask = target['attention_mask'].squeeze()

        return {
            'source_ids': source_ids.to(dtype=torch.long),
            'source_mask': source_mask.to(dtype=torch.long),
            'target_ids': target_ids.to(dtype=torch.long),
            'target_ids_y': target_ids.to(dtype=torch.long)
        }
