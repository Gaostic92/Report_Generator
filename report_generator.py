from core import file_manager as fm
from datetime import datetime
from datetime import date


def main():
    month = int(input("Enter month: "))
    folder_id = input("Enter Drive folder id: ")
    now = datetime.now()
    # d = datetime.date(now.year, month, 1)
    start_date = date(now.year, month, 1)
    fm.import_files(start_date, folder_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
