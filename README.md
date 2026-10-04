# Oscar Choi

Computer Science at CUHK (graduating July 2027). I build quant research infrastructure and test trading ideas against point-in-time data, with negative results kept. I am the sole developer and architect of the CUHK Quant Trading Society research team's data platform and a WorldQuant BRAIN research consultant.

## Results

- **IMC Prosperity 4** (team SHDC): 904th of 18,803 teams, 18th in Hong Kong.
- **Kaggle Pokémon TCG AI Battle**: team entry, 2,043rd of 6,807 teams on the Simulation leaderboard (read 2026-09-13).
- **MonsoonSIM Enterprise Resource Management Competition 2025**: 3rd place (second runner-up).

## Projects

| Project | Problem | Method | One number |
|---|---|---|---|
| [CUHK QTS research platform](https://github.com/hihihhi/qts-platform-showcase) (write-up; code private) | Give a student quant team tick-level market data it can trust | Raw → typed Parquet → cleaned layers, versioned query library and API, data-quality checks | 650B+ stored market-data rows; 0 of 23 commits lost in a concurrency test |
| [asof-research](https://github.com/hihihhi/asof-research) | Can an LLM pick better trading hypotheses than brute force, under one honest gate? | Point-in-time data contracts, frozen method cards, pre-registered protocols, a non-promoting LLM critic, a human gate; separate opt-in C++20 replay port (not used by the study) | Real-data run: 120 hypotheses screened; both controls' picks lost money out of sample, 0 of 2 promoted; LLM arm pending to 2027-08. 962 numbers recomputed by a separate script. C++ replay ~2.3× from Python (25× over Python batch when called from C++, synthetic) |
| [alpha-gp-lab](https://github.com/hihihhi/alpha-gp-lab) | Search factor expressions without fooling yourself | Genetic programming over a restricted, parsed grammar; train/validation/test roles; equal-budget random search and a one-line control; post-hoc beta/size neutralisation | Test rank IC 0.082 but net not significant (t 0.22); random search 0.080, one-line control 0.082; 60% survives post-hoc beta/size neutralisation |
| [imc-prosperity-4-shdc](https://github.com/hihihhi/imc-prosperity-4-shdc) | What we did in each round, what other teams did differently, and what I learned | Round-by-round write-up against 9 public Prosperity 4 write-ups (placements 2nd to 583rd, as stated) | 904 / 18,803 (IMC's team count) |
| [ptcg-ai-battle](https://github.com/hihihhi/ptcg-ai-battle) | Play a card game under imperfect information | Imitation learning (set transformer), self-play PPO (not submitted), search baselines | 2,043 / 6,807 (team entry) |
| [agent-harness](https://github.com/hihihhi/agent-harness) | Give seven AI coding tools shared rules and/or memory, and Claude Code a command guard | One standard-library install; A/B-evaluated on 2 of the 7 tools (private question set); guard tested on a held-out set written by the build session | Guard blocks 39 of 45 held-out dangerous commands, 20/20 safe pass |

Also: [Polymarket-Crypto-5min](https://github.com/hihihhi/Polymarket-Crypto-5min), a leakage-controlled chronological walk-forward on public Polymarket and Binance data.

## How I work

Code in these repositories was implemented with AI coding agents under my design and review; each flagship README says so. Every number in a README cites the file or command it came from, and synthetic data is labelled as such.

Python, SQL, C++20, DuckDB / Arrow / Parquet, Linux.
