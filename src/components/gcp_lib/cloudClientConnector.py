from components.logger import Log
from google.cloud import storage
import os
from abc import ABC, abstractmethod


log_instance = Log()
log = log_instance.logger()

class CloudClient(ABC):
    @abstractmethod
    def get_client(self):
        pass

class CloudStorageClient(CloudClient):
    def __init__(self):
        self.client = None

    def connect(self):
        try:
            self.client = storage.Client()
            log.info("GCS Client connected!")

        except Exception as e:
            log.error(f"Error connecting to storage client: {e}")

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client









