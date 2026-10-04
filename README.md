# Oscar Choi

Computer Science at CUHK (graduating July 2027). I build quant research infrastructure and test trading ideas against point-in-time data, with negative results kept. I am the sole developer and architect of the CUHK Quant Trading Society research team's data platform and a WorldQuant BRAIN research consultant.

## Results

- **IMC Prosperity 4** (team SHDC): 904th of 18,803 teams, 18th in Hong Kong.
- **Kaggle Pokémon TCG AI Battle**: 2,043rd of 6,807.
- **MonsoonSIM Enterprise Resource Management Competition 2025**: 3rd place.

## Projects

| Project | Problem | Method | One number |
|---|---|---|---|
| CUHK QTS research platform (private) | Give a student quant team tick-level market data it can trust | Raw → typed Parquet → cleaned layers, versioned query library and API, data-quality checks, multi-user access control | 650B+ stored market-data rows; 0 lost commits under concurrent writers |
| [asof-research](https://github.com/hihihhi/asof-research) | Can an LLM pick better trading hypotheses than brute force, under one honest gate? | Point-in-time data contracts, frozen method cards, pre-registered protocols, a non-promoting LLM critic, a human gate; C++20 replay hot path | Pre-registered real-data run, 962 numbers independently recomputed; C++ replay 5.5× from Python (61× core) |
| [alpha-gp-lab](https://github.com/hihihhi/alpha-gp-lab) | Search factor expressions without fooling yourself | Genetic programming over a typed grammar, train/validation/test roles, equal-budget random and naive controls, beta/size neutralisation | Every result shown against random, frozen-ranking and market-neutral controls |
| [imc-prosperity-4-shdc](https://github.com/hihihhi/imc-prosperity-4-shdc) | What we did in each round, what top teams did differently, and what I learned | Round-by-round write-up against 11 top-team write-ups | 904 / 18,803 |
| [ptcg-ai-battle](https://github.com/hihihhi/ptcg-ai-battle) | Play a card game under imperfect information within a time budget | Imitation learning (set transformer), self-play PPO, search baselines | 2,043 / 6,807 |
| [agent-harness](https://github.com/hihihhi/agent-harness) | Make seven AI coding tools share rules, memory and safety checks | One standard-library install, A/B-evaluated, command guard tested on held-out cases | Guard blocks 40 of 45 unseen dangerous commands, 20/20 safe pass |

Also: [Polymarket-Crypto-5min](https://github.com/hihihhi/Polymarket-Crypto-5min), a leakage-controlled chronological walk-forward on public Polymarket and Binance data.

## How I work

Code in these repositories was implemented with AI coding agents under my design and review; each README says which parts. Every number in a README cites the file or command it came from, and synthetic data is labelled as such.

Python, SQL, C++20, Rust, DuckDB / Arrow / Parquet, Linux.
