import wikipedia
import re

class CelebrityInfoBot:
    def __init__(self):
        wikipedia.set_user_agent("CelebrityInfoBot/1.0")

    def get_celebrity_summary(self, name):
        try:
            summary = wikipedia.summary(name)
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Multiple options found. Please be more specific: {', '.join(e.options)}"

        except wikipedia.exceptions.HTTPTimeoutError as e:
            return f"Error: {e}"

        except wikipedia.exceptions.PageError:
            return "Sorry, information not found."

        return {
            "name": name,
            "summary": summary
        }

celebrity_bot = CelebrityInfoBot()
celebrity_name = input("Enter the celebrity name")
celebrity_info = celebrity_bot.get_celebrity_summary(celebrity_name)

if isinstance(celebrity_info, dict):
    print(f"Summary for {celebrity_name}:")
    print(f"{celebrity_info.get('summary', 'Not available')}")
else:
    print(celebrity_info)
