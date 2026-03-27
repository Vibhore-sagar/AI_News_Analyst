from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from typing import List, Dict
import logging

logger = logging.getLogger("ainews.processing.cluster")

class ArticleClusterer:
    def cluster_articles(self, articles: List[dict], num_clusters: int = None) -> Dict[int, List[dict]]:
        """Groups articles dynamically using KMeans and TF-IDF vectors."""
        if not articles:
            return {}
            
        if len(articles) < 3:
            return {0: articles}
            
        # Determine number of clusters automatically if not provided
        n_clusters = num_clusters or max(2, min(len(articles) // 3 + 1, 5)) 

        texts = [a.get("content", "") + " " + a.get("title", "") for a in articles]

        try:
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
            X = vectorizer.fit_transform(texts)
            
            kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            kmeans.fit(X)
            
            clusters = {}
            for idx, label in enumerate(kmeans.labels_):
                label = int(label)
                if label not in clusters:
                    clusters[label] = []
                clusters[label].append(articles[idx])
                
            return clusters
        except Exception as e:
            logger.error(f"Clustering error: {e}")
            return {0: articles}

clusterer = ArticleClusterer()
