---
UID: NC.ntagp.PAGP_BUS_RESERVE_MEMORY
title: PAGP_BUS_RESERVE_MEMORY
author: windows-driver-content
description: 
ms.assetid: d47ac13f-4b2a-4a2a-be4d-b8491392cd8a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntagp.h
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

# PAGP_BUS_RESERVE_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_BUS_RESERVE_MEMORY PagpBusReserveMemory; 

// Definition

NTSTATUS PagpBusReserveMemory 
(
	IN PVOID AgpContext
	IN ULONG NumberOfPages
	IN MEMORY_CACHING_TYPE MemoryType
	OUT PVOID *MapHandle
	OUT OPTIONAL PHYSICAL_ADDRESS *PhysicalAddress
)
{...}

PAGP_BUS_RESERVE_MEMORY 


```

## -parameters

### -param AgpContext: 
### -param NumberOfPages: 
### -param MemoryType: 
### -param *MapHandle: 
### -param *PhysicalAddress: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also