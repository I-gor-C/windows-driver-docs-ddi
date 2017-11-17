---
UID: NC.d3d12umddi.PFND3D12DDI_SETERROR_CB
title: PFND3D12DDI_SETERROR_CB
author: windows-driver-content
description: 
ms.assetid: 9592bca7-e774-4c01-9898-81ef3b77479a
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

# PFND3D12DDI_SETERROR_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_SETERROR_CB Pfnd3d12ddiSeterrorCb; 

// Definition

VOID Pfnd3d12ddiSeterrorCb 
(
	 D3D10DDI_HRTDEVICE
	 HRESULT
)
{...}

PFND3D12DDI_SETERROR_CB 


```

## -parameters

### -param D3D10DDI_HRTDEVICE: 
### -param HRESULT: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also