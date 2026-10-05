# Oscar Choi

Computer Science at CUHK (graduating July 2027). I build quant research infrastructure and test trading ideas against point-in-time data, with negative results kept. I am the sole developer and architect of the CUHK Quant Trading Society research team's data platform and a WorldQuant BRAIN research consultant.

## Results

- **IMC Prosperity 4** (team SHDC): 904th of 18,803 teams, 18th in Hong Kong.
- **Kaggle Pokémon TCG AI Battle**: team entry, 2,043rd of 6,807 teams on the Simulation leaderboard (read 2026-09-13).
- **MonsoonSIM Enterprise Resource Management Competition 2025**: 3rd place (second runner-up).

## Projects

### Market data and infrastructure

| Project | What it is | One number |
|---|---|---|
| [CUHK QTS research platform](https://github.com/hihihhi/qts-platform-showcase) (write-up; code private) · [runnable demo](https://github.com/hihihhi/qts-platform-demo) | Tick-level market data a student quant team can trust: raw → typed Parquet → cleaned layers, versioned query library and API, data-quality checks. The demo is an independent stand-in on synthetic data | 700B+ stored market-data rows; 0 of 23 commits lost in a concurrency test |
| [asof-research](https://github.com/hihihhi/asof-research) | Can an LLM pick better trading hypotheses than brute force, under one honest gate? Point-in-time data contracts, pre-registered protocols, a non-promoting LLM critic, a human gate; separate opt-in C++20 replay port (not used by the study) | Real-data run: 120 hypotheses screened; both controls' picks lost money out of sample, 0 of 2 promoted; LLM arm pending to 2027-08. C++ replay ~2.3× from Python (25× over Python batch when called from C++, synthetic) |
| [streaming-reconciliation](https://github.com/hihihhi/streaming-reconciliation) | Counts each recorded trade close exactly once across JSONL/CSV copies and retries, streaming through sorted runs on disk (from the WQT 2025 hackathon; team strategy not included) | Peak memory 683.8 MB → 27.5 MB (−96%) and 11.8% faster than an in-memory reader, identical reports (100k synthetic closes) |

### Quant research

| Project | What it is | One number |
|---|---|---|
| [alpha-gp-lab](https://github.com/hihihhi/alpha-gp-lab) | Public-data companion to my WorldQuant BRAIN work: genetic programming over WorldQuant-style formulas with pre-registered train/validation/test roles, delay-1 and costs, equal-budget random search as a control | Test rank IC 0.082 but net not significant (t 0.22); random search 0.080, one-line control 0.082 |
| [Factor Lab](https://github.com/hihihhi/asof-research/tree/main/packages/factor) | Lagged momentum vs reversal by Spearman rank IC, chosen on validation; convex allocation under risk and position limits with a turnover cost | Solver checked against hand-solved cases (synthetic data) |
| [Market-Making Lab](https://github.com/hihihhi/asof-research/tree/main/packages/imc-sim) | Market-making simulator with partial fills, queue position and cancel delays; fill quality measured with as-of markouts | 18 synthetic scenarios (2 strategies × 3 price paths × 3 fill models) |
| [Polymarket-Crypto-5min](https://github.com/hihihhi/Polymarket-Crypto-5min) | A leakage-controlled chronological walk-forward on public Polymarket and Binance data | |

### Competitions

| Project | What it is | One number |
|---|---|---|
| [imc-prosperity-4-shdc](https://github.com/hihihhi/imc-prosperity-4-shdc) | What we did in each round, what other teams did differently, and what I learned, against 9 public Prosperity 4 write-ups (placements 2nd to 583rd, as stated) | 904 / 18,803 (IMC's team count) |
| [ptcg-ai-battle](https://github.com/hihihhi/ptcg-ai-battle) | A card game under imperfect information: imitation learning (set transformer), self-play PPO (not submitted), search baselines | 2,043 / 6,807 (team entry) |

### AI engineering

| Project | What it is | One number |
|---|---|---|
| [agent-harness](https://github.com/hihihhi/agent-harness) | Shared rules and/or memory for seven AI coding tools, and a command guard for Claude Code; one standard-library install, A/B-evaluated on 2 of the 7 tools (private question set) | Guard blocks 39 of 45 held-out dangerous commands, 20/20 safe pass |
| [gpt-cc](https://github.com/hihihhi/gpt-cc) | Local gateway translating Claude Code's Anthropic API requests to OpenAI-compatible APIs or Codex CLI; unsupported features fail closed | |
| [quant-research-vault](https://github.com/hihihhi/quant-research-vault) | Local arXiv/OpenAlex paper ingestion into SQLite and ChromaDB, served to AI assistants through a read-only MCP search server | |

## How I work

Code in these repositories was implemented with AI coding agents under my design and review; each flagship README says so. Every number in a README cites the file or command it came from, and synthetic data is labelled as such.

Python, SQL, C++20, DuckDB / Arrow / Parquet, Linux.
