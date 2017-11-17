---
UID: NC.wlanihv.DOT11EXT_NIC_SPECIFIC_EXTENSION
title: DOT11EXT_NIC_SPECIFIC_EXTENSION
author: windows-driver-content
description: 
ms.assetid: 13489331-16c7-40f3-a782-e84abddc238e
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

# DOT11EXT_NIC_SPECIFIC_EXTENSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_NIC_SPECIFIC_EXTENSION Dot11extNicSpecificExtension; 

// Definition

DWORD Dot11extNicSpecificExtension 
(
	HANDLE hDot11SvcHandle
	DWORD dwInBufferSize
	LPVOID pvInBuffer
	DWORD *pdwOutBufferSize
	LPVOID pvOutBuffer
)
{...}

DOT11EXT_NIC_SPECIFIC_EXTENSION 


```

## -parameters

### -param hDot11SvcHandle: 
### -param dwInBufferSize: 
### -param pvInBuffer: 
### -param *pdwOutBufferSize: 
### -param pvOutBuffer: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also