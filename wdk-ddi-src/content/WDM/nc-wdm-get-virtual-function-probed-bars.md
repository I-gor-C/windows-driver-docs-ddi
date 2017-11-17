---
UID: NC.wdm.GET_VIRTUAL_FUNCTION_PROBED_BARS
title: GET_VIRTUAL_FUNCTION_PROBED_BARS
author: windows-driver-content
description: 
ms.assetid: 412c4cf5-7f15-4b64-b9b5-aed91ad59259
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

# GET_VIRTUAL_FUNCTION_PROBED_BARS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_VIRTUAL_FUNCTION_PROBED_BARS GetVirtualFunctionProbedBars; 

// Definition

NTSTATUS GetVirtualFunctionProbedBars 
(
	PVOID Context
	PULONG BaseRegisterValues
)
{...}

GET_VIRTUAL_FUNCTION_PROBED_BARS PGET_VIRTUAL_FUNCTION_PROBED_BARS


```

## -parameters

### -param Context: 
### -param BaseRegisterValues: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also