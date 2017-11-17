---
UID: NC.ntagp.PAGP_UNMAP_MEMORY
title: PAGP_UNMAP_MEMORY
author: windows-driver-content
description: 
ms.assetid: 9ebc7697-020b-4357-a1f6-34b5bae0895c
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

# PAGP_UNMAP_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_UNMAP_MEMORY PagpUnmapMemory; 

// Definition

NTSTATUS PagpUnmapMemory 
(
	IN PVOID AgpContext
	IN PVOID MapHandle
	IN ULONG NumberOfPages
	IN ULONG OffsetInPages
	IN PMDL Mdl
)
{...}

PAGP_UNMAP_MEMORY 


```

## -parameters

### -param AgpContext: 
### -param MapHandle: 
### -param NumberOfPages: 
### -param OffsetInPages: 
### -param Mdl: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also