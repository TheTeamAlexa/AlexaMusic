#
# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki © AnonXMusic


import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL
from AlexaMusic import app


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def gen_thumb(videoid, user_id, theme):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"][:30]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await app.get_profile_photos(user_id)
            wxy = await app.download_media(
                wxyz[0]["file_id"], file_name=f"{user_id}.jpg"
            )
        except:
            hehe = await app.get_profile_photos(app.id)
            wxy = await app.download_media(
                hehe[0]["file_id"], file_name=f"{app.id}.jpg"
            )
        xy = Image.open(wxy)
        a = Image.new("L", [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640, 640)], 0, 360, fill=255, outline="white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((107, 107))

        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"Backgrounds/{theme}.PNG")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)

        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((365, 365), Image.LANCZOS)
        width = int((1280 - 365) / 2)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 138), mask=logo)
        background.paste(x, (710, 427), mask=x)
        background.paste(image3, (0, 0), mask=image3)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/font2.ttf", 40)
        ImageFont.truetype("assets/font2.ttf", 60)
        arial = ImageFont.truetype("assets/font2.ttf", 25)
        ImageFont.truetype("assets/font.ttf", 25)
        para = textwrap.wrap(title, width=32)
        try:
            text_w, text_h = draw.textsize(f"ALEXA MUSIC IS PLAYING OP", font=font)
            draw.text(
                ((1280 - text_w) / 2, 30),
                f"ALEXA MUSIC IS PLAYING OP",
                fill="red",
                font=font,
            )
            text_w, text_h = draw.textsize(
                f"Alexa Music One Of The Most Advanced Telegram Music Bot", font=arial
            )
            draw.text(
                ((1280 - text_w) / 2, 80),
                f"Alexa Music One Of The Most Advanced Telegram Music Bot",
                fill="green",
                font=arial,
            )
            if para[0]:
                text_w, text_h = draw.textsize(f"{para[0]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 550),
                    f"{para[0]}",
                    fill="yellow",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
            if para[1]:
                text_w, text_h = draw.textsize(f"{para[1]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 600),
                    f"{para[1]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
        except:
            pass
        text_w, text_h = draw.textsize(f"YouTube: Jankari Ki Duniya", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 620),
            f"YouTube: Jankari Ki Duniya",
            fill="white",
            font=arial,
        )
        text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 660),
            f"Duration: {duration} Mins",
            fill="black",
            font=arial,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}_{user_id}.png")
        return f"cache/{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


async def gen_qthumb(videoid, user_id, theme):
    if os.path.isfile(f"cache/que{videoid}_{user_id}.png"):
        return f"cache/que{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"][:30]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxyz = await app.get_profile_photos(user_id)
            wxy = await app.download_media(
                wxyz[0]["file_id"], file_name=f"{user_id}.jpg"
            )
        except:
            hehe = await app.get_profile_photos(app.id)
            wxy = await app.download_media(
                hehe[0]["file_id"], file_name=f"{app.id}.jpg"
            )
        xy = Image.open(wxy)
        a = Image.new("L", [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640, 640)], 0, 360, fill=255, outline="white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((107, 107))

        youtube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"Backgrounds/{theme}.PNG")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)

        image3 = changeImageSize(1280, 720, bg)
        image5 = image3.convert("RGBA")
        Image.alpha_composite(background, image5).save(f"cache/temp{videoid}.png")

        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo.save(f"cache/chop{videoid}.png")
        if not os.path.isfile(f"cache/cropped{videoid}.png"):
            im = Image.open(f"cache/chop{videoid}.png").convert("RGBA")
            add_corners(im)
            im.save(f"cache/cropped{videoid}.png")

        crop_img = Image.open(f"cache/cropped{videoid}.png")
        logo = crop_img.convert("RGBA")
        logo.thumbnail((365, 365), Image.LANCZOS)
        width = int((1280 - 365) / 2)
        background = Image.open(f"cache/temp{videoid}.png")
        background.paste(logo, (width + 2, 138), mask=logo)
        background.paste(x, (710, 427), mask=x)
        background.paste(image3, (0, 0), mask=image3)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/font2.ttf", 40)
        ImageFont.truetype("assets/font2.ttf", 60)
        arial = ImageFont.truetype("assets/font2.ttf", 25)
        ImageFont.truetype("assets/font.ttf", 25)
        para = textwrap.wrap(title, width=32)
        try:
            text_w, text_h = draw.textsize(f"ALEXA ADDED THIS SONG TO QUEUE", font=font)
            draw.text(
                ((1280 - text_w) / 2, 30),
                f"ALEXA ADDED THIS SONG TO QUEUE",
                fill="red",
                font=font,
            )
            text_w, text_h = draw.textsize(
                f"Alexa Music One Of The Most Advanced Telegram Music Bot", font=arial
            )
            draw.text(
                ((1280 - text_w) / 2, 80),
                f"Alexa Music One Of The Most Advanced Telegram Music Bot",
                fill="green",
                font=arial,
            )
            if para[0]:
                text_w, text_h = draw.textsize(f"{para[0]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 550),
                    f"{para[0]}",
                    fill="yellow",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
            if para[1]:
                text_w, text_h = draw.textsize(f"{para[1]}", font=font)
                draw.text(
                    ((1280 - text_w) / 2, 600),
                    f"{para[1]}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
        except:
            pass
        text_w, text_h = draw.textsize(f"YouTube: Jankari Ki Duniya", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 620),
            f"YouTube: Jankari Ki Duniya",
            fill="white",
            font=arial,
        )
        text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
        draw.text(
            ((1280 - text_w) / 2, 660),
            f"Duration: {duration} Mins",
            fill="black",
            font=arial,
        )

        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        file = f"cache/que{videoid}_{user_id}.png"
        background.save(f"cache/que{videoid}_{user_id}.png")
        return f"cache/que{videoid}_{user_id}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
