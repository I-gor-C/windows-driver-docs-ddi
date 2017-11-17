---
UID: NC.dxgiddi.PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAY1CB
title: PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAY1CB
author: windows-driver-content
description: 
ms.assetid: ec1a0b15-3bec-4c73-9a68-316cfa2f829d
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

# PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAY1CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAY1CB PfnddxgiddiPresentMultiplaneOverlay1cb; 

// Definition

HRESULT PfnddxgiddiPresentMultiplaneOverlay1cb 
(
	HANDLE hDevice
	CONST DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1 *
)
{...}

PFNDDXGIDDI_PRESENT_MULTIPLANE_OVERLAY1CB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also