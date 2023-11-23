from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'course': 'Data Analyst',
    'location': 'Remote',
    'salary': 'Ksh. 10000'
  },
  {
    'id': 2,
    'course': 'Data Scientist',
    'location': 'Remote',
    'salary': 'Ksh. 1500'
  },
  {
    'id': 3,
    'course': 'Frontend Engineer',
    'location': 'Remote',
    "salary": 'USD. 120'
  },
  {
    'id': 4,
    'course': 'Backend Engineer',
    'location': "Remote",
    'salary': 'USD. 150'
  }
]

@app.route("/")
def hello_Reloca():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Reloca')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)