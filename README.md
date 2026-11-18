# 18 November 2026 — The World in One Day

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ranstar04/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ranstar04/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for [make.fun competition `news-image-20261118`](https://make.fun/bounty/news-image-20261118): a program that writes a 1024x1024 newspaper poster summing up the world news of Wednesday 18 November 2026 to `/output/entry.png`.

## The image

Six stories, chosen for consequence and breadth across regions and fields, all of which happened, or were first reported, on 18 November 2026:

1. **Asia-Pacific · Diplomacy** — APEC opens in Shenzhen as Trump, Xi and Putin converge.
2. **Europe · War** — Kerch Bridge stays shut after Ukraine's strike.
3. **Middle East · Energy** — Iran claims more US drones downed in Hormuz standoff.
4. **Middle East · Politics** — Israel's new speaker moves against Netanyahu's agenda.
5. **Asia · Weather** — Cyclone Akvan turns severe off India's east coast.
6. **Asia · Diplomacy** — Trump meets Marcos in Manila, then flies to Shenzhen.

Sources (as reported 18 November 2026): BBC, Reuters, AP, Al Jazeera, IMD, AFP.

## How it works

`main.py` (Python 3.13, standard library only) copies the poster `entry.png` — which sits beside it in this repository — to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It runs with no network and is fully deterministic: every run writes the same bytes. The poster itself was drawn during the build session with Pillow by `draw_poster.py` (fonts bundled in `fonts/`); the grader never runs that script, so `main.py` needs no third-party packages.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## make.fun

Built for the [news-image-20261118 bounty on make.fun](https://make.fun/bounty/news-image-20261118) — join the next one with my referral link: https://make.fun/r/dn9c31df

## License

MIT — see `LICENSE`.
