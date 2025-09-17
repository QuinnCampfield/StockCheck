# 📊 Financial Data Assistant

A modern web application that allows you to analyze financial market data using AI. Built with FastAPI, Streamlit, and OpenAI.

## ✨ Features

- 📈 **Market Data Ingestion**: Download stock data for any tickers
- 🤖 **AI-Powered Analysis**: Ask questions about your financial data
- 🐳 **Docker Ready**: Easy deployment with Docker Compose
- 🌐 **Production Ready**: Deploy to Railway with one click

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd projproj
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

3. **Start with Docker**
   ```bash
   docker-compose up -d
   ```

4. **Access the app**
   - Frontend: http://localhost:8501
   - API Docs: http://localhost:8000/docs

### 🌐 Live Demo

[Try the Financial Data Assistant](https://your-deployed-url.railway.app) *(Update this URL after deployment)*

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: Streamlit
- **AI**: OpenAI GPT-4
- **Data**: yfinance
- **Deployment**: Docker, Railway

## 📁 Project Structure

```
├── app.py                 # FastAPI application
├── streamlit_app.py       # Streamlit frontend
├── pipeline.py           # Data ingestion logic
├── llm_utils.py          # AI integration
├── docker-compose.yml    # Local development
├── Dockerfile            # Production API
└── DEPLOYMENT.md         # Deployment guide
```

## 🚀 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to Railway.

## 📝 Usage

1. **Ingest Data**: Enter ticker symbols (e.g., AAPL, MSFT) and click "Ingest Market Data"
2. **Ask Questions**: Type questions like "How is Apple stock performing?" or "What's the trend for Microsoft?"
3. **Get AI Insights**: Receive detailed analysis of your financial data

## 🔧 Configuration

Set these environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `DB_FILE`: Path to store market data (default: market_data.csv)
- `API_URL`: API endpoint for frontend (for production)

## 📄 License

MIT License - feel free to use this project for learning and development!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Built with ❤️ for financial data analysis**