# AI News Analyst Architecture (100% Offline / Pure ML Approach)

This project deviates from standard generative RAG architectures by entirely eliminating LLMs to ensure data privacy, speed, and zero API costs.

## The Macro-Pipeline Flow
1. **Ingestion Layer (`app/services/fetchers`)**: Scrapes and fetches latest articles using NewsAPI or raw Scraping.
2. **Processing Layer (`cleaner.py`, `deduplicator.py`)**: Sanitizes HTML and removes identically duplicated URLs.
3. **Clustering Layer (`clusterer.py`)**: Vectorizes all incoming articles using `TfidfVectorizer` and dynamically groups identical stories using `KMeans`, calculating mathematical proximity.
4. **NLP Intelligence Layer (`app/services/analysis`)**: 
   - `entity_extractor.py`: Local `spaCy` detects proper nouns and geopolitical groups.
   - `sentiment_analyzer.py`: `VADER` scores explicit and implicit bias tones perfectly.
   - `summarizer.py`: Mathematical Extractive TextRank scoring via `NetworkX` PageRank.
5. **Rules Engine (`insight_generator.py`)**: Instead of generative guesswork, deterministic heuristic rules fire over the cluster statistics to form concrete insights (e.g. detecting if standard deviation in Tone implies market uncertainty).
6. **Delivery Layer (`report_routes.py`)**: Compiles the data into Markdown and ASCII statistical visual matrices for end-users.
