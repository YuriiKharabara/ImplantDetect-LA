# app.py
from flask import Flask, request, render_template, redirect
import os
import zipfile

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/', methods = ['GET', 'POST'])
def upload_image_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = os.path.join('static', f.filename)
      f.save(filename)
      print(filename)

      if zipfile.is_zipfile(filename):
         with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('static')
         os.remove(filename)

      # Call your function here and get the result
      # result = your_function(filename)
    #   print(filename)
      result = [1, 2, 3, 4, 5]
      
      return render_template('result.html', result = result)
   else:
      return redirect('/')

if __name__ == '__main__':
   app.run(debug = True, port=5000)
