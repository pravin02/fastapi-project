from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home() -> str:
    return "Home"


# To run fastapi server use below commands
# dev - parameter is used to run application in development mode
# run - parameter is used to run application in production mode
#fastapi dev main.py
#fastapi run main.py


# def main():
#     print("Hello from fastapi-project!")


# if __name__ == "__main__":
#     main()
