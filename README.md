# LLM_ChatBot_streamlit

LLM_ChatBot_streamlit- T-BOT, is an amazing chatbot application powered by the latest natural language processing technology. It is designed to provide a seamless conversational experience and assist users in various tasks. This repository contains the code and resources required to deploy the chatbot using Streamlit.

- Using HugChat, an innovative and versatile Python package designed to simplify the development of chatbot applications. With HugChat, developers can quickly and effortlessly create intelligent conversational agents that interact with users in a natural and engaging manner.
## Features

- Natural language processing capabilities
- Contextual understanding of user queries
- Rich and engaging conversation flow
- Seamless integration with Streamlit
- Easy-to-use and interactive user interface


- Front-end: The user submits an input prompt (by providing a string of text to the text box via st.text_input()), and the app generates a response.
- Back-end: Input prompt is sent to hugchat (the unofficial port to the HuggingChat API) via streamlit-chat for generating a response.
- Front-end: Generated responses are displayed in the app via's message() command.


![Alt text](https://blog.streamlit.io/content/images/2023/05/hugchat-diagram.png)
## Installation

To run the LLM_ChatBot_streamlit locally, you need to follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/tushar2704/LLM_ChatBot_streamlit.git
   cd LLM_ChatBot_streamlit
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run chatbot.py
   ```

   This command will start the Streamlit app and you can access it in your web browser.

## Usage

Once the application is running, you can interact with the chatbot through the user interface. The chatbot will respond to your queries and engage in a conversation with you. Feel free to explore its features and capabilities.

## Deployment

The LLM_ChatBot_streamlit app is deployed using Streamlit Sharing, allowing you to access it directly from your web browser. Here are the deployment links:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tushar2704-llm-chatbot-streamlit-chatbot-dssay9.streamlit.app/)

## Demo

You can find a live demo of the LLM_ChatBot_streamlit app in action at the following link:

- [Demo](https://tushar2704-llm-chatbot-streamlit-chatbot-dssay9.streamlit.app/)


## Author
- <ins><b>©2023 Tushar Aggarwal. All rights reserved</b></ins>
- <b>[LinkedIn](https://www.linkedin.com/in/tusharaggarwalinseec/)</b>
- <b>[Medium](https://medium.com/@tushar_aggarwal)</b> 
- <b>[Tushar-Aggarwal.com](https://www.tushar-aggarwal.com/)</b>
- <b>[Kaggle](https://www.kaggle.com/tusharaggarwal27)</b> 

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

LLM_ChatBot_streamlit is licensed under the [MIT License](https://github.com/tushar2704/LLM_ChatBot_streamlit/blob/main/LICENSE).


## Acknowledgements

We would like to express our gratitude to the open-source community for their invaluable contributions and support.
