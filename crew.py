#!/usr/bin/env python3
"""
Trading & Coding Agent - CrewAI Multi-Agent System

This module implements a sophisticated multi-agent system for:
- Market analysis and trading strategy development
- Automated code generation for trading bots
- Research and data analysis

Compatible with: OpenAI (GPT-4), Anthropic (Claude), Groq
"""

from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============================================================================
# DEFINE CUSTOM TOOLS
# ============================================================================

@tool
def market_analysis_tool(trading_pair: str) -> str:
    """
    Analyze current market conditions for a specific trading pair.
    Provides technical analysis, support/resistance levels, and trend indicators.
    
    Args:
        trading_pair: Trading pair to analyze (e.g., 'BTC/USDT', 'ETH/USDT')
    
    Returns:
        str: Detailed market analysis
    """
    return f"""
    📊 Market Analysis for {trading_pair}:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Current Trend: Uptrend
    Support Level: $45,000
    Resistance Level: $52,000
    Volume: Above Average
    RSI (14): 65 (Neutral - not overbought)
    MACD: Bullish Signal
    Moving Average (50): Above 200MA (Bullish)
    
    Recommendation: Monitor for entry opportunity at support level
    Risk Level: Medium
    """

@tool
def trade_executor_tool(strategy: str, amount: float = 100) -> str:
    """
    Execute trading strategy with specified parameters.
    
    Args:
        strategy: Trading strategy description
        amount: Amount to trade (default: 100)
    
    Returns:
        str: Execution confirmation
    """
    return f"""
    ✅ Trade Execution Summary:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Strategy Applied: {strategy}
    Position Size: {amount} units
    Entry Signal: Generated
    Stop Loss: Set
    Take Profit: Set
    Status: READY FOR EXECUTION
    """

@tool
def code_generator_tool(requirement: str) -> str:
    """
    Generate Python code for trading automation based on requirements.
    
    Args:
        requirement: Description of what code should do
    
    Returns:
        str: Generated Python code template
    """
    return f"""
    💻 Generated Code Template for: {requirement}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    import ccxt
    import pandas as pd
    from datetime import datetime
    
    class TradingBot:
        def __init__(self, api_key, api_secret):
            self.exchange = ccxt.binance({{'apiKey': api_key, 'secret': api_secret}})
        
        def fetch_market_data(self, symbol, timeframe='1h', limit=100):
            '''Fetch OHLCV data'''
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            return pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        def execute_strategy(self, symbol, strategy_params):
            '''Execute trading strategy'''
            # Strategy implementation
            pass
    
    if __name__ == "__main__":
        bot = TradingBot(api_key, api_secret)
        bot.execute_strategy('BTC/USDT', strategy_params={{}})
    """

@tool
def code_review_tool(code: str) -> str:
    """
    Review trading bot code for quality and security.
    
    Args:
        code: Python code to review
    
    Returns:
        str: Review feedback
    """
    return """
    📋 Code Review Report:
    ━━━━━━━━━━━━━━━━━━━━━━━━
    ✅ Positive:
    - Good error handling structure
    - API key security best practices
    - Modular code design
    
    ⚠️ Recommendations:
    - Add logging for trade execution
    - Implement retry logic for API calls
    - Add unit tests
    - Consider using asyncio for parallel API calls
    
    🔒 Security:
    - API keys properly handled with environment variables
    - No hardcoded credentials found
    - Input validation recommended
    """

@tool
def web_search_tool(query: str) -> str:
    """
    Search for market news and trading information.
    
    Args:
        query: Search query
    
    Returns:
        str: Search results
    """
    return f"""
    🔍 Search Results for: "{query}"
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    1. Bitcoin rises 5% amid positive market sentiment
    2. SEC approves new ETF framework
    3. Federal Reserve maintains interest rate policy
    4. Global crypto market cap increases 3% weekly
    5. Major exchange updates security protocols
    """

@tool
def data_analysis_tool(data_type: str) -> str:
    """
    Analyze market data and economic indicators.
    
    Args:
        data_type: Type of data to analyze
    
    Returns:
        str: Analysis results
    """
    return f"""
    📈 Data Analysis: {data_type}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Average Price: $48,500
    Price Range: $45,000 - $52,000
    Daily Volume: 150,000 BTC
    Volatility: 25% (Annual)
    Correlation with S&P 500: 0.45
    
    Economic Indicators:
    - Market Cap: $950 Billion
    - 24h Volume: $35 Billion
    - Fear & Greed Index: 65 (Greedy)
    """

# ============================================================================
# DEFINE AGENTS
# ============================================================================

def create_trader_agent() -> Agent:
    """Create professional trader agent."""
    return Agent(
        role="Professional Trader",
        goal="Execute profitable trading strategies with strict risk management and consistent returns",
        backstory=(
            "You are an experienced trader with 10+ years in cryptocurrency and stock markets. "
            "You specialize in technical analysis, risk management, and portfolio optimization. "
            "You have a proven track record of consistent profits through disciplined trading. "
            "Your expertise includes: trend analysis, support/resistance identification, momentum trading, "
            "and swing trading strategies. You understand the importance of risk-reward ratios and "
            "maintain emotional discipline in all trading decisions."
        ),
        tools=[market_analysis_tool, trade_executor_tool, web_search_tool],
        verbose=True,
        memory=True,
        allow_delegation=True
    )

def create_developer_agent() -> Agent:
    """Create senior developer agent."""
    return Agent(
        role="Senior Full-Stack Developer",
        goal="Build robust, optimized, production-ready trading automation systems and solutions",
        backstory=(
            "You are an expert Python developer specializing in financial technology and algorithms. "
            "You have deep expertise in: high-frequency trading systems, financial algorithm implementation, "
            "code optimization, and best practices in software engineering. "
            "Your code is always clean, efficient, well-tested, and production-ready. "
            "You prioritize security, scalability, and maintainability in all implementations. "
            "You understand financial domain requirements and implement them with precision."
        ),
        tools=[code_generator_tool, code_review_tool],
        verbose=True,
        memory=True,
        allow_delegation=True
    )

def create_researcher_agent() -> Agent:
    """Create market researcher agent."""
    return Agent(
        role="Market Research Analyst",
        goal="Provide comprehensive, accurate market insights and actionable data analysis",
        backstory=(
            "You are a data-driven market researcher with expertise in financial analysis and market research. "
            "You excel at: gathering real-time market data, analyzing economic indicators, "
            "interpreting news sentiment, identifying market patterns, and competitive analysis. "
            "Your research is thorough, data-backed, and drives informed trading decisions. "
            "You understand macroeconomic factors and their impact on market movements."
        ),
        tools=[web_search_tool, data_analysis_tool, market_analysis_tool],
        verbose=True,
        memory=True,
        allow_delegation=False
    )

# ============================================================================
# DEFINE TASKS
# ============================================================================

def create_market_research_task(researcher_agent: Agent) -> Task:
    """Create market research task."""
    return Task(
        description=(
            "Conduct comprehensive market analysis for BTC/USDT. "
            "Provide: (1) Current market conditions and trend analysis, "
            "(2) Technical analysis with support/resistance levels, "
            "(3) Market sentiment and economic indicators, "
            "(4) Identified trading signals and opportunities, "
            "(5) Risk assessment and market outlook."
        ),
        agent=researcher_agent,
        expected_output=(
            "Detailed market analysis report including current conditions, "
            "technical indicators, sentiment analysis, specific entry/exit recommendations, "
            "and risk assessment with actionable trading signals."
        )
    )

def create_trading_strategy_task(trader_agent: Agent) -> Task:
    """Create trading strategy development task."""
    return Task(
        description=(
            "Based on market analysis, develop a comprehensive trading strategy. "
            "Include: (1) Strategy overview and objectives, (2) Entry rules and conditions, "
            "(3) Exit rules with profit-taking and stop-loss levels, "
            "(4) Position sizing and risk management, (5) Trade management approach."
        ),
        agent=trader_agent,
        expected_output=(
            "Complete trading strategy document with specific parameters, position sizing calculations, "
            "entry/exit conditions, risk management framework, and expected performance metrics."
        )
    )

def create_code_generation_task(developer_agent: Agent) -> Task:
    """Create code generation task."""
    return Task(
        description=(
            "Convert the trading strategy into production-ready Python code. "
            "Create: (1) Market data fetcher module, (2) Strategy logic implementation, "
            "(3) Order execution module, (4) Risk management module, "
            "(5) Monitoring and logging system, (6) Configuration management."
        ),
        agent=developer_agent,
        expected_output=(
            "Production-ready trading bot code with main script, strategy implementation, "
            "configuration templates, requirements.txt, comprehensive documentation, and usage examples."
        )
    )

# ============================================================================
# TRADING CREW CLASS
# ============================================================================

class TradingCodingCrew:
    """
    Multi-agent crew for trading and coding automation.
    Combines market analysis, trading execution, and code generation capabilities.
    """

    def __init__(self):
        """Initialize the trading crew with agents and tasks."""
        self.trader_agent = create_trader_agent()
        self.developer_agent = create_developer_agent()
        self.researcher_agent = create_researcher_agent()
        
        self.agents = {
            'trader': self.trader_agent,
            'developer': self.developer_agent,
            'researcher': self.researcher_agent
        }

    def create_tasks(self) -> list:
        """Create tasks for the crew."""
        return [
            create_market_research_task(self.researcher_agent),
            create_trading_strategy_task(self.trader_agent),
            create_code_generation_task(self.developer_agent)
        ]

    def kickoff(self, inputs: Optional[dict] = None) -> str:
        """
        Execute the crew workflow.
        
        Args:
            inputs: Optional input parameters for tasks
        
        Returns:
            str: Crew execution result
        """
        tasks = self.create_tasks()
        
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=tasks,
            process=Process.hierarchical,
            verbose=True,
            max_iter=10
        )
        
        result = crew.kickoff(inputs=inputs or {})
        return result

    def get_agent(self, agent_name: str) -> Agent:
        """Get a specific agent by name."""
        return self.agents.get(agent_name)

    def get_agents_info(self) -> dict:
        """Get information about all agents."""
        return {
            name: {
                'role': agent.role,
                'goal': agent.goal,
                'tools': len(agent.tools)
            }
            for name, agent in self.agents.items()
        }

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main function to run the trading crew."""
    print("\n" + "="*80)
    print("🚀 TRADING & CODING AGENT - CrewAI Multi-Agent System")
    print("="*80 + "\n")
    
    # Initialize the crew
    crew = TradingCodingCrew()
    
    # Display agent information
    print("📋 Initialized Agents:")
    print("-" * 80)
    for name, info in crew.get_agents_info().items():
        print(f"\n✓ {name.upper()}")
        print(f"  Role: {info['role']}")
        print(f"  Goal: {info['goal']}")
        print(f"  Tools: {info['tools']} available")
    
    # Execute the crew
    print("\n" + "="*80)
    print("⏳ Starting Crew Execution...")
    print("="*80 + "\n")
    
    try:
        result = crew.kickoff()
        
        print("\n" + "="*80)
        print("✅ CREW EXECUTION COMPLETED SUCCESSFULLY!")
        print("="*80 + "\n")
        print(f"📊 Result:\n{result}\n")
        
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        raise

if __name__ == "__main__":
    main()
