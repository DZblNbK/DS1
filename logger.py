import logging

def setup_logger(name, log_file, level=logging.DEBUG):
    """Настройка логгера."""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Создание обработчика для записи в файл
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Создание логгера
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger