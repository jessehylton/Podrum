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

from podrum.utils.BinaryStream import BinaryStream

class DataPacket(BinaryStream):
    NID = 0
    PID_MASK = 0x3ff # 10 Bits
    
    SUBCLIENT_ID_MASK = 0x03 # 2 Bits
    SENDER_SUBCLIENT_ID_SHIFT = 10
    RECIPIENT_SUBCLIENT_ID_SHIFT = 12
    
    isEncoded = False
    _encapsulatedPacket = None
    
    senderSubId = 0
    recipientSubId = 0
    
    def pid(self):
        return self.NID
        
    def getName(self):
        return type(object).__name__
        
    def canBeBatched():
        return True
        
    def canBeSentBeforeLogin():
        return False
        
    def mayHaveUnreadBytes():
        return False
        
    def decodePayload(): pass
        
    def decode(self):
        self.offset = 0
        self.decodeHeader()
        self.decodePayload()
        
    def decodeHeader(self):
        header = self.getUnsignedVarInt()
        pid = header & self.PID_MASK
        if pid != self.NID:
            raise Exception("Expected " + self.NID + " for packet ID, got " + pid)
        self.senderSubId = (header >> self.SENDER_SUBCLIENT_ID_SHIFT) & self.SUBCLIENT_ID_MASK
        self.recipientSubId = (header >> self.RECIPIENT_SUBCLIENT_ID_SHIFT) & self.SUBCLIENT_ID_MASK;
    
    def encodePayload(): pass
    
    def encode(self):
        self.reset()
        self.encodeHeader()
        self.encodePayload()
        self.isEncoded = True
        
    def encodeHeader(self):
        self.putUnsignedVarInt(
            self.NID |
            (self.senderSubId << self.SENDER_SUBCLIENT_ID_SHIFT) |
            (self.recipientSubId << self.RECIPIENT_SUBCLIENT_ID_SHIFT)
        )
        
    def writePayload(): pass
    
    def clean():
        self.buffer = ""
        self.isEncoded = False
        self.offset = 0
        return self
