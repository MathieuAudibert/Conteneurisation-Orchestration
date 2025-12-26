import pytest
from db.classes.connect import ConnectDB

class FakeMongoClient:
    def __init__(self, uri):
        self.uri = uri
        self.closed = False

    def __getitem__(self, name):
        return {"_fake_db_name": name}

    def close(self):
        self.closed = True

class FakeBadMongoClient: 
    def __init__(self, uri):
        raise RuntimeError("caca")

def test_connect_read_only_success(monkeypatch, capsys):
    monkeypatch.setattr("cfg.db.classes.connect.MongoClient", FakeMongoClient)
    monkeypatch.setenv("MONGO_URI", "mongodb://localhost:27017")

    con = ConnectDB(adm=False)
    con.connect()
    assert isinstance(con.client, FakeMongoClient)
    assert con.db == {"_fake_db_name": "Cars"}
    captured = capsys.readouterr()
    assert "[INFO]: succesfully connected to db as **READ ONLY**" in captured.out

    con.disconnect()
    assert con.client.closed is True
    captured = capsys.readouterr()
    assert "[INFO]: disconnected successfully" in captured.out


def test_connect_admin_success(monkeypatch, capsys):
    monkeypatch.setattr("cfg.db.classes.connect.MongoClient", FakeMongoClient)
    monkeypatch.setenv("ADM_MONGO_URI", "mongodb://admin:27017")

    con = ConnectDB(adm=True)
    con.connect()
    assert isinstance(con.client, FakeMongoClient)
    assert con.db == {"_fake_db_name": "Cars"}
    captured = capsys.readouterr()
    assert "[INFO]: succesfully connected to db as **ADMIN**" in captured.out

    con.disconnect()
    assert con.client.closed is True


def test_connect_raises_exception(monkeypatch, capsys):
    monkeypatch.setattr("cfg.db.classes.connect.MongoClient", FakeBadMongoClient)
    monkeypatch.setenv("MONGO_URI", "mongodb://localhost:27017")
    con = ConnectDB(adm=False)
    con.connect()

    assert con.client is None
    captured = capsys.readouterr()
    assert "[ERROR]: error while connecting to db - boom" in captured.out
