---
UID: NC.dsm.DSM_FUNCTION_CONTROL
title: DSM_FUNCTION_CONTROL
author: windows-driver-content
description: 
ms.assetid: 503a3231-a78c-4602-81ad-a8931892a9f4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_FUNCTION_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_FUNCTION_CONTROL DsmFunctionControl; 

// Definition

NTSTATUS DsmFunctionControl 
(
	IN PVOID DsmContext
	IN PIRP Irp
	IN ULONG GuidIndex
	IN WMIENABLEDISABLECONTROL Function
	IN BOOLEAN Enable
)
{...}

DSM_FUNCTION_CONTROL 


```

## -parameters

### -param DsmContext: 
### -param Irp: 
### -param GuidIndex: 
### -param Function: 
### -param Enable: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also