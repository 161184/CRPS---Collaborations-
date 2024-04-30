import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy 
from scipy import stats
import seaborn as sns

# Path to CSV file
csv_file_path = '/Users/rk354/Desktop_CRPS_TET_P01_all_means30sec_flippedcorrrectly_,.csv'


# Read the CSV file, treating 'REJECTED' as NaN
df = pd.read_csv(csv_file_path, na_values=['REJECTED'], skip_blank_lines=True)

# Check the columns to ensure they are as expected
#print(df.columns)
# check certain fields       
#print(df.iloc[2, 2])


######PLOT all the variables of pain intensity and emotionbad over sessions/ conditions. 


##### DESCRIPTIVE VISUAL OVERVIEW
# Initialize an empty list to store the values
values_emotiongood = []
values_emotionbad = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotionbad':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotionbad.extend(row.iloc[4:14].tolist())

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotiongood':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotiongood.extend(row.iloc[4:14].tolist())

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(values_emotionbad, marker='o', linestyle='-')
plt.title('Values Extracted from Rows Containing "emotionbad"')
plt.xlabel('Order')
plt.ylabel('Values')
plt.grid(True)
#plt.show()

#now lets plot  
# Setting the style of seaborn for better aesthetics
sns.set(style="whitegrid")

# Creating histograms
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(values_emotiongood, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Pleasant Emotion')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(values_emotionbad, bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram of Unpleasant Emotion')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
#plt.show()
# Creating boxplots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.boxplot(y=values_emotiongood, color='lightblue')
plt.title('Boxplot of Pleasant Emotion')
plt.ylabel('Value')

plt.subplot(1, 2, 2)
sns.boxplot(y=values_emotionbad, color='lightgreen')
plt.title('Boxplot of Unpleasant Emotion')
plt.ylabel('Value')

plt.tight_layout()
#plt.show()




######Splitting descriptives into parts: 
######DESCRIPTIVE central (median, mean, mode)

"""
#central tendency 
print('emotiongood median =', statistics.median(values_emotiongood))
print('emotionbad median =', statistics.median(values_emotionbad))

print('emotiongood mean =', statistics.mean(values_emotiongood))
print('emotionbad mean =', statistics.mean(values_emotionbad))

print('emotiongood mode =', statistics.mode(values_emotiongood))
print('emotionbad mode =', statistics.mode(values_emotionbad))


#variability (range, interquartile range, variance, standard deviation)
print('emotiongood range =', numpy.ptp(values_emotiongood))
print('emotionbad range =', numpy.ptp(values_emotionbad))

print('emotiongood interquartile range =', stats.iqr(values_emotiongood))
print('emotionbad interquartile range =', stats.iqr(values_emotionbad))

print('emotiongood variance =', numpy.var(values_emotiongood))
print('emotionbad variance =', numpy.var(values_emotionbad))

print('emotiongood standard deviation =', numpy.std(values_emotiongood))
print('emotionbad standard deviation =', numpy.std(values_emotionbad))
"""

"""
###Insight into distribution of values 

emotiongood_series = pd.Series(values_emotiongood)
emotionbad_series = pd.Series(values_emotionbad)


print("print(emotiongood_series.describe()")
print(emotiongood_series.describe())

print("print(emotionbad_series.describe()")
print(emotionbad_series.describe())

#histogram emotionbad
plt.figure(figsize=(10,6))
sns.histplot(emotionbad_series, kde=True)
plt.title('Distribution of emotionbad')
plt.xlabel('Value')
plt.ylabel('Frequency')
#plt.show()

#histogram emotiongood
plt.figure(figsize=(10,6))
sns.histplot(emotionbad_series, kde=True)
plt.title('Distribution of emotionbad')
plt.xlabel('Value')
plt.ylabel('Frequency')
#plt.show()

#box plot emotionbad
plt.figure(figsize=(8,4))
sns.boxplot(x=emotionbad_series)
plt.title('Box Plot for emotionbad')
plt.show

#box plot emotiongood
plt.figure(figsize=(8,4))
sns.boxplot(x=emotiongood_series)
plt.title('Box Plot for emotiongood')
plt.show

"""
#######################
##  PER CONDITION





##### DESCRIPTIVE VISUAL OVERVIEW
#BREATH
values_emotiongood_breath = []
values_emotionbad_breath = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotionbad' and row[2]== 'breathing':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotionbad_breath.extend(row.iloc[4:14].tolist())

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotiongood' and row[2]== 'breathing':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotiongood_breath.extend(row.iloc[4:14].tolist())


#HEART
values_emotiongood_heart = []
values_emotionbad_heart = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotionbad' and row[2]== 'heartbeat':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotionbad_heart.extend(row.iloc[4:14].tolist())

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotiongood' and row[2]== 'heartbeat':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotiongood_heart.extend(row.iloc[4:14].tolist())

#Painfoc
values_emotiongood_painfoc = []
values_emotionbad_painfoc = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotionbad' and row[2]== 'pain':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotionbad_painfoc.extend(row.iloc[4:14].tolist())

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotiongood' and row[2]== 'pain':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotiongood_painfoc.extend(row.iloc[4:14].tolist())


#non-Painfoc
values_emotiongood_nonpainfoc = []
values_emotionbad_nonpainfoc = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotionbad' and row[2]== 'nonpain':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotionbad_nonpainfoc.extend(row.iloc[4:14].tolist())

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if 'emotiongood' is the value in the 'Dimension' column
    if row[3] == 'emotiongood' and row[2]== 'nonpain':
        # Add the values from Bin 1 to Bin 10 to the list (columns 4 to 13 in zero-based index)
        values_emotiongood_nonpainfoc.extend(row.iloc[4:14].tolist())
