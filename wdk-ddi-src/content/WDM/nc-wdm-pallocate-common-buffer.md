---
UID: NC.wdm.PALLOCATE_COMMON_BUFFER
title: PALLOCATE_COMMON_BUFFER
author: windows-driver-content
description: 
ms.assetid: 11c29745-975e-4342-9b06-1bbaa741f2e8
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

# PALLOCATE_COMMON_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PALLOCATE_COMMON_BUFFER PallocateCommonBuffer; 

// Definition

PVOID PallocateCommonBuffer 
(
	PDMA_ADAPTER DmaAdapter
	ULONG Length
	PPHYSICAL_ADDRESS LogicalAddress
	BOOLEAN CacheEnabled
)
{...}

PALLOCATE_COMMON_BUFFER 


```

## -parameters

### -param DmaAdapter: 
### -param Length: 
### -param LogicalAddress: 
### -param CacheEnabled: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also