from consumer.src.consumer import run
from consumer.src.persistence import initialise_database
from config.logging_config import configure_logging

def main():
    configure_logging("consumer")
    initialise_database()
    run()


if __name__ == "__main__":
    main()