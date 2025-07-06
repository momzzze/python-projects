import logging

logging.basicConfig(
    level=logging.INFO,
    format='--------\n%(asctime)s - %(levelname)s - %(message)s\n--------',
)

def login():
    logging.info("🔐 Login function called")

def register():
    logging.info("🔐 Register function called")