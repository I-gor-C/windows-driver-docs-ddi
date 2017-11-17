---
UID: NC.d3d10umddi.PFND3DWDDM2_1DDI_SYNC_TOKEN
title: PFND3DWDDM2_1DDI_SYNC_TOKEN
author: windows-driver-content
description: 
ms.assetid: c1d849f7-ab95-4b39-aa1f-f1b397e97fb2
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

# PFND3DWDDM2_1DDI_SYNC_TOKEN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_1DDI_SYNC_TOKEN Pfnd3dwddm21DdiSyncToken; 

// Definition

VOID Pfnd3dwddm21DdiSyncToken 
(
	 D3D10DDI_HDEVICE
	D3D10DDI_HRESOURCE hResource
	HANDLE hSyncToken
)
{...}

PFND3DWDDM2_1DDI_SYNC_TOKEN 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param hResource: 
### -param hSyncToken: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also