# Time Complexity Analyzer

This Python program analyzes the time complexity of any given function by measuring its execution time across various input sizes. It provides insights into how the function's performance scales with input size.

## Features

- Measures execution time for any function.
- Analyzes performance over increasing input sizes.
- Outputs results that help estimate time complexity.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required libraries:
   ```bash
   pip install numpy matplotlib
   ```
## Usage
1. Define the function you want to analyze within the script.
2. Run the program:
   ```bash
   python time_complexity_analyzer.py
   ```

   #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Indian Cities Fetcher

This Python program retrieves a list of all cities in India using an API and saves the data into a `.csv` file. It utilizes the `requests` library to fetch data from a suitable API.

## Features

- Fetches a comprehensive list of cities in India.
- Saves the data in a `.csv` file for easy access and analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required library:
   ```bash
   pip install requests pandas
   ```

2. The list of cities will be saved in a file named `indian_cities.csv`.

#------------------------------------------------------------------------------------------------------------------------------------------------#
# Wikipedia Explanation Retriever

This Python program fetches explanations from Wikipedia based on user input and saves the content into a `.txt` file. It utilizes the Wikipedia API to retrieve relevant information.

## Features

- Takes a word as input from the user.
- Retrieves the Wikipedia summary for the specified word.
- Saves the explanation to a `.txt` file for easy access.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required library:
   ```bash
   pip install wikipedia-api
   ```

## Usage

1. Run the program:
   ```bash
   python wikipedia_explanation.py
   ```

2. Enter the word you want to search for when prompted.

3. The explanation will be saved in a `.txt` file named `<word>_explanation.txt`.


This will create a file named `Python_explanation.txt` containing the Wikipedia explanation of "Python."

## Notes

- Ensure you have an active internet connection for fetching data from Wikipedia.
- You may customize the output file name and format by modifying the source code.
