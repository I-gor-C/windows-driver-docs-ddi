---
UID: NC.ntagp.PAGP_BUS_COMMIT_MEMORY
title: PAGP_BUS_COMMIT_MEMORY
author: windows-driver-content
description: 
ms.assetid: 04c80873-39f9-47d7-8a99-4d4f35ce1f3f
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

# PAGP_BUS_COMMIT_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_BUS_COMMIT_MEMORY PagpBusCommitMemory; 

// Definition

NTSTATUS PagpBusCommitMemory 
(
	IN PVOID AgpContext
	IN PVOID MapHandle
	IN ULONG NumberOfPages
	IN ULONG OffsetInPages
	IN OUT PMDL Mdl OPTIONAL
	OUT PHYSICAL_ADDRESS *MemoryBase
)
{...}

PAGP_BUS_COMMIT_MEMORY 


```

## -parameters

### -param AgpContext: 
### -param MapHandle: 
### -param NumberOfPages: 
### -param OffsetInPages: 
### -param OPTIONAL: 
### -param *MemoryBase: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also