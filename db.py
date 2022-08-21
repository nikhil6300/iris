from flask import Flask,render_template,request,jsonify
import mysql.connector
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_data', methods = ['POST'])
def student_data():
    s_name = request.form['student_name']
    s_roll_no = request.form['student_roll_no']
    s_sub1 = request.form['student_sub1']
    s_sub2 = request.form['student_sub2']
    s_sub3 = request.form['student_sub3']

    print(f"Student Name = {s_name}")
    conn=mysql.connector(host='localhost',
                        database='may11',
                        user='root',password='')
    cursor=conn.cursor()
    query = "INSERT INTO student_data(name,roll_no,sub1,sub2,sub3) VALUES(%s,%s,%s,%s,%s)"
    data = (s_name,s_roll_no,s_sub1,s_sub2,s_sub3)
    cursor.execute(query,data)

    conn.commit()
    conn.closed()


    return jsonify(s_name)


if __name__=="__main__":
    app.run(debug=True)