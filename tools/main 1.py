# Get input for hours, minutes, and seconds
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert hours, minutes, and seconds to total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

# Display the result
print(f"{hours} hours, {minutes} minutes, and {seconds} seconds is equal to {total_seconds} seconds.")

