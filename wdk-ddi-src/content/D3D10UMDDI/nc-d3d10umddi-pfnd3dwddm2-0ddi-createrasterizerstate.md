---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE
title: PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE
author: windows-driver-content
description: 
ms.assetid: 4ab6fb27-8578-43a4-b094-0488019ad1d5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE Pfnd3dwddm20DdiCreaterasterizerstate; 

// Definition

VOID Pfnd3dwddm20DdiCreaterasterizerstate 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDI_RASTERIZER_DESC *
	 D3D10DDI_HRASTERIZERSTATE
	 D3D10DDI_HRTRASTERIZERSTATE
)
{...}

PFND3DWDDM2_0DDI_CREATERASTERIZERSTATE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param D3D10DDI_HRASTERIZERSTATE: 
### -param D3D10DDI_HRTRASTERIZERSTATE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also