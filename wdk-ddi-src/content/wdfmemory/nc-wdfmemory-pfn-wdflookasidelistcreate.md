---
UID: NC.wdfmemory.PFN_WDFLOOKASIDELISTCREATE
title: *PFN_WDFLOOKASIDELISTCREATE
author: windows-driver-content
description: 
ms.assetid: 49a94d41-680d-4822-b9b8-868bd1a7d419
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfmemory.h
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

# *PFN_WDFLOOKASIDELISTCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFLOOKASIDELISTCREATE *PfnWdflookasidelistcreate; 

// Definition

NTSTATUS *PfnWdflookasidelistcreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES LookasideAttributes
	size_t BufferSize
	_Strict_type_match_ POOL_TYPE PoolType
	PWDF_OBJECT_ATTRIBUTES MemoryAttributes
	ULONG PoolTag
	WDFLOOKASIDE *Lookaside
)
{...}

*PFN_WDFLOOKASIDELISTCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param LookasideAttributes: 
### -param BufferSize: 
### -param PoolType: 
### -param MemoryAttributes: 
### -param PoolTag: 
### -param *Lookaside: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also