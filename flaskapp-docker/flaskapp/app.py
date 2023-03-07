from flask import Flask, render_template
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/')
def hello_world():
        app.logger.info('Hello, World!')  # log the message
        return  render_template("home.html")

        if __name__ == '__main__':
                app.run()
