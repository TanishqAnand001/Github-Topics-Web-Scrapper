import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st


# This @st.cache_data is a Streamlit "magic" command.
# It tells your app to save the data once it's scraped.
# This way, your app doesn't re-scrape GitHub every single time
# someone loads the page, which makes it much faster.
@st.cache_data
def scrape_github_topics():
    base_url = "https://github.com"
    topics_url = "https://github.com/topics"

    response = requests.get(topics_url)
    if response.status_code != 200:
        st.error("Failed to load GitHub Topics page")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    selection = 'f3 lh-condensed mb-0 mt-1 Link--primary'
    topic_title_p_tags = soup.find_all('p', class_=selection)
    topic_description_p_tags = soup.find_all('p', class_='f5 color-fg-muted mb-0 mt-1')

    # --- Helper Functions (copied from your notebook) ---
    def get_topic_page(topic_Url):
        response = requests.get(topic_Url)
        if response.status_code != 200:
            raise Exception('Failed to load page {}'.format(topic_Url))
        return BeautifulSoup(response.text, 'html.parser')

    def get_repo_info(h3_tag, star_tag):
        a_tags = h3_tag.find_all('a')
        author = a_tags[0].text.strip()
        repo_name = a_tags[1].text.strip()
        repo_url = base_url + a_tags[1]['href']
        stars = star_tag.text.strip()
        return author, repo_name, repo_url, stars

    def get_topic_repos(topic_soup):
        repo_tags = topic_soup.find_all('article', class_='border rounded color-shadow-small color-bg-subtle my-4')
        star_tags = topic_soup.find_all('span', class_='Counter js-social-count')

        topic_repos = []
        for i in range(len(repo_tags)):
            repo_info = get_repo_info(repo_tags[i].find('h3'), star_tags[i])
            topic_repos.append(repo_info)
        return topic_repos

    # --- End of Helper Functions ---

    all_repos_data = []

    # We'll use st.progress to show a cool loading bar in the UI
    progress_bar = st.progress(0, "Starting scrape...")

    for i, (title, desc) in enumerate(zip(topic_title_p_tags, topic_description_p_tags)):
        parent_a = title.find_parent('a')
        href = parent_a['href'] if parent_a and parent_a.has_attr('href') else None
        topic_title = title.text.strip()
        topic_desc = desc.text.strip()

        # Update the progress bar in the UI
        progress_text = f"Scraping Topic: {topic_title}"
        progress_bar.progress((i + 1) / len(topic_title_p_tags), text=progress_text)

        if href:
            topic_url = base_url + href
            try:
                topic_soup = get_topic_page(topic_url)
                topic_repos = get_topic_repos(topic_soup)

                for author, repo_name, repo_url, stars in topic_repos:
                    repo_dict = {
                        'Topic Title': topic_title,
                        'Topic Description': topic_desc,
                        'Author': author,
                        'Repository Name': repo_name,
                        'Stars': stars,
                        'Repository URL': repo_url
                    }
                    all_repos_data.append(repo_dict)
            except Exception as e:
                st.warning(f"Could not scrape topic {topic_title}: {e}")

    progress_bar.empty()  # Clear the progress bar when done

    # Create the DataFrame and return it
    repos_df = pd.DataFrame(all_repos_data)
    return repos_df