from flask import Flask, render_template, request, redirect,send_file, g
import requests
import csv
import pandas as pd

selcted_side = 0
chosen_product_1 = {}
chosen_product_2 = {}

app = Flask("Comparison Website")


@app.route('/')
def home():
  term = request.form.get("term")
  return render_template("home.html",term=term)

@app.route('/left')
def left():
  global selcted_side
  selcted_side = 0;
  term = request.form.get("term")
  return render_template("home.html",term=term)

@app.route('/right')
def right():
  global selcted_side
  selcted_side = 1;
  term = request.form.get("term")
  return render_template("home.html",term=term)

@app.route('/search')
def search():
  term=request.args.get('term')
  df = pd.read_csv('phones.csv', encoding='euc-kr')
  df = df.dropna()
  global found_phones
  found_phones = pd.DataFrame(columns=df.columns)
  for row in df.iterrows():
    if term in row[1]['기종']:
      found_phones=found_phones.append(row[1])
  return render_template("search_result.html", results=found_phones.iterrows(), term=term)

@app.route('/compare/<phoneID>')
def compare(phoneID):
  if selcted_side == 0:
    global chosen_product_1
    global chosen_product_2
    print(chosen_product_2)
    chosen_product_1 = found_phones.loc[int(phoneID)]
    return render_template("compare.html", chosen_product_1=chosen_product_1, chosen_product_2=chosen_product_2)
  
  else:
    
    chosen_product_2 = found_phones.loc[int(phoneID)]
    print("right")
    return render_template("compare.html", chosen_product_1=chosen_product_1, chosen_product_2=chosen_product_2)

  #print("phoneID: ", phoneID)
   # for row in found_phones:
    #  print(row)
    #print(found_phones.iloc)

app.run(host="0.0.0.0")