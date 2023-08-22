#
# Copyright (C) 2021-2022 by Alexsacei@Github, < https://github.com/kenta9900 >.
# A Powerful Music Bot Property Of Rocks NIRVANA

# Kanged By © @exsaezz
# Rocks © @groupjawanusantara
# Owner Alexsa cei
# Alexsa cei
# All rights reserved. © Alisha © Alexa © Yukki


import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
