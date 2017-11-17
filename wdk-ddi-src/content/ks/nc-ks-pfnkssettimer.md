---
UID: NC.ks.PFNKSSETTIMER
title: PFNKSSETTIMER
author: windows-driver-content
description: 
ms.assetid: 136223c3-879c-40df-9ec9-4720cf219924
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

# PFNKSSETTIMER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSSETTIMER Pfnkssettimer; 

// Definition

BOOLEAN Pfnkssettimer 
(
	PVOID Context
	PKTIMER Timer
	LARGE_INTEGER DueTime
	PKDPC Dpc
)
{...}

PFNKSSETTIMER 


```

## -parameters

### -param Context: 
### -param Timer: 
### -param DueTime: 
### -param Dpc: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also