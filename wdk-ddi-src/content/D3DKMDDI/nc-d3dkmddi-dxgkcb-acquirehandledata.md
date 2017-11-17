---
UID: NC.d3dkmddi.DXGKCB_ACQUIREHANDLEDATA
title: DXGKCB_ACQUIREHANDLEDATA
author: windows-driver-content
description: 
ms.assetid: 16ee1d16-4edc-434b-a42e-c6560bf90ce6
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

# DXGKCB_ACQUIREHANDLEDATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKCB_ACQUIREHANDLEDATA DxgkcbAcquirehandledata; 

// Definition

VOID * DxgkcbAcquirehandledata 
(
)
{...}

DXGKCB_ACQUIREHANDLEDATA 


```

## -parameters




## -returns

Returns VOID * that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also