---
UID: NC.wlanihv.DOT11EXT_FREE_BUFFER
title: DOT11EXT_FREE_BUFFER
author: windows-driver-content
description: 
ms.assetid: e30ed145-3953-4dee-8dc8-28ca547b03fc
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

# DOT11EXT_FREE_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_FREE_BUFFER Dot11extFreeBuffer; 

// Definition

VOID Dot11extFreeBuffer 
(
	LPVOID pvMemory
)
{...}

DOT11EXT_FREE_BUFFER 


```

## -parameters

### -param pvMemory: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also