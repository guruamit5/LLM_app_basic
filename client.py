import requests
import streamlit as st

def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": "French",
            "text": input_text  # Use the dynamic input_text here
        },
        "config": {},
        "kwargs": {}
    }
    
    try:
        # Send the POST request with the corrected JSON body
        response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        # Handle exceptions and return an error message
        return {"error": str(e)}

## Streamlit app
st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    result = get_groq_response(input_text)
    if "error" in result:
        st.error(f"Error: {result['error']}")
    else:
        translated_text = result.get("output", "No translation available.")
            
            # Display results in a human-readable format
        st.write("**Translation Result:**")
        st.write(translated_text)