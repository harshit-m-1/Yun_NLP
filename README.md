 You will be working with Web Scrapers / Langchain agents to fetch data from different sources for a particular company.
You will use Reliance Industries Ltd. (RIL) to find the latest news for RIL in the last 24 hours. This should include any posts on twitter, any news website, or any mention of RIL on any public internet. The data should be structured as follows:
The final output should be a list of dictionaries.
Each dictionary item should include the following keys:
source: the source url where the data was scraped.
text: the scraped text.
