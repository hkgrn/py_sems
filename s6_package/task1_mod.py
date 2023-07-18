import sys

__all__ = ['date_validate']

_LEAP = 4
_END_DAY = 31
_START_DAY = 1
_END_MONTH = 12
_START_MONTH = 1
_END_YEAR = 9999
_START_YEAR = 1


def date_validate(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    return ((_END_DAY >= day >= _START_DAY) and
            (_END_MONTH >= month >= _START_MONTH) and
            (_END_YEAR >= year >= _START_YEAR))


def _is_leap_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % _LEAP == 0:
        return True
    return False

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error")
        sys.exit(1)

    date = sys.argv[1]
    print(date_validate(date))