import os
from flask import Flask
from routes.api import api
from flasgger import Swagger
from dotenv import load_dotenv
import openai
from db.redis import test_redis_connection

load_dotenv()
test_redis_connection()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
# Initialize Swagger
swagger = Swagger(app)

app.register_blueprint(api, url_prefix="/api")

# main driver function
if __name__ == "__main__":
    app.run()
