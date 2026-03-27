class VisualReportGenerator:
    def generate_ascii_chart(self, positive: int, negative: int, neutral: int) -> str:
        total = positive + negative + neutral
        if total == 0:
            return "No data to chart."
            
        def draw_bar(count, total):
            if total == 0:
                return ""
            ratio = int((count / total) * 30)
            return "█" * ratio
            
        chart = "Sentiment Distribution:\n"
        chart += f"Positive: {draw_bar(positive, total)} ({positive})\n"
        chart += f"Negative: {draw_bar(negative, total)} ({negative})\n"
        chart += f"Neutral : {draw_bar(neutral, total)} ({neutral})\n"
        
        return chart

visual_report_generator = VisualReportGenerator()
