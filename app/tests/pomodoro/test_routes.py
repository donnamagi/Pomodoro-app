def test_todolist_success(client):
    #Page loads
    response = client.get('pomodoro.todolist')
    assert response.status_code == 404
