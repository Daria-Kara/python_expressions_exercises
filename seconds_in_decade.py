#Count Seconds in a Decade
#A Python program to calculate the number of seconds in 10 years. Assume that we have 2 leap years in this period. 
#Assign the result into a variable named seconds_in_10_years.

normal_year_days = 365
leap_year_days = 366

normal_years = 8
leap_years = 2

seconds_per_day = 24 * 60 * 60

seconds_in_10_years = (
    (normal_years * normal_year_days + leap_years * leap_year_days)
    * seconds_per_day
)

seconds_in_10_years
