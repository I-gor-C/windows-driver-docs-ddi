---
UID: NC.d3d12umddi.PFND3D12DDI_OPENADAPTER
title: PFND3D12DDI_OPENADAPTER
author: windows-driver-content
description: 
ms.assetid: 63489ce7-e6ce-497b-bb4e-7e0c0974bee2
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

# PFND3D12DDI_OPENADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OPENADAPTER Pfnd3d12ddiOpenadapter; 

// Definition

HRESULT Pfnd3d12ddiOpenadapter 
(
	D3D12DDIARG_OPENADAPTER *
)
{...}

PFND3D12DDI_OPENADAPTER 


```

## -parameters

### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also