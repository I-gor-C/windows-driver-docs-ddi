---
UID: NC.wdm.KBUGCHECK_REASON_CALLBACK_ROUTINE
title: KBUGCHECK_REASON_CALLBACK_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 28473fee-1c4e-4a79-9e0f-29f92ba8a8ae
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

# KBUGCHECK_REASON_CALLBACK_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

KBUGCHECK_REASON_CALLBACK_ROUTINE KbugcheckReasonCallbackRoutine; 

// Definition

_IRQL_requires_same_ VOID KbugcheckReasonCallbackRoutine 
(
	KBUGCHECK_CALLBACK_REASON Reason
	_KBUGCHECK_REASON_CALLBACK_RECORD * Record
	PVOID ReasonSpecificData
	ULONG ReasonSpecificDataLength
)
{...}

KBUGCHECK_REASON_CALLBACK_ROUTINE PKBUGCHECK_REASON_CALLBACK_ROUTINE


```

## -parameters

### -param Reason: 
### -param Record: 
### -param ReasonSpecificData: 
### -param ReasonSpecificDataLength: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also