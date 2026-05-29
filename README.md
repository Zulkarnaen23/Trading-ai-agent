# 🚀 Trading & Coding AI Agent - CrewAI

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Zulkarnaen23/Trading-ai-agent.svg)](https://github.com/Zulkarnaen23/Trading-ai-agent)

A sophisticated multi-agent AI system for automated trading and trading bot development, powered by CrewAI framework. Compatible with OpenAI (GPT-4), Anthropic (Claude), and Groq.

## 🎯 Features

- **🤖 Multi-Agent System**
  - Professional Trader Agent
  - Senior Developer Agent
  - Market Researcher Agent

- **📊 Market Analysis**
  - Real-time market data analysis
  - Technical analysis with indicators
  - Support/resistance identification
  - Trend analysis

- **💼 Trading Strategy Development**
  - Entry/exit rules generation
  - Risk management framework
  - Position sizing optimization
  - Performance metrics

- **💻 Automated Code Generation**
  - Production-ready trading bot code
  - API integration templates
  - Error handling implementation
  - Security best practices

- **🔄 LLM Flexibility**
  - OpenAI GPT-4 support
  - Anthropic Claude support
  - Groq support
  - Easy provider switching

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip or UV package manager
- API key from OpenAI, Claude, or Groq

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Zulkarnaen23/Trading-ai-agent.git
   cd Trading-ai-agent
   ```

2. **Install UV (Optional but Recommended)**
   
   macOS/Linux:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
   Windows:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Install Dependencies**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv
   uv pip install -r requirements.txt
   ```

4. **Setup Environment**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your API keys
   nano .env  # macOS/Linux
   # or
   notepad .env  # Windows
   ```

5. **Run the Agent**
   ```bash
   python crew.py
   ```

## 🔧 Configuration

### Environment Variables (.env)

```env
# Choose one LLM provider
OPENAI_API_KEY=sk-...
# OR
ANTHROPIC_API_KEY=sk-ant-...
# OR
GROQ_API_KEY=gsk-...

# Trading Configuration
TRADING_PAIR=BTC/USDT
TIMEFRAME=1h
MAX_POSITION_SIZE=1000
RISK_PER_TRADE=0.02
```

### Agents Configuration (agents.yaml)

Customize agent roles, goals, and backstories:

```yaml
trader_agent:
  role: "Professional Trader"
  goal: "Execute profitable trading strategies"
  backstory: "..."
  tools:
    - market_analysis_tool
    - trade_executor_tool
```

### Tasks Configuration (tasks.yaml)

Define what each agent should do:

```yaml
market_research_task:
  description: "Analyze current market conditions..."
  expected_output: "Detailed market analysis report..."
  agent: researcher_agent
```

## 🧠 How It Works

1. **Market Research Agent** analyzes current market conditions
2. **Trader Agent** develops trading strategy based on analysis
3. **Developer Agent** generates production-ready trading bot code
4. All agents collaborate hierarchically to produce comprehensive output

## 💬 Integration with AI Assistants

### Claude (claude.ai)
```
1. Open https://claude.ai
2. Paste crew.py content
3. Ask: "Explain this code and help me customize it for my trading strategy"
```

### ChatGPT (chat.openai.com)
```
1. Open https://chat.openai.com
2. Paste crew.py content
3. Ask: "How do I run this code? What are common issues?"
```

### GitHub Copilot (VS Code)
```
1. Install GitHub Copilot extension
2. Open crew.py
3. Start typing and Copilot will suggest completions
```

## 📁 Project Structure

```
Trading-ai-agent/
├── crew.py              # Main agent implementation
├── agents.yaml          # Agent configurations
├── tasks.yaml           # Task definitions
├── .env.example         # Environment template
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── setup.sh             # Installation script
└── docs/
    ├── SETUP_GUIDE.md
    ├── CLAUDE_GPT_INTEGRATION.md
    └── QUICK_START.md
```

## 🛠️ Troubleshooting

### ModuleNotFoundError: No module named 'crewai'
```bash
pip install 'crewai[tools]'
```

### OPENAI_API_KEY not set
```bash
export OPENAI_API_KEY="your_key_here"
```

### Build error (Windows)
Install Visual C++ Build Tools:
https://visualstudio.microsoft.com/downloads/

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [Groq Documentation](https://console.groq.com/docs)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Zulkarnaen23**
- GitHub: [@Zulkarnaen23](https://github.com/Zulkarnaen23)
- Project: [Trading-ai-agent](https://github.com/Zulkarnaen23/Trading-ai-agent)

## ⭐ Support

If you find this project helpful, please give it a star! ⭐

---

**Ready to automate your trading? Get started now!** 🚀
