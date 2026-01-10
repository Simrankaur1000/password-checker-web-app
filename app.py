from flask import Flask, render_template, request
from strength_checker.scorer import score_password, suggest_password
from breach_check.hash_utils import sha1_hash
from breach_check.hibp_api import check_breach

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    suggestion = None
    if request.method == "POST":
        password = request.form.get("password")
        strength = score_password(password)
        breach_count = check_breach(sha1_hash(password))
        result = {
            "strength": strength,
            "breach_count": breach_count
        }
        if strength in ["Very Weak", "Weak", "Moderate"]:
            suggestion = suggest_password()
    return render_template("index.html", result=result, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)

