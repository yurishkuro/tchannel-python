from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from tchannel.singleton import TChannel as TChannelSingleton

from .client import TChannel as SyncTChannel


class TChannel(TChannelSingleton):

    tchannel_cls = SyncTChannel
