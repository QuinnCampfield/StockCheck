import streamlit as st
import requests
import os

# Get API URL from environment variable (for Docker) or use localhost
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("Financial Data Assistant")

if 'tickers' not in st.session_state:
    st.session_state.tickers = ["AAPL"]

# Display current tickers
for i, ticker in enumerate(st.session_state.tickers):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.session_state.tickers[i] = st.text_input(f"Ticker {i+1}:", value=ticker, key=f"ticker_{i}")
    with col2:
        if st.button("Remove", key=f"remove_{i}"):
            st.session_state.tickers.pop(i)
            st.rerun()

# Add new ticker button
if st.button("Add Ticker"):
    st.session_state.tickers.append("")
    st.rerun()

# Ingest button
if st.button("📊 Ingest Market Data"):
    with st.spinner("Downloading market data..."):
        try:
            # Make API request to your FastAPI server
            if st.session_state.tickers:
                # Build query parameters for the tickers
                params = {"tickers": st.session_state.tickers}
                response = requests.post(f"{API_URL}/ingest", params=params)
            else:
                # No tickers specified, use default
                response = requests.post(f"{API_URL}/ingest")
            
            if response.status_code == 200:
                st.success("Data ingested successfully!")
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to API server. Make sure your FastAPI server is running on http://127.0.0.1:8000")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Question input
question = st.text_input("Ask a question about the market data:")

if question:
    with st.spinner("Thinking..."):
        try:
            # Make API request to ask endpoint
            response = requests.get(f"{API_URL}/ask", params={"q": question})

            if response.status_code == 200:
                result = response.json()
                st.write("**Answer:**")
                # Use a proper text area that handles multi-line text correctly
                st.text_area(
                    "",
                    value=result["answer"],
                    height=200,
                    disabled=True,
                    key="ai_response",
                    help="AI response about your financial data"
                )
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to API server. Make sure your FastAPI server is running on http://127.0.0.1:8000")
        except Exception as e:
            st.error(f"Error: {str(e)}")
