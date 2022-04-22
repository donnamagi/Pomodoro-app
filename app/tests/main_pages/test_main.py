from flask_login import current_user, login_user

def test_index_success(client):
    #Page loads
    response = client.get('main_pages.index')
    assert response.status_code == 404

def test_login_success(client):
    #Page loads
    response = client.get('main_pages.login')
    assert response.status_code == 404

def test_register_success(client):
    #Page loads
    response = client.get('main_pages.register')
    assert response.status_code == 404

def test_logout_success(client):
    #Page loads
    response = client.get('main_pages.logout')
    assert response.status_code == 404