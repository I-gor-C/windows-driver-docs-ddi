---
UID: NC.wlanihv.DOT11EXT_ALLOCATE_BUFFER
title: DOT11EXT_ALLOCATE_BUFFER
author: windows-driver-content
description: 
ms.assetid: 35987e98-edff-42a3-9781-7059e95f6d4d
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

# DOT11EXT_ALLOCATE_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_ALLOCATE_BUFFER Dot11extAllocateBuffer; 

// Definition

DWORD Dot11extAllocateBuffer 
(
	DWORD dwByteCount
	LPVOID *ppvBuffer
)
{...}

DOT11EXT_ALLOCATE_BUFFER 


```

## -parameters

### -param dwByteCount: 
### -param *ppvBuffer: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also