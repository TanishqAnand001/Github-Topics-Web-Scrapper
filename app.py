import streamlit as st
import pandas as pd
import scraper  # This imports your scraper.py file
import analysis  # This imports your analysis.py file

# Set up the page title and layout
st.set_page_config(layout="wide")
st.title("GitHub Topics Scraper 🚀")

st.write("""
Welcome! This app scrapes the GitHub Topics page to find the most popular topics 
and their top repositories. Click the button below to get the latest data.
""")

# Create a button. The code inside this 'if' block will only run when the button is clicked.
if st.button("Scrape Latest GitHub Topics"):

    st.info("Scraping in progress... This may take a minute.")

    # 1. Run the scraper function
    # A spinner will show while it's working
    with st.spinner('Fetching data from GitHub...'):
        df = scraper.scrape_github_topics()

    if df is not None:
        st.success("Scraping Complete! ✔️")

        # 2. Run the analysis and display charts
        st.header("Data Analytics and Visualization", divider='rainbow')

        st.subheader("Top 10 Most Starred Repositories")
        fig1 = analysis.plot_top_repos(df)
        st.pyplot(fig1)

        st.subheader("Top 10 Topics by Total Stars")
        fig2 = analysis.plot_top_topics(df)
        st.pyplot(fig2)

        # 3. Display the raw data in a table
        st.header("Full Scraped Data", divider='rainbow')
        st.dataframe(df)


        # 4. Add a download button for the data as a CSV
        @st.cache_data
        def convert_df_to_csv(df_to_convert):
            return df_to_convert.to_csv(index=False).encode('utf-8')


        csv_data = convert_df_to_csv(df)
        st.download_button(
            label="Download Data as CSV",
            data=csv_data,
            file_name='github_topics_repos.csv',
            mime='text/csv',
        )