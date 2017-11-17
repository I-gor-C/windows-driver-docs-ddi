---
UID: NC.dsm.DSM_SET_DATABLOCK_EX
title: DSM_SET_DATABLOCK_EX
author: windows-driver-content
description: 
ms.assetid: c8825185-0479-4648-819b-9330cd345724
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

# DSM_SET_DATABLOCK_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_SET_DATABLOCK_EX DsmSetDatablockEx; 

// Definition

NTSTATUS DsmSetDatablockEx 
(
	IN PVOID DsmContext
	IN PDSM_IDS DsmIds
	IN PIRP Irp
	IN ULONG GuidIndex
	IN ULONG InstanceIndex
	IN ULONG BufferSize
	IN PUCHAR Buffer
	 ...
)
{...}

DSM_SET_DATABLOCK_EX 


```

## -parameters

### -param DsmContext: 
### -param DsmIds: 
### -param Irp: 
### -param GuidIndex: 
### -param InstanceIndex: 
### -param BufferSize: 
### -param Buffer: 
### -param ...: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also