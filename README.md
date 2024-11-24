# 590016738 SUPRIT SRIVASTAVA MCA

#  SCREENSHOT OF OUTPUT 
![image](https://github.com/user-attachments/assets/27315404-eaff-4dad-b81b-4c7f6e60b8da)

## Requirements:
### Tools and Language:
- *Python 3.x*
- *Pandas*: Library for data manipulation and CSV file handling.
- *Matplotlib*: Used for creating the histogram and visualizing the data.

## Functions Used in the Code:

### 1. pd.read_csv()
- *Purpose*: Reads the CSV file containing sales data into a Pandas DataFrame.
- *Parameters*: 
  - file_path: The location of the CSV file.
  - delimiter=';': Specifies that the data in the CSV file is separated by semicolons.
  - usecols=["Month", "Sales"]: Ensures only the "Month" and "Sales" columns are read.

### 2. pd.to_numeric()
- *Purpose*: Converts the values in the "Sales" column to numeric values.
- *Parameters*: 
  - errors='coerce': If there are invalid or non-numeric values in the column, they are replaced with NaN.

### 3. data.dropna()
- *Purpose*: Removes rows with missing values (NaN) from the DataFrame.

### 4. plt.hist()
- *Purpose*: Plots a histogram using the sales data.
- *Parameters*:
  - data["Sales"]: The numeric sales data to plot.
  - bins=20: The number of bins (intervals) in the histogram.
  - color='blue': The color of the bars in the histogram.
  - edgecolor='black': The color of the borders around the bars.
  - alpha=0.7: Transparency level of the bars.

### 5. plt.title(), plt.xlabel(), plt.ylabel()
- *Purpose*: Customize the title and labels for the x and y axes.

### 6. plt.grid()
- *Purpose*: Adds a grid to the plot to make it easier to read.

### 7. plt.tight_layout()
- *Purpose*: Adjusts the layout to ensure everything fits within the figure area.

### 8. plt.show()
- *Purpose*: Displays the plot in a window.

### 9. Statistical Insights Calculation:
- *Mean*: data["Sales"].mean() calculates the average sales value.
- *Median*: data["Sales"].median() computes the middle value of the sales data.
- *Standard Deviation*: data["Sales"].std() calculates the spread of sales around the mean.
