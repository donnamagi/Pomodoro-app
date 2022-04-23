def test_todolist_success(client):
    #Page redirects
    response = client.get('/todolist')
    assert response.status_code == 302
