# -*- coding: utf-8 -*-

# (c) YashDK [yash-dk@github]

import asyncio,shlex,logging,time,os,aiohttp,shutil

import json, time, asyncio

from telethon.hints import MessageLike

from telethon import events

from telethon.tl.types import KeyboardButtonCallback, KeyboardButtonUrl

from typing import Union,List,Tuple,Dict,Optional

from ..functions.Human_Format import human_readable_bytes

from ..functions.tele_upload import upload_handel

from ..core.getVars import get_val

from ..functions.rclone_upload import get_config,rclone_driver

from functools import partial

from PIL import Image

torlog = logging.getLogger(__name__)

# attempt to decorate error prone areas

import traceback

def skipTorExp(func):

    def wrap_func(*args,**kwargs):

        try:

            return func(*args,**kwargs)

        except Exception as e:

            torlog.error(e)

            return

    return wrap_func

async def cli_call(cmd: Union[str,List[str]]) -> Tuple[str,str]:

    if isinstance(cmd,str):

        cmd = shlex.split(cmd)

    elif isinstance(cmd,(list,tuple)):

        pass

    else:

        return None,None

    

    process = await asyncio.create_subprocess_exec(

        *cmd,

        stderr=asyncio.subprocess.PIPE,

        stdout=asyncio.subprocess.PIPE

    )

    stdout, stderr = await process.communicate()

    

    stdout = stdout.decode().strip()

    stderr = stderr.decode().strip()

    with open("test.txt","w",encoding="UTF-8") as f:

        f.write(stdout)

    

    return stdout, stderr

async
