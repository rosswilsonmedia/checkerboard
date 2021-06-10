from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:height>')
def heightAdjust(height):
    return render_template('index.html', height=height)

@app.route('/<int:height>/<int:width>')
def sizeAdjust(height, width):
    return render_template('index.html', height=height, width=width)

if __name__=='__main__':
    app.run(debug=True)