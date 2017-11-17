---
UID: NC.d3d12umddi.PFND3D12DDI_RESETCOMMANDALLOCATOR
title: PFND3D12DDI_RESETCOMMANDALLOCATOR
author: windows-driver-content
description: 
ms.assetid: 8e8b8c82-e04e-4768-a22f-ee9ae7d1f5d3
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

# PFND3D12DDI_RESETCOMMANDALLOCATOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_RESETCOMMANDALLOCATOR Pfnd3d12ddiResetcommandallocator; 

// Definition

VOID Pfnd3d12ddiResetcommandallocator 
(
	 D3D12DDI_HCOMMANDALLOCATOR
)
{...}

PFND3D12DDI_RESETCOMMANDALLOCATOR 


```

## -parameters

### -param D3D12DDI_HCOMMANDALLOCATOR: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also