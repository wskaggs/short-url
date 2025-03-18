from fastapi.testclient import TestClient


def test_database_uri(test_client: TestClient) -> None:
    """
    Temporary test to validate testing configurations are working
    """
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"database_uri": "sqlite:///:memory:"}
