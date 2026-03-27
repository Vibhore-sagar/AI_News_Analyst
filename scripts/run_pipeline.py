import asyncio
import os
import sys

# Ensure pure module execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.storage.mongodb import connect_to_mongo, close_mongo_connection
from app.agents.report_agent import report_agent

async def main():
    print("🚀 Booting Local ML Analysis Pipeline...")
    await connect_to_mongo()
    
    topic = "AI Regulation"
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        
    print(f"📡 Fetching, Vectorizing, and Clustering live news for: '{topic}'")
    result = await report_agent.generate_comprehensive_report(topic, limit=10)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print("\n" + "="*60)
        print(result["markdown"])
        print("="*60)
        print(result["visual_chart"])
        print("="*60)
        print(f"✅ Saved to Local MongoDB with Report ID: {result['report_id']}")
        
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(main())
