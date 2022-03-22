def test_index_success(client):
    #Page loads
    response = client.get('main_pages.index')
    assert response.status_code == 404

def test_login_success(client):
    #Page loads
    response = client.get('main_pages.login')
    assert response.status_code == 404