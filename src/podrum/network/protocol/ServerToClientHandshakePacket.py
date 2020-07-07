"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
"""

from podrum.network.protocol.DataPacket import DataPacket
from podrum.network.protocol.ProtocolInfo import ProtocolInfo

class ServerToClientHandshakePacket(DataPacket):
    NID = ProtocolInfo.SERVER_TO_CLIENT_HANDSHAKE_PACKET

    jwt = None

    def canBeSentBeforeLogin():
        return True

    def decodePayload(self):
        self.jwt = self.getString()

    def encodePayload(self):
        self.putString(self.jwt)
