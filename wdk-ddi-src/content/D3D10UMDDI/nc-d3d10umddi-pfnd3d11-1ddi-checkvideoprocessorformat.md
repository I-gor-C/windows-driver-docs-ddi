---
UID: NC.d3d10umddi.PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT
title: PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT
author: windows-driver-content
description: 
ms.assetid: 6aa3d969-7222-41d3-945e-c1c46a34856c
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

# PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT Pfnd3d111DdiCheckvideoprocessorformat; 

// Definition

VOID Pfnd3d111DdiCheckvideoprocessorformat 
(
	 D3D10DDI_HDEVICE
	 D3D11_1DDI_HVIDEOPROCESSORENUM
	 DXGI_FORMAT
	UINT *
)
{...}

PFND3D11_1DDI_CHECKVIDEOPROCESSORFORMAT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3D11_1DDI_HVIDEOPROCESSORENUM: 
### -param DXGI_FORMAT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also