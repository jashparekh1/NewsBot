"""
NewsBot

This script utilizes OpenAI and NewsAPI to provide information and summaries based on user research questions.

Author: Jash Parekh

Date: 06-01-2023

Usage:
    - Make sure you have valid API keys for OpenAI and NewsAPI.
    - Run the script and follow the prompts to enter your research question.
"""

import openai
from newsapi import NewsApiClient
from transformers import pipeline

# Set up the OpenAI API
openai.api_key = "YOUR OPEN_AI KEY"  # Replace with your OpenAI API key

# Set up the NewsAPI client
newsapi = NewsApiClient(api_key="YOUR NEWS_API KEY")  # Replace with your NewsAPI API key

def getAnswer(prompt):
    """
    Retrieves an answer from the OpenAI API based on the given prompt.

    Args:
        prompt (str): The prompt to be sent to the OpenAI API.

    Returns:
        str: The generated answer from the OpenAI API.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.3,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()

def searchNewsAPI(keyword, language="en"):
    """
    Searches news articles using the NewsAPI client based on the given keyword.

    Args:
        keyword (str): The keyword to search for news articles.
        language (str, optional): The language of the news articles. Defaults to "en".

    Returns:
        str: The concatenated content of the news articles.
    """
    response = newsapi.get_everything(q=keyword, language=language, sort_by='publishedAt')
    articles = response['articles']
    text = "\n".join([article['content'] for article in articles])
    return text

def generateSummary(text):
    """
    Generates a summary for the given text using the T5 summarization model.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The generated summary.
    """
    summarizer = pipeline("text2text-generation", model="t5-base", tokenizer="t5-base")
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)[0]['generated_text']

    # Extract the first two sentences from the generated summary
    summary_sentences = summary.split('. ')
    limited_summary = '. '.join(summary_sentences[:2])

    return limited_summary


def determineAction(objective, memory, tools):
    """
    Determines the appropriate action based on the objective, memory, and available tools.

    Args:
        objective (str): The user's research question.
        memory (list): The past actions stored in the memory for reference.
        tools (list): The available tools that can be used.

    Returns:
        tuple: A tuple containing the generated answer, summary, and updated memory.
    """
    formattedPrompt = f"""
    Determine if the following memory is enough to answer
    the user's objective. Your past actions are stored in the memory for reference.
    If it is enough, answer the question in the format: 'FINAL ANSWER: <your answer>'.
    If the memory is not enough, you can use a tool in the available tools section
    to get more information. When using a tool you should use this format:
    'USE <tool name>:<parameter>'. If no tool can help you achieve the user's
    objective, then answer 'FINAL: CANNOT ANSWER'.

    Objective:
    Answer: {objective}

    Memory:
    {memory}

    Available Tools:
    {tools}
    """

    answer = getAnswer(formattedPrompt)
    text = searchNewsAPI(objective)
    if text:
        summary = generateSummary(text)
    else:
        summary = "No relevant news articles found."

    print("Objective:", objective)
    print("Answer:", answer)

    return answer, summary, memory

def startAgent():
    """
    Starts the autonomous agent and prompts the user for their research question.
    """
    objective = input("What is your research question? ")
    memory = []
    tools = ["searchNewsAPI"]

    finished, result, memory = determineAction(objective, memory, tools)


startAgent()
