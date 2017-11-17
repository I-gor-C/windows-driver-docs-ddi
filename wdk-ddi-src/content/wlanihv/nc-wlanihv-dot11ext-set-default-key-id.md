---
UID: NC.wlanihv.DOT11EXT_SET_DEFAULT_KEY_ID
title: DOT11EXT_SET_DEFAULT_KEY_ID
author: windows-driver-content
description: 
ms.assetid: 014e8ea7-7441-4486-a750-1239fcb18600
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

# DOT11EXT_SET_DEFAULT_KEY_ID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_DEFAULT_KEY_ID Dot11extSetDefaultKeyId; 

// Definition

DWORD Dot11extSetDefaultKeyId 
(
	HANDLE hDot11SvcHandle
	ULONG uDefaultKeyId
)
{...}

DOT11EXT_SET_DEFAULT_KEY_ID 


```

## -parameters

### -param hDot11SvcHandle: 
### -param uDefaultKeyId: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also