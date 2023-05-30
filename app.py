import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

def main():
    model_name = "deepset/roberta-base-squad2"

    # Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Create a Streamlit sidebar with input fields
    st.sidebar.title("Question Answering Demo")
    question = st.sidebar.text_input("Enter your question", "Why is model conversion important?")
    context = st.sidebar.text_area("Enter the context", "The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.")

    if st.sidebar.button("Get Answer"):
        # Get predictions
        nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
        QA_input = {'question': question, 'context': context}
        res = nlp(QA_input)

        # Display the answer
        st.write("Question:", question)
        st.write("Answer:", res['answer'])
        st.write("Score:", res['score'])

if __name__ == "__main__":
    main()
