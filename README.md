# Interview Assistant

A real-time interview assistance platform that provides live transcription and AI-powered response suggestions for job interviews.

## Features

- Real-time audio transcription using OpenAI Whisper API
- GPT-4o powered response suggestions
- Semi-transparent overlay UI for seamless interview experience
- Knowledge base integration for personalized responses
- Support for both system audio and microphone input

## Project Status

Currently in development. See [implementation plan](docs/implementation_plan.md) for details.

## Technical Stack

- Python 3.11+
- OpenAI API (Whisper & GPT-4o)
- SQLite/PostgreSQL
- PyQt/Tkinter

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/interview-assistant.git
cd interview-assistant
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup configuration:
```bash
cp config/default.yaml config/config.yaml
# Edit config.yaml with your settings
```

5. Run tests:
```bash
pytest
```

## Documentation

- [Project Summary](docs/project_summary.md)
- [Technical Specifications](docs/tech_specifications.md)
- [Implementation Plan](docs/implementation_plan.md)
- [Phase 1 Tasks](docs/phase1_tasks.md)
- [Phase 2 Tasks](docs/phase2_tasks.md)
- [Phase 3 Tasks](docs/phase3_tasks.md)
- [Phase 4 Tasks](docs/phase4_tasks.md)
- [Phase 5 Tasks](docs/phase5_tasks.md)

## License

MIT License - see the [LICENSE](LICENSE) file for details