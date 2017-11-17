---
UID: NC.wlanihv.DOT11EXT_SET_AUTH_ALGORITHM
title: DOT11EXT_SET_AUTH_ALGORITHM
author: windows-driver-content
description: 
ms.assetid: d5fa786d-f379-4ca5-974a-bd7d346c3dc4
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

# DOT11EXT_SET_AUTH_ALGORITHM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_AUTH_ALGORITHM Dot11extSetAuthAlgorithm; 

// Definition

DWORD Dot11extSetAuthAlgorithm 
(
	HANDLE hDot11SvcHandle
	DWORD dwAuthAlgo
)
{...}

DOT11EXT_SET_AUTH_ALGORITHM 


```

## -parameters

### -param hDot11SvcHandle: 
### -param dwAuthAlgo: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also