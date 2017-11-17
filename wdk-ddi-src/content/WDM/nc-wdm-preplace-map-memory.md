---
UID: NC.wdm.PREPLACE_MAP_MEMORY
title: PREPLACE_MAP_MEMORY
author: windows-driver-content
description: 
ms.assetid: 0afa255b-ad9e-4955-92ee-c2c8a7da9dcc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PREPLACE_MAP_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_MAP_MEMORY PreplaceMapMemory; 

// Definition

NTSTATUS PreplaceMapMemory 
(
	PHYSICAL_ADDRESS TargetPhysicalAddress
	PHYSICAL_ADDRESS SparePhysicalAddress
	PLARGE_INTEGER NumberOfBytes
	PVOID *TargetAddress
	PVOID *SpareAddress
)
{...}

PREPLACE_MAP_MEMORY 


```

## -parameters

### -param TargetPhysicalAddress: 
### -param SparePhysicalAddress: 
### -param NumberOfBytes: 
### -param *TargetAddress: 
### -param *SpareAddress: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also