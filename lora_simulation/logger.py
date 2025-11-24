import logging

logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s [%(levelname)s] %(message)s"
)

default_logger = logging.getLogger("lora-sim")