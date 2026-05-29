# 📚 Complete Setup Guide - Trading AI Agent

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Agent](#running-the-agent)
5. [AI Assistant Integration](#ai-assistant-integration)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)

---

## Prerequisites

### System Requirements
- Operating System: Windows, macOS, or Linux
- Python: 3.10 or higher
- RAM: 4GB minimum, 8GB recommended
- Internet: Required for API calls

### Required API Keys
- **One LLM Provider** (choose one):
  - OpenAI API key: https://platform.openai.com/api-keys
  - Anthropic Claude: https://console.anthropic.com/
  - Groq: https://console.groq.com/

### Optional API Keys
- Binance API: For live trading
- Alpha Vantage: For stock data
- Serply: For web search

---

## Installation

### 1. Install Python 3.10+

**Windows:**
- Download: https://www.python.org/downloads/
- Install with "Add Python to PATH" checked

**macOS:**
```bash
brew install python@3.11
```

**Linux:**
```bash
sudo apt-get install python3.10 python3-pip
```

### 2. Clone Repository

```bash
git clone https://github.com/Zulkarnaen23/Trading-ai-agent.git
cd Trading-ai-agent
```

### 3. Install UV Package Manager (Optional but Recommended)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then reload shell:
```bash
source $HOME/.cargo/env
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv --version
```

### 4. Install CrewAI

```bash
# Using pip
pip install -r requirements.txt

# OR using uv (faster)
uv pip install -r requirements.txt

# OR just CrewAI with tools
pip install 'crewai[tools]'
```

Verify installation:
```bash
python -c "from crewai import Agent; print('✅ CrewAI installed successfully')"
```

### 5. Create Virtual Environment (Optional)

**Using venv:**
```bash
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

**Using uv:**
```bash
uv venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows
```

---

## Configuration

### 1. Setup Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit the file
nano .env          # macOS/Linux
notepade .env      # Windows
code .env          # VS Code
```

### 2. Add API Keys

#### OpenAI (GPT-4)
```env
OPENAI_API_KEY=sk-your_actual_key_here
OPENAI_MODEL_NAME=gpt-4
```

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and paste into .env

#### Anthropic Claude
```env
ANTHROPIC_API_KEY=sk-ant-your_actual_key_here
```

1. Go to https://console.anthropic.com/
2. Click "Create new API key"
3. Copy and paste into .env

#### Groq
```env
GROQ_API_KEY=gsk_your_actual_key_here
```

1. Go to https://console.groq.com/
2. Click "Create API key"
3. Copy and paste into .env

### 3. Configure Trading Parameters

```env
# Trading Configuration
TRADING_PAIR=BTC/USDT      # Trading pair
TIMEFRAME=1h                # 1h, 4h, 1d, etc.
MAX_POSITION_SIZE=1000      # Maximum position size
RISK_PER_TRADE=0.02         # 2% risk per trade

# Feature Flags
ENABLE_PAPER_TRADING=true   # Recommended for testing
ENABLE_LIVE_TRADING=false   # Set to true only when ready
```

### 4. Customize Agents (agents.yaml)

Edit the agent configurations:

```yaml
trader_agent:
  role: "Professional Trader"
  goal: "Execute profitable trading strategies"
  backstory: "..."
  # Customize as needed
```

### 5. Customize Tasks (tasks.yaml)

Edit the task descriptions:

```yaml
market_research_task:
  description: "Analyze market conditions for..."
  expected_output: "Detailed market report..."
```

---

## Running the Agent

### Basic Execution

```bash
# Direct Python
python crew.py

# Using uv
uv run crew.py

# With explicit Python path
/usr/bin/python3 crew.py
```

### With API Key Export

**macOS/Linux:**
```bash
export OPENAI_API_KEY="sk-your-key"
python crew.py
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=sk-your-key
python crew.py
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-key"
python crew.py
```

### Expected Output

```
================================================================================
🚀 TRADING & CODING AGENT - CrewAI Multi-Agent System
================================================================================

📋 Initialized Agents:
────────────────────────────────────────────────────────────────────────────

✓ TRADER
  Role: Professional Trader
  Goal: Execute profitable trading strategies
  Tools: 3 available

✓ DEVELOPER
  Role: Senior Full-Stack Developer
  Goal: Build robust trading automation systems
  Tools: 2 available

✓ RESEARCHER
  Role: Market Research Analyst
  Goal: Provide market insights
  Tools: 3 available

================================================================================
⏳ Starting Crew Execution...
================================================================================

[Agent interactions...]

================================================================================
✅ CREW EXECUTION COMPLETED SUCCESSFULLY!
================================================================================

📊 Result:
[Results from agents...]
```

---

## AI Assistant Integration

### Claude (claude.ai)

1. Go to https://claude.ai
2. Create new conversation
3. Paste `crew.py` content
4. Ask questions:

```
"I have this CrewAI trading agent. Can you:
1. Explain what each agent does
2. Help me customize it for swing trading
3. Add risk management features"
```

### ChatGPT (chat.openai.com)

1. Go to https://chat.openai.com
2. Start new chat
3. Paste code sections
4. Ask for help:

```
"Here's my CrewAI code. How do I:
1. Add Binance API integration
2. Implement email notifications
3. Debug this error: [error]"
```

### GitHub Copilot (VS Code)

1. Install VS Code: https://code.visualstudio.com/
2. Install GitHub Copilot extension
3. Sign in with GitHub
4. Open `crew.py`
5. Start coding and Copilot suggests:

```python
# Copilot will suggest code completions
def fetch_market_data(symbol):
    # Start typing and Copilot helps
```

---

## Troubleshooting

### Issue 1: ModuleNotFoundError

```
Error: No module named 'crewai'
```

**Solution:**
```bash
pip install 'crewai[tools]'
# Or
uv pip install 'crewai[tools]'
```

### Issue 2: API Key Not Found

```
Error: OPENAI_API_KEY not set
```

**Solution:**
1. Check .env file exists: `ls -la .env`
2. Verify key is set: `grep OPENAI_API_KEY .env`
3. Export manually:
   ```bash
   export OPENAI_API_KEY="sk-..."
   python crew.py
   ```

### Issue 3: Build Error (Windows)

```
Error: Failed building wheel for tiktoken
fatal error C1083: Cannot open include file: 'float.h'
```

**Solution:**
1. Install Visual C++ Build Tools: https://visualstudio.microsoft.com/downloads/
2. Select "Desktop development with C++"
3. Retry installation

### Issue 4: Dependency Conflicts

```
Error: pip's dependency resolver does not currently take into account all...
```

**Solution:**
```bash
# Upgrade pip
pip install --upgrade pip

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt
```

### Issue 5: Connection Timeout

```
Error: Connection timeout to API
```

**Solution:**
1. Check internet connection
2. Verify API key is valid
3. Check API rate limits
4. Use proxy if behind corporate firewall:
   ```env
   HTTP_PROXY=http://proxy:port
   HTTPS_PROXY=http://proxy:port
   ```

---

## Advanced Usage

### Custom Tools

Add your own tools to `crew.py`:

```python
from crewai_tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """Description of what the tool does"""
    return f"Result: {param}"
```

### Custom Agents

Add new agents in `agents.yaml`:

```yaml
custom_agent:
  role: "Your Role"
  goal: "Your Goal"
  backstory: "Your backstory"
  tools:
    - tool1
    - tool2
```

### Batch Processing

```python
trading_pairs = ['BTC/USDT', 'ETH/USDT', 'ADA/USDT']

for pair in trading_pairs:
    crew = TradingCodingCrew()
    result = crew.kickoff(inputs={'trading_pair': pair})
    print(f"Results for {pair}: {result}")
```

### Scheduled Execution

Use APScheduler:

```bash
pip install APScheduler
```

```python
from apscheduler.schedulers.background import BackgroundScheduler
import time

def scheduled_task():
    crew = TradingCodingCrew()
    crew.kickoff()

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'interval', hours=1)
scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    scheduler.shutdown()
```

---

## Performance Optimization

### Use Async Execution

```python
import asyncio

async def run_crew_async():
    crew = TradingCodingCrew()
    result = await crew.kickoff()
    return result

# Run
asyncio.run(run_crew_async())
```

### Enable Caching

```env
ENABLE_CACHE=true
CACHE_TTL=3600
```

### Parallel Agent Execution

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(lambda pair: crew.kickoff({'pair': pair}), pairs))
```

---

## Production Deployment

### Docker Setup

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "crew.py"]
```

### Environment Management

```bash
# Production
export ENV=production
export LOG_LEVEL=INFO
export ENABLE_LIVE_TRADING=true

python crew.py
```

---

## Resources

- **CrewAI**: https://docs.crewai.com
- **OpenAI**: https://platform.openai.com/docs
- **Claude**: https://docs.anthropic.com
- **Groq**: https://console.groq.com/docs
- **Python**: https://docs.python.org/3.10/

---

**Need Help? Check the README.md or open an issue on GitHub!** 🚀
