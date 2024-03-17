import streamlit as st
from newsapi import NewsApiClient

# Initialize News API client
newsapi = NewsApiClient(api_key='94d9380232e241fd9c50f99809656112')

# Configure the page
st.set_page_config(
    page_title="Stock News",
    page_icon="📰",
)

# Add title to the app
st.markdown("# *Stock News*")

# Add a subtitle to the app
st.markdown("##### *Stay Updated with the Latest Stock News*")

# Add a sidebar
st.sidebar.markdown("## *User Input Features*")

# Add a text input for entering the stock ticker
st.sidebar.markdown("### *Enter Stock Ticker*")
stock_ticker = st.sidebar.text_input("Enter a stock ticker (e.g., AAPL):")

if stock_ticker:
    # Fetch news articles related to the stock ticker
    news_articles = newsapi.get_everything(q=stock_ticker, language='en', sort_by='publishedAt')

    # Display the news headlines
    if news_articles['articles']:
        for article in news_articles['articles']:
            st.write(f"*{article['publishedAt']}*: {article['title']}")
    else:
        st.warning("No news available for the selected stock.")