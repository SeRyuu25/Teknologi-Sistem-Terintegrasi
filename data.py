from http.client import HTTPException
import json
from fastapi import FastAPI
with open("data.json", "r") as read_file:
	data = json.load(read_file)
app = FastAPI()
@app.get("/")
async def root():
	return{"Page":"Root"}
@app.get('/data/{item_id}')
async def read_data():
	dictMahasiswa = []
	for dataMahasiswa in data['data']:
		dictMahasiswa.append(dataMahasiswa)
	return dictMahasiswa

	raise HTTPException(
		status_code=404, detail=f'Item not found'
	)
