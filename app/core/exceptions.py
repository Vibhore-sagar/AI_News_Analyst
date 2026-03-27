from fastapi import HTTPException

class FetcherError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=f"Fetcher Error: {message}")

class ProcessingError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=f"Processing Error: {message}")

class AnalysisError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=500, detail=f"Analysis Error: {message}")
