class TextReportGenerator:
    def generate_markdown(self, raw_report: dict) -> str:
        query = raw_report.get("query", raw_report.get("topic", "Unknown Topic"))
        clusters = raw_report.get("topic_clusters", [])
        
        md = f"# AI News Analyst Report: {query}\n"
        md += f"**Total Articles Processed:** {raw_report.get('total_articles', 0)}\n"
        md += "---\n\n"
        
        if not clusters:
            return md + "*No distinct news clusters generated for this topic.*"
            
        for cluster in clusters:
            md += f"## Cluster {cluster.get('cluster_number', 0)} ({cluster.get('articles_in_cluster', 0)} Articles)\n"
            md += f"**Aggregated Sentiment**: {cluster.get('aggregate_sentiment', 'Neutral')}\n\n"
            md += "### Machine Given Insights\n"
            for insight in cluster.get('insights', []):
                md += f"- {insight}\n"
            
            md += "\n### Top Clippings\n"
            for idx, art in enumerate(cluster.get('top_articles', [])):
                md += f"> **{art.get('source', 'Source')}**: {art.get('summary', '')}\n\n"
                
            md += "---\n"
            
        return md

text_report_generator = TextReportGenerator()
