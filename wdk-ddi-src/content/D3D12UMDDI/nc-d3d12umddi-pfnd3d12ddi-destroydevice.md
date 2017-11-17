---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYDEVICE
title: PFND3D12DDI_DESTROYDEVICE
author: windows-driver-content
description: 
ms.assetid: 04484fd5-43f7-4482-b685-8f1b58e33917
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

# PFND3D12DDI_DESTROYDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYDEVICE Pfnd3d12ddiDestroydevice; 

// Definition

VOID Pfnd3d12ddiDestroydevice 
(
	 D3D12DDI_HDEVICE
)
{...}

PFND3D12DDI_DESTROYDEVICE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also