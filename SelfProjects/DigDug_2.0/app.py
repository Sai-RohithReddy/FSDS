from flask import Flask, request, render_template
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_job():
    if request.method == "POST":
        regions = ["na", "eu", "nrt", "integ"]
        job_requested = request.form["job_id"].replace(" ", "")
        for region in regions:
            digDugUrl = f"https://dig-dug-{region}.aka.amazon.com/stows/{job_requested}"
            digdugClient = uReq(digDugUrl)
            digdugPage = digdugClient.read()
            digdugClient.close()
            digdubHtml = bs(digdugPage, "html.parser")
            job = digdubHtml.find_all("div", {"class": "container"})
            if (len(job) == 0):
                continue
            else:
                return digdubHtml          

if __name__ == ("__main__"):
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)