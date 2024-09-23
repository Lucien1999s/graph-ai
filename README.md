# Graph AI

Graph AI is a powerful API that integrates with GPTs to generate visual diagrams such as **timelines** and **quadrant charts** based on conversational inputs. The application can be easily deployed on **Heroku** and provides a seamless interface to create insightful visualizations through natural language.

![Graph AI](static/timeline.png)

## Features

- **Conversation-based diagrams**: Generate visual timelines and quadrant charts from conversations.
- **Seamless GPT integration**: Leverages GPT's powerful natural language understanding to interpret and convert text into meaningful visuals.
- **Heroku deployment**: Deploy easily to Heroku and start using the API without any hassle.
- **Customizable API**: Designed to be flexible and extensible to suit various use cases.

## Getting Started

Follow these steps to get the project up and running on Heroku.

### Prerequisites

- Heroku account
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Python 3.x

### Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:Lucien1999s/graph-ai.git
    cd graph-ai
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the project root and add the following configurations:
    ```
    GITHUB_TOKEN
    REPO_NAME
    BRANCH_NAME
    ```

### Deploying to Heroku

1. **Login to Heroku**:
    ```bash
    heroku login
    ```

2. **Create a new Heroku app**:
    ```bash
    heroku create graph-ai
    ```

3. **Deploy the application**:
    ```bash
    git push heroku main
    ```

4. **Set environment variables** for GitHub storage integration:
    ```bash
    heroku config:set GITHUB_TOKEN=your_github_token REPO_NAME=lucien1999s/graph-ai-storage BRANCH_NAME=main
    ```

5. **Open your deployed app**:
    ```bash
    heroku open
    ```

### API Usage Example

After deployment, you can interact with the API by sending requests. Here is an example of calling the API to generate a timeline chart:

```python
import requests
import json

url = "http://localhost:8000/generate_chart/"

payload = json.dumps({
  "chart_type": "timeline",
  "data": {
    "page_title": "時間軸範例",
    "time_list": [
      "事件1",
      "事件2",
      "事件3",
      "事件4"
    ],
    "data_list": [
      {
        "title": "事件1",
        "content": "描述1"
      },
      {
        "title": "事件2",
        "content": "描述2"
      },
      {
        "title": "事件3",
        "content": "描述3"
      },
      {
        "title": "事件4",
        "content": "描述4"
      }
    ],
    "count": 4
  }
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
```

The OpenAPI structure of description:
```
openapi: 3.1.0
info:
  title: Chart Generation API
  description: |
    API to generate different types of charts. The API supports generating timelines, quadrant charts, hierarchy charts, and mind maps based on the provided data.
  version: 1.0.6
servers:
  - url: https://graphai-7de103b06d45.herokuapp.com
    description: Production server
paths:
  /generate_chart/:
    post:
      operationId: generateChart
      summary: Generate a chart based on the chart_type
      description: |
        This API generates various types of charts based on the provided `chart_type`. 
        Supported chart types include:
        - `timeline`: Generates a timeline chart.
        - `quadrant`: Generates a four-quadrant chart.
        - `hierarchy`: Generates a hierarchy chart.
        - `mindmap`: Generates a mind map.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                chart_type:
                  type: string
                  description: The type of chart to generate. Must be either 'timeline', 'quadrant', 'hierarchy', or 'mindmap'.
                  enum: [timeline, quadrant, hierarchy, mindmap]
                  example: "timeline"
                data:
                  type: object
                  description: Data required to generate the chart. The structure of this object varies based on the `chart_type`.
                  properties:
                    # Timeline chart parameters
                    page_title:
                      type: string
                      description: Title of the timeline. Required for timeline chart.
                      example: "My Timeline"
                    time_list:
                      type: array
                      description: |
                        List of time or dates for the timeline, the length of it must same as data_list.
                      maxItems: 8
                      items:
                        type: string
                        maxLength: 6
                        example: "Date1"
                    data_list:
                      type: array
                      description: |
                        List of detailed event data for the timeline. Must not exceed 8 events, and the length of it must same as text_list.
                      maxItems: 8
                      items:
                        type: object
                        properties:
                          title:
                            type: string
                            description: The title of the event.
                            example: "Event Title"
                          content:
                            type: string
                            description: The content or description of the event.
                            example: "This is the event content."
                    count:
                      type: integer
                      description: Number of events in the timeline. Must not exceed 8, and the it must same as text_list's length.
                      maximum: 8
                      example: 4
                    # Quadrant chart parameters
                    main_title:
                      type: string
                      description: Title of the quadrant chart. Required for quadrant chart.
                      example: "Quadrant Chart Example"
                    x_axis_label:
                      type: string
                      description: |
                        Label for the x-axis, representing importance. Max 10 characters.
                      maxLength: 10
                      example: "Importance"
                    y_axis_label:
                      type: string
                      description: |
                        Label for the y-axis, representing urgency. Max 10 characters.
                      maxLength: 10
                      example: "Urgency"
                    quadrant_titles:
                      type: array
                      description: |
                        Titles for each quadrant. Each title must not exceed 15 characters.
                      maxItems: 4
                      items:
                        type: string
                        maxLength: 15
                        example: "Quadrant 1"
                    quadrant_contents:
                      type: array
                      description: |
                        List of content arrays for each quadrant. Each string must not exceed 12 characters.
                      maxItems: 4
                      items:
                        type: array
                        items:
                          type: string
                          maxLength: 12
                          example: "Task 1"
                    # Hierarchy chart parameters
                    title:
                      type: string
                      description: Required if chart_type is 'hierarchy'. The title of the hierarchy chart.
                      example: "Company Hierarchy"
                    levels:
                      type: array
                      description: |
                        A list of hierarchy levels, up to 5, usually the name of the level plus a one-sentence description.
                      maxItems: 5
                      items:
                        type: string
                        maxLength: 30
                        example: "Senior Management: Possess excellent and proficient technology."
                    # Mindmap chart parameters
                    title:
                      type: string
                      description: Required if chart_type is 'mindmap'. The title of the mind map.
                      example: "Mind Map Example"
                    mindMapData:
                      type: object
                      description: |
                        Data structure for the mind map. It includes the central theme and child nodes.
                      properties:
                        text:
                          type: string
                          description: The central theme of the mind map.
                          example: "Central Topic"
                        children:
                          type: array
                          description: Child nodes connected to the central theme.
                          items:
                            type: object
                            properties:
                              text:
                                type: string
                                description: The text for a child node.
                                example: "Sub-topic 1"
                              children:
                                type: array
                                description: Further sub-nodes of the child node.
                                items:
                                  type: object
                                  properties:
                                    text:
                                      type: string
                                      description: The text for a sub-node.
                                      example: "Sub-topic 1-1"
      responses:
        '200':
          description: Chart generated successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  url:
                    type: string
                    description: The URL where the generated chart can be accessed.
                    example: "https://lucien1999s.github.io/graph-ai-storage/mindmap_m2wElg.html"
        '400':
          description: Bad Request - Invalid input or data exceeds allowed limits.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message explaining the issue.
                    example: "The mind map data structure is invalid."
                  details:
                    type: string
                    description: More detailed information about the error.
                    example: "The child node is missing a text field."
```
