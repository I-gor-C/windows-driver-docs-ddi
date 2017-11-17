---
UID: NC.dsm.DSM_SET_DATABLOCK
title: DSM_SET_DATABLOCK
author: windows-driver-content
description: 
ms.assetid: ff8851a2-2392-4112-bddc-3f62d219d0c2
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

# DSM_SET_DATABLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_SET_DATABLOCK DsmSetDatablock; 

// Definition

NTSTATUS DsmSetDatablock 
(
	IN PVOID DsmContext
	IN PIRP Irp
	IN ULONG GuidIndex
	IN ULONG InstanceIndex
	IN ULONG BufferSize
	IN PUCHAR Buffer
)
{...}

DSM_SET_DATABLOCK 


```

## -parameters

### -param DsmContext: 
### -param Irp: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param BufferSize: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also