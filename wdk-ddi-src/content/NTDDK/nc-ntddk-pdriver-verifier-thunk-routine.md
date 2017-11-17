---
UID: NC.ntddk.PDRIVER_VERIFIER_THUNK_ROUTINE
title: PDRIVER_VERIFIER_THUNK_ROUTINE
author: windows-driver-content
description: 
ms.assetid: df513201-c042-494d-8b9e-d7ec1e99c54f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PDRIVER_VERIFIER_THUNK_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDRIVER_VERIFIER_THUNK_ROUTINE PdriverVerifierThunkRoutine; 

// Definition

ULONG_PTR PdriverVerifierThunkRoutine 
(
	PVOID Context
)
{...}

PDRIVER_VERIFIER_THUNK_ROUTINE 


```

## -parameters

### -param Context: 



## -returns

Returns ULONG_PTR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also