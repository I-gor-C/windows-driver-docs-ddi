---
UID: NC.wdm.PALLOCATE_COMMON_BUFFER_EX
title: PALLOCATE_COMMON_BUFFER_EX
author: windows-driver-content
description: 
ms.assetid: da6321b7-605b-4bbc-900a-610282d20820
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

# PALLOCATE_COMMON_BUFFER_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PALLOCATE_COMMON_BUFFER_EX PallocateCommonBufferEx; 

// Definition

PVOID PallocateCommonBufferEx 
(
	PDMA_ADAPTER DmaAdapter
	PPHYSICAL_ADDRESS MaximumAddress
	ULONG Length
	PPHYSICAL_ADDRESS LogicalAddress
	BOOLEAN CacheEnabled
	NODE_REQUIREMENT PreferredNode
)
{...}

PALLOCATE_COMMON_BUFFER_EX 


```

## -parameters

### -param DmaAdapter: 
### -param MaximumAddress: 
### -param Length: 
### -param LogicalAddress: 
### -param CacheEnabled: 
### -param PreferredNode: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also