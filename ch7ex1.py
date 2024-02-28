seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
month = int(input("Enter the month number between 1 to 12: "))
season = seasons[(month % 12) // 3]
print("The season for month is:" + season)