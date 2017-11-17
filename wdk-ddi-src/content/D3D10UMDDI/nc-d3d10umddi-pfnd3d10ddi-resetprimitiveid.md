---
UID: NC.d3d10umddi.PFND3D10DDI_RESETPRIMITIVEID
title: PFND3D10DDI_RESETPRIMITIVEID
author: windows-driver-content
description: 
ms.assetid: 0c70066a-bf09-4a3f-9e40-b987ff1404d2
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

# PFND3D10DDI_RESETPRIMITIVEID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D10DDI_RESETPRIMITIVEID Pfnd3d10ddiResetprimitiveid; 

// Definition

VOID Pfnd3d10ddiResetprimitiveid 
(
	 D3D10DDI_HDEVICE
	 BOOL
)
{...}

PFND3D10DDI_RESETPRIMITIVEID 


```

## -parameters

### -param D3D10DDI_HDEVICE: 
### -param BOOL: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also