# WARNING LAST UPDATE TWO YEAR AGO
import pendulum

def main() -> None:

    print('')
    print('SOME DATE')
    some_date = pendulum.datetime(2022,10,9,18,0,tz="UTC") # UTC is deafult
    print(some_date)
    print(some_date.in_timezone('Australia/Sydney'))

    print('')
    print('MY DATE')
    my_date = pendulum.datetime(2013, 3, 31, 1, 59, 59, 999999, tz='Europe/Paris')
    print(my_date)
    my_date = my_date.add(microseconds=1)
    print(my_date)
    my_date = my_date.subtract(microseconds=1)
    print(my_date)

    print('')
    print('Localization')
    pendulum.set_locale('pl')
    print(some_date.format('dddd DD MMMM YYYY', locale="en"))
    print(some_date.format('LT', locale="de")) # LOCALIZE FORMAT
    print(some_date.format('LT', locale="en"))

    print('')
    print('Time diff for human')
    print(pendulum.now().add(years=1).diff_for_humans(locale='en'))
    print(pendulum.now().add(years=1).diff_for_humans(locale='pl'))
    print(pendulum.now().add(years=1).diff_for_humans(absolute=True, locale='pl')) #ABSOLUTE

    print('')
    print('Some functions')
    print(pendulum.now().day_of_year)
    print(pendulum.now().day_of_week)
    print(pendulum.now().int_timestamp)
    print(pendulum.now().float_timestamp)
    print(pendulum.now().start_of('day'))
    print(pendulum.now().end_of('day'))

    print('')
    print('Duration')
    duration = pendulum.duration(years=3, months=3)
    print(duration.days)


if __name__ == '__main__':
    main()