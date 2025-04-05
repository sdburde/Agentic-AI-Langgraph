# AgenticAI - LangGraph Project
Agentic-AI-Langgraph
AgenticAI is a Streamlit-based application that integrates Groq's language models with a graph-based workflow (LangGraph) to enable interactive AI functionalities, such as chatbots and extensible use cases. The project is designed with a modular architecture for easy development and scalability.

## Features

- **Streamlit UI**: Interactive web interface for user input and result display.
- **Groq LLM Integration**: Configurable language model support via Groq API.
- **Graph-Based Workflow**: Utilizes LangGraph for structured AI processing.
- **Modular Structure**: Separates UI, LLM, graph logic, nodes, and state management.
- **Extensible Design**: Supports adding new use cases and nodes.

## Project Structure

```
LangGraphProject/
├── app.py                  # Application entry point
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── src/
│   ├── AgenticAI/
│   │   ├── frontend_ui/    # Frontend components
│   │   │   ├── config_ui.py        # Configuration loader
│   │   │   ├── streamlit_ui/       # Streamlit UI logic
│   │   │   │   ├── load_ui.py      # UI initialization
│   │   │   │   └── display_result.py  # Result rendering
│   │   │   └── ui_config.ini       # UI configuration file
│   │   ├── LLM/           # Language model integration
│   │   │   └── groqllm.py        # Groq LLM wrapper
│   │   ├── graph/         # Graph workflow
│   │   │   └── graph_builde.py   # Graph builder
│   │   ├── nodes/         # Graph nodes
│   │   │   └── basic_chatbot_node.py  # Basic chatbot node
│   │   ├── state/         # State management
│   │   │   └── state.py         # State definitions
│   │   ├── tools/         # Utility tools (placeholder)
│   │   ├── vectorstore/   # Vector storage (placeholder)
│   │   └── main.py        # Core application logic
├── venv/                  # Virtual environment (ignored by Git)
└── .gitignore             # Git ignore rules
```

*Note*: `__pycache__` directories and `__init__.py` files are omitted for brevity but are present for Python package structure.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- Groq API Key ([Get one here](https://console.groq.com/keys))

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/AgenticAI.git
   cd LangGraphProject
   ```

2. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Ensure `requirements.txt` includes:
   ```
   streamlit
   langchain-groq
   ```

4. **Set Up Environment** (optional):
   Add your Groq API key to a `.env` file:
   ```bash
   echo "GROQ_API_KEY=your-api-key" > .env
   ```

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.

2. **Interact with the App**:
   - In the sidebar, select an LLM (e.g., "Groq") and enter your API key if not set in `.env`.
   - Choose a use case (e.g., "Basic Chatbot").
   - Enter a message in the chat input to see the AI response.

## Development

- **Adding Features**:
  - Extend `graph_builde.py` for new workflows.
  - Add nodes in `nodes/` for custom functionality.
  - Update `ui_config.ini` for new UI options.

- **Debugging**:
  - Check terminal output for Streamlit logs.
  - Verify Groq API key if LLM initialization fails.

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "feat: add new feature"
   ```
4. Push and open a Pull Request:
   ```bash
   git push origin feature/new-feature
   ```


## Acknowledgments

- [Streamlit](https://streamlit.io/) for the UI framework.
- [Groq](https://groq.com/) for LLM capabilities.
- LangGraph for graph-based workflows.

---



```
git remote set-url origin git@github-sdburde:sdburde/Agentic-AI-Langgraph.git
git remote -v
ssh -T git@github-sdburde
git push --set-upstream origin main

```