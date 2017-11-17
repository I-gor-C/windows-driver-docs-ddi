---
UID: NC.d3d12umddi.PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE
title: PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE
author: windows-driver-content
description: 
ms.assetid: c119aea9-f2d2-4577-8f71-74d5505dea60
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

# PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE Pfnd3d12ddiCalcprivatedeserializedobjectsize; 

// Definition

SIZE_T Pfnd3d12ddiCalcprivatedeserializedobjectsize 
(
	D3D12DDI_HDEVICE HDEVICE
	D3D12DDI_HANDLETYPE HandleType
	SIZE_T BlobSize
	CONST UINT *pBlob
)
{...}

PFND3D12DDI_CALCPRIVATEDESERIALIZEDOBJECTSIZE 


```

## -parameters

### -param HDEVICE: 
### -param HandleType: 
### -param BlobSize: 
### -param *pBlob: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also