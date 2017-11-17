---
UID: NC.dxgiddi.PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB
title: PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB
author: windows-driver-content
description: 
ms.assetid: c00a04fb-8bf7-4bf1-aa00-6c6c6ba33d31
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dxgiddi.h
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

# PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB PfnddxgiddiPresentMultiplaneOverlaycb; 

// Definition

HRESULT PfnddxgiddiPresentMultiplaneOverlaycb 
(
	HANDLE hDevice
	CONST DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY *
)
{...}

PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAYCB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also