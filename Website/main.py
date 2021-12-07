from flask import Flask, render_template, request, redirect,send_file
import requests
import csv
import pandas as pd

app = Flask("Comparison Website")

@app.route('/')
def home():
  term = request.form.get("term")
  return render_template("home.html",term=term)


@app.route('/search')
def search():
  term=request.args.get('term')
  df = pd.read_csv('phones.csv', encoding='euc-kr')
  found_phones = pd.DataFrame(columns=df.columns)
  #found_phones.columns = df.columns
  print(found_phones)
  #for row in phone_result:
   # if term in row[0]:
    #  db.app


 # return render_template("search.html", term=term, )

  return render_template("search_result.html")

@app.route('/compare')
def compare():
    return "Compare"

app.run(host="0.0.0.0")