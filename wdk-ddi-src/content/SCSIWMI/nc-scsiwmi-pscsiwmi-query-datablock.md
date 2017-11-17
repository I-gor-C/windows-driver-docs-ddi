---
UID: NC.scsiwmi.PSCSIWMI_QUERY_DATABLOCK
title: PSCSIWMI_QUERY_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: b38cab2f-66e5-4518-b60b-2a9a7ee19000
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scsiwmi.h
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

# PSCSIWMI_QUERY_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_QUERY_DATABLOCK PscsiwmiQueryDatablock; 

// Definition

BOOLEAN PscsiwmiQueryDatablock 
(
	PVOID Context
	PSCSIWMI_REQUEST_CONTEXT DispatchContext
	ULONG GuidIndex
	ULONG InstanceIndex
	ULONG InstanceCount
	PULONG InstanceLengthArray
	ULONG BufferAvail
	PUCHAR Buffer
)
{...}

PSCSIWMI_QUERY_DATABLOCK 


```

## -parameters

### -param Context: 
### -param DispatchContext: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param InstanceCount: 
### -param InstanceLengthArray: 
### -param BufferAvail: 
### -param Buffer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also