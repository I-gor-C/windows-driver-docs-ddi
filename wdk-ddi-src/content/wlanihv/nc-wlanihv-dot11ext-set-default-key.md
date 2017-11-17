---
UID: NC.wlanihv.DOT11EXT_SET_DEFAULT_KEY
title: DOT11EXT_SET_DEFAULT_KEY
author: windows-driver-content
description: 
ms.assetid: 8714b9c0-7acb-47cc-8b7c-97671e18100e
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

# DOT11EXT_SET_DEFAULT_KEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_DEFAULT_KEY Dot11extSetDefaultKey; 

// Definition

DWORD Dot11extSetDefaultKey 
(
	HANDLE hDot11SvcHandle
	PDOT11_CIPHER_DEFAULT_KEY_VALUE pKey
	DOT11_DIRECTION dot11Direction
)
{...}

DOT11EXT_SET_DEFAULT_KEY 


```

## -parameters

### -param hDot11SvcHandle: 
### -param pKey: 
### -param dot11Direction: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also