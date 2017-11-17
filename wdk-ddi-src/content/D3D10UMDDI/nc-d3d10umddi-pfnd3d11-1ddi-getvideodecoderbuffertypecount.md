---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT
title: PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT
author: windows-driver-content
description: 
ms.assetid: 99cc6662-9bcb-477e-9e35-8f7baf7c5507
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

# PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT Pfnd3d111DdiGetvideodecoderbuffertypecount; 

// Definition

VOID Pfnd3d111DdiGetvideodecoderbuffertypecount 
(
	 D3D10DDI_HDEVICE
	CONST D3D11_1DDI_VIDEO_DECODER_DESC *
	UINT *
)
{...}

PFND3D11_1DDI_GETVIDEODECODERBUFFERTYPECOUNT 


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