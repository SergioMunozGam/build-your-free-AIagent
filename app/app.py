import streamlit as st
from llama_index.core.llms import ChatMessage
import logging
import time
from llama_index.llms.ollama import Ollama

logging.basicConfig(level=logging.INFO)

# Initialize chat history in session state if not already present
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a formal assistant expert on programming. "
                                      "Always respond in spanish and maintain a polite and professional tone. "
                                      "Remember to add comment if you have to create some code for me."
         }
    ]


# Function to stream chat response based on selected model
def stream_chat(model, messages):
    try:
        # Initialize the language model with a timeout
        llm = Ollama(model=model, request_timeout=120.0)
        # Stream chat responses from the model
        resp = llm.stream_chat(messages)
        response = ""
        response_placeholder = st.empty()
        # Append each piece of the response to the output
        for r in resp:
            response += r.delta
            response_placeholder.write(response)
        # Log the interaction details
        logging.info(f"Model: {model}, Messages: {messages}, Response: {response}")
        return response
    except Exception as e:
        # Log and re-raise any errors that occur
        logging.error(f"Error during streaming: {str(e)}")
        raise e


def main():
    st.title("Chat with LLMs Models")  # Set the title of the Streamlit app
    logging.info("App started")  # Log that the app has started

    # Sidebar for model selection
    model = st.sidebar.selectbox("Choose a model", ["llama3.2:1b", "phi3", "mistral"])
    logging.info(f"Model selected: {model}")

    # Display the existing conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Prompt for user input
    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        logging.info(f"User input: {prompt}")

        # Display the user's query
        with st.chat_message("user"):
            st.write(prompt)

        # Generate a new response if the last message is not from the assistant
        with st.chat_message("assistant"):
            start_time = time.time()  # Start timing the response generation
            logging.info("Generating response")

            with st.spinner("Writing..."):
                try:
                    # Prepare messages for the LLM and stream the response
                    messages = [ChatMessage(role=msg["role"], content=msg["content"]) for msg in st.session_state.messages]
                    response_message = stream_chat(model, messages)
                    duration = time.time() - start_time  # Calculate the duration
                    response_message_with_duration = f"{response_message}\n\nDuration: {duration:.2f} seconds"
                    st.session_state.messages.append(
                        {"role": "assistant", "content": response_message_with_duration}
                    )
                    #st.write(response_message_with_duration)
                    logging.info(f"Response: {response_message}, Duration: {duration:.2f} s")

                except Exception as e:
                    # Handle errors and display an error message
                    error_message = str(e)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    st.error("An error occurred while generating the response.")
                    logging.error(f"Error: {error_message}")


if __name__ == "__main__":
    main()
