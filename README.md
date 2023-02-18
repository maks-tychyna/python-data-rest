# python-data-rest

## Usage
### 1. Ensure you have Python installed:
```bash
python -V
```

### 2. Create Virtual env
```bash
python -m venv ./env
```

### 3. Activate Virtual env
```bash
./env/Scripts/activate
```

### 4. Install packages in Virtual env
```bash
./env/Scripts/pip install -r src/requirements.txt
```

### 5. Run the server with one of the following commands:
```bash
PYTHONPATH=src ./env/Scripts/uvicorn backend.server:app --reload
```

```bash
PYTHONPATH=src ./env/Scripts/python -m backend
```

### 6. Navigate to the following URL in Browser to view REST API endpoints
- [Swagger UI](http://127.0.0.1:8000/docs)
