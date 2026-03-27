import re
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger("ainews.analysis.summarize")

class TextRankSummarizer:
    def summarize(self, text: str, num_sentences: int = 3) -> str:
        """Extractive summarization using TF-IDF and PageRank algorithms."""
        if not text:
            return ""

        # Basic sentence tokenization (split by periods ignoring abbreviations if possible, or simple regex)
        sentences = re.split(r'(?<=[.!?]) +', text.replace('\n', ' '))
        sentences = [s.strip() for s in sentences if len(s.split()) > 4]

        if len(sentences) <= num_sentences:
            return " ".join(sentences)

        try:
            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(sentences)
            
            # Calculate similarity matrix combining tf-idf vectors
            similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
            
            # Build the graph and run PageRank
            nx_graph = nx.from_numpy_array(similarity_matrix)
            scores = nx.pagerank(nx_graph)
            
            # Rank sentences by score
            ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
            
            # Extract the top N sentences and maintain original chronological order
            top_sent_indices = [sentences.index(s[1]) for s in ranked_sentences[:num_sentences]]
            top_sent_indices.sort()
            
            summary = " ".join([sentences[i] for i in top_sent_indices])
            return summary
        except Exception as e:
            logger.error(f"Summarization error: {e}")
            return " ".join(sentences[:num_sentences])

summarizer = TextRankSummarizer()
