import os

from chalice import Chalice

app = Chalice(app_name="template")

env = os.environ.get("ENVIRONMENT")


@app.route("/")
def index():
    app.log.info("Endpoint / reached in env %s", env)
    return {"hello": "world"}
