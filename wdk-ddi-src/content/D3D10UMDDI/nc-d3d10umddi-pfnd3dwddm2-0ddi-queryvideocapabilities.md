---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES
title: PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 1b8eea4b-7f15-4aba-a6f3-d3927afb6605
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

# PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES Pfnd3dwddm20DdiQueryvideocapabilities; 

// Definition

VOID Pfnd3dwddm20DdiQueryvideocapabilities 
(
	D3D10DDI_HDEVICE hDevice
	D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY QueryType
	UINT DataSize
	VOID *pData
)
{...}

PFND3DWDDM2_0DDI_QUERYVIDEOCAPABILITIES 


```

## -parameters

### -param hDevice: 
### -param QueryType: 
### -param DataSize: 
### -param *pData: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also