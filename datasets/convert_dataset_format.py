import pandas as pd

# List of dataset files
datasets = ["Jazz_dataset.txt", "hamster_dataset.txt", "euroroad_dataset.txt","Blogs_dataset.txt"]  # Add your file names here

# Process each dataset
for file in datasets:
    df = pd.read_csv(file, delim_whitespace=True)
    df.columns = ["Source", "Target"]
    
    # Generate output filename based on input file
    output_file = file.replace(".txt", ".csv")
    df.to_csv(output_file, index=False)

