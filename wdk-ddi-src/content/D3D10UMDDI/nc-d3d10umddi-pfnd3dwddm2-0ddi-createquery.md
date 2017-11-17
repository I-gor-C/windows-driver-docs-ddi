---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATEQUERY
title: PFND3DWDDM2_0DDI_CREATEQUERY
author: windows-driver-content
description: 
ms.assetid: 8dc84f47-6d08-492b-aff6-e432b747fd8b
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

# PFND3DWDDM2_0DDI_CREATEQUERY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATEQUERY Pfnd3dwddm20DdiCreatequery; 

// Definition

VOID Pfnd3dwddm20DdiCreatequery 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDIARG_CREATEQUERY *
	 D3D10DDI_HQUERY
	 D3D10DDI_HRTQUERY
)
{...}

PFND3DWDDM2_0DDI_CREATEQUERY 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param D3D10DDI_HQUERY: 
### -param D3D10DDI_HRTQUERY: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also