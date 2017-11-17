---
UID: NC.wlanihv.DOT11EXT_PROCESS_ONEX_PACKET
title: DOT11EXT_PROCESS_ONEX_PACKET
author: windows-driver-content
description: 
ms.assetid: e08e07b4-b782-4786-aa12-28757daee2d6
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

# DOT11EXT_PROCESS_ONEX_PACKET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_PROCESS_ONEX_PACKET Dot11extProcessOnexPacket; 

// Definition

DWORD Dot11extProcessOnexPacket 
(
	HANDLE hDot11SvcHandle
	DWORD dwInPacketSize
	LPVOID pvInPacket
)
{...}

DOT11EXT_PROCESS_ONEX_PACKET 


```

## -parameters

### -param hDot11SvcHandle: 
### -param dwInPacketSize: 
### -param pvInPacket: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also