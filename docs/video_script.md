# Hackathon Video Pitch Script: AI News Analyst Engine

**Target Video Length**: ~3 Minutes
**Pacing**: Energetic, confident, and highly technical when explaining the "Non-LLM" advantage.

---

## Part 1: The Problem (0:00 - 0:30)
**Visuals**: Show your face (picture-in-picture) alongside a screen showing articles or a fake high invoice for OpenAI API credits.

**Audio / Script**:
> "Hi, I'm [Your Name], and I built the AI News Analyst Engine. 
> Every day, financial analysts and PR teams spend hours manually parsing through completely unstructured news stories to find market insights. To automate this, enterprises currently spend thousands of dollars on generative AI subscriptions—risking massive strategic data leaks when they send their private queries to OpenAI or Anthropic.
> So, I asked myself: Can we build a private, ultra-fast Multi-Agent pipeline to find breaking market intelligence *without* spending a single dime on LLMs? Yes, we can."

---

## Part 2: The Solution & Architecture (0:30 - 1:00)
**Visuals**: Open up the `docs/hackathon_architecture.md` file and put the Mermaid Flowchart on the screen so judges see the 3 Agents.

**Audio / Script**:
> "My solution is a 100% offline Statistical Machine Learning engine.
> It uses three distinct autonomous agents: 
> First, the **Research Agent** actively scrapes and ingests breaking global news. 
> Next, the **Analysis Agent** takes over. But instead of asking ChatGPT to summarize the text, it mathematically plots the articles using TF-IDF vectorization and clusters identical stories together utilizing scikit-learn. It extracts the raw market tone using Vader Sentiment Lexicons, and summarizes the articles using graph-based TextRank.
> Finally, the **Report Agent** translates that math into a stunning delivery dashboard."

---

## Part 3: The Live Demo (1:00 - 2:15)
**Visuals**: Open up `http://localhost:8000/`. Type something like "Quantum Computing" or "Global Technology Trends" into the Search bar. Emphasize the sleek loading animations.

**Audio / Script**:
> "Let’s see it in action. I'm going to trigger a live hunt for 'Quantum Computing'.
> Right now, the Research Agent is actively pulling dozens of articles. The Analysis Agent is vectorizing them locally on my CPU in milliseconds. 
> And... done."
*(Hover over one of the generated clusters).*
> "Look at this. The engine successfully deduplicated the noise and formed a 'Story Group' around a specific breakthrough. It evaluated the Overall News Tone mathematically.
> And because I built a deterministic Rules Engine underneath everything, it flagged this specific cluster with a unique AI insight, proving it's trending globally. All of this happening offline, with zero API latency."

---

## Part 4: Business Impact & Closing (2:15 - 3:00)
**Visuals**: Cut to the `docs/business_impact.md` OR have a slide showing "$0.00 API Costs" and "Zero Data Leakage".

**Audio / Script**:
> "The business impact here is completely undeniable. 
> By running this Multi-Agent pipeline strictly on local hardware and bypassing major LLM providers, an enterprise firm with 500 analysts avoids paying over $60,000 a year in pure generative compute fees. More importantly, they maintain absolute data privacy, ensuring their strategic research queries never leak to competitors.
> It’s intelligent, it’s secure, and it's 100% free to operate. Thank you."
