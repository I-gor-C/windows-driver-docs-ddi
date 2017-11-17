---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERPROFILE
title: PFND3D11_1DDI_GETVIDEODECODERPROFILE
author: windows-driver-content
description: 
ms.assetid: 5e8d697c-73ef-4fbe-b18c-6bcb0702f1f9
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

# PFND3D11_1DDI_GETVIDEODECODERPROFILE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEODECODERPROFILE Pfnd3d111DdiGetvideodecoderprofile; 

// Definition

VOID Pfnd3d111DdiGetvideodecoderprofile 
(
	 D3D10DDI_HDEVICE
	 UINT
	GUID *
)
{...}

PFND3D11_1DDI_GETVIDEODECODERPROFILE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param UINT: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also