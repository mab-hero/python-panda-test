import time
import pandas as pd
import numpy as np
#here we just name the extrnel files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
   lklm
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    

    city = input("enter a city 'chicago', 'new york city', 'washington'\n")
    while ( city not in ['chicago', 'new york city', 'washington']):
        print("enter a valid city value \n")
        city = input("enter a city 'chicago', 'new york city', 'washington'\n")

    month = input("enter a month \n")
    while ( month not in ['all', 'january', 'february','March','April','May','June','July','August ','September','October','November','December']):
        print("enter a valid month value \n")
        month = input("enter a month \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter a day \n")
    while ( day not in ['all', 'monday', 'tuesday','sunday','Wednesday','Saturday','Friday','Thursday']):
        print("enter a valid m  onth value \n")
        day = input("enter a day \n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the spmnecified city and filters by month and day if applicable.

    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['day'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    popular_month = df['month'].mode()[0]
    print("most month\n {} \n".format(popular_month))

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print("most day ")
    print( popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("most hour\n {} \n".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    df['Start'] = df['Start Station']
    rate = df['Start'].mode()[0]
    print("commonly used start station \n")
    print(rate)


    # display most commonly used end station
    df['End'] = df['End Station']
    End_rate = df['End'].mode()[0]
    print("commonly used end station \n")
    print(End_rate)

    # display most frequent combination of start station and end station trip
    df['common'] = df['Start Station'] + df['End Station']
    common = df['common'].mode()[0]
    print("commonly used start station and end station \n")
    print(common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df["Trip Duration"].sum()
    print("the total travel time \n")
    print(total)

    # display mean travel time
    mean = df["Trip Duration"].mean()
    print("the mean for travel time \n")
    print(mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Display counts of user types \n {} \n".format(user_type))

    # Display counts of gender
    if 'Gender' in df:
     user_gender = df['Gender'].value_counts()
     print("Display counts of user types \n ")
     print(user_gender)
    else:
     print("no gender \n")
    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df:
     earliest = df['Birth Year'].min()
     most_recent = df['Birth Year'].max()
     common_year = df['Birth Year'].mode()[0]

     print("earliest year of birth \n {} \n".format(earliest))
     print("most recent year of birth \n {} \n".format(most_recent))
     print("common year of birth \n {} \n".format(common_year))
    else:
     print("no Birth Year \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        data_raw = input("would you like the raw data? enter yes \n").strip().lower()
        start = 0
        end = 5
        while data_raw == "yes":
            print(df.iloc[start:end])
            start = start + 5
            end = end + 5
            data_raw = input("see more enter yes")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
