---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW
title: PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: 
ms.assetid: da7d9418-d3d4-4e3b-89c4-2d7ed262d251
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

# PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW Pfnd3dwddm20DdiCreateshaderresourceview; 

// Definition

VOID Pfnd3dwddm20DdiCreateshaderresourceview 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDIARG_CREATESHADERRESOURCEVIEW *
	 D3D10DDI_HSHADERRESOURCEVIEW
	 D3D10DDI_HRTSHADERRESOURCEVIEW
)
{...}

PFND3DWDDM2_0DDI_CREATESHADERRESOURCEVIEW 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param D3D10DDI_HSHADERRESOURCEVIEW: 
### -param D3D10DDI_HRTSHADERRESOURCEVIEW: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also