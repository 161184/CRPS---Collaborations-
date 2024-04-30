#segmenting the string of coordinates from the csv files into bins of 30 seconds and getting their mean. writing these means into one big csv file. 
#also: the traces are upside down, so this code corrects this


import matplotlib.pyplot as plt
import statistics 
import os
import csv
import math
import re


input_folder = '/Users/rk354/Desktop/CRPS_TET_P01_all_means30sec_flippedcorrrectly_,.csv'

import matplotlib.pyplot as plt
import statistics 
import os
import csv
import math
import re


input_folder = '/Users/rk354/Desktop/CRPS_TET_P01_all_means30sec_flippedcorrrectly_,.csv'
output = r"/Users/rk453/DesktopCRPS_predpain_attentiontask_p01jatos.csv"

#the time points that I predefined to get the bins within
points= [228, 279, 330, 381, 430, 483, 534, 585, 636, 687, 735]

# Get all CSV files in the input folder, but in the correct order!
files = sorted([f for f in os.listdir(input_folder) if f.endswith('.csv')], key=lambda x: int(x.split('session')[1].split('.')[0]))

titles = []
#creating a list, that will contain all the data from all the files I'm looping through (each) to then write this into one huge csv file after the loop
alldocsallmeans = []


# Loop through all CSV files and read all their arrays and create means per bin
for file_name in files:
    # Check if file is labeled as rejected
    if "REJECTED" in file_name:
        base_name = os.path.splitext(file_name)[0]
        titles.append(base_name)
        # Extract the actual dimension from the file name for rejected files
        labels = base_name.split('_')
        condition = labels[1]
        dimension = labels[2]
        # The dimension is preserved, and "REJECTED" is only placed in the first bin column
        alldocsallmeans.append(["REJECTED"] + [None] * (len(points)-2))
        continue
    else:
        titles.append(os.path.splitext(file_name)[0])

    with open(os.path.join(input_folder, file_name), mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        
        # Initialize empty lists for x and y coordinates
        x_coordinates = []
        y_coordinates = []

        # Skip the header if there is one
        # next(reader, None)  # Uncomment this line if your CSV files have headers

        # Loop through each row in the csv file
        for row in reader:
            # Append the x value to the x_coordinates list and convert it to float
            x_coordinates.append(float(row[0]))
            # Append the y value to the y_coordinates list and convert it to float
            y_coordinates.append(float(row[1]))

        #now we correct the traces. first the value -42 to floor it and then flip the x around (negative) and then plus 313 to make it positive again. Background: the picture has a coordinate system. there the y=0 is actually around 46 and the top value is around 351. I gave it a bit of space unter the y=0 and over the max y value, in case participants drew over the line a bit.  
        flipped_y = [313-(x-42) for x in y_coordinates]

        # Initialize a list to count the number of y values in each bin

        bin1 = []
        bin2 = []
        bin3 = []
        bin4 = []
        bin5 = []
        bin6 = []
        bin7 = []
        bin8 = []
        bin9 = []
        bin10 = []

        index = 0
        # Assign each y value to a bin
        for y in flipped_y:
            x = x_coordinates[index]
            if x >= points[0] and x < points[1]:
                bin1.append(y)
            elif x >= points[1] and x < points[2]:
                bin2.append(y)   
            elif x >= points[2] and x < points[3]:
                bin3.append(y)   
            elif x >= points[3] and x < points[4]:
                bin4.append(y)   
            elif x >= points[4] and x < points[5]:
                bin5.append(y)   
            elif x >= points[5] and x < points[6]:
                bin6.append(y)   
            elif x >= points[6] and x < points[7]:
                bin7.append(y)   
            elif x >= points[7] and x < points[8]:
                bin8.append(y)   
            elif x >= points[8] and x < points[9]:
                bin9.append(y)
            elif x >= points[9] and x <= points[10]:
                bin10.append(y)
            index = index+1

        # Calculate means for bins with a check to handle empty bins
        meanbin1 = math.ceil(statistics.mean(bin1)) if bin1 else None
        meanbin2 = math.ceil(statistics.mean(bin2)) if bin2 else None
        meanbin3 = math.ceil(statistics.mean(bin3)) if bin3 else None
        meanbin4 = math.ceil(statistics.mean(bin4)) if bin4 else None
        meanbin5 = math.ceil(statistics.mean(bin5)) if bin5 else None
        meanbin6 = math.ceil(statistics.mean(bin6)) if bin6 else None
        meanbin7 = math.ceil(statistics.mean(bin7)) if bin7 else None
        meanbin8 = math.ceil(statistics.mean(bin8)) if bin8 else None
        meanbin9 = math.ceil(statistics.mean(bin9)) if bin9 else None
        meanbin10 = math.ceil(statistics.mean(bin10)) if bin10 else None


        #append list of all means per csv
        allmeans30sec = [meanbin1, meanbin2, meanbin3, meanbin4, meanbin5, meanbin6, meanbin7, meanbin8, meanbin9, meanbin10]
        alldocsallmeans.append(allmeans30sec)


# Prepare the column headers with the first one being a label for bin numbers
# and the rest being the titles from the titles list
bin_labels = [f"Bin {i+1}" for i in range(len(points)-1)]

# Write the data to a CSV file with column and row headings
with open(output, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    # Write the column headers
    csv_writer.writerow(["Titles"] + ["Session"] +["Condition"] +["Dimension"] + bin_labels)
    # Write each row with a bin label as the first entry
    for index, means in enumerate(alldocsallmeans):
        if index < len(titles):  # Check if the index is within the range of titles

        #separate each label for Session, Condition and Dimension and apply them to the csv
            current_title = titles[index]
            labels = current_title.split('_')
            condition = labels[1]
            dimension = labels[2]
            # Extract the session number using a regular expression
            session_match = re.search(r'session(\d+)', labels[0])
            if session_match:
                session_number = session_match.group(1)  # Extracted session number
            else:
                session_number = "Unknown"  # Handle cases where the session number is not found

            csv_writer.writerow([current_title] + [session_number] + [condition] + [dimension] + means)
        else:
            print(f"No title for index {index}.") #just making sure there are no issues with the data


"""
session3.txt_heartbeat_bodyperception
labels = current_title.split('_')
session_name = current_title[:8]
if current_title[:9] is not ".":
    session_name = current_title[:8,9]
else: session_name = current_title[:8]
"""

#testing
"""
print(len(bin10))

# Assuming the bins are defined as before
for i in range(1, 11):
    print(f"bin{i}: {len(eval(f'bin{i}'))}")

print(len(y_coordinates))
#print(y_coordinates)
print("this is", x)

print("mean", meanbin10)
"""


#plot the x and y coordinates
"""
# Create a plot
plt.figure(figsize=(10, 6))  # Optional: Specifies the figure size
plt.plot(x_coordinates, y_coordinates, marker='o', linestyle='-', color='b')  # Plot x and y using blue line and circle markers

plt.title('Plot of X and Y Coordinates')  # Set the title of the plot
plt.xlabel('X Coordinates')  # Set the x-axis label
plt.ylabel('Y Coordinates')  # Set the y-axis label
plt.grid(True)  # Show grid lines

# Optionally, you can add this line to ensure that the aspect ratio is equal, 
# making the scale of x to y 1:1, which is especially useful for spatial data.
plt.axis('equal')

# Display the plot
plt.show()
""""

#the time points that I predefined to get the bins within
points= [228, 279, 330, 381, 430, 483, 534, 585, 636, 687, 735]

# Get all CSV files in the input folder, but in the correct order!
files = sorted([f for f in os.listdir(input_folder) if f.endswith('.csv')], key=lambda x: int(x.split('session')[1].split('.')[0]))

titles = []
#creating a list, that will contain all the data from all the files I'm looping through (each) to then write this into one huge csv file after the loop
alldocsallmeans = []


# Loop through all CSV files and read all their arrays and create means per bin
for file_name in files:
    # Check if file is labeled as rejected
    if "REJECTED" in file_name:
        base_name = os.path.splitext(file_name)[0]
        titles.append(base_name)
        # Extract the actual dimension from the file name for rejected files
        labels = base_name.split('_')
        condition = labels[1]
        dimension = labels[2]
        # The dimension is preserved, and "REJECTED" is only placed in the first bin column
        alldocsallmeans.append(["REJECTED"] + [None] * (len(points)-2))
        continue
    else:
        titles.append(os.path.splitext(file_name)[0])

    with open(os.path.join(input_folder, file_name), mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        
        # Initialize empty lists for x and y coordinates
        x_coordinates = []
        y_coordinates = []

        # Skip the header if there is one
        # next(reader, None)  # Uncomment this line if your CSV files have headers

        # Loop through each row in the csv file
        for row in reader:
            # Append the x value to the x_coordinates list and convert it to float
            x_coordinates.append(float(row[0]))
            # Append the y value to the y_coordinates list and convert it to float
            y_coordinates.append(float(row[1]))

        #now we correct the traces. first the value -42 to floor it and then flip the x around (negative) and then plus 313 to make it positive again. Background: the picture has a coordinate system. there the y=0 is actually around 46 and the top value is around 351. I gave it a bit of space unter the y=0 and over the max y value, in case participants drew over the line a bit.  
        flipped_y = [313-(x-42) for x in y_coordinates]

        # Initialize a list to count the number of y values in each bin

        bin1 = []
        bin2 = []
        bin3 = []
        bin4 = []
        bin5 = []
        bin6 = []
        bin7 = []
        bin8 = []
        bin9 = []
        bin10 = []

        index = 0
        # Assign each y value to a bin
        for y in flipped_y:
            x = x_coordinates[index]
            if x >= points[0] and x < points[1]:
                bin1.append(y)
            elif x >= points[1] and x < points[2]:
                bin2.append(y)   
            elif x >= points[2] and x < points[3]:
                bin3.append(y)   
            elif x >= points[3] and x < points[4]:
                bin4.append(y)   
            elif x >= points[4] and x < points[5]:
                bin5.append(y)   
            elif x >= points[5] and x < points[6]:
                bin6.append(y)   
            elif x >= points[6] and x < points[7]:
                bin7.append(y)   
            elif x >= points[7] and x < points[8]:
                bin8.append(y)   
            elif x >= points[8] and x < points[9]:
                bin9.append(y)
            elif x >= points[9] and x <= points[10]:
                bin10.append(y)
            index = index+1

        # Calculate means for bins with a check to handle empty bins
        meanbin1 = math.ceil(statistics.mean(bin1)) if bin1 else None
        meanbin2 = math.ceil(statistics.mean(bin2)) if bin2 else None
        meanbin3 = math.ceil(statistics.mean(bin3)) if bin3 else None
        meanbin4 = math.ceil(statistics.mean(bin4)) if bin4 else None
        meanbin5 = math.ceil(statistics.mean(bin5)) if bin5 else None
        meanbin6 = math.ceil(statistics.mean(bin6)) if bin6 else None
        meanbin7 = math.ceil(statistics.mean(bin7)) if bin7 else None
        meanbin8 = math.ceil(statistics.mean(bin8)) if bin8 else None
        meanbin9 = math.ceil(statistics.mean(bin9)) if bin9 else None
        meanbin10 = math.ceil(statistics.mean(bin10)) if bin10 else None


        #append list of all means per csv
        allmeans30sec = [meanbin1, meanbin2, meanbin3, meanbin4, meanbin5, meanbin6, meanbin7, meanbin8, meanbin9, meanbin10]
        alldocsallmeans.append(allmeans30sec)


# Prepare the column headers with the first one being a label for bin numbers
# and the rest being the titles from the titles list
bin_labels = [f"Bin {i+1}" for i in range(len(points)-1)]

# Write the data to a CSV file with column and row headings
with open(output, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    # Write the column headers
    csv_writer.writerow(["Titles"] + ["Session"] +["Condition"] +["Dimension"] + bin_labels)
    # Write each row with a bin label as the first entry
    for index, means in enumerate(alldocsallmeans):
        if index < len(titles):  # Check if the index is within the range of titles

        #separate each label for Session, Condition and Dimension and apply them to the csv
            current_title = titles[index]
            labels = current_title.split('_')
            condition = labels[1]
            dimension = labels[2]
            # Extract the session number using a regular expression
            session_match = re.search(r'session(\d+)', labels[0])
            if session_match:
                session_number = session_match.group(1)  # Extracted session number
            else:
                session_number = "Unknown"  # Handle cases where the session number is not found

            csv_writer.writerow([current_title] + [session_number] + [condition] + [dimension] + means)
        else:
            print(f"No title for index {index}.") #just making sure there are no issues with the data

