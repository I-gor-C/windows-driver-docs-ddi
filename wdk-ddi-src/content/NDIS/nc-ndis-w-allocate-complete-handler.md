---
UID: NC.ndis.W_ALLOCATE_COMPLETE_HANDLER
title: W_ALLOCATE_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 771667b2-f742-4014-8910-6bb46c91fc1a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# W_ALLOCATE_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_ALLOCATE_COMPLETE_HANDLER WAllocateCompleteHandler; 

// Definition

VOID WAllocateCompleteHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	PVOID VirtualAddress
	PNDIS_PHYSICAL_ADDRESS PhysicalAddress
	ULONG Length
	PVOID Context
)
{...}

W_ALLOCATE_COMPLETE_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param VirtualAddress: 
### -param PhysicalAddress: 
### -param Length: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also