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