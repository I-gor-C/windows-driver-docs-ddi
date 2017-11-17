---
UID: NC.d3d10umddi.PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION
title: PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION
author: windows-driver-content
description: 
ms.assetid: 4860b00b-cb70-487c-b630-d0e03ad2736a
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

# PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION Pfnd3dwddm22DdiSetShadercacheSession; 

// Definition

VOID Pfnd3dwddm22DdiSetShadercacheSession 
(
	 D3D10DDI_HDEVICE
	 D3DWDDM2_2DDI_HCACHESESSION
)
{...}

PFND3DWDDM2_2DDI_SET_SHADERCACHE_SESSION 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param D3DWDDM2_2DDI_HCACHESESSION: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also