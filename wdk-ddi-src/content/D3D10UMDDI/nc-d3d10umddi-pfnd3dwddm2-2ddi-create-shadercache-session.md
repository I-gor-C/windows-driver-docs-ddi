---
UID: NC.d3d10umddi.PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
title: PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION
author: windows-driver-content
description: 
ms.assetid: f17b4ee0-5cfa-41e8-8f7d-4349a2900f87
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

# PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION Pfnd3dwddm22DdiCreateShadercacheSession; 

// Definition

VOID Pfnd3dwddm22DdiCreateShadercacheSession 
(
	 D3D10DDI_HDEVICE
	 D3DWDDM2_2DDI_HCACHESESSION
	 D3DWDDM2_2DDI_HRTCACHESESSION
)
{...}

PFND3DWDDM2_2DDI_CREATE_SHADERCACHE_SESSION 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3DWDDM2_2DDI_HCACHESESSION: 
### -param D3DWDDM2_2DDI_HRTCACHESESSION: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also