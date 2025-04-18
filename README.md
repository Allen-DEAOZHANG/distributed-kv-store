# Distributed Key-Value Store

A lightweight distributed key-value store implemented in Python using Flask. This project simulates core components of distributed systems such as data partitioning, concurrent access, and eventual consistency.

---

## 📌 Features

- Multiple Flask-based nodes acting as independent KV stores
- Consistent hashing to determine responsible nodes
- Simple GET, PUT, DELETE operations with REST API
- Basic simulation of concurrent writes and eventual consistency

---

## 🧠 Architecture

```
Client → Load Balancer → [Node 1, Node 2, Node 3]
          (Consistent Hashing Based Routing)
```

---

## 🚀 How to Run

> Requires Python 3.8+

```bash
pip install -r requirements.txt
python node.py --port 5000
python node.py --port 5001
python node.py --port 5002
```

Send requests using curl or Postman:
```bash
curl -X PUT http://localhost:5000/kv/testkey -d "value=testvalue"
curl http://localhost:5000/kv/testkey
```

---

## 🧑‍💻 Author

Deao Zhang  
Waseda University
