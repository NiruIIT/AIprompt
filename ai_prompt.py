from flask import Flask,render_template,request
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from config import geminiapikey

app=Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def ai():
    #prompt = "write an essay about higgs boson along with mathematical derivations."
    prompt = request.form['prompt']

    genai.configure(api_key=geminiapikey)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    reply = response.candidates[0].content.parts[0].text
#    print(reply)

    text = f"*******************************************\n \n GeminiAI response for prompt: {prompt} \n *************************************\n \n \n"
    text += reply
    
    return render_template('result.html', text_content=reply,prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)
