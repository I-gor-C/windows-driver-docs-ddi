---
UID: NC.ntagp.PAGP_MAP_MEMORY
title: PAGP_MAP_MEMORY
author: windows-driver-content
description: 
ms.assetid: 86958c19-efd0-48b3-b825-c4f6579b15b3
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

# PAGP_MAP_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_MAP_MEMORY PagpMapMemory; 

// Definition

NTSTATUS PagpMapMemory 
(
	IN PVOID AgpContext
	IN PVOID MapHandle
	IN ULONG NumberOfPages
	IN ULONG OffsetInPages
	IN PMDL Mdl
	OUT PHYSICAL_ADDRESS *MemoryBase
)
{...}

PAGP_MAP_MEMORY 


```

## -parameters

### -param AgpContext: 
### -param MapHandle: 
### -param NumberOfPages: 
### -param OffsetInPages: 
### -param Mdl: 
### -param *MemoryBase: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also