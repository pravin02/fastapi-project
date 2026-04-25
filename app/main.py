from fastapi import FastAPI

from router import albums

try:
    app = FastAPI(title="Albums DB", version="1.0.0")

    @app.get("/heath")
    def health():
        return {"status": "OK"}

    app.include_router(albums.router, prefix="/api/v1", tags=["albums"])
except Exception as e:
    print(f"Application at startup. Exception: {e}")
















# To run fastapi server use below commands
# dev - parameter is used to run application in development mode
# run - parameter is used to run application in production mode
#fastapi dev main.py
#fastapi run main.py


# def main():
#     print("Hello from fastapi-project!")


# if __name__ == "__main__":
#     main()
