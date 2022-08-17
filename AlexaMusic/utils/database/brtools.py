import asyncio
import datetime
import os
import random
import string
import time
import traceback

import aiofiles
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)
from protector.brdb import db, dcmdb

# BR Tools

broadcast_ids = {}


async def main_broadcast_handler(m, db):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text="**💡 Bʀᴏᴀᴅᴄᴀsᴛ Sᴛᴀʀᴛᴇᴅ...**\n\n**» Wʜᴇɴ ɪᴛ's ᴅᴏɴᴇ, ʏᴏᴜ'ʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʜᴇʀᴇ...!**"
    )

    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users, current=done, failed=failed, success=success
    )
    async with aiofiles.open("broadcast-logs.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success)
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"✅ Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Cᴏᴍᴘʟᴇᴛᴇᴅ! \n**Completed in:** `{completed_in}` \n\n**Total users:** `{total_users}` \n**Total done:** `{done}` \n**Total success:** `{success}` \n**Total failed:** `{failed}`",
            quote=True,
        )
    else:
        await m.reply_document(
            document="broadcast-logs.txt",
            caption=f"✅ Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Cᴏᴍᴘʟᴇᴛᴇᴅ! \n**Completed in:** `{completed_in}`\n\n**Total users:** `{total_users}` \n**Total done:** `{done}` \n**Total success:** `{success}` \n**Total failed:** `{failed}`",
            quote=True,
        )
    os.remove("broadcast-logs.txt")
