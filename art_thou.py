from flask import Flask, render_template, json, request

app = Flask(__name__)

#This is the bare bones of your app


@app.route('/')
def index():
    """Please just show the rendered page"""
    return render_template('landing.html')

if __name__ == '__main__':
    app.run()
