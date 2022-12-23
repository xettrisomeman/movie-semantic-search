import uvicorn


if __name__ == "__main__":
    uvicorn.run("movie_app.api:app", host="localhost", port=8000, reload=True)
