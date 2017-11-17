---
UID: NC.d3d10umddi.PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE
title: PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE
author: windows-driver-content
description: 
ms.assetid: afa37abe-83fb-45bf-bf35-3f5587393a03
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

# PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE Pfnd3dwddm22DdiCalcprivateShadercacheSessionSize; 

// Definition

SIZE_T Pfnd3dwddm22DdiCalcprivateShadercacheSessionSize 
(
	 D3D10DDI_HDEVICE
)
{...}

PFND3DWDDM2_2DDI_CALCPRIVATE_SHADERCACHE_SESSION_SIZE 


```

## -parameters

### -param D3D10DDI_HDEVICE: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also