import json
import random
import string
from dotenv import load_dotenv
import os
from github import Github
from src.template import TEMPLATE

load_dotenv()

# GitHub token and repo details
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
BRANCH_NAME = os.getenv('BRANCH_NAME')
g = Github(GITHUB_TOKEN)

# Function to generate a hash ID
def _gen_hashid(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

# Function to upload HTML file to GitHub Pages
def upload_html_to_github(file_path, commit_message="Upload HTML file"):
    try:
        repo = g.get_repo(REPO_NAME)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        file_name = os.path.join('docs', os.path.basename(file_path))
        try:
            contents = repo.get_contents(file_name, ref=BRANCH_NAME)
            repo.update_file(contents.path, commit_message, content, contents.sha, branch=BRANCH_NAME)
            print(f"已更新文件：{file_name}")
        except:
            repo.create_file(file_name, commit_message, content, branch=BRANCH_NAME)
            print(f"已創建文件：{file_name}")
        url = f"https://{REPO_NAME}/{os.path.basename(file_path)}"
        _refresh_github_pages(repo)
        return url
    except Exception as e:
        print(f"上傳失敗：{e}")
        return None

# Function to force refresh GitHub Pages
def _refresh_github_pages(repo):
    try:
        readme = repo.get_contents("README.md", ref=BRANCH_NAME)
        updated_content = readme.decoded_content.decode() + " "
        repo.update_file(readme.path, "Force refresh GitHub Pages", updated_content, readme.sha, branch=BRANCH_NAME)
    except Exception as e:
        print(f"刷新失敗：{e}")

# Function to delete file from GitHub
def delete_file_from_github(file_name, commit_message="Delete HTML file"):
    try:
        repo = g.get_repo(REPO_NAME)
        file_path = os.path.join('docs', file_name)
        contents = repo.get_contents(file_path, ref=BRANCH_NAME)
        repo.delete_file(contents.path, commit_message, contents.sha, branch=BRANCH_NAME)
        print(f"已刪除文件：{file_name}")
        return True
    except Exception as e:
        print(f"刪除失敗：{e}")
        return False

# Function to generate timeline HTML
def generate_timeline(page_title, text_list, data_list, count):
    html_template = TEMPLATE["timeline"]
    text_list_js = str(text_list).replace("'", '"')
    data_list_js = str(data_list).replace("'", '"')

    html_content = html_template.format(
        page_title=page_title,
        text_list=text_list_js,
        data_list=data_list_js,
        count=count,
    )

    hash_id = _gen_hashid()
    output_html = f"timeline_{hash_id}.html"

    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    
    # Upload to GitHub and delete locally
    url = upload_html_to_github(output_html)
    os.remove(output_html)
    return url

# Function to generate quadrant HTML
def generate_quadrant(main_title, x_axis_label, y_axis_label, quadrant_titles, quadrant_contents):
    html_template = TEMPLATE["quadrant"]
    main_title_js = '"' + main_title.replace('"', '\\"') + '"'
    x_axis_label_js = '"' + x_axis_label.replace('"', '\\"') + '"'
    y_axis_label_js = '"' + y_axis_label.replace('"', '\\"') + '"'
    quadrant_titles_js = str(quadrant_titles).replace("'", '"')
    quadrant_contents_js = str(quadrant_contents).replace("'", '"')

    html_content = html_template.format(
        main_title=main_title_js,
        x_axis_label=x_axis_label_js,
        y_axis_label=y_axis_label_js,
        quadrant_titles=quadrant_titles_js,
        quadrant_contents=quadrant_contents_js,
    )

    hash_id = _gen_hashid()
    output_html = f"quadrant_{hash_id}.html"

    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Upload to GitHub and delete locally
    url = upload_html_to_github(output_html)
    os.remove(output_html)
    return url

# Function to generate hierarchy HTML
def generate_hierarchy(title, levels):
    html_template = TEMPLATE["hierarchy"]
    title_js = title.replace('"', '\\"')
    levels_js = json.dumps(levels, ensure_ascii=False)

    html_content = html_template.format(
        page_title=title_js, title=title_js, levels=levels_js
    )

    hash_id = _gen_hashid()
    output_html = f"hierarchy_{hash_id}.html"

    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Upload to GitHub and delete locally
    url = upload_html_to_github(output_html)
    os.remove(output_html)
    return url

# Function to generate mindmap HTML
def generate_mindmap(title, mindMapData):
    html_template = TEMPLATE["mindmap"]
    title_js = title.replace('"', '\\"')
    mindMapData_js = json.dumps(mindMapData, ensure_ascii=False)

    html_content = html_template.format(title=title_js, mindMapData=mindMapData_js)

    hash_id = _gen_hashid()
    output_html = f"mindmap_{hash_id}.html"

    with open(output_html, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    # Upload to GitHub and delete locally
    url = upload_html_to_github(output_html)
    os.remove(output_html)
    return url

# Example usage
if __name__ == "__main__":
    # Example for generating and uploading a timeline HTML
    page_title = "時間軸示例"
    text_list = ["事件1", "事件2", "事件3", "事件4", "事件5"]
    data_list = [
        {"title": "事件1", "content": "描述1"},
        {"title": "事件2", "content": "描述2"},
        {"title": "事件3", "content": "描述3"},
        {"title": "事件4", "content": "描述4"},
        {"title": "事件5", "content": "描述5"},
    ]
    count = 5
    timeline_url = generate_timeline(page_title, text_list, data_list, count)
    print(f"時間軸網址: {timeline_url}")

    # Example for generating and uploading a quadrant HTML
    main_title = "重要性與緊急性矩陣"
    x_axis_label = "重要性"
    y_axis_label = "緊急性"
    quadrant_titles = [
        "象限一（高重要性，高緊急性）",
        "象限二（高重要性，低緊急性）",
        "象限三（低重要性，高緊急性）",
        "象限四（低重要性，低緊急性）",
    ]
    quadrant_contents = [
        ["處理客戶投訴", "解決系統故障", "項目截止日期"],
        ["制定長期戰略", "員工培訓", "建立客戶關係"],
        ["參加不相關的會議", "處理部分電子郵件"],
        ["瀏覽社交媒體", "無意義的娛樂活動", "瀏覽社交媒體", "無意義的娛樂活動"],
    ]
    quadrant_url = generate_quadrant(main_title, x_axis_label, y_axis_label, quadrant_titles, quadrant_contents)
    print(f"四象限圖的網址: {quadrant_url}")

    # Example for generating and uploading a hierarchy HTML
    hierarchy_title = "公司層級"
    hierarchy_levels = ["高層管理", "中層管理", "基層員工", "操作人員", "基礎設施"]
    hierarchy_url = generate_hierarchy(hierarchy_title, hierarchy_levels)
    print(f"層級圖網址: {hierarchy_url}")

    # Example for generating and uploading a mindmap HTML
    mindmap_title = "心智圖示例"
    mindmap_data = {
        "text": "中心主題",
        "children": [
            {
                "text": "子主題 1",
                "children": [
                    {"text": "子主題 1-1", "children": [{"text": "子主題 1-1-1"}, {"text": "子主題 1-1-2"}]},
                    {"text": "子主題 1-2"}
                ]
            },
            {
                "text": "子主題 2",
                "children": [
                    {"text": "子主題 2-1", "children": [{"text": "子主題 2-1-1"}, {"text": "子主題 2-1-2"}]},
                    {"text": "子主題 2-2"},
                    {"text": "子主題 2-3"}
                ]
            }
        ]
    }
    mindmap_url = generate_mindmap(mindmap_title, mindmap_data)
    print(f"心智圖網址: {mindmap_url}")
