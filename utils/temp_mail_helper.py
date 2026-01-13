from mailtm import Email
from utils.logger import Logger
import time
import re

class TempMailHelper:
    def __init__(self):
        self.email = Email()
        self.email_address = None
        self.email_message = None
        self.email_domain = None
        self.logger = Logger.get_logger(__name__)

    def create_email_account(self):
        try:
            self.logger.info("Creating email account")
            self.email.register()
            self.email_address = self.email.address
            self.email_domain = self.email.domain
            self.logger.info(f"Email account created successfully: {self.email_address}")
            return self.email_address
        except Exception as e:
            self.logger.error(f"Failed to create email account. Error: {str(e)}")
            raise

    

    def listener(self, message):
        try:
            self.logger.info(f"New email received: {message['subject']}")

            content = message["text"] or message["html"]
            self.logger.info(f"Content: {content}")

            token = self.extract_token(content)
            if token:
                self.email_message = token
                self.email.stop()
                return
            self.logger.warning("Token not found in email")

        except Exception as e:
            self.logger.error(f"Failed to listen for email. Error: {str(e)}")
            self.email.stop()
            raise


    
    def wait_for_email(self, timeout=120):
        self.logger.info("Waiting for email...")
        self.email.start(self.listener)

        start = time.time()
        while self.email_message is None:
            if time.time() - start > timeout or self.email_message is not None:
                self.email.stop()
                raise TimeoutError("Email not received within timeout duration")
            time.sleep(1)

        return self.email_message

    def extract_token(self, email_content: str) -> str | None:
        match = re.search(r"token=([A-Za-z0-9_-]+)", email_content)
        return match.group(1) if match else None