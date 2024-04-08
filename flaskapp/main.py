from webapp import create_app
from config import DevConfig

app = create_app(DevConfig)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
