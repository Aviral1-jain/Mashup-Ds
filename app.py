from flask import Flask, render_template, request, flash
import subprocess

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == "POST":
        email = request.form['email']
        singerName = request.form['singerName']
        songNumber = int(request.form['songNumber'])
        songDuration = int(request.form['songDuration'])
        outputName = request.form['outputName']

        
        try:
            subprocess.call(["python", "mashup.py", singerName, str(songNumber), str(songDuration), outputName, email])
        except Exception as e:
            flash(e)
            return render_template('index.html')    
    return render_template('index.html')


    





