import pandas as pd
import matplotlib.pyplot as plt

print("stealb9443")

data = { 'Ballroom':['Ballroom 1', 'Ballroom 2', 'Ballroom 3'], 'Capacity': [25000, 11000, 5000]}

df = pd.DataFrame(data)

print("\nBallroom Capacities:")
print(df)

df.plot( x='Ballroom', y='Capacity', kind='bar', title='Ballroom Capacity')

plt.ylabel("Number of People")
plt.show()

attendanceData = { "Attendees" : [18000, 13000, 10000]}
attendanceDF = pd.DataFrame(attendanceData, index=["Children", "Adults", "Teenagers"])
attendanceDF.plot.pie( y="Attendees")

plt.ylabel("")
plt.show()
