---
UID: NC.wdm.PFREE_COMMON_BUFFER
title: PFREE_COMMON_BUFFER
author: windows-driver-content
description: 
ms.assetid: b0f180f1-2fd1-40ea-b50e-f85eed8c1b1c
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

# PFREE_COMMON_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFREE_COMMON_BUFFER PfreeCommonBuffer; 

// Definition

VOID PfreeCommonBuffer 
(
	PDMA_ADAPTER DmaAdapter
	ULONG Length
	PHYSICAL_ADDRESS LogicalAddress
	PVOID VirtualAddress
	BOOLEAN CacheEnabled
)
{...}

PFREE_COMMON_BUFFER 


```

## -parameters

### -param DmaAdapter: 
### -param Length: 
### -param LogicalAddress: 
### -param VirtualAddress: 
### -param CacheEnabled: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also