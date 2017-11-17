---
UID: NC.nfccx.EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE
title: EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6479838b-d814-4984-8beb-b074deca4482
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: nfccx.h
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

# EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE EvtNfcCxSequenceCompletionRoutine; 

// Definition

_IRQL_requires_same_ VOID EvtNfcCxSequenceCompletionRoutine 
(
	WDFDEVICE Device
	NTSTATUS Status
	ULONG Flags
	WDFCONTEXT Context
)
{...}

EVT_NFC_CX_SEQUENCE_COMPLETION_ROUTINE PFN_NFC_CX_SEQUENCE_COMPLETION_ROUTINE


```

## -parameters

### -param Device: 
### -param Status: 
### -param Flags: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also