"""
Temporary Email Helper for test automation framework
Provides functionality to create temporary email accounts and retrieve messages
Uses mail.tm API for temporary email generation
"""
import requests
import time
from utils.logger import Logger


class TempEmailHelper:
    """Helper class for managing temporary email accounts during testing"""
    
    BASE_URL = "https://api.mail.tm"
    
    def __init__(self):
        """Initialize TempEmailHelper with logger"""
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.email = None
        self.password = None
        self.headers = None
        
    def create_account(self, password="StrongPass123!"):
        """
        Create a new temporary email account
        
        Args:
            password (str): Password for the email account (default: StrongPass123!)
            
        Returns:
            tuple: (email, password)
            
        Raises:
            Exception: If account creation fails
        """
        try:
            self.logger.info("Creating temporary email account")
            
            # Get available domain
            domain_response = requests.get(f"{self.BASE_URL}/domains")
            domain_response.raise_for_status()
            domain = domain_response.json()["hydra:member"][0]["domain"]
            
            # Generate unique email
            email = f"Automation{int(time.time())}@{domain}"
            self.password = password
            
            # Create account
            account_response = requests.post(
                f"{self.BASE_URL}/accounts",
                json={"address": email, "password": password}
            )
            account_response.raise_for_status()
            
            self.email = email
            self.logger.info(f"Successfully created temporary email: {email}")
            return email, password
            
        except Exception as e:
            self.logger.error(f"Failed to create temporary email account. Error: {str(e)}")
            raise
    
    def get_token(self, email=None, password=None):
        """
        Get authentication token for email account
        
        Args:
            email (str): Email address (uses instance email if not provided)
            password (str): Password (uses instance password if not provided)
            
        Returns:
            dict: Authorization headers with bearer token
            
        Raises:
            Exception: If token generation fails
        """
        try:
            email = email or self.email
            password = password or self.password
            
            if not email or not password:
                raise ValueError("Email and password are required")
            
            self.logger.debug(f"Generating authentication token for: {email}")
            
            response = requests.post(
                f"{self.BASE_URL}/token",
                json={"address": email, "password": password}
            )
            response.raise_for_status()
            
            token = response.json()["token"]
            self.headers = {"Authorization": f"Bearer {token}"}
            
            self.logger.debug("Authentication token generated successfully")
            return self.headers
            
        except Exception as e:
            self.logger.error(f"Failed to generate authentication token. Error: {str(e)}")
            raise
    
    def get_messages(self, headers=None):
        """
        Retrieve all messages from the mailbox
        
        Args:
            headers (dict): Authorization headers (uses instance headers if not provided)
            
        Returns:
            list: List of message objects
            
        Raises:
            Exception: If message retrieval fails
        """
        try:
            headers = headers or self.headers
            
            if not headers:
                raise ValueError("Authorization headers are required")
            
            self.logger.debug("Retrieving messages from mailbox")
            
            response = requests.get(f"{self.BASE_URL}/messages", headers=headers)
            response.raise_for_status()
            
            messages = response.json().get("hydra:member", [])
            self.logger.debug(f"Retrieved {len(messages)} message(s)")
            
            return messages
            
        except Exception as e:
            self.logger.error(f"Failed to retrieve messages. Error: {str(e)}")
            raise
    
    def read_message(self, msg_id, headers=None):
        """
        Read a specific message by ID
        
        Args:
            msg_id (str): Message ID
            headers (dict): Authorization headers (uses instance headers if not provided)
            
        Returns:
            dict: Message details including from, subject, text, html
            
        Raises:
            Exception: If message reading fails
        """
        try:
            headers = headers or self.headers
            
            if not headers:
                raise ValueError("Authorization headers are required")
            
            self.logger.debug(f"Reading message with ID: {msg_id}")
            
            response = requests.get(f"{self.BASE_URL}/messages/{msg_id}", headers=headers)
            response.raise_for_status()
            
            message = response.json()
            self.logger.info(f"Successfully read message: {message.get('subject', 'No Subject')}")
            
            return message
            
        except Exception as e:
            self.logger.error(f"Failed to read message {msg_id}. Error: {str(e)}")
            raise
    
    def wait_for_email(self, timeout=30, poll_interval=2, subject_filter=None):
        """
        Wait for email to arrive in mailbox
        
        Args:
            timeout (int): Maximum time to wait in seconds (default: 60)
            poll_interval (int): Time between checks in seconds (default: 2)
            subject_filter (str): Optional subject filter to match specific email
            
        Returns:
            dict: First matching message details or None if timeout
            
        Raises:
            Exception: If email waiting fails
        """
        try:
            self.logger.info(f"Waiting for email (timeout: {timeout}s, interval: {poll_interval}s)")
            
            if subject_filter:
                self.logger.info(f"Filtering by subject: {subject_filter}")
            
            start_time = time.time()
            attempts = 0
            
            while time.time() - start_time < timeout:
                attempts += 1
                self.logger.debug(f"Checking for emails (attempt {attempts})")
                
                messages = self.get_messages()
                
                if messages:
                    # Read the first message (or filtered message)
                    for msg in messages:
                        message_details = self.read_message(msg["id"])
                        
                        # If subject filter is provided, check for match
                        if subject_filter:
                            if subject_filter.lower() in message_details.get("subject", "").lower():
                                self.logger.info("Email received and matched subject filter")
                                return message_details
                        else:
                            self.logger.info("Email received")
                            return message_details
                
                time.sleep(poll_interval)
            
            self.logger.warning(f"No email received within {timeout}s timeout")
            return None
            
        except Exception as e:
            self.logger.error(f"Failed while waiting for email. Error: {str(e)}")
            raise
    
    def setup_mailbox(self, password="StrongPass123!"):
        """
        Complete setup: Create account and get token
        
        Args:
            password (str): Password for the email account
            
        Returns:
            str: Email address
            
        Raises:
            Exception: If mailbox setup fails
        """
        try:
            self.logger.info("Setting up temporary mailbox")
            
            email, pwd = self.create_account(password)
            self.get_token(email, pwd)
            
            self.logger.info(f"Mailbox setup complete: {email}")
            return email
            
        except Exception as e:
            self.logger.error(f"Failed to setup mailbox. Error: {str(e)}")
            raise
    
    def delete_account(self):
        """
        Delete the temporary email account
        
        Returns:
            bool: True if deletion successful, False otherwise
        """
        try:
            if not self.headers or not self.email:
                self.logger.warning("No active account to delete")
                return False
            
            self.logger.info(f"Deleting temporary email account: {self.email}")
            
            # Get account ID
            response = requests.get(f"{self.BASE_URL}/accounts", headers=self.headers)
            response.raise_for_status()
            
            # Delete account
            delete_response = requests.delete(
                f"{self.BASE_URL}/accounts/{response.json()['id']}",
                headers=self.headers
            )
            delete_response.raise_for_status()
            
            self.logger.info("Email account deleted successfully")
            self.email = None
            self.password = None
            self.headers = None
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to delete email account. Error: {str(e)}")
            return False