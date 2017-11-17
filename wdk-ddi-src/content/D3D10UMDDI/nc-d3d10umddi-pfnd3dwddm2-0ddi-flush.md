---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_FLUSH
title: PFND3DWDDM2_0DDI_FLUSH
author: windows-driver-content
description: 
ms.assetid: c82ef6aa-f2ec-4b37-96e0-90a476494817
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

# PFND3DWDDM2_0DDI_FLUSH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_FLUSH Pfnd3dwddm20DdiFlush; 

// Definition

BOOL Pfnd3dwddm20DdiFlush 
(
	 D3D10DDI_HDEVICE
	UINT contextType
	UINT FlushFlags
)
{...}

PFND3DWDDM2_0DDI_FLUSH 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param contextType: 
### -param FlushFlags: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also