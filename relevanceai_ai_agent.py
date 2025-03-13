from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def chat():
    chat_url = "https://app.relevanceai.com/agents/d7b62b/e297ad670489-4668-949b-3b9fd37f419d/e393cbde-673e-4392-bcce-1e3f181fc142/embed-chat?hide_tool_steps=false&hide_file_uploads=false&hide_conversation_list=false&bubble_style=agent&primary_color=%23685FFF&bubble_icon=pd%2Fchat&input_placeholder_text=Type+your+message...&hide_logo=false"
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Chat App</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f4f4f4;
                }
                iframe {
                    width: 80%;
                    height: 80%;
                    border: none;
                    box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <iframe src="{{ chat_url }}"></iframe>
        </body>
        </html>
    ''', chat_url=chat_url)

if __name__ == '__main__':
    app.run(debug=True)
