from flask import Flask, request, url_for, render_template, send_file, redirect
import os

archives = []
for root, folder, files in os.walk('./archives'):
    for file in files:
        archives.append(file)

print(archives)

app = Flask(__name__)
app.config['upload_folder'] = 'archives'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No filepart')
            return redirect('/')
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect('/')
        if file:
            file.save(os.path.join(app.config['upload_folder'], file.filename))
    return render_template('home.html', archives=archives)


@app.route('/download/<file>')
def download(file):
    return send_file(f'{app.config["upload_folder"]}/{file}', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
