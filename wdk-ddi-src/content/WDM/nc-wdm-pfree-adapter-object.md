---
UID: NC.wdm.PFREE_ADAPTER_OBJECT
title: PFREE_ADAPTER_OBJECT
author: windows-driver-content
description: 
ms.assetid: babaeddc-ef10-437e-ac7e-08a62d902052
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

# PFREE_ADAPTER_OBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFREE_ADAPTER_OBJECT PfreeAdapterObject; 

// Definition

VOID PfreeAdapterObject 
(
	PDMA_ADAPTER DmaAdapter
	IO_ALLOCATION_ACTION AllocationAction
)
{...}

PFREE_ADAPTER_OBJECT 


```

## -parameters

### -param DmaAdapter: 
### -param AllocationAction: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also