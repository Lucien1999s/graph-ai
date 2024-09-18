import tempfile
import random
import string
from src.template import TEMPLATE
from html2image import Html2Image
import os
import json

def _gen_hashid(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def _html_to_png(html_file, output_png):
    hti = Html2Image(browser_executable="/app/.apt/usr/bin/google-chrome")
    hti.screenshot(html_file=html_file, save_as=output_png)

def generate_timeline(page_title, text_list, data_list, count):
    html_template = TEMPLATE['timeline']
    text_list_js = str(text_list).replace("'", '"')
    data_list_js = str(data_list).replace("'", '"')
    html_content = html_template.format(page_title=page_title, text_list=text_list_js, data_list=data_list_js, count=count)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as tmp_html:
        tmp_html.write(html_content)
        tmp_html_path = tmp_html.name

    hash_id = _gen_hashid()
    output_png = f"timeline_{hash_id}.png"
    _html_to_png(tmp_html_path, output_png)
    os.remove(tmp_html_path)
    return output_png

def generate_quadrant(main_title, x_axis_label, y_axis_label, quadrant_titles, quadrant_contents):
    html_template = TEMPLATE['quadrant']
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
        quadrant_contents=quadrant_contents_js
    )
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as tmp_html:
        tmp_html.write(html_content)
        tmp_html_path = tmp_html.name
    hash_id = _gen_hashid()
    output_png = f"quadrant_{hash_id}.png"
    _html_to_png(tmp_html_path, output_png)
    os.remove(tmp_html_path)
    return output_png


def generate_hierarchy(title, levels):
    html_template = TEMPLATE['hierarchy']

    title_js = title.replace('"', '\\"')
    levels_js = json.dumps(levels, ensure_ascii=False)

    html_content = html_template.format(
        page_title=title_js,
        title=title_js,
        levels=levels_js
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as tmp_html:
        tmp_html.write(html_content)
        tmp_html_path = tmp_html.name

    hash_id = _gen_hashid()
    output_png = f"hierarchy_{hash_id}.png"
    _html_to_png(tmp_html_path, output_png)
    os.remove(tmp_html_path)
    return output_png


def generate_mindmap(title, mindMapData):
    html_template = TEMPLATE['mindmap']
    title_js = title.replace('"', '\\"')
    mindMapData_js = json.dumps(mindMapData, ensure_ascii=False)
    html_content = html_template.format(
        title=title_js,
        mindMapData=mindMapData_js
    )
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as tmp_html:
        tmp_html.write(html_content)
        tmp_html_path = tmp_html.name
    hash_id = _gen_hashid()
    output_png = f"mindmap_{hash_id}.png"
    _html_to_png(tmp_html_path, output_png)
    os.remove(tmp_html_path)
    return output_png


if __name__ == "__main__":
    # Timeline example
    page_title="哈哈哈哈哈"
    text_list = ["這是1", "這是2", "這是3", "這是4", "這是5"]
    data_list = [
        {"title": "標題 1", "content": "內文內容 1"},
        {"title": "標題 2", "content": "內文內容 2"},
        {"title": "標題 3", "content": "內文內容 3"},
        {"title": "標題 4", "content": "內文內容 4"},
        {"title": "標題 5", "content": "內文內容 5"}
    ]
    count = 5
    png_path = generate_timeline(page_title, text_list, data_list, count)
    print(f"生成的 PNG 文件路徑: {png_path}")

    # Quadrant example
    # main_title = '重要性與緊急性矩陣'
    # x_axis_label = '重要性'
    # y_axis_label = '緊急性'

    # quadrant_titles = [
    #     '象限一（高重要性，高緊急性）',
    #     '象限二（高重要性，低緊急性）',
    #     '象限三（低重要性，高緊急性）',
    #     '象限四（低重要性，低緊急性）'
    # ]

    # quadrant_contents = [
    #     ['處理客戶投訴', '解決系統故障', '項目截止日期'],
    #     ['制定長期戰略', '員工培訓', '建立客戶關係'],
    #     ['參加不相關的會議', '處理部分電子郵件'],
    #     ['瀏覽社交媒體', '無意義的娛樂活動', '瀏覽社交媒體', '無意義的娛樂活動']
    # ]

    # output_png = generate_quadrant(
    #     main_title,
    #     x_axis_label,
    #     y_axis_label,
    #     quadrant_titles,
    #     quadrant_contents
    # )

    # print(f"生成的四象限圖文件：{output_png}")

    # # Hierarchy example
    # test_title = "測試的金字塔階層圖"
    # test_levels = [
    #     "頂層管理",
    #     "中層管理",
    #     "基層員工",
    #     "操作人員",
    #     "基礎設施"
    # ]
    # png_file = generate_hierarchy(test_title, test_levels)
    # print(f"生成的 PNG 文件: {png_file}")

    # # Mind map example
    # title = "我的心智图"
    # mindMapData = {
    #     "text": "中心主题",
    #     "children": [
    #         {
    #             "text": "子主题 1",
    #             "children": [
    #                 {
    #                     "text": "子主题 1-1",
    #                     "children": [
    #                         {"text": "子主题 1-1-1"},
    #                         {"text": "子主题 1-1-2"}
    #                     ]
    #                 },
    #                 {"text": "子主题 1-2"}
    #             ]
    #         },
    #         {
    #             "text": "子主题 2",
    #             "children": [
    #                 {
    #                     "text": "子主题 2-1",
    #                     "children": [
    #                         {"text": "子主题 2-1-1"},
    #                         {"text": "子主题 2-1-2"},
    #                         {"text": "子主题 2-1-3"},
    #                         {"text": "子主题 2-1-4"}
    #                     ]
    #                 },
    #                 {"text": "子主题 2-2"},
    #                 {"text": "子主题 2-3"}
    #             ]
    #         },
    #         {
    #             "text": "子主题 3",
    #             "children": [
    #                 {"text": "子主题 3-1",
    #                  "children": [
    #                         {"text": "子主题 2-1-1"},
    #                         {"text": "子主题 2-1-2"},
    #                     ]},
    #                 {"text": "子主题 3-2",
    #                  "children": [
    #                         {"text": "子主题 2-2-1"},
    #                         {"text": "子主题 2-2-2"},
    #                     ]}
    #             ]
    #         }
    #     ]
    # }
    # output_png = generate_mindmap(title, mindMapData)
    # print(f"心智图已生成：{output_png}")
