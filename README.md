<div align="center">

# 🛰️ iSpaceRobot

**A production Telegram bot platform that runs a whole chat ecosystem — moderation, an AI companion, economy, games and userbot automation — inside one asyncio service.**

[![Telegram](https://img.shields.io/badge/Telegram-@iSpaceRobot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/iSpaceRobot)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-1F8ACB?style=for-the-badge)](https://docs.aiogram.dev/)

**Live bot → [@iSpaceRobot](https://t.me/iSpaceRobot)** · add it to a group and send `!космос`

</div>

---

## 🧰 Tech Stack

- 🐍 **Python 3.12** — fully async, `asyncio` end to end
- 🤖 **aiogram 3** — routers, FSM, middlewares, custom filters
- 🔥 **Pyrogram 2 (MTProto)** — userbot pool for daily cleanup & Star Gifts
- 🐘 **PostgreSQL + asyncpg** — data layer, one module per table
- 🧩 **Redis** — FSM storage, rate limits, hot counters
- 🧠 **OpenAI / OpenRouter** — persona chat, voice, meme generation
- 🖼️ **Pillow + matplotlib** — profile cards, charts, rendered media
- ⏰ **APScheduler** — scheduled jobs (night mode, daily logs, cleanup)
- 🌍 **JSON i18n** — Russian / English / Ukrainian

## 📁 Project Structure

```text
iSpaceRobot-tg-bot/
├── main.py                     # entry point: routers, polling, graceful shutdown
├── config.py                   # env-driven settings contract (no secrets)
├── redis_client.py             # async Redis connection
├── requirements.txt
├── .env.example
└── app/
    ├── AI.py                   # LLM router: persona chat, voice, memes
    ├── db.py                   # asyncpg pool + SQL call tracing
    ├── kbs.py                  # shared inline keyboards (UI contract)
    ├── states.py               # FSM state groups (contract)
    ├── i18n.py                 # JSON localisation loader
    ├── ai_chat/                # "Space" persona: memory, mood, style
    │   ├── models.py           #   DTOs & enums (kept intact)
    │   ├── repository.py       #   persistence contract
    │   ├── nsfw_*.py           #   media safety pipeline
    │   └── video_meme/         #   video meme renderer
    ├── agent_of_stars/         # scammer reports & agent panel
    ├── chat_owner/             # per-chat settings, night mode, kicks, migration
    ├── owner/                  # global admin panel, catalog, protection, broadcast
    ├── user/                   # profile, inventory, duels, donations, business
    ├── user_bot/               # Pyrogram userbots: cleanup pool, Star Gifts API
    ├── crud_tables/            # data-access layer (one module per table)
    ├── middlewares/            # stats, activity, night mode, banlist, updates
    ├── roulette/               # roulette game engine
    ├── daily_jobs/             # scheduled maintenance
    ├── debug/                  # structured runtime diagnostics
    ├── logs/                   # daily chat logs
    ├── help_system/            # help texts & guides
    ├── filters/                # custom aiogram filters
    ├── offers/                 # purchasable offers
    ├── server_settings/        # stand-alone node settings
    └── locales/                # ru.json / en.json / ua.json
```

## ✨ Key Features

- 🧠 **AI companion with memory** — the "Space" persona keeps per-chat and per-user memory, adapts its mood and writing style, answers with text, voice or memes.
- 🛡️ **Moderation & protection** — anti-spam, anti-forward, blacklists, banlists, allowed-links filters, night mode and scheduled activity-based kicks.
- 🎮 **Economy & games** — coins and star coins, inventory, roulette, duels, marriages and weekly tops with rendered charts.
- 🧹 **Userbot cleanup pool** — a pool of MTProto accounts verifies that a group is really dead before the bot drops its settings, with proof-of-life snapshots and hard safety caps.
- 🎁 **Star Gifts API** — a small REST layer on top of a userbot that serves gift catalogues to the Telegram Mini App, plus an NSFW media-safety pipeline for generated content.

## 🖼️ Screenshots

![App Preview](demo.png)

## 📌 About This Repository

This is a **public showcase copy** of a private production bot:

- folder layout, interfaces, DTOs, models, FSM states and UI contracts are kept as-is;
- every implementation body is replaced with `pass  # TODO: Commercial logic`;
- secrets, API keys, sessions, database dumps and runtime artifacts are removed — see `.env.example` for the expected environment.

© iSpaceRobot · the bot itself is live at [@iSpaceRobot](https://t.me/iSpaceRobot)
