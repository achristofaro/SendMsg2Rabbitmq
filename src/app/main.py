import logging

from .dependencies import get_process_logs_use_case


def main():
    process_logs_use_case = get_process_logs_use_case()

    try:
        process_logs_use_case.execute()
    except Exception as e:
        logging.error(f"An error occurred while processing logs: {e}")
    finally:
        process_logs_use_case.close()


if __name__ == "__main__":
    main()
