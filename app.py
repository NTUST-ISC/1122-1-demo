from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route("/get_ip",methods=["GET","POST"])
def get_ip():
    if request.method == "POST":
        domain_name = request.form.get("domain_name")
        data = os.popen(f"nslookup {domain_name}").read().split('\n')
        return render_template("get_ip.html", data=data)
    return render_template("get_ip.html")


@app.route("/get_files",methods=["GET","POST"])
def get_files():
    if request.method == "POST":
        directory = request.form.get("directory")
        data = os.popen(f'ls directories/{directory}').read().split('\n')
        return render_template("get_files.html", data=data)
    return render_template("get_files.html")


if __name__ == "__main__":
    app.run("0.0.0.0",port= 8080,debug=True)