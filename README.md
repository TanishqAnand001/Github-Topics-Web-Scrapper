# GitHub Topics Scraper App

[](https://githob-topics-scrapper.streamlit.app/)

This project is a Python-based web application that scrapes GitHub's topics page to find popular topics and their most-starred repositories. It presents the scraped data in a clean user interface, provides data analysis and visualizations, and allows for downloading the data as a CSV.

This application is deployed live on Streamlit Community Cloud.

**Visit the live app:** [**https://githob-topics-scrapper.streamlit.app/**](https://githob-topics-scrapper.streamlit.app/)

-----

## Features

  * **User-Friendly UI:** A simple web interface built with Streamlit.
  * **On-Demand Scraping:** Get the latest data from GitHub by clicking a single button.
  * **Data Visualization:** Automatically generates plots for:
      * Top 10 Most Starred Repositories
      * Top 10 Topics by Total Stars
  * **Interactive Data Table:** View the full scraped dataset in a sortable, filterable table.
  * **Download Data:** Download the complete dataset as a `github_topics_repos.csv` file.

-----

## Technology Stack

  * **Backend & UI:** [Streamlit](https://streamlit.io/)
  * **Web Scraping:** [Requests](https://requests.readthedocs.io/en/latest/) & [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * **Data Analysis:** [Pandas](https://pandas.pydata.org/docs/)
  * **Data Visualization:** [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/)

-----

## Project Structure

  * **`app.py`**: The main Streamlit application file that builds the UI.
  * **`scraper.py`**: A module containing all the Python functions for scraping GitHub.
  * **`analysis.py`**: A module for data processing and generating visualizations.
  * **`requirements.txt`**: A list of all Python dependencies required to run the project.

-----

## How to Run Locally

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

  * **Python 3.x**
  * **Git** (for cloning the repository)

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tanishqanand001/web-scrapper-project.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd web-scrapper-project
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

Your web browser will automatically open to `http://localhost:8501`, where you can use the app.
