---
UID: NC.wdm.KSERVICE_ROUTINE
title: KSERVICE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: a5257de1-cfdb-4ce4-808e-fe7dc2c1a3fa
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

# KSERVICE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KSERVICE_ROUTINE KserviceRoutine; 

// Definition

_IRQL_requires_same_ BOOLEAN KserviceRoutine 
(
	_KINTERRUPT * Interrupt
	PVOID ServiceContext
)
{...}

KSERVICE_ROUTINE PKSERVICE_ROUTINE


```

## -parameters

### -param Interrupt: 
### -param ServiceContext: 



## -returns

Returns _IRQL_requires_same_ BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also