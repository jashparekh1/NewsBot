# Project Description


This project is a Python script that implements an autonomous agent and utilizes the OpenAI and NewsAPI services to provide users with information and summaries based on their research questions. By leveraging OpenAI's language model, NewsAPI's news article database, and HuggingFace's text summarization pipeline, the script can generate answers to research questions and provide summaries of relevant news articles. Users can interact with the script by entering their research question, and the system will use the available tools to retrieve information and generate concise summaries to aid in their research process.

In this repository, we designed a distributed file system that is tolerant to up to three simultaneous machine failures. After failure(s), we ensure that data is rereplicated quickly so that another (set of) failures that happens soon after is tolerated.

# Usage
Make sure you have valid API keys for both OpenAI and NewsAPI. Run the script and follow the prompts to enter your specific research question. If the agent is able to summarize an answer to your question, it will print the summary as the 'Final Answer', else it will print 'No relevant news articles found'.

## Examples
    Query: What are recent advances in the field of artificial intelligence?
    Agent Response: Recent advances in the field of artificial intelligence include the development of natural language processing systems, machine learning algorithms, and autonomous robots.
    
    Query: Explain the rise of decentralized finance (DeFi) in the cryptocurrency space.
    Agent Response: Decentralized finance (DeFi) is a new trend in the cryptocurrency space that has seen rapid growth in recent years. It is a form of financial technology that enables users to access a range of financial services without the need for a centralized intermediary.
    
    Query: LeBron James NBA championships
    Agent Response: 4 NBA Championships
