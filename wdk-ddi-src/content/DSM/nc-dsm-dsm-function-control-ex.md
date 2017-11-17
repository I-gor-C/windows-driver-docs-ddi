---
UID: NC.dsm.DSM_FUNCTION_CONTROL_EX
title: DSM_FUNCTION_CONTROL_EX
author: windows-driver-content
description: 
ms.assetid: 9f18224a-69aa-4c9a-bc41-acdbf7c4b34e
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

# DSM_FUNCTION_CONTROL_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_FUNCTION_CONTROL_EX DsmFunctionControlEx; 

// Definition

NTSTATUS DsmFunctionControlEx 
(
	IN PVOID DsmContext
	IN PDSM_IDS DsmIds
	IN PIRP Irp
	IN ULONG GuidIndex
	IN WMIENABLEDISABLECONTROL Function
	IN BOOLEAN Enable
	 ...
)
{...}

DSM_FUNCTION_CONTROL_EX 


```

## -parameters

### -param DsmContext: 
### -param DsmIds: 
### -param Irp: 
### -param GuidIndex: 
### -param Function: 
### -param Enable: 
### -param ...: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also