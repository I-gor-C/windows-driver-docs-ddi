---
UID: NC.d3d10umddi.PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT
title: PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT
author: windows-driver-content
description: 
ms.assetid: e40e453a-ce6f-4afc-9024-09a8c7992864
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

# PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT Pfnd3d111DdiGetvideodecoderprofilecount; 

// Definition

VOID Pfnd3d111DdiGetvideodecoderprofilecount 
(
	 D3D10DDI_HDEVICE
	UINT *
)
{...}

PFND3D11_1DDI_GETVIDEODECODERPROFILECOUNT 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also