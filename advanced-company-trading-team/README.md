# Advanced Company Trading Team

Folder ini berisi workflow v4 untuk **Apex Trading Intelligence Team**: tim agent perusahaan/trader profesional yang dipakai untuk riset strategi trading dari YouTube, dokumen, chart, Pine Script, dan data market.

Tujuan utama:

- Mengubah sumber trading menjadi strategy blueprint.
- Membuat rule trading IF / AND / THEN.
- Membuat prompt agent sesuai materi sumber.
- Membuat draft Pine Script v6.
- Melakukan risk review dan repaint audit.
- Membuat backtest plan.
- Menghasilkan keputusan akhir: VALID, WAIT, REJECT, NEEDS_DATA, atau NEEDS_BACKTEST.

## Struktur

```text
advanced-company-trading-team/
├── README.md
├── WORKFLOW.md
├── AGENTS.md
├── config/
│   └── company-trading-team.json
├── prompts/
│   └── company-system-prompt.md
├── protocols/
│   ├── operating-protocol.md
│   └── information-access-policy.md
└── scripts/
    └── validate_company_team.py
```

## Prinsip utama

1. Disiplin lebih penting daripada banyak sinyal.
2. Tidak ada klaim profit tanpa backtest.
3. Tidak ada setup valid tanpa SL, TP, RR, dan invalidation.
4. Pisahkan logic asli sumber dan improvement AI.
5. Semua output penting harus melewati risk review.
6. Jika data kurang, status harus NEEDS_DATA atau NEEDS_BACKTEST.

## GitHub Action

Workflow GitHub Action berada di:

```text
.github/workflows/advanced-company-team.yml
```

Action ini memvalidasi file JSON config, memastikan dokumen penting tersedia, dan memeriksa agar tidak ada API key hardcoded.