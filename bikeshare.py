import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('What is the name of the city?').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('What is the month, or type "all" for all the months?').lower()
    # If the user inputs a numeric value, it gets converted to the name of the month
    int_months = {
        '1':'january', '2':'Febuary', '3':'march', '4':'april', '5':'may', '6':'june'}
    if month in int_months:
        month = int_months[month]

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What is the day of week? or type "all" for all the days of the week?').lower()
    print('-'*40)
    print(city, month, day)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months_list = ['januar', 'febuary', 'march', 'april','may','june','july','augest','september','october','november','december']
        month = months_list.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_com_month = df['month'].mode()[0]
    print('The most common month is ', most_com_month)
    # TO DO: display the most common day of week
    most_com_day = df['day'].mode()[0]
    print('The most common day is ', most_com_day)
    # TO DO: display the most common start hour
    most_com_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is ', most_com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_com_st_station = df['Start Station'].mode()[0]
    print('The most common Start Station is ', most_com_st_station)

    # TO DO: display most commonly used end station
    most_com_en_station = df['End Station'].mode()[0]
    print('The most common End Station is ', most_com_en_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_com_comb_stations = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print(most_com_comb_stations)
    print('The most common combination of start station and end station trip is ', most_com_comb_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time
    total_travel_time = (df['End Time'] - df['Start Time']).sum()
    print('The total travel time is ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = (df['End Time'] - df['Start Time']).mean()
    print('The mean travel time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_type = df['User Type'].value_counts()
    print('There are {} {} and {} {} '.format(counts_of_user_type[0],counts_of_user_type.index[0],counts_of_user_type[1],counts_of_user_type.index[1]))

    # TO DO: Display counts of gender
    try:
        counts_of_user_gender = df['Gender'].value_counts()
        print('There are {} {} users and {} {} users'.format(counts_of_user_gender[0],counts_of_user_gender.index[0],counts_of_user_gender[1],counts_of_user_gender.index[1] ))
    except:
        print('There is no data about gender for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print('The earliest year of birth is ', earliest_year_of_birth)
        print('The most recent year of birth is ', most_recent_year_of_birth)
        print('The most common year of birth is ', most_common_year_of_birth)
    except:
        print('There is no data for the year of birth for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display 5 lines of the row data
def display_raw_data(df):
    while True:
        raw_data= input('Would you like to see 5 lines of the raw data? Enter yes or no.\n').lower()
        if raw_data == 'yes':
            print(df.head())
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
