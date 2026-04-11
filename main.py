from flask import Flask , render_template, request
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()  



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate' , methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant who writes a interesting blogs on the topic that the user provides."),
            ("human", "{question}")
        ])
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("Groq_API_KEY")
        )

        chain = prompt | llm

        title = request.form.get('title')
        output = chain.invoke({"question": title})
        return output.content

if __name__ == '__main__':
    app.run(debug=True)