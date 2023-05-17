from flask import Flask, request, render_template, redirect
import os
import zipfile
from Hotsko_Kharabara_project import run

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
      result = run([filename])
      result = [{'method': 'Decision Tree Model', 'result': result[0][0]},\
         {'method': 'Random Forest Model', 'result': result[1][0]},\
         {'method': 'KNN Model', 'result': result[2][0]},\
         {'method': 'SVD Model', 'result': result[3][0]}]
      
      #print(filename)
      return render_template('result.html', result = result)
   
   else:
      return redirect('/')

if __name__ == '__main__':
   app.run(debug = True, port=8000)
