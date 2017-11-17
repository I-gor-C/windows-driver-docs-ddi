---
UID: NC.wdm.PPUT_SCATTER_GATHER_LIST
title: PPUT_SCATTER_GATHER_LIST
author: windows-driver-content
description: 
ms.assetid: df025f3e-ee96-444a-8688-e477d8622276
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

# PPUT_SCATTER_GATHER_LIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPUT_SCATTER_GATHER_LIST PputScatterGatherList; 

// Definition

VOID PputScatterGatherList 
(
	PDMA_ADAPTER DmaAdapter
	PSCATTER_GATHER_LIST ScatterGather
	BOOLEAN WriteToDevice
)
{...}

PPUT_SCATTER_GATHER_LIST 


```

## -parameters

### -param DmaAdapter: 
### -param ScatterGather: 
### -param WriteToDevice: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also