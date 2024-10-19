def determine_specific_percentile(age, length, data): 
    # Extract relevant data for the given age
    row = data[data["Month"] == age].iloc[0]
    
    # List of percentile labels
    labels = ["0.1st", "1st", "3rd", "5th", "10th", "15th", "25th", "50th", "75th", "85th", "90th", "95th", "97th", "99th", "99.9th"]
    
    # Determine specific percentile
    for i in range(len(labels) - 1):
        if row[labels[i]] <= length <= row[labels[i+1]]:
            return labels[i+1]
    return "Below 0.1st" if length < row["0.1st"] else "Above 99.9th"