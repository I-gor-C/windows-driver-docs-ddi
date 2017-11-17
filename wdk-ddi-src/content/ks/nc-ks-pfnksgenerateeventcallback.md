---
UID: NC.ks.PFNKSGENERATEEVENTCALLBACK
title: PFNKSGENERATEEVENTCALLBACK
author: windows-driver-content
description: 
ms.assetid: 9b59be4d-861c-44ac-9eb5-78f7bc2b503b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSGENERATEEVENTCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSGENERATEEVENTCALLBACK Pfnksgenerateeventcallback; 

// Definition

BOOLEAN Pfnksgenerateeventcallback 
(
	PVOID Context
	PKSEVENT_ENTRY EventEntry
)
{...}

PFNKSGENERATEEVENTCALLBACK 


```

## -parameters

### -param Context: 
### -param EventEntry: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also