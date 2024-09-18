from fastapi import FastAPI
from pydantic import BaseModel
from src.plot_generator import generate_timeline, generate_quadrant, generate_hierarchy, generate_mindmap
import requests
import os

# Imgur API
CLIENT_ID = '2e0f5606aa17a8f'
CLIENT_SECRET = '66634a39a6cd419e3ee5aada2897f375617fa3d4'

app = FastAPI()

# Function to upload image to Imgur
def upload_to_imgur(image_path):
    url = "https://api.imgur.com/3/image"
    headers = {
        'Authorization': f'Client-ID {CLIENT_ID}',
    }
    with open(image_path, 'rb') as img:
        response = requests.post(url, headers=headers, files={'image': img})
    if response.status_code == 200:
        return response.json()['data']['link']
    return None

# API to generate timeline
class TimelineRequest(BaseModel):
    page_title: str
    text_list: list
    data_list: list
    count: int

@app.post("/generate_timeline/")
async def generate_timeline_api(request: TimelineRequest):
    image_path = generate_timeline(request.page_title, request.text_list, request.data_list, request.count)
    imgur_link = upload_to_imgur(image_path)
    os.remove(image_path)  # Remove the local file after upload
    return {"imgur_link": imgur_link}

# API to generate quadrant
class QuadrantRequest(BaseModel):
    main_title: str
    x_axis_label: str
    y_axis_label: str
    quadrant_titles: list
    quadrant_contents: list

@app.post("/generate_quadrant/")
async def generate_quadrant_api(request: QuadrantRequest):
    image_path = generate_quadrant(request.main_title, request.x_axis_label, request.y_axis_label, request.quadrant_titles, request.quadrant_contents)
    imgur_link = upload_to_imgur(image_path)
    os.remove(image_path)
    return {"imgur_link": imgur_link}

# API to generate hierarchy
class HierarchyRequest(BaseModel):
    title: str
    levels: list

@app.post("/generate_hierarchy/")
async def generate_hierarchy_api(request: HierarchyRequest):
    image_path = generate_hierarchy(request.title, request.levels)
    imgur_link = upload_to_imgur(image_path)
    os.remove(image_path)
    return {"imgur_link": imgur_link}

# API to generate mindmap
class MindMapRequest(BaseModel):
    title: str
    mindMapData: dict

@app.post("/generate_mindmap/")
async def generate_mindmap_api(request: MindMapRequest):
    image_path = generate_mindmap(request.title, request.mindMapData)
    imgur_link = upload_to_imgur(image_path)
    os.remove(image_path)
    return {"imgur_link": imgur_link}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
