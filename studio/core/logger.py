from datetime import datetime


class Logger:

    @staticmethod
    def _time():

        return datetime.now().strftime(
            "%H:%M:%S"
        )

    @staticmethod
    def info(message):

        print(
            f"[{Logger._time()}] [INFO] {message}"
        )

    @staticmethod
    def success(message):

        print(
            f"[{Logger._time()}] [SUCCESS] {message}"
        )

    @staticmethod
    def warning(message):

        print(
            f"[{Logger._time()}] [WARNING] {message}"
        )

    @staticmethod
    def error(message):

        print(
            f"[{Logger._time()}] [ERROR] {message}"
        )