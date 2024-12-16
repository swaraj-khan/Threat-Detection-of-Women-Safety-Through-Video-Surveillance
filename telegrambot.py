import asyncio
from telegram import Bot


BOT_TOKEN = "7690326782:AAE0w6MMKiudA9L-Ww-WfmfsyfKEgcDvV8Q" 
CHAT_ID = "6786809522" 

alert_message = "🚨 Alert! Suspicious activity detected.\nPlease check the attached video."
video_file_path = r"C:\Major Project\peelings.mp4" 


async def send_alert_with_video():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=alert_message)
        print("Alert message sent successfully!")

        with open(video_file_path, "rb") as video_file:
            await bot.send_video(chat_id=CHAT_ID, video=video_file, caption="🔍 Video Footage")
            print("Video clip sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_alert_with_video())
