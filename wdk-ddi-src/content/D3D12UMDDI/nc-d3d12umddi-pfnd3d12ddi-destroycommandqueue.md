---
UID: NC.d3d12umddi.PFND3D12DDI_DESTROYCOMMANDQUEUE
title: PFND3D12DDI_DESTROYCOMMANDQUEUE
author: windows-driver-content
description: 
ms.assetid: 0b02b870-8565-41f1-841f-53f9b4f2cb83
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

# PFND3D12DDI_DESTROYCOMMANDQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_DESTROYCOMMANDQUEUE Pfnd3d12ddiDestroycommandqueue; 

// Definition

VOID Pfnd3d12ddiDestroycommandqueue 
(
	 D3D12DDI_HDEVICE
	 D3D12DDI_HCOMMANDQUEUE
)
{...}

PFND3D12DDI_DESTROYCOMMANDQUEUE 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param D3D12DDI_HCOMMANDQUEUE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also