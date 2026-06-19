import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors({ origin: process.env.ALLOWED_ORIGIN || "*" }));
app.use(express.json({ limit: "3mb" }));

const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const SYSTEM_PROMPT = `
Kamu adalah Universal Trading Agent berbasis Apex Trading Intelligence Team.

Role internal:
- Coordinator Agent
- Head of Research Agent
- YouTube Intelligence Analyst
- Indicator Logic Engineer
- Market Structure Analyst
- SMC/ICT Analyst
- Risk Manager
- Repaint & Code Audit
- Pine Script Engineer
- Backtest Planner
- Prompt Architect
- Final Review Committee

Tugas:
Ubah input user menjadi riset trading yang terstruktur:
- link YouTube
- transkrip
- Pine Script
- catatan strategi
- ide indikator

Aturan:
1. Jangan klaim profit tanpa backtest.
2. Jangan memberi instruksi auto-entry.
3. Pisahkan original source logic dan AI improvement.
4. Wajib identifikasi missing information.
5. Wajib cek repaint risk jika ada logic indikator/Pine Script.
6. Wajib ada SL, TP, invalidation, dan RR sebelum status VALID.
7. Jika data kurang, status harus NEEDS_DATA atau NEEDS_BACKTEST.
8. Output dalam bahasa Indonesia.
9. Final Decision hanya salah satu: VALID, WAIT, REJECT, NEEDS_DATA, NEEDS_BACKTEST.

Format:
# Apex Trading Intelligence Output
## 1. Task Classification
## 2. Source / Data Status
## 3. Findings
## 4. Strategy Logic
## 5. Scenario Analysis
## 6. Risk Review
## 7. Pine Script / Prompt / Backtest Plan
## 8. Validation
## 9. Final Decision
## 10. Next Action
`;

app.get("/", (_req, res) => {
  res.json({
    ok: true,
    service: "Universal Trading Agent Backend v6",
    endpoint: "POST /api/agent"
  });
});

app.post("/api/agent", async (req, res) => {
  try {
    const input = String(req.body?.input || "").trim();
    const mode = String(req.body?.mode || "advanced_company_trading_team");

    if (!input) {
      return res.status(400).json({ error: "input is required" });
    }

    if (!process.env.OPENAI_API_KEY) {
      return res.status(500).json({ error: "OPENAI_API_KEY is not configured" });
    }

    const response = await client.responses.create({
      model: process.env.OPENAI_MODEL || "gpt-5.5",
      input: [
        { role: "system", content: SYSTEM_PROMPT },
        { role: "user", content: `Mode: ${mode}\n\nInput:\n${input}` }
      ],
      max_output_tokens: Number(process.env.MAX_OUTPUT_TOKENS || 3000)
    });

    res.json({
      report: response.output_text,
      mode,
      model: process.env.OPENAI_MODEL || "gpt-5.5"
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "agent_request_failed",
      message: error?.message || String(error)
    });
  }
});

const port = Number(process.env.PORT || 3000);
app.listen(port, () => console.log(`Universal Trading Agent backend v6 running on ${port}`));
