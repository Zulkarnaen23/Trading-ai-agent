# 🚀 Quick Start Guide - Trading AI Agent

## 📋 Prerequisites

- Python 3.10 or higher
- API key (OpenAI, Claude, or Groq)
- Git (optional)

---

## 1️⃣ Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/Zulkarnaen23/Trading-ai-agent.git
cd Trading-ai-agent
```

### Step 2: Install UV (Recommended)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 3: Install Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or using uv
uv pip install -r requirements.txt
```

### Step 4: Setup Environment
```bash
# Copy example file
cp .env.example .env

# Edit with your API keys
nano .env        # macOS/Linux
notepade .env    # Windows
```

---

## 2️⃣ Configuration

### API Key Setup

#### OpenAI (GPT-4)
```env
OPENAI_API_KEY=sk-your_key_here
```
Get key: https://platform.openai.com/api-keys

#### Anthropic (Claude)
```env
ANTHROPIC_API_KEY=sk-ant-your_key_here
```
Get key: https://console.anthropic.com/

#### Groq
```env
GROQ_API_KEY=gsk_your_key_here
```
Get key: https://console.groq.com/

### Trading Configuration
```env
TRADING_PAIR=BTC/USDT
TIMEFRAME=1h
MAX_POSITION_SIZE=1000
RISK_PER_TRADE=0.02
```

---

## 3️⃣ Running the Agent

### Basic Run
```bash
python crew.py
```

### With Environment Export
```bash
# macOS/Linux
export OPENAI_API_KEY="sk-..."
python crew.py

# Windows
set OPENAI_API_KEY=sk-...
python crew.py
```

### Using UV
```bash
uv run crew.py
```

---

## 4️⃣ Using with AI Assistants

### Claude (Best for Explanations)
1. Go to https://claude.ai
2. Create new conversation
3. Paste `crew.py` code
4. Ask:
   - "Explain what this code does"
   - "How do I customize this for my trading strategy?"
   - "Help me debug this error: [error]"

### ChatGPT (Best for Implementation)
1. Go to https://chat.openai.com
2. Start new chat
3. Paste `crew.py` code
4. Ask:
   - "How do I run this?"
   - "What error am I getting?"
   - "Show me how to add feature X"

### GitHub Copilot (Best for Code Completion)
1. Install VS Code
2. Install GitHub Copilot extension
3. Open `crew.py`
4. Start typing and Copilot suggests

---

## ✅ Verification Checklist

- [ ] Python 3.10+ installed
- [ ] Dependencies installed
- [ ] .env file created and filled
- [ ] API key configured
- [ ] `python crew.py` runs without errors
- [ ] Agents display in output
- [ ] Tasks complete successfully

---

## 🐛 Common Issues

### Issue: ModuleNotFoundError
```bash
# Solution
pip install 'crewai[tools]'
```

### Issue: API Key Not Found
```bash
# Check .env file exists and has your key
cat .env | grep OPENAI_API_KEY
```

### Issue: Build Error (Windows)
```
# Install Visual C++ Build Tools
https://visualstudio.microsoft.com/downloads/
```

---

## 🚀 Next Steps

1. Read `SETUP_GUIDE.md` for detailed configuration
2. Check `CLAUDE_GPT_INTEGRATION.md` for AI assistant usage
3. Customize `agents.yaml` for your needs
4. Modify `tasks.yaml` with your specific requirements
5. Run `crew.py` and iterate!

---

## 📚 Resources

- CrewAI: https://docs.crewai.com
- OpenAI: https://platform.openai.com/docs
- Claude: https://docs.anthropic.com
- Groq: https://console.groq.com/docs

---

**Happy trading! 🎯**
