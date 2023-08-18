from dataclasses import dataclass
import yaml


@dataclass
class DatabaseConfig:
    user: str
    password: str
    host: str
    port: int
    db_name: str


@dataclass
class Config:
    database: DatabaseConfig = None


def setup_config(config_path: str):
    with open(config_path, 'r') as file:
        raw_config = yaml.safe_load(file)

    return Config(
        database=DatabaseConfig(
            user=raw_config['database']['user'],
            password=raw_config['database']['password'],
            host=raw_config['database']['host'],
            port=raw_config['database']['port'],
            db_name=raw_config['database']['db'],
        ),
    )


config = setup_config('testask/config.yaml')


