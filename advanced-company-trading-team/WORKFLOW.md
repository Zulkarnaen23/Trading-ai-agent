# Advanced Company Trading Team Workflow

Workflow ini melanjutkan v4 **Advanced Company Trading Team** tanpa n8n.

## Main Flow

```text
Input User
  ↓
Task Classification
  ↓
Source Verification
  ↓
Research Review
  ↓
Strategy Extraction
  ↓
Logic Normalization
  ↓
Scenario Analysis
  ↓
Risk Review
  ↓
Pine Script / Prompt / Backtest Plan
  ↓
Repaint & Code Audit
  ↓
Final Committee Review
  ↓
Output Final
```

## Input yang didukung

```text
- YouTube link
- transkrip video
- Pine Script
- catatan strategi
- screenshot chart
- data candle CSV
- request prompt agent
- request backtest plan
```

## Output wajib

```markdown
# Apex Trading Intelligence Output

## 1. Task Classification
## 2. Source / Data Status
## 3. Research Findings
## 4. Strategy Logic
## 5. Scenario Analysis
## 6. Risk Review
## 7. Repaint / Code Audit
## 8. Backtest Plan
## 9. Final Decision
## 10. Next Action
```

## Decision Status

```text
VALID
WAIT
REJECT
NEEDS_DATA
NEEDS_BACKTEST
```

## Committee Rule

Output hanya boleh dinyatakan VALID jika:

```text
source jelas
+ rule buy/sell lengkap
+ SL/TP jelas
+ invalidation jelas
+ risk/reward masuk akal
+ repaint risk terkendali
+ siap diuji/backtest
```

Jika salah satu belum lengkap, hasil harus WAIT, NEEDS_DATA, atau NEEDS_BACKTEST.