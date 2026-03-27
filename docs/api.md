# AI News Analyst API Reference

The primary capability of the system is the localized Macro-Pipeline execution.

### `POST /api/v1/reports/generate-markdown-report`
Triggers the pure-ML flow start-to-finish and returns formatted Markdown.
**Query Parameters**:
- `query` (str): The specific topic to track (e.g. "AI Regulation").
- `limit` (int): Maximum articles to ingest per run (default: 15).

**Response**:
`text/plain` Markdown String + ASCII Chart.

### `POST /api/v1/news/ingest_newsapi`
Triggers ingestion independently of the analysis layer.
**Query Parameters**:
- `query` (str)
- `limit` (int)

### `POST /api/v1/analysis/investigate-and-analyze`
Returns the raw structured `application/json` output of the full Macro-Pipeline without the text markdown formatting. Use this layer if connecting a React or Vue frontend.
