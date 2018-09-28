
def test_details_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.details_contact()
    app.session.logout()
