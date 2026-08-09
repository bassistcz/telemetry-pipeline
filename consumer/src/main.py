from consumer import run
from persistence import initialise_database


def main():
    initialise_database()
    run()


if __name__ == "__main__":
    main()