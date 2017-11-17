---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT
title: PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT
author: windows-driver-content
description: 
ms.assetid: 8d3bf376-efba-4064-bb39-9436e1738aaa
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

# PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT Pfnd3d111DdiGetvideodecoderconfigcount; 

// Definition

VOID Pfnd3d111DdiGetvideodecoderconfigcount 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDI_VIDEO_DECODER_DESC *
	UINT *
)
{...}

PFND3D11_1DDI_GETVIDEODECODERCONFIGCOUNT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also