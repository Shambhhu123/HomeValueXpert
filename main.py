from flask import Flask, request, render_template
import pickle
import pandas as pd
app = Flask(__name__)


@app.route('/')
def predict():
    return




if __name__ == '__main__':
    app.run(debug=True, port=5001)
