import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler('file.log')
handler.setLevel(logging.ERROR)

error_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(error_format)

logger.addHandler(handler)

