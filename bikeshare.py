'''
Explore US Bikeshare Data Project by Sai Abhiroop Tanjavuru
'''

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Would you like to see data for chicago, new york city, or washington? \n').lower()

    while True:
        if city not in ['chicago', 'new york city', 'washington']:
            city = input('Invalid input! Please enter chicago, new york, or washington \n').lower()
            continue
        else:
            break


    # get user input for month (all, january, february, ... , june)
    
    month = input('Data for which month? january, february, march, april, may, june, or all? \n').lower()

    while True:
        if month not in ['all', 'january', 'february', 'march', 'april', 'june', 'all']:
            month = input('Invalid input! Please enter january, february, march, april, may, june, or all \n').lower()
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('Data for which day? monday, tuesday, wednesday, thursday, friday, saturday, sunday, all \n').lower()

    while True:
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input('Invalid input! Please enter monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all \n').lower()
            continue
        else:
            break


    print('-'*40)
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

    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month the create the new dataframe
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """
    
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('\nMost common day of week: ', most_common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nMost common start hour: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station: ', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station: ', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Frequent Combination'] = df['Start Station'] + " " + df['End Station']
    most_frequent_combination = df['Frequent Combination'].mode()[0]
    print('\nMost frequent combination of start station and end station trip: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    
    Displays statistics on the total and average trip duration.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time is: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types: \n', user_types)


    if city == 'chicago' or city == 'new york city':
         # Display counts of gender
         genders = df['Gender'].value_counts()
         print('\nCounts of gender: \n', genders)

         # Display earliest, most recent, and most common year of birth
         earliest_year_of_birth = df['Birth Year'].min()
         print('\nEarliest year of birth: ', earliest_year_of_birth)

         most_recent_year_of_birth = df['Birth Year'].max()
         print('\nMost recent year of birth: ', most_recent_year_of_birth)

         most_common_year_of_birth = df['Birth Year'].mode()[0]
         print('\nMost common year of birth: ', most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_raw_data(df):
    """Displays raw data 5 rows at a time"""
    print(df.head())
    nextRows = 0

    while True:
        see_more_raw_data = input('\nWould you like to see 5 more rows of the data? Yes or No\n').lower()
        if see_more_raw_data != 'yes':
            return
        nextRows = nextRows + 5
        print(df.iloc[nextRows:nextRows+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        while True:
            see_more_raw_data = input('\nWould you like to see the raw data? Yes or No\n').lower()
            if see_more_raw_data != 'yes':
                break
            see_raw_data(df)
            break
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
