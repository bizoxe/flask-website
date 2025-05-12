import datetime

import pytest
from flask import url_for

ORDER_DATE = datetime.datetime.now().date() + datetime.timedelta(days=1)
ORDER_TIME = datetime.datetime.now().time().strftime("%H:%M")


def is_success_res(client, path) -> None:
    resp = client.get(path)
    assert resp.status_code == 200


class TestBaseRoutes:

    def test_index(self, client) -> None:
        is_success_res(client, url_for("base.index"))

    def test_about(self, client) -> None:
        is_success_res(client, url_for("base.about"))

    def test_portfolio(self, client) -> None:
        is_success_res(client, url_for("base.portfolio"))

    def test_price_page(self, client) -> None:
        is_success_res(client, url_for("base.price_page"))

    def test_contact_page(self, client) -> None:
        is_success_res(client, url_for("base.contact_page"))

    def test_sitemap_xml(self, client) -> None:
        is_success_res(client, url_for("base.sitemap_xml"))

    def test_robots_txt(self, client) -> None:
        is_success_res(client, url_for("base.robots_txt"))


class TestContactPage:

    def test_contact_page_post_req(
        self,
        client,
        mock_send_email,
    ) -> None:
        data = {
            "name": "Пупкин",
            "phone": "+375(25)-708-22-22",
            "services": "лифтинг - макияж",
            "date": ORDER_DATE,
            "time": ORDER_TIME,
            "message": "получить консультацию",
        }
        response = client.post(url_for("base.contact_page"), data=data)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "data, status_code",
        [
            (
                {
                    "phone": "+375(25)-708-22-22",
                    "services": "лифтинг - макияж",
                    "date": ORDER_DATE,
                    "time": ORDER_TIME,
                    "message": "получить консультацию",
                },
                400,
            ),
            (
                {
                    "name": "Пупкин",
                    "services": "лифтинг - макияж",
                    "date": ORDER_DATE,
                    "time": ORDER_TIME,
                    "message": "получить консультацию",
                },
                400,
            ),
            (
                {
                    "name": "Пупкин",
                    "phone": "+375(25)-708-22-22",
                    "date": ORDER_DATE,
                    "time": ORDER_TIME,
                    "message": "получить консультацию",
                },
                400,
            ),
        ],
    )
    def test_contact_invalid_input(
        self,
        client,
        data,
        status_code,
    ) -> None:
        response = client.post(url_for("base.contact_page"), data=data)
        assert response.status_code == status_code

    def test_contact_send_email_failed(
        self,
        client,
        mock_send_email_failed,
    ) -> None:
        data = {
            "name": "Пупкин",
            "phone": "+375(25)-708-22-22",
            "services": "лифтинг - макияж",
            "date": ORDER_DATE,
            "time": ORDER_TIME,
            "message": "получить консультацию",
        }
        response = client.post(url_for("base.contact_page"), data=data)
        msg = response.json["message"]
        assert response.status_code == 500
        assert msg == "Failed to send an e-mail"
