---
UID: NC.d3d12umddi.PFND3D12DDI_GETCAPS
title: PFND3D12DDI_GETCAPS
author: windows-driver-content
description: 
ms.assetid: 2ae35dbe-de5b-4929-ab23-f265f956fca9
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

# PFND3D12DDI_GETCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GETCAPS Pfnd3d12ddiGetcaps; 

// Definition

HRESULT Pfnd3d12ddiGetcaps 
(
	 D3D12DDI_HADAPTER
	CONST D3D12DDIARG_GETCAPS *
)
{...}

PFND3D12DDI_GETCAPS 


```

## -parameters

### -param D3D12DDI_HADAPTER: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also