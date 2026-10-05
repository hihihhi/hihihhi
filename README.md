<a href="https://oscar-chw.github.io"><img src="assets/header.svg" width="100%" alt="Victoria Harbour drawn from data: each building is one month of BTC/USDT prices, lit windows are up days, the glowing roofline is the price chart, the beams are the data platform's concurrent readers and writers, and the water holds a live order book"></a>

<p align="center"><sub><a href="https://oscar-chw.github.io"><b>Hover the interactive version</b></a> &nbsp;·&nbsp; <code>roofline</code> BTC/USDT monthly close &nbsp;·&nbsp; <code>windows</code> green up days, red down days &nbsp;·&nbsp; <code>beams</code> the <a href="https://github.com/oscar-chw/qts-platform-showcase">QTS data platform</a>: 12 readers, 5 writers, 0 lost &nbsp;·&nbsp; <code>t = now</code> nothing to its right is used (<a href="https://github.com/oscar-chw/asof-research">asof-research</a>) &nbsp;·&nbsp; <code>water</code> a live order book, green bids and red asks (<a href="https://github.com/oscar-chw/asof-research/tree/main/packages/imc-sim">Market-Making Lab</a>)</sub></p>

# Oscar Choi

<img align="right" width="230" src="assets/fourier_portrait.gif" alt="A line portrait of Oscar being drawn by 500 rotating circles (a Fourier series)">

Computer Science at CUHK (graduating July 2027). I build quant research infrastructure and test trading ideas against point-in-time data, with explicit controls and costs. I am the sole developer and architect of the CUHK Quant Trading Society research team's data platform and a WorldQuant BRAIN research consultant.


<details>
<summary><b>How this page is drawn</b></summary>

- **The harbour** is built from data: one building per month of BTC/USDT (Binance daily closes, 2020 to now). The roof is the monthly close on a log scale, the white light is the monthly high, and each window is one trading day: green up, red down. Past "now" the towers are unlit blueprints, because nothing from the future is used. Packets on the beams replay the data platform's race test: 12 readers and 5 writers (4 appending, 1 rewriting a partition), with no commit lost. The water holds a Binance order-book snapshot (5 Oct 2026): green bids, red asks. It all moves in plain SVG and CSS, since GitHub runs no scripts.
- **The portrait** is one continuous line through the edges of my photo, rewritten as a Fourier series, z(t) = Σ c<sub>k</sub> e<sup>2πikt</sup>: 500 circles, each turning at its own frequency, and the pen at the end of the chain redraws the face.

</details>

## Results

- **IMC Prosperity 4** (team SHDC): 904th of 18,803 teams, 18th in Hong Kong.
- **Kaggle Pokémon TCG AI Battle**: team entry, 2,043rd of 6,807 teams on the Simulation leaderboard (read 2026-09-13).
- **MonsoonSIM Enterprise Resource Management Competition 2025**: 3rd place (second runner-up).

## Projects

### Market data and infrastructure

| Project | What it is | One number |
|---|---|---|
| [CUHK QTS research platform](https://github.com/oscar-chw/qts-platform-showcase) (write-up; code private) · [runnable demo](https://github.com/oscar-chw/qts-platform-demo) | Tick-level market data a student quant team can trust: raw → typed Parquet → cleaned layers, versioned query library and API, data-quality checks. The demo is an independent stand-in on synthetic data | 700B+ stored market-data rows; 23 of 23 concurrent commits preserved in a race test |
| [asof-research](https://github.com/oscar-chw/asof-research) | Can an LLM pick better trading hypotheses than brute force, under one honest gate? Point-in-time data contracts, pre-registered protocols, a non-promoting LLM critic, a human gate; separate opt-in C++20 replay port (not used by the study) | 120 hypotheses screened on real Binance data; the pre-registered gate blocked both control picks, which lost money out of sample. C++20 replay port ~2.3× faster end-to-end from Python (synthetic benchmark) |
| [streaming-reconciliation](https://github.com/oscar-chw/streaming-reconciliation) | Counts each recorded trade close exactly once across JSONL/CSV copies and retries, streaming through sorted runs on disk (from the WQT 2025 hackathon; team strategy not included) | Peak memory 683.8 MB → 27.5 MB (−96%) in 11.8% less time than an in-memory reader, identical reports (100k synthetic closes) |

### Quant research

| Project | What it is | One number |
|---|---|---|
| [alpha-gp-lab](https://github.com/oscar-chw/alpha-gp-lab) | Public-data companion to my WorldQuant BRAIN work: genetic programming over WorldQuant-style formulas with pre-registered train/validation/test roles, delay-1 and costs, equal-budget random search as a control | 34 coins, 6.7 years, pre-registered splits; test rank IC 0.08, matched by an equal-budget random search |
| [Factor Lab](https://github.com/oscar-chw/asof-research/tree/main/packages/factor) | Lagged momentum vs reversal by Spearman rank IC, chosen on validation; convex allocation under risk and position limits with a turnover cost | Solver checked against hand-solved cases (synthetic data) |
| [Market-Making Lab](https://github.com/oscar-chw/asof-research/tree/main/packages/imc-sim) | Market-making simulator with partial fills, queue position and cancel delays; fill quality measured with as-of markouts | 18 synthetic scenarios (2 strategies × 3 price paths × 3 fill models) |
| [Polymarket-Crypto-5min](https://github.com/oscar-chw/Polymarket-Crypto-5min) | Point-in-time walk-forward backtester for Polymarket's Bitcoin 5-minute markets; an availability audit caught candles indexed at open, not close (a look-ahead leak) | 512 entry × 192 exit rules over 26 chronological folds |

### Competitions

| Project | What it is | One number |
|---|---|---|
| [imc-prosperity-4-shdc](https://github.com/oscar-chw/imc-prosperity-4-shdc) | What we did in each round, what other teams did differently, and what I learned, against 9 public Prosperity 4 write-ups (placements 2nd to 583rd, as stated) | Top 5% (904 / 18,803 teams) |
| [ptcg-ai-battle](https://github.com/oscar-chw/ptcg-ai-battle) | A card game under imperfect information: imitation learning (set transformer), self-play PPO (not submitted), search baselines | 2,043 / 6,807 (team entry) |

### AI engineering

| Project | What it is | One number |
|---|---|---|
| [agent-harness](https://github.com/oscar-chw/agent-harness) | Shared rules and memory tools for seven AI coding tools (as far as each supports them), and a command guard for Claude Code; one standard-library install | Guard blocks 39 of 45 held-out dangerous commands, 20/20 safe pass |
| [gpt-cc](https://github.com/oscar-chw/gpt-cc) | Local gateway translating Claude Code's Anthropic API requests to OpenAI-compatible APIs or Codex CLI; unsupported features fail closed | 29 offline unit tests |
| [quant-research-vault](https://github.com/oscar-chw/quant-research-vault) | Local arXiv/OpenAlex paper ingestion into SQLite and ChromaDB, served to AI assistants through a read-only MCP search server | 18,492 paper records at a 2026-07-30 audit (database unpublished) |

## How I work

Code in these repositories was implemented with AI coding agents under my design and review; each flagship README says so. Every number in a README cites the file or command it came from, synthetic data is labelled as such, and negative results are kept in each README's results and limits.

Python, SQL, C++20, DuckDB / Arrow / Parquet, Linux.
