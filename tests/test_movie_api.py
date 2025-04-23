def test_get_empty_movies(client):
    response = client.get("/api/movies/")
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_movie(client):
    data = {
        "title": "The Matrix",
        "director": "Wachowskis",
        "year": 1999
    }
    response = client.post("/api/movies/", json=data)
    assert response.status_code == 201
    assert response.get_json()["title"] == "The Matrix"

def test_update_movie(client):
    # Tạo trước
    client.post("/api/movies/", json={"title": "Old Title"})
    
    # Cập nhật
    response = client.put("/api/movies/1", json={"title": "New Title"})
    assert response.status_code == 200
    assert response.get_json()["title"] == "New Title"

def test_delete_movie(client):
    # Tạo trước
    client.post("/api/movies/", json={"title": "Delete Me"})

    # Xoá
    response = client.delete("/api/movies/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Phim đã bị xoá"
