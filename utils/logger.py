"""
Logging utility for test automation framework
Provides centralized logging configuration with file and console handlers
"""
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler


class Logger:
    """Custom logger class for test automation framework"""
    
    _loggers = {}
    
    @staticmethod
    def get_logger(name=None, log_level=logging.INFO):
        """
        Get or create a logger instance
        
        Args:
            name (str): Logger name (typically __name__ from calling module)
            log_level: Logging level (default: INFO)
            
        Returns:
            logging.Logger: Configured logger instance
        """
        if name is None:
            name = "TestFramework"
            
        # Return existing logger if already created
        if name in Logger._loggers:
            return Logger._loggers[name]
        
        # Create new logger
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        logger.propagate = False
        
        # Avoid duplicate handlers
        if logger.handlers:
            return logger
        
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Create log file with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(log_dir, f"test_execution_{timestamp}.log")
        
        # File handler with rotation (10MB max, keep 5 backups)
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,  # 10 MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        simple_formatter = logging.Formatter(
            fmt='%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%H:%M:%S'
        )
        
        # Set formatters
        file_handler.setFormatter(detailed_formatter)
        console_handler.setFormatter(simple_formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Cache logger
        Logger._loggers[name] = logger
        
        return logger
    
    @staticmethod
    def create_test_logger(test_name):
        """
        Create a dedicated logger for a specific test
        
        Args:
            test_name (str): Name of the test
            
        Returns:
            logging.Logger: Test-specific logger
        """
        return Logger.get_logger(f"Test.{test_name}")
    
    @staticmethod
    def log_test_start(logger, test_name):
        """Log the start of a test"""
        logger.info("=" * 100)
        logger.info(f"TEST STARTED: {test_name}")
        logger.info("=" * 100)
    
    @staticmethod
    def log_test_end(logger, test_name, status="PASSED"):
        """Log the end of a test"""
        logger.info("=" * 100)
        logger.info(f"TEST {status}: {test_name}")
        logger.info("=" * 100)
    
    @staticmethod
    def log_step(logger, step_description):
        """Log a test step"""
        logger.info(f"STEP: {step_description}")
    
    @staticmethod
    def cleanup_old_logs(days=7):
        """
        Remove log files older than specified days
        
        Args:
            days (int): Number of days to keep logs
        """
        import time
        
        log_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(log_dir):
            return
        
        now = time.time()
        for filename in os.listdir(log_dir):
            filepath = os.path.join(log_dir, filename)
            if os.path.isfile(filepath):
                # Check if file is older than specified days
                if os.stat(filepath).st_mtime < now - days * 86400:
                    try:
                        os.remove(filepath)
                        print(f"Deleted old log file: {filename}")
                    except Exception as e:
                        print(f"Error deleting {filename}: {e}")


# Convenience function for quick logger access
def get_logger(name=None):
    """Get logger instance - convenience function"""
    return Logger.get_logger(name)

