from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

malware_data = [
    {
        "id": 1,
        "name": "Koi Stealer",
        "type": "Infostealer",
        "platform": "Windows"
    },
    {
        "id": 2,
        "name": "Emotet",
        "type": "Trojan",
        "platform": "Windows"
    },
    {
        "id": 3,
        "name": "Mirai",
        "type": "Botnet",
        "platform": "Linux"
    }    
]

@app.get("/")
def root():
    return{
        "project": "Database Kejahatan Siber"
    }

@app.get("/malware")
def get_malware():
    return malware_data

@app.get("/malware/{malware_id}")
def get_malware_by_id(malware_id: int):

    for malware in malware_data:

        if malware["id"] == malware_id:
            return malware
    
    return {
        "error": "Malware not found"
    }

@app.get("/search")
def search_malware(
    type: str = Query(None),
    platform: str = Query(None)
):
    result = []

    for malware in malware_data:

        if type and malware["type"] !=type:
            continue

        if platform and malware["platform"] !=platform:
            continue

        result.append(malware)
                
    return result

@app.post("/malware")
def create_malware(
    malware: dict
):
    return {
        "message": "Database diterima",
        "data": malware
    }