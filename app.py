from flask import Flask, render_template, url_for, request,redirect
import requests
from googlesearch import search
from bs4 import BeautifulSoup
app = Flask(__name__)
def titles(url):  
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        h3_elements = soup.find_all('h3')
        webs = []
        for h3 in h3_elements:
            print(h3.text)
            webs.append(h3.text)
        return webs

    else:
        print('Failed to retrieve the website.')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_name = request.form.get('Name')
        login_email = request.form.get('email').lower()
        login_number = request.form.get('number')
        if login_email.endswith("@gmail.com") and login_number.isdigit():
            return redirect("/home")
        else:
             return render_template("index.html")
    
    else:
            return render_template("index.html")

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/resource', methods=['GET', 'POST'])
def resource():
    if request.method == "POST":
        query = request.form.get("query")
        query = query + "notes file type: pdf "
        num_results = 5
        results= search( query, num_results=num_results)
        results = list(results)
        names = titles(f"https://www.google.com/search?q={query}")
        return render_template("shows.html" , results = results,names = names)
    else:
        return render_template("resource.html")
@app.route('/shows')
def shows():
    return render_template('shows.html')
@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    if request.method == "POST":
        query = request.form.get("query")
        query = query + "roadmap sh"
        num_results = 5
        results= search( query, num_results=num_results)
        results = list(results)
        names = titles(f"https://www.google.com/search?q={query}")
        return render_template("shows.html" , results = results,names = names)
    else:
        return render_template("roadmap.html")

if __name__ == '__main__':
    app.run(debug=True)
