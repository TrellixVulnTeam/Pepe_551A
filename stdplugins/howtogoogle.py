# Modded from dagd.py
"""
Animate How To Google
Command .ggl Search Query
By @loxxi
"""
import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ggl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        input_str.replace(" ", "+")
    )
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit(
            "Here you go Sur 😉 [{}]({})\n`Le Link aur dalde apne piche 🖕` ".format(
                input_str, response_api.rstrip()
            )
        )
    else:
        await event.edit("something is wrong. please try again later.")
