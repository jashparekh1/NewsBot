# Project Description


This project is a Python script that implements an autonomous agent and utilizes the OpenAI and NewsAPI services to provide users with information and summaries based on their research questions. By leveraging OpenAI's language model, NewsAPI's news article database, and HuggingFace's text summarization pipeline, the script can generate answers to research questions and provide summaries of relevant news articles. Users can interact with the script by entering their research question, and the system will use the available tools to retrieve information and generate concise summaries to aid in their research process.

In this repository, we designed a distributed file system that is tolerant to up to three simultaneous machine failures. After failure(s), we ensure that data is rereplicated quickly so that another (set of) failures that happens soon after is tolerated.

# Usage
Make sure you have valid API keys for both OpenAI and NewsAPI.
Run the script and follow the prompts to enter your specific research question.

### Start Server
> $ python3 server.py

### Commands
Once the server is started, it will show the commands which you can use and the program will continously run util you kill the process.

You can input the following numbers for each command one at a time and enter the input that it asks for.

    0. exit: exit the file system
    1. put: add a file to the file system
    2. get: get a file from the file system
    3. delete: delete a file from the file system
    4. ls: print all files in the filesystem
    5. store: list all files being stored in the machine
    6. get-versions: get the last N versions of the file in the machine
    7. list_mem: list the membership list"
    8. list_self: list self's id"
    9. leave: command to voluntarily leave the group (different from a failure, which will be Ctrl-C or kill)"

For example, to run put, the terminal would look like the following:

    Please enter command: 1
    Selected put
    Enter local filename: hi
    local file does not exist! please try again
    Please enter command: 1 
    Selected put
    Enter local filename: v3
    Enter SDFS filename: v
    Finished Operation! Time Taken: 0:00:01.405673
