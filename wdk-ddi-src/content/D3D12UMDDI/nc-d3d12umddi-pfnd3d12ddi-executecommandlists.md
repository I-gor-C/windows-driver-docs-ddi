---
UID: NC.d3d12umddi.PFND3D12DDI_EXECUTECOMMANDLISTS
title: PFND3D12DDI_EXECUTECOMMANDLISTS
author: windows-driver-content
description: 
ms.assetid: 7acd75ea-58f3-409e-86de-ffa92c594749
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_EXECUTECOMMANDLISTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_EXECUTECOMMANDLISTS Pfnd3d12ddiExecutecommandlists; 

// Definition

VOID Pfnd3d12ddiExecutecommandlists 
(
	 D3D12DDI_HCOMMANDQUEUE
	UINT Count
	CONST D3D12DDI_HCOMMANDLIST *pCommandLists
)
{...}

PFND3D12DDI_EXECUTECOMMANDLISTS 


```

## -parameters

### -param D3D12DDI_HCOMMANDQUEUE: 
### -param Count: 
### -param *pCommandLists: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also