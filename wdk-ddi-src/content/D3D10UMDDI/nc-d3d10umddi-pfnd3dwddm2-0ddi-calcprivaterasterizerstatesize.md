---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE
title: PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE
author: windows-driver-content
description: 
ms.assetid: 8f40419a-6ad4-4b27-af06-a4f94494f8ca
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

# PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE Pfnd3dwddm20DdiCalcprivaterasterizerstatesize; 

// Definition

SIZE_T Pfnd3dwddm20DdiCalcprivaterasterizerstatesize 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDI_RASTERIZER_DESC *
)
{...}

PFND3DWDDM2_0DDI_CALCPRIVATERASTERIZERSTATESIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also