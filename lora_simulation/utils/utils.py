from ..models import Config, State
import math

def lora_log(command: str, cfg: Config | State) -> str:
  return  command + ";" + ",".join(f"{k}={v}" for k, v in cfg.items())
  

def chunks_count(payload_size: int, implicit_header: bool = False,  header_size: int = 200):
  chunkSize = header_size if implicit_header else 200
  return math.ceil(payload_size / chunkSize)