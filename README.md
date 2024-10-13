# Python Web Scraping and Analysis Project

This project consists of Python scripts for web scraping and analyzing meta information from web pages. It utilizes several libraries, including BeautifulSoup for scraping, Pandas for data manipulation, and Matplotlib for data visualization. Additionally, it incorporates the SERP API for retrieving results from Google and the Nomic API for visualizing data in a knowledge graph.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   
   ```git clone https://github.com/Mateusz-Grencel/isa-project-mg/tree/test```
   
   ```cd your-repository```

3. Create a virtual environment (optional but recommended):
   ```python -m venv venv```
   
   ```source venv/bin/activate  # On Windows use `venv\Scripts\activate```

4. Install the required packages:
   ```pip install -r requirements.txt```

## Usage
1. Run the main script to fetch metadata and analyze web pages:

```python main.py```

Follow the prompts to enter the website URL and the keyword related to your website.

After processing, which will take up to 10 minutes, you will receive an email with the completed map from Nomic. Please open it using the email associated with your Nomic account. Copy the dataset ID name (in this case, it is intuitive-fisher).

![image](https://github.com/user-attachments/assets/13fc1066-388c-4845-a788-27664befe4da)


Once the map is opened, copy your ID from our page (here, it is HQ).

![id](https://github.com/user-attachments/assets/f467287b-5f78-4408-9ba8-04a2d1325195)



Now  you can perform various analyses by running the sec.py script:

```python sec.py```

Enter the dataset ID from Nomic to load and analyze the data. Next, provide the ID of your page. Then, select the analysis that interests you.

## Features
-**Dynamic Data Analysis:** Perform various analyses on metadata, including meta description length, keyword occurrences, title lengths, and duplicate titles, allowing users to gain insights into their datasets.

-**Interactive Menu:** Utilize a user-friendly command-line interface that guides users through the analysis process, providing clear options and feedback throughout the workflow.

-**Knowledge Graph Integration:** Leverage the Nomic library to access and visualize knowledge graphs, enabling users to explore relationships and connections between data points effectively.

-**Histogram Visualization:** Generate histograms for various metrics, such as meta description lengths, title lengths, and URL lengths, providing a visual representation of data distributions for better understanding.

-**Keyword Analysis:** Analyze the frequency of specific keywords in both meta descriptions and titles, helping users optimize their content for search engines and improve SEO performance.

-**URL Parameter Detection:** Examine URLs for the presence of parameters and count the number of parameters in each URL, assisting users in understanding the structure and complexity of their links.

-**Data Filtering Capabilities:** Implement filtering options based on user-defined criteria (e.g., minimum and maximum lengths), allowing for tailored analysis of specific subsets of data.

-**Duplicate Detection:** Identify and highlight duplicate titles within the dataset, assisting users in maintaining content uniqueness and enhancing overall quality.

-**Error Handling and Validation:** Include robust error handling for user inputs, ensuring a smooth experience even when invalid data is provided, which enhances program reliability.

-**Comprehensive Output Highlighting:** Use color-coded outputs to highlight specific data points or rows based on user selections, making it easier to interpret and analyze results visually.

## Requirements
- Python 3.x
- A list of required libraries can be found in the requirements.txt.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Licence
This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.
