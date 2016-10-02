from flask import Flask
from IPython import get_ipython
app = Flask(__name__)


@app.route("/")
@app.route("/<path:path>")
def hello(path=""):
    if path:
        repo.value = path
        return (__x(**get_ipython().user_ns)
                | repo_template.render
                > mistune.markdown
                )
    return "Hello New World!" + path

if __name__ == "__main__":
    app.run(port=5000)
