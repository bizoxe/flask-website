from flask import url_for


def is_success_res(client, path) -> None:
    resp = client.get(path)
    assert resp.status_code == 200


class TestBlogPages:

    def test_blog_one(self, client) -> None:
        is_success_res(client, url_for("blog.blog_one"))

    def test_blog_two(self, client) -> None:
        is_success_res(client, url_for("blog.blog_two"))

    def test_blog_everyday(self, client) -> None:
        is_success_res(client, url_for("blog.blog_everyday"))

    def test_blog_evening(self, client) -> None:
        is_success_res(client, url_for("blog.blog_evening"))

    def test_blog_lifting(self, client) -> None:
        is_success_res(client, url_for("blog.blog_lifting"))

    def test_blog_bridal(self, client) -> None:
        is_success_res(client, url_for("blog.blog_bridal"))

    def test_blog_photo_shoot(self, client) -> None:
        is_success_res(client, url_for("blog.blog_photo_shoot"))

    def test_blog_magazines(self, client) -> None:
        is_success_res(client, url_for("blog.blog_magazines"))
