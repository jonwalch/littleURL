import random
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.debug = True

db = {}

@app.route("/")
def homepage():
	return render_template('index.html')
	
def createShort(url):
	rand = random.randint(0,999999)
	shortUrl = str(rand)
	if url.startswith("http://") == False and url.startswith("https://") == False:
		url = "http://" + url
	
	if shortUrl in db:
		return createShort(url)
	else:	
		db[url] = shortUrl
		return shortUrl
	
def pullShort(url):
	if url in db: 
		return render_template("result.html", url = db[url])
	else:
		return render_template("result.html", url = createShort(url))
	
@app.route("/getUrl", methods=['POST'])
def getUrl():
	return pullShort(request.form['url'])
	
@app.route("/<page>", methods=["GET"])
def sendDomain(page):
	for key, value in db.items():
		if value == page:
			return redirect(key)
	return render_template("notfound.html")
		
if __name__ == "__main__":
    app.run()
