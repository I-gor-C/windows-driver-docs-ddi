---
UID: NC.rxstruc.PMRX_CALLDOWN_ROUTINE
title: PMRX_CALLDOWN_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 5f105359-2cab-47e4-9eb2-3ef4a8d68701
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxstruc.h
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

# PMRX_CALLDOWN_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_CALLDOWN_ROUTINE PmrxCalldownRoutine; 

// Definition

NTSTATUS PmrxCalldownRoutine 
(
	IN OUT PVOID CalldownParameter
)
{...}

PMRX_CALLDOWN_ROUTINE 


```

## -parameters

### -param CalldownParameter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also