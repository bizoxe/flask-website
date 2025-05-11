from flask import render_template

from src.routes import bp_blog


@bp_blog.get("/blog-one")
def blog_one():
    return render_template(
        "blog/blog_one.html",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="Дневной макияж. Вечерний макияж. Лифтинг-макияж.",
    )


@bp_blog.get("/blog-two")
def blog_two():
    return render_template(
        "blog/blog_two.html",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="Свадебный макияж. Макияж для фотосессии. Публикации работ визажиста "
        "в зарубежных журналах.",
    )


@bp_blog.get("/everyday-makeup")
def blog_everyday():
    return render_template(
        "blog/blog_everyday.html",
        title_h1="Читать",
        title_h6="дневной макияж",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ЧИТАТЬ дневной макияж акценты макияж на каждый день",
    )


@bp_blog.get("/evening-makeup")
def blog_evening():
    return render_template(
        "blog/blog_evening.html",
        title_h1="Читать",
        title_h6="вечерний макияж",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ЧИТАТЬ правильно подобрать вечерний макияж",
    )


@bp_blog.get("/lifting-makeup")
def blog_lifting():
    return render_template(
        "blog/blog_lifting.html",
        title_h1="Читать",
        title_h6="лифтинг-макияж",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ЧИТАТЬ особенности лифтинг-макияжа возрастной макияж",
    )


@bp_blog.get("/bridal-makeup")
def blog_bridal():
    return render_template(
        "blog/blog_bridal.html",
        title_h1="Читать",
        title_h6="свадебный макияж",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ЧИТАТЬ свадебный макияж идеальный образ для невесты",
    )


@bp_blog.get("/photo-shoot")
def blog_photo_shoot():
    return render_template(
        "blog/blog_photo_shoot.html",
        title_h1="Читать",
        title_h6="макияж для фотосессии",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ЧИТАТЬ рекомендации макияж для фотосессии",
    )


@bp_blog.get("/publications-journals")
def blog_magazines():
    return render_template(
        "blog/blog_magazines.html",
        title_h1="Блог",
        title_h6="публикации в журналах",
        page_title="Блог - Профессиональный макияж. Визажист Минск",
        meta_descr_content="ПУБЛИКАЦИИ ВИЗАЖИСТА В ЖУРНАЛАХ Edith, Malvie, Editorial, The Mermaid, Vigour",
    )
