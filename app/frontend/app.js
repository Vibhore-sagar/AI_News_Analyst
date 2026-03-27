document.addEventListener('DOMContentLoaded', () => {
    // Fire a default trending analysis on load
    runAnalysis("Global Technology Trends", 15);
});

document.getElementById('homeLogo').addEventListener('click', () => {
    document.getElementById('queryInput').value = ''; // clear input
    runAnalysis("Global Technology Trends", 15);
});

document.getElementById('analyzeBtn').addEventListener('click', () => {
    const query = document.getElementById('queryInput').value.trim();
    const limit = document.getElementById('limitInput').value;

    if (!query) {
        alert("Please enter a topic to analyze.");
        return;
    }
    runAnalysis(query, limit);
});

// Allow Enter key
document.getElementById('queryInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        document.getElementById('analyzeBtn').click();
    }
});

async function runAnalysis(query, limit) {
    // UI States
    document.getElementById('resultsDashboard').classList.add('hidden');
    document.getElementById('errorState').classList.add('hidden');
    document.getElementById('loadingState').classList.remove('hidden');

    try {
        const response = await fetch(`/api/v1/reports/generate-report?query=${encodeURIComponent(query)}&limit=${limit}`, {
            method: 'POST'
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        renderDashboard(data);

    } catch (err) {
        console.error(err);
        document.getElementById('errorText').innerText = `Error generating report: ${err.message}`;
        document.getElementById('errorState').classList.remove('hidden');
    } finally {
        document.getElementById('loadingState').classList.add('hidden');
    }
}

function formatDate(dateString) {
    if (dateString === "Just now") return "Today";
    try {
        const d = new Date(dateString);
        return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute:'2-digit' });
    } catch {
        return dateString;
    }
}

function renderDashboard(data) {
    const rawData = data.raw_json || data.raw_data;
    
    // Header Metrics
    document.getElementById('statArticles').innerText = rawData.total_articles;
    document.getElementById('statTopic').innerText = (rawData.topic || rawData.query).toUpperCase();
    document.getElementById('statReportId').innerText = data.report_id || "N/A";

    // Render Clusters
    const container = document.getElementById('clustersContainer');
    container.innerHTML = '';

    if (!rawData.topic_clusters || rawData.topic_clusters.length === 0) {
        container.innerHTML = '<div class="glass-panel"><p style="text-align:center;">No distinct thematic nodes discovered for this topic.</p></div>';
    } else {
        rawData.topic_clusters.forEach((cluster, idx) => {
            const card = document.createElement('div');
            card.className = 'cluster-card fade-in-up';
            card.style.animationDelay = `${idx * 0.1}s`;
            
            // Generate Insights HTML
            let insightsHtml = '';
            cluster.insights.forEach(insight => {
                insightsHtml += `<div class="insight-pill">💡 ${insight}</div> `;
            });

            // Generate Hover-Accordion Articles HTML
            let articlesHtml = '';
            cluster.top_articles.forEach(art => {
                let displayTitle = art.title ? art.title : `Live Article from ${art.source}`;
                
                articlesHtml += `
                    <div class="article-clip">
                        <div class="article-header">
                            <div class="article-title-row">
                                <a href="${art.url}" target="_blank" class="article-link" title="Read Full Article">
                                    🔗 ${displayTitle}
                                </a>
                            </div>
                            <div class="article-meta">
                                <span>Source: <strong>${art.source}</strong></span>
                                <span class="timestamp">⌚ ${formatDate(art.published_at)}</span>
                            </div>
                        </div>
                        <div class="article-body">
                            <p><strong>AI Summary:</strong> ${art.summary}</p>
                            ${art.bias_flags && art.bias_flags.length > 0 ? `<p style="color:#fbbf24; font-size:0.9rem;">⚠️ Detected Bias: ${art.bias_flags.join(", ")}</p>` : ''}
                        </div>
                    </div>
                `;
            });

            card.innerHTML = `
                <h2>Story Group ${cluster.cluster_number} 
                    <span style="font-size:0.9rem; color:#94a3b8; font-weight:400; float:right;">Combined from ${cluster.articles_in_cluster} Articles</span>
                </h2>
                <p style="margin-bottom: 20px;"><strong>Overall News Tone:</strong> <span style="color:var(--accent);">${cluster.aggregate_sentiment}</span></p>
                <div style="margin-bottom: 24px;">
                    ${insightsHtml}
                </div>
                <h3 style="color:#e2e8f0; font-size: 1rem; text-transform: uppercase;">Articles in this Story <span style="font-size:0.8rem; color:#64748b; font-weight:400;">(Hover below to expand summary)</span></h3>
                <div class="articles-list">
                    ${articlesHtml}
                </div>
            `;
            container.appendChild(card);
        });
    }

    // Show Dashboard
    document.getElementById('resultsDashboard').classList.remove('hidden');
}
