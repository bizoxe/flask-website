"""
Main pages of the site.
"""

import json
from pathlib import Path

from flask import (
    current_app,
    jsonify,
    make_response,
    render_template,
    request,
)

from src.orders.forms import OrderForm
from src.orders.mailing import send_email
from src.routes import bp_base


@bp_base.get("/sitemap.xml")
def sitemap_xml():
    """
    Generates sitemap.xml. Creates a list of page URLs and their modification dates.
    """
    root_dir = Path(__file__).absolute().parent.parent.parent
    file_path = root_dir / "pages_modified.json"
    base_url = current_app.config["BASE_URL"]
    with open(file_path, "r") as file:
        pages_modified = json.load(file)
    try:
        pages = {}
        for rule in current_app.url_map.iter_rules():
            if str(rule) == "/sitemap.xml" or str(rule) == "/robots.txt":
                continue
            if "GET" in rule.methods and len(rule.arguments) == 0:
                if str(rule) in pages_modified:
                    pages[f"{base_url}{str(rule.rule)}"] = pages_modified[f"{rule}"]
                else:
                    pages[f"{base_url}{str(rule.rule)}"] = pages_modified["last_modified"]
        sitemap = render_template("sitemap.xml", pages=pages)
        response = make_response(sitemap)
        response.headers["Content-Type"] = "application/xml"
        response.mimetype = "application/xml"
        return response
    except Exception as e:
        return str(e)


@bp_base.get("/robots.txt")
def robots_txt():
    rb_txt = render_template("robots.txt")
    response = make_response(rb_txt)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    response.mimetype = "text/plain"
    return response


@bp_base.get("/")
def index():
    return render_template(
        "main/index.html",
        page_title="Визажист Минск Елена Долгорукая",
        meta_descr_content="Услуги профессионального визажиста в городе Минск. Любые виды макияжа.",
    )


@bp_base.get("/about-me")
def about():
    return render_template(
        "main/about.html",
        page_title="Обо мне - Визажист Елена Долгорукая",
        meta_descr_content="Сертифицированный визажист. Преподаватель курсов визажа (макияжа).",
    )


@bp_base.get("/portfolio")
def portfolio():
    return render_template(
        "main/portfolio.html",
        page_title="Профессиональный макияж любой сложности",
        meta_descr_content="Любые виды макияжа Минск. Современные образы.",
    )


@bp_base.get("/price-page")
def price_page():
    return render_template(
        "main/price_page.html",
        page_title="Цена на макияж в Минске, визажист Елена Долгорукая",
        meta_descr_content="Услуги - Макияж в городе Минск. Цена - Свадебный, вечерний, дневной "
        "макияж, лифтинг-макияж, макияж для фотосессии, смоки айс.",
    )


@bp_base.route("/contacts", methods=["GET", "POST"])
def contact_page():
    form = OrderForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if not send_email(form=form):
                return jsonify({"message": "Failed to send an e-mail"}), 500
            return jsonify({"message": "The email was successfully sent"}), 200
        else:
            return jsonify(form.errors), 400
    return render_template(
        "main/contact.html",
        form=form,
        page_title="Визажист Минск. Профессиональный макияж Минск",
        meta_descr_content="Елена Долгорукая визажист в городе Минск. Все виды макияжа. Заказать макияж онлайн.",
    )
