---
UID: NC.wlanihv.DOT11EXT_REQUEST_VIRTUAL_STATION
title: DOT11EXT_REQUEST_VIRTUAL_STATION
author: windows-driver-content
description: 
ms.assetid: 3c66df03-bf5b-47e4-adb8-96c714cd5c67
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

# DOT11EXT_REQUEST_VIRTUAL_STATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_REQUEST_VIRTUAL_STATION Dot11extRequestVirtualStation; 

// Definition

DWORD Dot11extRequestVirtualStation 
(
	HANDLE hDot11PrimaryHandle
	LPVOID pvReserved
)
{...}

DOT11EXT_REQUEST_VIRTUAL_STATION 


```

## -parameters

### -param hDot11PrimaryHandle: 
### -param pvReserved: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also