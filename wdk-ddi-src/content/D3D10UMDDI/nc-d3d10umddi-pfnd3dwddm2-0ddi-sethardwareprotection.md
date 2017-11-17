---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION
title: PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION
author: windows-driver-content
description: 
ms.assetid: bde1ab7d-7ac2-4e5d-b8ee-2b7a2dbabf88
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

# PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION Pfnd3dwddm20DdiSethardwareprotection; 

// Definition

VOID Pfnd3dwddm20DdiSethardwareprotection 
(
	D3D10DDI_HDEVICE hDevice
	D3D10DDI_HRESOURCE hResource
	BOOL Protected
)
{...}

PFND3DWDDM2_0DDI_SETHARDWAREPROTECTION 


```

## -parameters

### -param hDevice: 
### -param hResource: 
### -param Protected: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also