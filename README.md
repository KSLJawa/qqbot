# QQ Task Management Bot
> COMP2116 Software Engineering Final Project  
> Macao Polytechnic University

---

## Graphical Abstract
```text
qq-task-bot/
|-- .env
|-- .env.dev
|-- bot.py
|-- requirements.txt
|-- models/
|   |-- __init__.py
|   `-- models.py
`-- plugins/
    |-- __init__.py
    `-- task_manager/
        |-- __init__.py
        |-- config.py
        `-- data_source.py


```

## Purpose

### Software Development Process
This project adopts the **Agile Scrum** development process, divided into 3 sprints:
1. **Sprint 1 (Days 1-2)**: Environment setup, QQ bot account creation, database model design
2. **Sprint 2 (Days 3-4)**: Core command implementation, local testing
3. **Sprint 3 (Days 5-6)**: Documentation, demo video recording, final testing

### Reason for Choosing Agile Scrum
We chose Agile Scrum over the Waterfall model because:
- **Flexibility**: Allows for iterative development and quick adjustment of feature priorities
- **Fast Feedback**: Core features can be tested early, and bugs can be fixed in subsequent sprints
- **Suitability**: Ideal for small-team (1-person) projects with evolving requirements

### Target Market
This bot is designed for **individual QQ users** who want a simple, convenient way to manage their tasks without installing additional apps. It integrates seamlessly into their daily QQ usage.

---

## Software Development Plan

### Development Process
1. **Environment Setup**: Install Python, PyCharm, and configure go-cqhttp
2. **Model Design**: Define SQLAlchemy models for QQ users and tasks
3. **Bot Logic**: Implement command handlers using NoneBot2
4. **Local Testing**: Test all commands with a real QQ account
5. **Documentation**: Write this README.md and record the demo video

### Members (Roles & Responsibilities & Portion)
- **[Your Full Name]**: Full-stack development, testing, documentation (100%)

### Schedule
| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Sprint 1 | Days 1-2 | Environment setup, database models |
| Sprint 2 | Days 3-4 | Core commands, local testing |
| Sprint 3 | Days 5-6 | README.md, demo video, final submission |

### Algorithm
This project uses:
- **Command Pattern**: To handle user input commands (`/start`, `/add`, `/list`, etc.)
- **ORM Pattern**: SQLAlchemy for database operations
- **Reverse WebSocket**: For real-time communication between go-cqhttp and NoneBot2

### Current Status
All core features are fully implemented and tested locally. The bot can:
- Register new users
- Add, list, complete, and delete tasks
- Persist data in an SQLite database

### Future Plan
1. Add task due date reminders
2. Support task categories and tags
3. Add task notes functionality
4. Deploy to a cloud server for 24/7 availability

---

## Demo
[Click here to watch the demo video on YouTube](https://www.youtube.com/watch?v=H4KngLi8UQU)  
*Replace the link with your actual YouTube video URL*

---

## Environments
- **Development Tool**: PyCharm 2024+
- **Programming Language**: Python 3.12
- **Web Framework**: FastAPI
- **QQ Bot Framework**: NoneBot2
- **Protocol Client**: go-cqhttp
- **Database**: SQLAlchemy + SQLite
- **Required Packages**:
  - `nonebot2[fastapi]`
  - `nonebot-adapter-onebot`
  - `sqlalchemy`
  - `python-dotenv`
- **Hardware Requirements**: Any computer capable of running Python
- **Software Requirements**: QQ client (for testing)

---

## Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/qqbot.git
   cd qqbot
   ```

2. **Create a virtual environment and install dependencies**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Copy `.env.example` to `.env` and `.env.dev`
   - Edit `.env.dev` and fill in your QQ bot information

4. **Configure and run go-cqhttp**:
   - Follow the instructions in `go-cqhttp_config_example.yml`
   - Start `go-cqhttp.exe` and log in with your bot QQ account

5. **Run the bot**:
   ```bash
   python bot.py
   ```

6. **Test the bot**:
   - Send `/start` to your bot QQ account from your main QQ account

---

## Declaration
This project uses the following open-source projects:
- **NoneBot2** (MIT License): https://github.com/nonebot/nonebot2
- **go-cqhttp** (AGPL-3.0 License): https://github.com/Mrs4s/go-cqhttp
- **FastAPI** (MIT License): https://github.com/tiangolo/fastapi
- **SQLAlchemy** (MIT License): https://github.com/sqlalchemy/sqlalchemy

All third-party code has been properly declared in this document.

---

## License
MIT License
