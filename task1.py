MINUTES_PER_HOUR = 60
total_minutes = int(input("Enter the number of minutes: "))
hours = total_minutes // MINUTES_PER_HOUR
remaining_minutes = total_minutes % MINUTES_PER_HOUR
print(f"{total_minutes} minutes are equal to {hours} hours and {remaining_minutes} minutes.")