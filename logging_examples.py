import logging
import logging.config


def all_logging_level_message():
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


def assign_logging_level():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(msg='This will get logged')


def logging_to_file():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')


def format_logging():
    # add process id
    # logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    # logging.warning('This is a Warning')
    # add date
    # logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # logging.info('Admin logged in')
    # add formatted date
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('Admin logged out')


def logging_var():
    name = 'John'
    logging.error(f'{name} raised an error')


def capture_stack_trace():
    a = 5
    b = 0

    try:
        c = a / b
    except Exception as e:
        # logging.error("Exception occurred", exc_info=True)
        logging.exception(msg="Exception occurred")


def create_logger():
    logger = logging.getLogger(__name__)
    logger.warning('This is a warning')


def create_logger_handler():
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')


def get_logger_config_by_file():
    logging.config.fileConfig(fname='logging.ini', disable_existing_loggers=False)

    # Get the logger specified in the file
    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('appLogger')

    logger.debug('This is a debug message')
    logger.warning('This is a warning message')


def main():
    get_logger_config_by_file()


if __name__ == '__main__':
    main()
