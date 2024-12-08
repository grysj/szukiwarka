# Szukiwarka
![image](https://github.com/user-attachments/assets/aeee62e9-65a5-4ed9-b77c-0b68e8325354)

## How to run

### Basic requirements
Before instalation make sure you kave `poetry` library installed. Unfortunatelu due to the size of some files, you need to [download this folder](https://mega.nz/file/inpngSBS#ETXbYKmKtvuEJmqa3S86kP8PySfVFaWpz3ERXcEvM7U)
and unzip it in `backend`.


In root directory of the project, run 

```bash
cd backend/
poetry install
poetry shell --no-root
uvicorn main:app --reload
```
and wait until all files are downloaded.

In root project open another terminal and run
```bash
cd frontend
npm install
npm run
```

