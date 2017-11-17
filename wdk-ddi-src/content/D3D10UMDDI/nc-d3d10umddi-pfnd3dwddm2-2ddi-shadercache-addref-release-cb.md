---
UID: NC.d3d10umddi.PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB
title: PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB
author: windows-driver-content
description: 
ms.assetid: a8d566f6-d30f-4739-a130-244dcc7b69f0
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

# PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB Pfnd3dwddm22DdiShadercacheAddrefReleaseCb; 

// Definition

void Pfnd3dwddm22DdiShadercacheAddrefReleaseCb 
(
	D3DWDDM2_2DDI_HRTCACHESESSION hCacheSession
)
{...}

PFND3DWDDM2_2DDI_SHADERCACHE_ADDREF_RELEASE_CB 


```

## -parameters

### -param hCacheSession: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also