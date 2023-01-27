import hydra
from loguru import logger
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="config", config_name="training")
def sql_app(cfg: DictConfig) -> None:
    logger.info(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    sql_app()
