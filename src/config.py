from dataclasses import dataclass


@dataclass
class Config(object):
    # crawler
    ip: str = ''