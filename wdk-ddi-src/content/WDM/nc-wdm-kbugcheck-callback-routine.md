---
UID: NC.wdm.KBUGCHECK_CALLBACK_ROUTINE
title: KBUGCHECK_CALLBACK_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 807dbb57-2cd1-4b1a-b44d-bacd83ea265d
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

# KBUGCHECK_CALLBACK_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KBUGCHECK_CALLBACK_ROUTINE KbugcheckCallbackRoutine; 

// Definition

_IRQL_requires_same_ VOID KbugcheckCallbackRoutine 
(
	IN PVOID Buffer
	IN ULONG Length
)
{...}

KBUGCHECK_CALLBACK_ROUTINE PKBUGCHECK_CALLBACK_ROUTINE


```

## -parameters

### -param Buffer: 
### -param Length: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also