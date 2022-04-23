def test_index_success(client):
    #Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_login_success(client):
    #Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_register_success(client):
    #Page loads
    response = client.get('/register')
    assert response.status_code == 200

def test_logout_success(client):
    #Page redirects
    response = client.get('/logout')
    assert response.status_code == 302