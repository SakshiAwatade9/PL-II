days=int(input("Enter the days: "))
years=days//365
weeks=(days%365)//7
remaining_days=days % 7
print("Years= ",years)
print("Weeks= ",weeks)
print("Remaining days= ", remaining_days)