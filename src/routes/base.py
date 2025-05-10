"""
Main pages of the site.
"""

from flask import (
    jsonify,
    render_template,
    request,
)

from src.orders.forms import OrderForm
from src.orders.mailing import send_email
from src.routes import bp_base


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
