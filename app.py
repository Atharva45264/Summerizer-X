import requests
from flask import Flask, render_template,url_for
from flask import request as req

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("contact.html")

@app.route("/services.html", methods=["GET","POST"])
def Service():
    return render_template("services.html")

@app.route("/contact.html", methods=["GET","POST"])
def Contact():
    return render_template("contact.html")

@app.route("/contact.html")
def image():
    return render_template("/static/pexels_videos_2029251 (2160p).mp4")    
@app.route("/summary.html", methods=["GET","POST"])
def Summary():
    return render_template("summary.html")

# @app.route("/summary.html")
# def image2():
#     return render_template("/static/pexels_videos_2029251 (2160p).mp4")

@app.route("/index.html", methods=["GET","POST"])
def Home():
    return render_template("index.html")

@app.route("/about.html", methods=["GET","POST"])
def About():
    return render_template("about.html")

@app.route("/Summarize", methods =["GET","POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
        headers = {"Authorization": "Bearer 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"}


        data = req.form["rawtext"]

        # maxL = 500
        # minL = maxL//3
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload, verify=False)
            return response.json()
	
        output = query({
	    "inputs": data,
	    # "parameters": {"min_length": minL, "max_length": maxL},
        })
    
        return render_template("summary.html", rawtext2 = data ,result = output)
    else:
        return render_template("index.html")








if __name__ == '__main__':
    app.debug = True
    app.run()