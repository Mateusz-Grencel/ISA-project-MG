import pandas as pd
import re
import matplotlib.pyplot as plt
from colorama import init, Fore, Style
from nomic import AtlasDataset

# Initialize Colorama
init(autoreset=True)

def main_program():
    while True:
        # Get dataset ID from user with error handling
        while True:
            try:
                dataset_id = input("Enter the dataset ID from Nomic: ")

                # Initialize AtlasDataset with dynamically provided identifier
                dataset = AtlasDataset(identifier=dataset_id)

                # Retrieve the first map from the dataset
                map = dataset.maps[0]
                print(map)

                print(f"Successfully loaded dataset with ID: {dataset_id}")
                print(f"Loading analyses...")
                break  # Exit loop if everything went well
            except Exception as e:
                print(f"Error: {e}. Please try again.")

        while True:
            # Ask for knowledge graph ID
            id_input = input("Enter the knowledge graph ID: ")

            # Get neighbors for the specified point
            neighbor, distances = map.embeddings.vector_search(ids=[id_input], k=30)

            # Sample data analysis
            data = []
            for neighbor_id in neighbor[0]:
                neighbor_info = dataset.get_data(ids=[neighbor_id])
                if neighbor_info:
                    data.append({
                        'id': neighbor_info[0]['id_'],
                        'title': neighbor_info[0]['title'],
                        'link': neighbor_info[0]['link'],
                        'meta_description': neighbor_info[0]['meta_description']
                    })

            df = pd.DataFrame(data)

            # Main menu for selecting analysis
            while True:
                print("\nSelect analysis to perform:")
                print("1. Meta Description Length Analysis")
                print("2. Keyword in Meta Description Analysis")
                print("3. Keyword in Title Analysis")
                print("4. Title Length Analysis")
                print("5. Duplicate Title Analysis")
                print("6. URL Length Analysis")
                print("7. Parameters in URL Analysis")
                print("8. Enter new knowledge graph ID")
                print("9. Exit program")

                choice = input("Enter your choice (1-9): ")

                if choice == '1':
                    meta_desc_length_analysis(df, id_input)
                elif choice == '2':
                    keyword_in_meta_description_analysis(df, id_input)
                elif choice == '3':
                    keyword_in_title_analysis(df, id_input)
                elif choice == '4':
                    title_length_analysis(df, id_input)
                elif choice == '5':
                    duplicate_title_analysis(df, id_input)
                elif choice == '6':
                    url_length_analysis(df, id_input)
                elif choice == '7':
                    params_in_url_analysis(df, id_input)
                elif choice == '8':
                    # Exit the current loop and go back to dataset selection
                    print("Returning to dataset selection.")
                    break
                elif choice == '9':
                    print("Exiting the program.")
                    return  # Exit the entire program
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")

# Functions for data analysis with plots
def meta_desc_length_analysis(df, id_input):
    # Get user input for minimum and maximum meta description length
    min_length = int(input("Enter the minimum meta description length: "))
    max_length = int(input("Enter the maximum meta description length: "))

    df["meta_desc_length"] = df["meta_description"].str.len()
    filtered_df = df[(df["meta_desc_length"] >= min_length) & (df["meta_desc_length"] <= max_length)]

    print(f"Meta descriptions with length between {min_length} and {max_length} characters:")

    highlight_rows_local(id_input, filtered_df, ['id', 'meta_desc_length', 'meta_description'])

    # Plotting meta description lengths
    plt.hist(df["meta_desc_length"], bins=20, color='blue', edgecolor='black')
    plt.title("Meta Description Lengths")
    plt.xlabel("Meta Description Length (character count)")
    plt.ylabel("Number of Entries")
    plt.show()

    input("Press Enter to return to the menu...")

# Other functions remain the same, just add 'df' and 'id_input' as arguments.

def keyword_in_meta_description_analysis(df, id_input):
    keyword = input("Enter the keyword to search in the meta description: ")
    keyword_pattern = re.escape(keyword)

    df['keyword_count'] = df['meta_description'].str.count(rf'\b{keyword_pattern}\b', flags=re.IGNORECASE)

    print(f"Number of occurrences of the keyword '{keyword}' in the meta description:")

    highlight_rows_local(id_input, df, ['id', 'keyword_count', 'meta_description'])

    # Plotting keyword occurrences in meta descriptions
    plt.hist(df['keyword_count'], bins=10, color='green', edgecolor='black')
    plt.title(f"Occurrences of the Keyword '{keyword}' in the Meta Description")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Number of Entries")
    plt.show()

    input("Press Enter to return to the menu...")

def keyword_in_title_analysis(df, id_input):
    keyword = input("Enter the keyword to search in the title: ")
    keyword_pattern = re.escape(keyword)

    df['keyword_count'] = df['title'].str.count(rf'\b{keyword_pattern}\b', flags=re.IGNORECASE)

    print(f"Number of occurrences of the keyword '{keyword}' in the title:")

    highlight_rows_local(id_input, df, ['id', 'keyword_count', 'title'])

    # Plotting keyword occurrences in titles
    plt.hist(df['keyword_count'], bins=10, color='purple', edgecolor='black')
    plt.title(f"Occurrences of the Keyword '{keyword}' in the Title")
    plt.xlabel("Number of Occurrences")
    plt.ylabel("Number of Entries")
    plt.show()

    input("Press Enter to return to the menu...")

def title_length_analysis(df, id_input):
    # Get user input for minimum and maximum title length
    min_length = int(input("Enter the minimum title length: "))
    max_length = int(input("Enter the maximum title length: "))

    df['title_len'] = df['title'].str.len()
    filtered_df = df[(df["title_len"] >= min_length) & (df["title_len"] <= max_length)]

    print(f"Titles with length between {min_length} and {max_length} characters:")

    highlight_rows_local(id_input, filtered_df, ['id', 'title_len', 'title'])

    # Plotting title lengths
    plt.hist(df['title_len'], bins=20, color='orange', edgecolor='black')
    plt.title("Title Lengths")
    plt.xlabel("Title Length (character count)")
    plt.ylabel("Number of Entries")
    plt.show()

    input("Press Enter to return to the menu...")

def duplicate_title_analysis(df, id_input):
    duplicate_titles = df[df.duplicated(subset='title', keep=False)]

    print("Duplicate Titles:")
    highlight_rows_local(id_input, duplicate_titles, ['id', 'title', 'link', 'meta_description'])

    # Plotting the number of duplicate titles
    title_counts = df['title'].value_counts()
    plt.hist(title_counts[title_counts > 1], bins=10, color='red', edgecolor='black')
    plt.title("Number of Duplicate Titles")
    plt.xlabel("Number of Duplicates")
    plt.ylabel("Number of Titles")
    plt.show()

    input("Press Enter to return to the menu...")

def url_length_analysis(df, id_input):
    # Add a new column with URL length
    df['url_length'] = df['link'].apply(len)

    print("URL Lengths:")

    highlight_rows_local(id_input, df, ['id', 'url_length', 'link'])

    # Plotting URL lengths
    plt.hist(df['url_length'], bins=20, color='cyan', edgecolor='black')
    plt.title("URL Lengths")
    plt.xlabel("URL Length (character count)")
    plt.ylabel("Number of Entries")
    plt.show()

    input("Press Enter to return to the menu...")

def params_in_url_analysis(df, id_input):
    # Add a column that checks if the URL has parameters
    df['has_params'] = df['link'].apply(lambda x: '?' in x)

    # Add a column with the part of the URL after the domain
    df['params_count'] = df['link'].apply(lambda x: len(x.split('?')[1].split('&')) if '?' in x else 0)

    print("URLs with Parameters:")

    highlight_rows_local(id_input, df, ['id', 'has_params', 'params_count', 'link'])

    # Plotting parameters in URLs
    plt.hist(df['params_count'], bins=10, color='magenta', edgecolor='black')
    plt.title("Parameters in URLs")
    plt.xlabel("Number of Parameters")
    plt.ylabel("Number of URLs")
    plt.show()

    input("Press Enter to return to the menu...")

def highlight_rows_local(id_value, df, cols_to_show):
    for index, row in df.iterrows():
        output = row[cols_to_show].tolist()
        if str(row['id']) == str(id_value):
            print(Fore.YELLOW + str(output) + Style.RESET_ALL)  # Highlight the row
        else:
            print(str(output))  # Regular display of the row

# Start the main program
main_program()

