In this small project, we’ll build a Llama 2 chatbot in Python using Streamlit for the frontend, while the LLM backend is handled through API calls to the Llama 2 model hosted on Replicate. 


Following are the steps to take to build the app:
1. Get a Replicate API token
2. Set up the coding environment
3. Build the app
4. Set the API token
5. Deploy the app

What is Llama 2?
Meta released the second version of their open-source Llama language model on July 18, 2023. They’re democratizing access to this model by making it free to the community for both research and commercial use. They also prioritize the transparent and responsible use of AI, as evidenced by their Responsible Use Guide.

Here are the five key features of Llama 2:

Llama 2 outperforms other open-source LLMs in benchmarks for reasoning, coding proficiency, and knowledge tests.
The model was trained on almost twice the data of version 1, totaling 2 trillion tokens. Additionally, the training included over 1 million new human annotations and fine-tuning for chat completions.
The model comes in three sizes, each trained with 7, 13, and 70 billion parameters.
Llama 2 supports longer context lengths, up to 4096 tokens.
Version 2 has a more permissive license than version 1, allowing for commercial use.


App overview
Here is a high-level overview of the Llama2 chatbot app:

The user provides two inputs: (1) a Replicate API token (if requested) and (2) a prompt input (i.e. ask a question).
An API call is made to the Replicate server, where the prompt input is submitted and the resulting LLM-generated response is obtained and displayed in the app.


