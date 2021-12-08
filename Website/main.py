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
  df = df.dropna()
  found_phones = pd.DataFrame(columns=df.columns)
  for row in df.iterrows():
    if term in row[1]['기종']:
      #print(row[1])
      #print("--------------------------------------")
      found_phones=found_phones.append(row[1])
  #print(found_phones.iloc[0])
  for phone in found_phones.iterrows():
    print(phone[1]['기종'])

  return render_template("search_result.html", results=found_phones.iterrows(), term=term)
  #print(df)
    #if term in row[0]:
      
      #found_phones.add(row)
    #  print(row)
  print(found_phones.index.values)


 # return render_template("search.html", term=term, )

  #return render_template("search_result.html")

@app.route('/compare')
def compare():
      
    return "Compare"

app.run(host="0.0.0.0")