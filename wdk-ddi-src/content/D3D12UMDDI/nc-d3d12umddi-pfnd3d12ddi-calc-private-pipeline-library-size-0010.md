---
UID: NC.d3d12umddi.PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010
title: PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010
author: windows-driver-content
description: 
ms.assetid: 28b7fb1a-7cf3-4d10-9615-93c0db01977d
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

# PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010 Pfnd3d12ddiCalcPrivatePipelineLibrarySize0010; 

// Definition

SIZE_T Pfnd3d12ddiCalcPrivatePipelineLibrarySize0010 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_CREATE_PIPELINE_LIBRARY_0010 *
)
{...}

PFND3D12DDI_CALC_PRIVATE_PIPELINE_LIBRARY_SIZE_0010 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also