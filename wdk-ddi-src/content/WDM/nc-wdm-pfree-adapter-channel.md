---
UID: NC.wdm.PFREE_ADAPTER_CHANNEL
title: PFREE_ADAPTER_CHANNEL
author: windows-driver-content
description: 
ms.assetid: 591f377b-5d43-4ef7-bb15-308cf0c1fd10
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

# PFREE_ADAPTER_CHANNEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFREE_ADAPTER_CHANNEL PfreeAdapterChannel; 

// Definition

VOID PfreeAdapterChannel 
(
	PDMA_ADAPTER DmaAdapter
)
{...}

PFREE_ADAPTER_CHANNEL 


```

## -parameters

### -param DmaAdapter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also