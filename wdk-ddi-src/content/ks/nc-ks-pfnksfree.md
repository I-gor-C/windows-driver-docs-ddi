---
UID: NC.ks.PFNKSFREE
title: PFNKSFREE
author: windows-driver-content
description: 
ms.assetid: e7a6621c-30f5-4661-9adc-4ee7c3f63388
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

# PFNKSFREE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFREE Pfnksfree; 

// Definition

void Pfnksfree 
(
	PVOID Data
)
{...}

PFNKSFREE 


```

## -parameters

### -param Data: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also