# Code written by Parth Trivedi :

import wikipedia 
def fetch_and_save_summary(word):
    try:
        summary_text = wikipedia.summary(word, sentences=5) 
        file_name = f"{word}_wikipedia_summary.txt"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Wikipedia Summary for '{word}':\n\n")
            file.write(summary_text)
        
        print(f"The summary for '{word}' has been saved in '{file_name}'.")
    
    except wikipedia.exceptions.DisambiguationError as disambiguation_error:
        print(f"The word '{word}' has multiple meanings. Please be more specific.")
        print(f"Here are some options you can consider: {disambiguation_error.options}")
    
    except wikipedia.exceptions.PageError:
        print(f"Sorry, there is no 'Wikipedia page' for the word '{word}'.")
    
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")

user_word = input("Please enter a word to search for on Wikipedia: ")

fetch_and_save_summary(user_word)
