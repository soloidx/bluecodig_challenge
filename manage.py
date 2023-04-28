#!/usr/bin/env python
import typer
import uvicorn  # type: ignore

from project.crud import analyze_pages
from project.deps import get_db_context

manager = typer.Typer()


@manager.command()
def runserver(reload: bool = True):
    uvicorn.run(
        "project.app:app",  # remember <project_name>.app:app
        host="0.0.0.0",
        port=8000,
        reload=reload,
    )


@manager.command()
def analyze():
    with get_db_context() as db:
        analyze_pages(db)


if __name__ == "__main__":
    manager()
