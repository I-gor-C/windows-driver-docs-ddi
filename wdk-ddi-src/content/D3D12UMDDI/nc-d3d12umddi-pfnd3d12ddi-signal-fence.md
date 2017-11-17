---
UID: NC.d3d12umddi.PFND3D12DDI_SIGNAL_FENCE
title: PFND3D12DDI_SIGNAL_FENCE
author: windows-driver-content
description: 
ms.assetid: 2fae9afa-8d31-4e67-9744-ee49d274e804
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

# PFND3D12DDI_SIGNAL_FENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SIGNAL_FENCE Pfnd3d12ddiSignalFence; 

// Definition

void Pfnd3d12ddiSignalFence 
(
	 D3D12DDI_HCOMMANDQUEUE
	D3D12DDIARG_FENCE_OPERATION *
)
{...}

PFND3D12DDI_SIGNAL_FENCE 


```

## -parameters

### -param D3D12DDI_HCOMMANDQUEUE: 
### -param *: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also