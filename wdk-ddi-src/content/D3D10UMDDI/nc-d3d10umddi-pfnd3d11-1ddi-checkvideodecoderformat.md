---
UID: NC.d3d10umddi.PFND3D11_1DDI_CHECKVIDEODECODERFORMAT
title: PFND3D11_1DDI_CHECKVIDEODECODERFORMAT
author: windows-driver-content
description: 
ms.assetid: ac4d57bf-53a4-443f-b1b7-c8604ce4503b
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

# PFND3D11_1DDI_CHECKVIDEODECODERFORMAT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CHECKVIDEODECODERFORMAT Pfnd3d111DdiCheckvideodecoderformat; 

// Definition

VOID Pfnd3d111DdiCheckvideodecoderformat 
(
	 D3D10DDI_HDEVICE
	CONST GUID *
	 DXGI_FORMAT
	BOOL *
)
{...}

PFND3D11_1DDI_CHECKVIDEODECODERFORMAT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 
### -param DXGI_FORMAT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also