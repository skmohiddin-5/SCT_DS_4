import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("US_Accidents_March23.csv", nrows=100000)

print("Dataset Shape:")
print(data.shape)

print("\nFirst 5 Rows:")
print(data.head())

print("\nMissing Values:")
print(data.isnull().sum())

data['Start_Time'] = pd.to_datetime(data['Start_Time'])

data['Hour'] = data['Start_Time'].dt.hour

plt.figure(figsize=(10,5))
data['Hour'].value_counts().sort_index().plot(kind='bar')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

plt.figure(figsize=(12,5))
data['Weather_Condition'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Weather Conditions")
plt.xlabel("Weather Condition")
plt.ylabel("Accident Count")
plt.show()


plt.figure(figsize=(12,5))
data['State'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 States by Accident Count")
plt.xlabel("State")
plt.ylabel("Number of Accidents")
plt.show()


plt.figure(figsize=(10,6))
plt.scatter(
    data['Start_Lng'],
    data['Start_Lat'],
    s=1
)

plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


print("\nPROJECT INSIGHTS")
print("- Peak accident hours can be identified from the hourly graph.")
print("- Certain weather conditions contribute more accidents.")
print("- Some states experience significantly more accidents.")
print("- Hotspot visualization shows regions with dense accident activity.")