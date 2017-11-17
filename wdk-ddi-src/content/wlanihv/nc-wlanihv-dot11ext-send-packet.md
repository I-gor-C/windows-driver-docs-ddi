---
UID: NC.wlanihv.DOT11EXT_SEND_PACKET
title: DOT11EXT_SEND_PACKET
author: windows-driver-content
description: 
ms.assetid: 3e8a0aa1-9c29-4966-8802-38970aa2cd77
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wlanihv.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# DOT11EXT_SEND_PACKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SEND_PACKET Dot11extSendPacket; 

// Definition

DWORD Dot11extSendPacket 
(
	HANDLE hDot11SvcHandle
	ULONG uPacketLen
	LPVOID pvPacket
	HANDLE hSendCompletion
)
{...}

DOT11EXT_SEND_PACKET 


```

## -parameters

### -param hDot11SvcHandle: 
### -param uPacketLen: 
### -param pvPacket: 
### -param hSendCompletion: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also