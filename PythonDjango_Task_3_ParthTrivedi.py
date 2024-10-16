# Code Done by Parth Trivedi - 
# Contact me at parthtrivediparthtrivedi@gmail.com

# Import necessary libraries
import time 
import numpy as np  
import matplotlib.pyplot as plt

# Function to measure how long a given function takes to run for different input sizes
def analyze_time_complexity(function_to_test, input_sizes):
    time_taken = [] 
    
    for size in input_sizes: 
        start = time.time()  
        function_to_test(size) 
        end = time.time()  
        time_taken.append(end - start)  
    
    return time_taken 

def sample_function(n):
    return [i for i in range(n)]

# Define different input sizes to test
input_sizes = [10, 100, 1000, 10000, 100000]

# Get the times taken for each input size using the sample function
time_results = analyze_time_complexity(sample_function, input_sizes)

# Plotting the input sizes vs time taken to visualize time complexity
plt.plot(input_sizes, time_results, marker='o')  
plt.title('Time Complexity Analysis') 
plt.xlabel('Input Size (n)')  
plt.ylabel('Time (in seconds)') 
plt.show()  
