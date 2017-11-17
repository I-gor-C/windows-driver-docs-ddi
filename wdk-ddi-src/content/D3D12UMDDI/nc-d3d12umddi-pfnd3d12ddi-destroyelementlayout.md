---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYELEMENTLAYOUT
title: PFND3D12DDI_DESTROYELEMENTLAYOUT
author: windows-driver-content
description: 
ms.assetid: 8162881d-6616-4c75-806c-a60122af75e7
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

# PFND3D12DDI_DESTROYELEMENTLAYOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYELEMENTLAYOUT Pfnd3d12ddiDestroyelementlayout; 

// Definition

VOID Pfnd3d12ddiDestroyelementlayout 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HELEMENTLAYOUT
)
{...}

PFND3D12DDI_DESTROYELEMENTLAYOUT 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HELEMENTLAYOUT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also