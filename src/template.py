TEMPLATE = {
     "timeline": '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{page_title}</title>  <!-- 動態設置頁面標題 -->
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                display: flex;
                flex-direction: column;
                background-color: #FAF0E6; /* 設定整體背景色 */
            }}

            .title {{
                font-size: 40px;  /* 增大主標題字體 */
                font-weight: bold;
                text-align: center;
                margin: 30px 0;  /* 增大間距 */
            }}

            .container {{
                flex-grow: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
            }}

            .line-container {{
                display: flex;
                align-items: center;
                width: 100%;
            }}

            .line {{
                flex-grow: 1;
                border-top: 3px solid black;  /* 加粗時間線 */
                margin: 0;
            }}

            .rectangle-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                position: relative;
                width: auto;
            }}

            .rectangle {{
                width: 120px;    /* 增大方框寬度 */
                height: 60px;    /* 增大方框高度 */
                border: 3px solid black;  /* 加粗方框邊框 */
                box-sizing: border-box;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 18px;  /* 增大方框內文字 */
            }}

            .vertical-line {{
                width: 3px;     /* 加粗垂直線 */
                height: 150px;  /* 增加垂直線高度 */
                background-color: black;
                position: absolute;
            }}

            .up {{
                top: -150px;    /* 調整垂直線位置 */
            }}

            .down {{
                bottom: -150px; /* 調整垂直線位置 */
            }}

            /* 新增文字的樣式 */
            .text-above-line {{
                position: absolute;
                text-align: center;
                white-space: normal;
                width: 400%;   /* 增加文字區域寬度 */
                max-width: 1000px;
                padding: 10px;  /* 增加內邊距 */
            }}

            .up-text {{
                top: -230px;    /* 調整文字位置 */
            }}

            .down-text {{
                bottom: -230px; /* 調整文字位置 */
            }}

            /* 標題和內文樣式 */
            .title-text {{
                font-size: 20px;   /* 增大標題字體 */
                font-weight: bold;
                margin-bottom: 5px; /* 增加標題和內容間距 */
            }}

            .body-text {{
                font-size: 18px;    /* 增大內文字體 */
            }}
        </style>
    </head>
    <body>

    <div class="title">{page_title}</div>  <!-- 動態設置頁面內部標題 -->

    <div class="container">
        <div class="line-container" id="lineContainer">
            <!-- 長方形將動態插入 -->
        </div>
    </div>

    <script>
        function createRectangles(textList, dataList, count) {{
            if (count < 3) count = 3;
            if (count > 10) count = 10;

            const lineContainer = document.getElementById('lineContainer');
            lineContainer.innerHTML = '';

            for (let i = 0; i < count; i++) {{
                const line = document.createElement('div');
                line.className = 'line';
                lineContainer.appendChild(line);

                const rectangleContainer = document.createElement('div');
                rectangleContainer.className = 'rectangle-container';

                const verticalLine = document.createElement('div');
                verticalLine.className = 'vertical-line';

                if (i % 2 === 0) {{
                    verticalLine.classList.add('up');

                    const textAboveLine = document.createElement('div');
                    textAboveLine.className = 'text-above-line up-text';

                    const title = document.createElement('div');
                    title.className = 'title-text';
                    title.textContent = dataList[i].title;

                    const body = document.createElement('div');
                    body.className = 'body-text';
                    body.textContent = dataList[i].content;

                    textAboveLine.appendChild(title);
                    textAboveLine.appendChild(body);

                    rectangleContainer.appendChild(textAboveLine);
                }} else {{
                    verticalLine.classList.add('down');

                    const textAboveLine = document.createElement('div');
                    textAboveLine.className = 'text-above-line down-text';

                    const title = document.createElement('div');
                    title.className = 'title-text';
                    title.textContent = dataList[i].title;

                    const body = document.createElement('div');
                    body.className = 'body-text';
                    body.textContent = dataList[i].content;

                    textAboveLine.appendChild(title);
                    textAboveLine.appendChild(body);

                    rectangleContainer.appendChild(textAboveLine);
                }}

                rectangleContainer.appendChild(verticalLine);

                const rectangle = document.createElement('div');
                rectangle.className = 'rectangle';
                rectangle.textContent = textList[i];

                rectangleContainer.appendChild(rectangle);
                lineContainer.appendChild(rectangleContainer);
            }}

            const lastLine = document.createElement('div');
            lastLine.className = 'line';
            lineContainer.appendChild(lastLine);
        }}

        const textList = {text_list};
        const dataList = {data_list};
        const count = {count};

        createRectangles(textList, dataList, count);
    </script>

    </body>
    </html>
    ''',
    "quadrant": '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>{main_title}</title>
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                display: flex;
                flex-direction: column;
                background-color: #FAF0E6;
                overflow: hidden; /* 防止滾動條出現 */
            }}

            .title {{
                font-size: 40px; /* 主標題字體適當放大 */
                font-weight: bold;
                text-align: center;
                margin: 20px 0; /* 調整間距 */
            }}

            .quadrant-container {{
                flex-grow: 1;
                position: relative;
                width: 80%;
                margin: 0 auto;
                max-height: calc(100vh - 140px); /* 保持象限圖高度可見，避免滾動條 */
            }}

            .quadrant-table {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                grid-template-rows: 1fr 1fr;
                width: 100%;
                height: 100%;
                border-collapse: collapse;
                position: relative;
            }}

            .quadrant-cell {{
                border: 2px solid black;
                box-sizing: border-box;
                overflow: auto; /* 當內容超出時，啟用滾動條 */
                position: relative;
                padding: 15px; /* 調整內邊距 */
            }}

            /* 移除外框線 */
            .quadrant-cell:nth-child(1),
            .quadrant-cell:nth-child(2) {{
                border-top: transparent;
            }}

            .quadrant-cell:nth-child(1),
            .quadrant-cell:nth-child(3) {{
                border-left: transparent;
            }}

            .quadrant-cell:nth-child(2),
            .quadrant-cell:nth-child(4) {{
                border-right: transparent;
            }}

            .quadrant-cell:nth-child(3),
            .quadrant-cell:nth-child(4) {{
                border-bottom: transparent;
            }}

            /* 軸標籤樣式 */
            .x-axis-label, .y-axis-label {{
                position: absolute;
                font-size: 22px; /* 增大軸標籤字體 */
                font-weight: bold;
                background-color: #FAF0E6;
                padding: 5px;
            }}

            .x-axis-label {{
                bottom: -35px; /* 調整位置，保持在頁面內 */
                left: 50%;
                transform: translateX(-50%);
            }}

            .y-axis-label {{
                top: 50%;
                left: -60px; /* 調整位置，避免過多佔用空間 */
                transform: translateY(-50%) rotate(-90deg);
            }}

            /* 象限標題樣式 */
            .quadrant-title {{
                font-size: 20px; /* 略微增大象限標題字體 */
                font-weight: bold;
                margin-bottom: 10px;
            }}

            /* 象限內容樣式 */
            .quadrant-content {{
                font-size: 18px; /* 調整象限內容字體 */
            }}
        </style>
    </head>
    <body>

    <div class="title" id="mainTitle"></div>

    <div class="quadrant-container">
        <!-- 軸標籤 -->
        <div class="x-axis-label" id="xAxisLabel"></div>
        <div class="y-axis-label" id="yAxisLabel"></div>

        <div class="quadrant-table">
            <div class="quadrant-cell">
                <div class="quadrant-title" id="quadrantTitle1"></div>
                <ul class="quadrant-content" id="quadrantContent1">
                    <!-- 內容將通過JavaScript動態插入 -->
                </ul>
            </div>
            <div class="quadrant-cell">
                <div class="quadrant-title" id="quadrantTitle2"></div>
                <ul class="quadrant-content" id="quadrantContent2">
                    <!-- 內容將通過JavaScript動態插入 -->
                </ul>
            </div>
            <div class="quadrant-cell">
                <div class="quadrant-title" id="quadrantTitle3"></div>
                <ul class="quadrant-content" id="quadrantContent3">
                    <!-- 內容將通過JavaScript動態插入 -->
                </ul>
            </div>
            <div class="quadrant-cell">
                <div class="quadrant-title" id="quadrantTitle4"></div>
                <ul class="quadrant-content" id="quadrantContent4">
                    <!-- 內容將通過JavaScript動態插入 -->
                </ul>
            </div>
        </div>
    </div>

    <script>
        // 定義一個函數，用於生成四象限圖
        function createQuadrantChart(mainTitle, xAxisLabel, yAxisLabel, quadrantTitles, quadrantContents) {{
            // 設置主標題
            document.getElementById('mainTitle').textContent = mainTitle;

            // 設置軸標籤
            document.getElementById('xAxisLabel').textContent = xAxisLabel;
            document.getElementById('yAxisLabel').textContent = yAxisLabel;

            // 遍歷四個象限，設置標題和內容
            for (let i = 1; i <= 4; i++) {{
                // 設置象限標題
                document.getElementById('quadrantTitle' + i).textContent = quadrantTitles[i - 1];

                // 獲取象限內容的容器
                let contentList = document.getElementById('quadrantContent' + i);
                contentList.innerHTML = ''; // 清空內容

                // 插入列表項
                quadrantContents[i - 1].forEach(item => {{
                    let li = document.createElement('li');
                    li.textContent = item;
                    contentList.appendChild(li);
                }});
            }}
        }}

        // 調用函數生成四象限圖
        createQuadrantChart({main_title}, {x_axis_label}, {y_axis_label}, {quadrant_titles}, {quadrant_contents});
    </script>

    </body>
    </html>
    ''',
    "hierarchy": '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{page_title}</title> <!-- 動態設置頁面標題 -->
        <style>
            body, html {{
                height: 100%;
                width: 100%;
                margin: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: #FAF0E6;
            }}

            .title {{
                font-size: 40px; /* 調整標題字體 */
                font-weight: bold;
                text-align: center;
                position: absolute;
                top: 30px; /* 固定標題位置到正上方 */
                left: 50%;
                transform: translateX(-50%);
            }}

            .hierarchy-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                flex-grow: 1;
                width: 100%;  /* 設定階層圖的寬度 */
                margin-top: 150px; /* 調整距離 */
            }}

            .hierarchy-level {{
                width: 180%; /* 增大階層圖寬度 */
                margin: 20px 0; /* 增大每層之間的間距 */
                padding: 40px; /* 增加填充 */
                font-size: 30px; /* 調整層級文字大小 */
                text-align: center;
                font-weight: bold;
                color: white;
                border-radius: 20px; /* 長方形邊角圓滑 */
                word-wrap: break-word; /* 允許根據寬度自動換行 */
            }}

            /* 顏色列表 */
            .level-1 {{ background-color: #FF5733; width: 45%; }}
            .level-2 {{ background-color: #FF8D1A; width: 55%; }}
            .level-3 {{ background-color: #FFC300; width: 65%; }}
            .level-4 {{ background-color: #DAF7A6; width: 75%; color: black; }}
            .level-5 {{ background-color: #33C3FF; width: 85%; }}

            /* 手機響應式設計 */
            @media (max-width: 600px) {{
                .hierarchy-level {{
                    font-size: 18px;  /* 手機端調小文字 */
                    padding: 20px;
                }}
                .title {{
                    font-size: 40px; /* 手機端調小標題 */
                }}
            }}
        </style>
    </head>
    <body>

    <div class="title">{title}</div> <!-- 動態設置頁面標題 -->

    <div class="hierarchy-container">
        <!-- 各層的長方形將動態插入 -->
    </div>

    <script>
        function createRectangularHierarchy(title, levels) {{
            const container = document.querySelector('.hierarchy-container');

            // 清空先前的層級內容
            container.innerHTML = '';

            const rainbowColors = ['#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33C3FF'];
            const numLevels = Math.max(3, Math.min(5, levels.length));

            // 根據層數動態生成層次
            for (let i = 0; i < numLevels; i++) {{
                const levelDiv = document.createElement('div');
                levelDiv.className = `hierarchy-level level-${{i + 1}}`;

                // 動態設置文字內容和背景顏色
                levelDiv.textContent = levels[i];

                // 根據層級調整長度
                levelDiv.style.backgroundColor = rainbowColors[i];
                levelDiv.style.width = `${{45 + (i * 10)}}%`;  // 每層遞增長度

                container.appendChild(levelDiv);
            }}
        }}

        const title = "{title}";
        const levels = {levels};

        // 根據輸入的數據生成階層圖
        createRectangularHierarchy(title, levels);
    </script>

    </body>
    </html>
    ''',
    'mindmap': '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body, html {{
                height: 100%;
                width: 100%;
                margin: 0;
                overflow: hidden;
                position: relative;
                background-color: #FAF0E6;
            }}
            .title {{
                position: absolute;
                top: 10px;
                width: 100%;
                text-align: center;
                font-size: 40px;
                font-weight: bold;
            }}
            .node {{
                position: absolute;
                padding: 10px 20px; /* 增加内边距，节点变大 */
                background-color: #f1c40f;
                border-radius: 5px;
                text-align: center;
                font-size: 20px; /* 增加字体大小，节点变大 */
                box-sizing: border-box;
            }}
            .line {{
                position: absolute;
                width: 2px;
                background-color: #2c3e50;
                transform-origin: top left;
            }}
        </style>
    </head>
    <body>
        <!-- 标题 -->
        <div class="title">{title}</div>
        <!-- 心智图容器 -->
        <div id="mindmap"></div>
        <script>
            // 用户传入的心智图数据
            const mindMapData = {mindMapData};
            // 定义一级子节点的基本颜色
            const baseBranchColors = ["#e74c3c", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]; // 红、黄、绿、蓝、紫

            // 获取窗口尺寸
            let windowWidth = window.innerWidth;
            let windowHeight = window.innerHeight;

            // 存储每一层的节点，用于布局计算
            const levels = [];

            // 构建心智图
            function buildMindMap(data, level = 0, parent = null, parentColor = null, siblingIndex = 0, siblingCount = 1) {{
                let color;

                if (level === 0) {{
                    color = '#ffffff'; // 母节点为白色
                }} else if (level === 1) {{
                    // 一级子节点，分配基本颜色
                    color = baseBranchColors[siblingIndex % baseBranchColors.length];
                }} else {{
                    // 更深层的节点，颜色与父节点相近
                    color = adjustColor(parentColor, siblingIndex, siblingCount); // 调整颜色
                }}

                const node = createNode(data.text, level, color);
                document.body.appendChild(node);

                if (!levels[level]) levels[level] = [];
                levels[level].push(node);

                // 设置节点位置
                if (parent) {{
                    // 稍后统一布局
                }} else {{
                    // 母节点，放置在更靠下的位置，增加与标题的距离
                    node.style.left = (windowWidth / 2 - node.offsetWidth / 2) + 'px';
                    node.style.top = '150px'; // 增加顶部间距
                }}

                // 绘制连线
                if (parent) {{
                    drawLine(parent, node);
                }}

                // 递归构建子节点
                if (data.children && data.children.length > 0) {{
                    data.children.forEach((child, index) => {{
                        buildMindMap(child, level + 1, node, color, index, data.children.length);
                    }});
                }}
            }}

            // 创建节点元素
            function createNode(text, level, color) {{
                const node = document.createElement('div');
                node.className = 'node';
                node.innerText = text;
                node.style.backgroundColor = color;
                if (level === 0) {{
                    node.style.fontSize = '28px'; // 增加母节点字体大小
                    node.style.fontWeight = 'bold';
                    node.style.padding = '12px 24px'; // 增加母节点内边距
                }}
                return node;
            }}

            // 绘制连线
            function drawLine(startElem, endElem) {{
                const line = document.createElement('div');
                line.className = 'line';
                document.body.appendChild(line);

                const startRect = startElem.getBoundingClientRect();
                const endRect = endElem.getBoundingClientRect();

                const startX = startRect.left + startRect.width / 2;
                const startY = startRect.top + startRect.height;
                const endX = endRect.left + endRect.width / 2;
                const endY = endRect.top;

                const deltaX = endX - startX;
                const deltaY = endY - startY;
                const distance = Math.hypot(deltaX, deltaY);
                const angle = Math.atan2(deltaY, deltaX) * (180 / Math.PI);

                line.style.left = startX + 'px';
                line.style.top = startY + 'px';
                line.style.width = distance + 'px';
                line.style.transform = `rotate(${{angle}}deg)`;
            }}

            // 布局节点
            function layoutNodes() {{
                levels.forEach((nodes, level) => {{
                    const totalWidth = nodes.reduce((sum, node) => sum + node.offsetWidth, 0);
                    const spacing = (windowWidth - totalWidth) / (nodes.length + 1);
                    let currentX = spacing;

                    nodes.forEach(node => {{
                        node.style.left = currentX + 'px';
                        node.style.top = (150 + level * 150) + 'px'; // 增加层级之间的垂直间距
                        currentX += node.offsetWidth + spacing;
                    }});
                }});
            }}

            // 调整颜色逻辑（保持原来的颜色调整逻辑）
            function adjustColor(hex, index, totalSiblings) {{
                let {{ h, s, l }} = hexToHSL(hex);

                // 保持与父节点相同的色相（hue）
                // 通过调整饱和度（s）和亮度（l）来区分兄弟节点

                const saturationVariation = 20; // 饱和度总变化量
                const lightnessVariation = 10;  // 亮度总变化量

                if (totalSiblings > 1) {{
                    const sStep = saturationVariation / (totalSiblings - 1);
                    const lStep = lightnessVariation / (totalSiblings - 1);

                    // 调整饱和度和亮度，使兄弟节点略有不同
                    s = s - saturationVariation / 2 + sStep * index;
                    l = l - lightnessVariation / 2 + lStep * index;

                    // 确保值在0到100之间
                    s = Math.max(0, Math.min(100, s));
                    l = Math.max(0, Math.min(100, l));
                }}

                return hslToHex(h, s, l);
            }}

            // HEX 转 HSL
            function hexToHSL(H) {{
                let r = 0, g = 0, b = 0;
                if (H.length == 4) {{
                    r = "0x" + H[1] + H[1];
                    g = "0x" + H[2] + H[2];
                    b = "0x" + H[3] + H[3];
                }} else if (H.length == 7) {{
                    r = "0x" + H[1] + H[2];
                    g = "0x" + H[3] + H[4];
                    b = "0x" + H[5] + H[6];
                }}
                r /= 255;
                g /= 255;
                b /= 255;
                let cmin = Math.min(r, g, b),
                    cmax = Math.max(r, g, b),
                    delta = cmax - cmin,
                    h = 0,
                    s = 0,
                    l = 0;

                if (delta == 0)
                    h = 0;
                else if (cmax == r)
                    h = ((g - b) / delta) % 6;
                else if (cmax == g)
                    h = (b - r) / delta + 2;
                else
                    h = (r - g) / delta + 4;

                h = Math.round(h * 60);
                if (h < 0)
                    h += 360;

                l = (cmax + cmin) / 2;
                s = delta == 0 ? 0 : delta / (1 - Math.abs(2 * l - 1));
                s = +(s * 100).toFixed(1);
                l = +(l * 100).toFixed(1);

                return {{ h, s, l }};
            }}

            // HSL 转 HEX
            function hslToHex(h, s, l) {{
                s /= 100;
                l /= 100;

                let c = (1 - Math.abs(2 * l - 1)) * s,
                    x = c * (1 - Math.abs((h / 60) % 2 - 1)),
                    m = l - c / 2,
                    r = 0,
                    g = 0,
                    b = 0;

                if (0 <= h && h < 60) {{
                    r = c; g = x; b = 0;
                }} else if (60 <= h && h < 120) {{
                    r = x; g = c; b = 0;
                }} else if (120 <= h && h < 180) {{
                    r = 0; g = c; b = x;
                }} else if (180 <= h && h < 240) {{
                    r = 0; g = x; b = c;
                }} else if (240 <= h && h < 300) {{
                    r = x; g = 0; b = c;
                }} else if (300 <= h && h < 360) {{
                    r = c; g = 0; b = x;
                }}
                r = Math.round((r + m) * 255);
                g = Math.round((g + m) * 255);
                b = Math.round((b + m) * 255);

                return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
            }}

            // 初始化心智图
            function initMindMap() {{
                // 清空内容
                document.getElementById('mindmap').innerHTML = '';
                document.querySelectorAll('.node, .line').forEach(elem => elem.remove());

                // 重置层级数组
                levels.length = 0;

                // 构建心智图
                buildMindMap(mindMapData);

                // 布局节点
                layoutNodes();
            }}

            // 监听窗口大小变化，重新布局
            window.addEventListener('resize', () => {{
                windowWidth = window.innerWidth;
                windowHeight = window.innerHeight;
                initMindMap();
            }});

            // 初始绘制
            initMindMap();
        </script>
    </body>
    </html>
    '''
}

