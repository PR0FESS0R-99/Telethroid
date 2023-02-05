import asyncio

async def generate_string_session(pyrogram, api_id=False, api_hash=False, out_put="PHONE_NUMBER"): # PHONE_NUMBER or BOT_TOKEN
  async def main():
    
    if api_id & api_hash == False:
      api_id = input("Enter your teegram API_ID")
      api_hash = input("Okke, Enter your teegram API_HASH")
    
    try:
      app = pyrogram.Client("my_account", api_id=int(api_id), api_hash=api_hash)
    except Exception as e:
      print(f"Error {e}")
      return

    async with app:
      s = await app.export_session_string()

      if out_put == "PHONE_NUMBER":
        caption = (f"Pyro String Session v{pyrogram.__version__}! \n\n<code>{s}</code>")
        await app.send_message(chat_id="me", text=caption)
      elif out_put == "BOT_TOKEN":
        caption = (f"Pyro String Session v{pyrogram.__version__}! \n\n<code>{s}</code>")
        print(caption)

  app.run(main())
