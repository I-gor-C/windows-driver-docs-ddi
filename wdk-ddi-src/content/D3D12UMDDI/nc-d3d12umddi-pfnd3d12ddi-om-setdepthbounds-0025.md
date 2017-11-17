---
UID: NC.d3d12umddi.PFND3D12DDI_OM_SETDEPTHBOUNDS_0025
title: PFND3D12DDI_OM_SETDEPTHBOUNDS_0025
author: windows-driver-content
description: 
ms.assetid: 5beac862-3862-493d-8994-68880e42e915
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

# PFND3D12DDI_OM_SETDEPTHBOUNDS_0025 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OM_SETDEPTHBOUNDS_0025 Pfnd3d12ddiOmSetdepthbounds0025; 

// Definition

VOID Pfnd3d12ddiOmSetdepthbounds0025 
(
	 D3D12DDI_HCOMMANDLIST
	FLOAT Min
	FLOAT Max
)
{...}

PFND3D12DDI_OM_SETDEPTHBOUNDS_0025 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param Min: 
### -param Max: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also