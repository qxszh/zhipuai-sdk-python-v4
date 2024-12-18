from typing import Optional, List

from ...core import BaseModel

__all__ = ["AudioRequest", "AudioResult"]


class AudioRequest(BaseModel):
    """音频格式，当前支持 wav 和 mp3 两种格式"""
    format: str


class AudioResult(BaseModel):
    """语音唯一标识"""
    id: str
    """语音base64数据"""
    data: str

