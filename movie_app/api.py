from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from routes import movie_search


app = FastAPI()
app.include_router(movie_search.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(404)
def custom_404_handler(request: Request, __):
    return movie_search.templates.TemplateResponse(
        "404.html", context={"request": request, "error": True}
    )
