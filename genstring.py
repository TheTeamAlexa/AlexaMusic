# Credits to Pranav


import asyncio
from pyrogram import Client


async def generate_and_send_string_session(api_id, api_hash):
    async with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
        string_session = await app.export_session_string()
        await app.send_message(
            "me",
            f"<b>Your Pyrogram String Session:</b>\n\n<code>{string_session}</code>",
        )
        print("String session has been sent to your 'Saved Messages'.")


if __name__ == "__main__":
    api_id = int(input("Enter your API ID: "))
    api_hash = input("Enter your API Hash: ")
    asyncio.run(generate_and_send_string_session(api_id, api_hash))
