from app.main_pages import models


def test_todolist_success(client):
    #Page loads
    response = client.get('pomodoro.todolist')
    assert response.status_code == 404

def test_deletion_success(client):
    #Page loads
    response = client.get('pomodoro.delete')
    assert response.status_code == 404