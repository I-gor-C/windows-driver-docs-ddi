---
UID: NC.wlanihv.DOT11EXT_SET_EXCLUDE_UNENCRYPTED
title: DOT11EXT_SET_EXCLUDE_UNENCRYPTED
author: windows-driver-content
description: 
ms.assetid: 66f8a654-7536-4cba-9f5e-d1fe312101e8
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

# DOT11EXT_SET_EXCLUDE_UNENCRYPTED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_EXCLUDE_UNENCRYPTED Dot11extSetExcludeUnencrypted; 

// Definition

DWORD Dot11extSetExcludeUnencrypted 
(
	HANDLE hDot11SvcHandle
	BOOL bExcludeUnencrypted
)
{...}

DOT11EXT_SET_EXCLUDE_UNENCRYPTED 


```

## -parameters

### -param hDot11SvcHandle: 
### -param bExcludeUnencrypted: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also