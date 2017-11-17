---
UID: NC.wdm.PALLOCATE_DOMAIN_COMMON_BUFFER
title: PALLOCATE_DOMAIN_COMMON_BUFFER
author: windows-driver-content
description: 
ms.assetid: 2493b067-33d1-43ee-ac56-0f2e5d3b01b4
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

# PALLOCATE_DOMAIN_COMMON_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PALLOCATE_DOMAIN_COMMON_BUFFER PallocateDomainCommonBuffer; 

// Definition

NTSTATUS PallocateDomainCommonBuffer 
(
	PDMA_ADAPTER DmaAdapter
	HANDLE DomainHandle
	PPHYSICAL_ADDRESS MaximumAddress
	ULONG Length
	ULONG Flags
	MEMORY_CACHING_TYPE *CacheType
	NODE_REQUIREMENT PreferredNode
	PPHYSICAL_ADDRESS LogicalAddress
	PVOID *VirtualAddress
)
{...}

PALLOCATE_DOMAIN_COMMON_BUFFER 


```

## -parameters

### -param DmaAdapter: 
### -param DomainHandle: 
### -param MaximumAddress: 
### -param Length: 
### -param Flags: 
### -param *CacheType: 
### -param PreferredNode: 
### -param LogicalAddress: 
### -param *VirtualAddress: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also