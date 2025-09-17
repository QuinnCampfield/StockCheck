# 🚀 Deployment Guide

This guide will help you deploy your Financial Data Assistant to Railway so others can access it via a public URL.

## 📋 Prerequisites

1. **GitHub Account** - Your code should be in a GitHub repository
2. **Railway Account** - Sign up at [railway.app](https://railway.app) (free tier available)
3. **OpenAI API Key** - Get one from [OpenAI](https://platform.openai.com/api-keys)

## 🚀 Deployment Steps

### Option 1: Single Deployment (Recommended - Simpler & Cheaper)

1. Go to [Railway](https://railway.app) and sign in
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. In deployment settings, change Dockerfile to `Dockerfile.single`
5. Add environment variables:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   DB_FILE=market_data.csv
   ```
6. Deploy!

**Result**: One URL that serves both API and Streamlit frontend

### Option 2: Two Separate Deployments (More Complex)

#### Step 1: Deploy the API
1. Go to [Railway](https://railway.app) and sign in
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Choose "Deploy Now"
5. Railway will automatically detect the `Dockerfile` and deploy your API

#### Step 2: Set Environment Variables
In your Railway project dashboard:
1. Go to "Variables" tab
2. Add these environment variables:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   DB_FILE=market_data.csv
   ```

#### Step 3: Get Your API URL
1. In Railway dashboard, go to "Settings" → "Domains"
2. Copy your API URL (something like `https://your-app-name.railway.app`)

#### Step 4: Deploy the Frontend
1. Create a new Railway project
2. Connect the same GitHub repository
3. In the deployment settings, change the Dockerfile to `Dockerfile.streamlit-prod`
4. Add environment variable:
   ```
   API_URL=https://your-api-url.railway.app
   ```
5. Deploy

## 🔗 Final Result

- **API**: `https://your-api-name.railway.app` (for developers)
- **Frontend**: `https://your-frontend-name.railway.app` (for users)

## 📝 Adding to Your GitHub README

Add this to your main README.md:

```markdown
## 🌐 Live Demo

Try the Financial Data Assistant: [https://your-frontend-url.railway.app](https://your-frontend-url.railway.app)

## 🚀 Quick Start

1. Clone the repository
2. Set up your `.env` file with your OpenAI API key
3. Run `docker-compose up -d`
4. Visit http://localhost:8501
```

## 🛠️ Troubleshooting

- **API not working**: Check that `OPENAI_API_KEY` is set correctly
- **Frontend can't connect**: Verify `API_URL` points to your deployed API
- **Build fails**: Make sure all files are committed to GitHub

## 💰 Cost

Railway's free tier includes:
- 500 hours of usage per month
- $5 credit monthly
- Perfect for personal projects and demos
