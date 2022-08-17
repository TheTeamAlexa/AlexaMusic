# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


from typing import Dict, List, Union

from AlexaMusic.core.mongo import mongodb


pmpermitdb = mongodb.permit


async def is_pmpermit_approved(user_id: int) -> bool:
    user = await pmpermitdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def approve_pmpermit(user_id: int):
    is_pmpermit = await is_pmpermit_approved(user_id)
    if is_pmpermit:
        return
    return await pmpermitdb.insert_one({"user_id": user_id})


async def disapprove_pmpermit(user_id: int):
    is_pmpermit = await is_pmpermit_approved(user_id)
    if not is_pmpermit:
        return
    return await pmpermitdb.delete_one({"user_id": user_id})
