import app
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))

    app.run(host=host, port=port)
