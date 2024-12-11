import fasthtml.common as cm
from playground import list_loadable_datasets, load_ds_preview


headers = (
    cm.Meta(charset="UTF-8"),
    cm.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    cm.Title("My headers."),
    cm.Link(rel="icon", href="./static/favicon.ico", type="image/x-icon"),
)

app, rt = cm.fast_app(live=True, hdrs=headers)
app.mount("/static", cm.StaticFiles(directory="static"), name="static")


@rt("/")
def home():
    return cm.Titled(
        "Welcome to My Portfolio",
        cm.Body(
            cm.P("Explora mis proyectos y aprende más sobre mí."),
            cm.Header(
                cm.Nav(
                    cm.A("Sobre mí", href="/about", cls="nav-link"),
                    cm.A("Proyectos", href="/projects", cls="nav-link"),
                    cm.A("Contacto", href="/contact", cls="nav-link"),
                    cm.A("ML playgroud", href="/playground", cls="nav-link"),
                    cls="nav-menu",
                ),
            ),
            cls="landing-body",
        ),
    )


@rt("/playground")
def ml_playground():
    return cm.Titled(
        "Learn and train your own ML algorithm",
        cm.P("Sklearn basic data preprocessing and simple MLP training"),
        cm.Select(
            *[cm.Option(ds, value=ds) for ds in list_loadable_datasets()], id="dataset-selector"
        ),
        cm.NotStr(load_ds_preview())
    )


cm.serve(reload=True)
