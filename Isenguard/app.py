from flask import Flask, render_template, request
from NPFB import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    cname,t,d,w,h,p25,p10,co,o3,so2,no2 = application(request.form.get('cname'))
    

    
    return render_template('result.html', cname=cname,t=t,d=d,w=w,h=h,p25=p25,p10=p10,co=co,o3=o3,so2=so2,no2=no2)

if __name__ == '__main__':
    app.run(debug=True)

