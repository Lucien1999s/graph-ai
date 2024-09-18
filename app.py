from fastapi import FastAPI
from pydantic import BaseModel
from src.plot_generator import generate_timeline, generate_quadrant, generate_hierarchy, generate_mindmap
import os

app = FastAPI()

# API to generate timeline
class TimelineRequest(BaseModel):
    page_title: str
    text_list: list
    data_list: list
    count: int

@app.post("/generate_timeline/")
async def generate_timeline_api(request: TimelineRequest):
    # 生成 timeline 的 HTML 文件並上傳到 GitHub Pages
    html_url = generate_timeline(request.page_title, request.text_list, request.data_list, request.count)
    return {"url": html_url}

# API to generate quadrant
class QuadrantRequest(BaseModel):
    main_title: str
    x_axis_label: str
    y_axis_label: str
    quadrant_titles: list
    quadrant_contents: list

@app.post("/generate_quadrant/")
async def generate_quadrant_api(request: QuadrantRequest):
    # 生成 quadrant 的 HTML 文件並上傳到 GitHub Pages
    html_url = generate_quadrant(request.main_title, request.x_axis_label, request.y_axis_label, request.quadrant_titles, request.quadrant_contents)
    return {"url": html_url}

# API to generate hierarchy
class HierarchyRequest(BaseModel):
    title: str
    levels: list

@app.post("/generate_hierarchy/")
async def generate_hierarchy_api(request: HierarchyRequest):
    # 生成 hierarchy 的 HTML 文件並上傳到 GitHub Pages
    html_url = generate_hierarchy(request.title, request.levels)
    return {"url": html_url}

# API to generate mindmap
class MindMapRequest(BaseModel):
    title: str
    mindMapData: dict

@app.post("/generate_mindmap/")
async def generate_mindmap_api(request: MindMapRequest):
    # 生成 mindmap 的 HTML 文件並上傳到 GitHub Pages
    html_url = generate_mindmap(request.title, request.mindMapData)
    return {"url": html_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
