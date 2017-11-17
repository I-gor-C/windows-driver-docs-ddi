---
UID: NC.d3dkmddi.DXGKCB_RELEASEHANDLEDATA
title: DXGKCB_RELEASEHANDLEDATA
author: windows-driver-content
description: 
ms.assetid: e1268851-a7c6-4c95-ab9b-d7dc406815a8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
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

# DXGKCB_RELEASEHANDLEDATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_RELEASEHANDLEDATA DxgkcbReleasehandledata; 

// Definition

VOID DxgkcbReleasehandledata 
(
)
{...}

DXGKCB_RELEASEHANDLEDATA 


```

## -parameters




## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also