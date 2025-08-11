import time
import logging

def retry_on_exception(func, retries=3, delay=2, logger=None):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if logger:
                    logger.warning(f"Attempt {attempts+1} failed: {e}")
                attempts += 1
                time.sleep(delay)
        raise Exception(f"Failed after {retries} retries")
    return wrapper
