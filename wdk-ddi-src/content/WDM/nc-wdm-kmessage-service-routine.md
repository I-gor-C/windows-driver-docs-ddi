---
UID: NC.wdm.KMESSAGE_SERVICE_ROUTINE
title: KMESSAGE_SERVICE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: d759b107-8a66-495d-ba66-f3e57490c0d2
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

# KMESSAGE_SERVICE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KMESSAGE_SERVICE_ROUTINE KmessageServiceRoutine; 

// Definition

_IRQL_requires_same_ BOOLEAN KmessageServiceRoutine 
(
	_KINTERRUPT * Interrupt
	PVOID ServiceContext
	ULONG MessageID
)
{...}

KMESSAGE_SERVICE_ROUTINE PKMESSAGE_SERVICE_ROUTINE


```

## -parameters

### -param Interrupt: 
### -param ServiceContext: 
### -param MessageID: 



## -returns

Returns _IRQL_requires_same_ BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also