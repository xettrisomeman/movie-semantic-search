from fastapi import Form, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.routing import APIRouter


from utils import search

router = APIRouter(prefix="", tags=["home"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse(
        "home.html", context={"request": request, "error": False}
    )


@router.post("/search", response_class=HTMLResponse)
def get_search(request: Request, query: str = Form(default="Alien invasion movie")):
    response = search.movie_search(query)
    return templates.TemplateResponse(
        "search.html", context={"request": request, "response": response}
    )


@router.get("/search")
def get_search_():
    return RedirectResponse("/")
