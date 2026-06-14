# Operating Protocol

## 1. Task Classification

Setiap input harus diklasifikasi:

```text
YOUTUBE_LINK
TRANSCRIPT
PINE_SCRIPT
STRATEGY_NOTES
CHART_SCREENSHOT
CANDLE_DATA
PROMPT_REQUEST
BACKTEST_REQUEST
REPOSITORY_TASK
```

## 2. Source Verification

Tim wajib menjawab:

```text
Apa sumbernya?
Apakah sumber lengkap?
Apakah data cukup?
Apa yang belum diketahui?
Apa yang hanya klaim?
Apa yang bisa diuji?
```

## 3. Strategy Extraction

Jika sumber berasal dari YouTube/transkrip, output wajib berisi:

```text
- nama strategi
- indikator
- setting
- cara kerja
- buy rule
- sell rule
- exit rule
- stop loss
- take profit
- market
- timeframe
- missing information
```

## 4. Scenario Analysis

Strategi harus diuji secara konseptual pada skenario:

```text
trend bullish kuat
trend bearish kuat
sideways/range
high volatility
low volatility
news event
liquidity sweep fakeout
late entry
spread melebar
consecutive loss
```

## 5. Risk Gate

Strategi tidak boleh lanjut jika:

```text
tidak ada rule buy/sell jelas
tidak ada stop loss
tidak ada invalidation
tidak ada timeframe
trigger terlalu subjektif
repaint risk tinggi dan tidak bisa diperbaiki
```

## 6. Final Status

Gunakan salah satu:

```text
VALID
WAIT
REJECT
NEEDS_DATA
NEEDS_BACKTEST
```
