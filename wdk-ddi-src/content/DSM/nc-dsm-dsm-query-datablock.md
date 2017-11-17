---
UID: NC.dsm.DSM_QUERY_DATABLOCK
title: DSM_QUERY_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: 8fae251b-7afa-42fa-9055-90dc31a844fc
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

# DSM_QUERY_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_QUERY_DATABLOCK DsmQueryDatablock; 

// Definition

NTSTATUS DsmQueryDatablock 
(
	IN PVOID DsmContext
	IN PIRP Irp
	IN ULONG GuidIndex
	IN ULONG InstanceIndex
	IN ULONG InstanceCount
	IN OUT PULONG InstanceLengthArray
	IN ULONG BufferAvail
	OUT PUCHAR Buffer
	OUT PULONG DsmDataLength
)
{...}

DSM_QUERY_DATABLOCK 


```

## -parameters

### -param DsmContext: 
### -param Irp: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param InstanceCount: 
### -param InstanceLengthArray: 
### -param BufferAvail: 
### -param Buffer: 
### -param DsmDataLength: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also