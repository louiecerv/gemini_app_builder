import streamlit as st
import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def generate_app_code(framework, task):
    """
    Generates Python code for the selected framework and task using the AI model.

    Args:
        framework (str): The selected framework ('Streamlit' or 'Gradio').
        task (str): The task for which the app will be generated.

    Returns:
        str: Generated Python code or an error message.
    """
    try:
        # Construct the prompt
        prompt = (
            f"Create a {framework} app for the following task: {task}. "
            "Provide the full Python code and ensure it is functional."
        )

        # Send the prompt to the model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    
    # Streamlit UI
    st.title("App Builder: Streamlit or Gradio")

    with st.expander("ℹ️ About"):
        st.write(
            "This tool generates Python code for a Streamlit or Gradio app based on a selected task. "
            "It uses the Gemini 1.5 flash model to generate the code. "
            "You can select a predefined task or enter a custom one.")
        st.markdown("Programmed by: \n\n \
        Louie F. Cervantes, M.Eng (Information Engineering) \n\n\
        West Visayas State University")


    # Step 1: Select the framework
    framework = st.selectbox("Select a framework:", ["Streamlit", "Gradio"])

    # Step 2: Select a task or enter a custom one
    predefined_tasks = [
        "Interactive Data Explorer",
        "Simple Linear Regression",
        "Image Classification with Pre-trained Model",
        "Text Summarizer",
        "Sentiment Analysis Tool",
        "Interactive Quiz App",
        "Basic Calculator",
        "Unit Converter",
        "Color Mixer",
        "Simple Game (e.g., Number Guessing)"
    ]

    task = st.selectbox("Select a predefined task:", predefined_tasks)
    custom_task = st.text_input("Or enter a custom task:")

    # Use the custom task if provided
    task = custom_task if custom_task.strip() else task

    # Step 3: Generate the app code
    if st.button("Generate App Code"):
        with st.spinner("Generating code..."):
            app_code = generate_app_code(framework, task)
            if app_code:
                st.subheader("Generated Code")
                st.code(app_code, language="python")
            else:
                st.error("Failed to generate the app code. Please try again.")

if __name__ == "__main__":
    main()