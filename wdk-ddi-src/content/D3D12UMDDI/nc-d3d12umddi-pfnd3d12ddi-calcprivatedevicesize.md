---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATEDEVICESIZE
title: PFND3D12DDI_CALCPRIVATEDEVICESIZE
author: windows-driver-content
description: 
ms.assetid: 0e43556b-8d3d-4d9f-b7f3-7dfd37cb6cc2
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

# PFND3D12DDI_CALCPRIVATEDEVICESIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATEDEVICESIZE Pfnd3d12ddiCalcprivatedevicesize; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatedevicesize 
(
	 D3D12DDI_HADAPTER
	CONST D3D12DDIARG_CALCPRIVATEDEVICESIZE *
)
{...}

PFND3D12DDI_CALCPRIVATEDEVICESIZE 


```

## -parameters

### -param D3D12DDI_HADAPTER: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also