---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS
title: PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS
author: windows-driver-content
description: 
ms.assetid: 7e0e3f45-a393-46c6-9764-6c2e2c2d90a7
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

# PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS Pfnd3d111DdiGetcontentprotectioncaps; 

// Definition

HRESULT Pfnd3d111DdiGetcontentprotectioncaps 
(
	D3D10DDI_HDEVICE hDevice
	CONST GUID *pCryptoType
	CONST GUID *pDecodeProfile
	D3D11_1DDI_VIDEO_CONTENT_PROTECTION_CAPS *pCaps
)
{...}

PFND3D11_1DDI_GETCONTENTPROTECTIONCAPS 


```

## -parameters

### -param hDevice: 
### -param *pCryptoType: 
### -param *pDecodeProfile: 
### -param *pCaps: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also