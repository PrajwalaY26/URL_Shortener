from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            try:
                s = pyshorteners.Shortener()
                short_url = s.tinyurl.short(original_url)
            except Exception as e:
                short_url = f"Error: {str(e)}"
    
    return render_template('index.html', short_url=short_url if original_url else None)

if __name__ == '__main__':
    app.run(debug=True)