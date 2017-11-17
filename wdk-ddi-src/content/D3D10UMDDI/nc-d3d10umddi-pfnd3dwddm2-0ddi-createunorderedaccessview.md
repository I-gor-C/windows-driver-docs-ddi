---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW
title: PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW
author: windows-driver-content
description: 
ms.assetid: 23ecdfb6-7a83-461f-bc46-e91e4b38fb00
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

# PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW Pfnd3dwddm20DdiCreateunorderedaccessview; 

// Definition

VOID Pfnd3dwddm20DdiCreateunorderedaccessview 
(
	 D3D10DDI_HDEVICE
	CONST D3DWDDM2_0DDIARG_CREATEUNORDEREDACCESSVIEW *
	 D3D11DDI_HUNORDEREDACCESSVIEW
	 D3D11DDI_HRTUNORDEREDACCESSVIEW
)
{...}

PFND3DWDDM2_0DDI_CREATEUNORDEREDACCESSVIEW 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param D3D11DDI_HUNORDEREDACCESSVIEW: 
### -param D3D11DDI_HRTUNORDEREDACCESSVIEW: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also