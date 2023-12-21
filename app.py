from flask import Flask, redirect, url_for, render_template, request,jsonify

app = Flask(__name__)
JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'Location':'Benguluru',
        'salary':'8k'
        
    },
    
       {'id': 2, 'title': 'Software Engineer', 'Location': 'Hyderabad', 'salary': '10k'},
       {'id': 3, 'title': 'Marketing Specialist', 'Location': 'Mumbai', 'salary': '12k'},
        {'id': 5, 'title': 'Financial Analyst', 'Location': 'Delhi', 'salary': '11k'},
    
]

@app.route('/')
def welcome():
    return render_template('index.html',jobs=JOBS,company_name='Jovian',)
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
if __name__=='__main__':
    app.run(debug='True')
   
