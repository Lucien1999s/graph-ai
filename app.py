from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.plot_generator import generate_timeline, generate_quadrant, generate_hierarchy, generate_mindmap

app = FastAPI()

# API 請求模型
class ChartRequest(BaseModel):
    chart_type: str  # 圖表類型
    data: dict  # 圖表所需數據，具體格式依據 chart_type 而定

# 單一 API，根據 chart_type 呼叫對應的生成函數
@app.post("/generate_chart/")
async def generate_chart_api(request: ChartRequest):
    # 根據 chart_type 決定調用哪個函數
    if request.chart_type == "timeline":
        try:
            page_title = request.data["page_title"]
            text_list = request.data["time_list"]
            data_list = request.data["data_list"]
            count = request.data["count"]
            html_url = generate_timeline(page_title, text_list, data_list, count)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid data format for timeline")
    elif request.chart_type == "quadrant":
        try:
            main_title = request.data["main_title"]
            x_axis_label = request.data["x_axis_label"]
            y_axis_label = request.data["y_axis_label"]
            quadrant_titles = request.data["quadrant_titles"]
            quadrant_contents = request.data["quadrant_contents"]
            html_url = generate_quadrant(main_title, x_axis_label, y_axis_label, quadrant_titles, quadrant_contents)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid data format for quadrant")
    elif request.chart_type == "hierarchy":
        try:
            title = request.data["title"]
            levels = request.data["levels"]
            html_url = generate_hierarchy(title, levels)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid data format for hierarchy")
    elif request.chart_type == "mindmap":
        try:
            title = request.data["title"]
            mindMapData = request.data["mindMapData"]
            html_url = generate_mindmap(title, mindMapData)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid data format for mindmap")
    else:
        raise HTTPException(status_code=400, detail="Invalid chart type")

    return {"url": html_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
