---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYDEPTHSTENCILSTATE
title: PFND3D12DDI_DESTROYDEPTHSTENCILSTATE
author: windows-driver-content
description: 
ms.assetid: 6a4b4cd8-6742-4f7d-8118-21e9a591b073
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

# PFND3D12DDI_DESTROYDEPTHSTENCILSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYDEPTHSTENCILSTATE Pfnd3d12ddiDestroydepthstencilstate; 

// Definition

VOID Pfnd3d12ddiDestroydepthstencilstate 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HDEPTHSTENCILSTATE
)
{...}

PFND3D12DDI_DESTROYDEPTHSTENCILSTATE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HDEPTHSTENCILSTATE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also