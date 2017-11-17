---
UID: NC.wdm.KSYNCHRONIZE_ROUTINE
title: KSYNCHRONIZE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 46923be6-e2d8-4a30-ab5f-e20a4a89f6ee
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# KSYNCHRONIZE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KSYNCHRONIZE_ROUTINE KsynchronizeRoutine; 

// Definition

_IRQL_requires_same_ BOOLEAN KsynchronizeRoutine 
(
	PVOID SynchronizeContext
)
{...}

KSYNCHRONIZE_ROUTINE PKSYNCHRONIZE_ROUTINE


```

## -parameters

### -param SynchronizeContext: 



## -returns

Returns _IRQL_requires_same_ BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also