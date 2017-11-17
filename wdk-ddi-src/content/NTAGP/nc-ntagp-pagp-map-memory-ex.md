---
UID: NC.ntagp.PAGP_MAP_MEMORY_EX
title: PAGP_MAP_MEMORY_EX
author: windows-driver-content
description: 
ms.assetid: ed1a69a6-0552-46fd-80c2-9f624f325e1d
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

# PAGP_MAP_MEMORY_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_MAP_MEMORY_EX PagpMapMemoryEx; 

// Definition

NTSTATUS PagpMapMemoryEx 
(
	IN PVOID AgpContext
	IN PVOID MapHandle
	IN ULONG NumberOfPages
	IN ULONG OffsetInPages
	IN PMDL Mdl
	IN OPTIONAL MEMORY_CACHING_TYPE *CacheTypeOverride
	OUT PHYSICAL_ADDRESS *MemoryBase
)
{...}

PAGP_MAP_MEMORY_EX 


```

## -parameters

### -param AgpContext: 
### -param MapHandle: 
### -param NumberOfPages: 
### -param OffsetInPages: 
### -param Mdl: 
### -param *CacheTypeOverride: 
### -param *MemoryBase: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also