from flask import Flask, render_template
from flask import request
import random
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

app = Flask(__name__)


@app.route("/<get_rand_no>/",  methods=['GET'])
def get_random_no(get_rand_no=None):
    """
    description - Generate the random number from given range.
    returns - random number from given range
    """
    start_no = int(request.args.get("from", 0))
    end_no = int(request.args.get("to", 1000))
    return str(random.randint(start_no, end_no))

@app.route("/")
def index():
    return "Well come in random number generator"


@app.errorhandler(Exception)
def all_exception_handler(error):
    """
        description - Used to handle all exceptions
        @returns - correct URL format
        """
    return f"Error: {error.code}, " \
           f"Please recheck URL, format should be: /get_rand_no/?from='start no'?to='end no'", 500



if __name__ == "__main__":
    app.run("127.0.0.1", 8080)