---
UID: NC.wlanihv.DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM
title: DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM
author: windows-driver-content
description: 
ms.assetid: 6893414d-8e41-402f-b20d-af6fec30874d
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

# DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM Dot11extSetUnicastCipherAlgorithm; 

// Definition

DWORD Dot11extSetUnicastCipherAlgorithm 
(
	HANDLE hDot11SvcHandle
	DWORD dwUnicastCipherAlgo
)
{...}

DOT11EXT_SET_UNICAST_CIPHER_ALGORITHM 


```

## -parameters

### -param hDot11SvcHandle: 
### -param dwUnicastCipherAlgo: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also