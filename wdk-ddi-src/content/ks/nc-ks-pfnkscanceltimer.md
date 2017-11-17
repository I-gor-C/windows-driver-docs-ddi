---
UID: NC.ks.PFNKSCANCELTIMER
title: PFNKSCANCELTIMER
author: windows-driver-content
description: 
ms.assetid: 93bde12d-65ab-4ac3-8e32-ba3e8a839189
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

# PFNKSCANCELTIMER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSCANCELTIMER Pfnkscanceltimer; 

// Definition

BOOLEAN Pfnkscanceltimer 
(
	PVOID Context
	PKTIMER Timer
)
{...}

PFNKSCANCELTIMER 


```

## -parameters

### -param Context: 
### -param Timer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also