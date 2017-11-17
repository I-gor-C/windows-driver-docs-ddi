---
UID: NC.d3d12umddi.PFND3D12DDI_CREATE_PASS
title: PFND3D12DDI_CREATE_PASS
author: windows-driver-content
description: 
ms.assetid: 14aa8cdf-46db-4d78-9161-11c1de2ab4d7
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

# PFND3D12DDI_CREATE_PASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CREATE_PASS Pfnd3d12ddiCreatePass; 

// Definition

HRESULT Pfnd3d12ddiCreatePass 
(
	 D3D12DDI_HDEVICE
	CONST D3D12DDIARG_CREATE_PASS *
	 D3D12DDI_HPASS
)
{...}

PFND3D12DDI_CREATE_PASS 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param *: 
### -param D3D12DDI_HPASS: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also