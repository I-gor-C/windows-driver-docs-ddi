---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW
title: PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW
author: windows-driver-content
description: 
ms.assetid: 355fba9a-e7e4-48a1-9e16-23b4b304c37e
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

# PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW Pfnd3dwddm20DdiCreaterendertargetview; 

// Definition

VOID Pfnd3dwddm20DdiCreaterendertargetview 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDIARG_CREATERENDERTARGETVIEW *
	 D3D10DDI_HRENDERTARGETVIEW
	 D3D10DDI_HRTRENDERTARGETVIEW
)
{...}

PFND3DWDDM2_0DDI_CREATERENDERTARGETVIEW 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param D3D10DDI_HRENDERTARGETVIEW: 
### -param D3D10DDI_HRTRENDERTARGETVIEW: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also