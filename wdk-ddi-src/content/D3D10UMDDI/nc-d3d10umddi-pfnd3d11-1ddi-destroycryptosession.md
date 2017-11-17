---
UID: NC.d3d10umddi.PFND3D11_1DDI_DESTROYCRYPTOSESSION
title: PFND3D11_1DDI_DESTROYCRYPTOSESSION
author: windows-driver-content
description: 
ms.assetid: 74f3e8a6-aa51-4dc0-80fa-cb3b6b38ab24
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

# PFND3D11_1DDI_DESTROYCRYPTOSESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_DESTROYCRYPTOSESSION Pfnd3d111DdiDestroycryptosession; 

// Definition

VOID Pfnd3d111DdiDestroycryptosession 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HCRYPTOSESSION hCryptoSession
)
{...}

PFND3D11_1DDI_DESTROYCRYPTOSESSION 


```

## -parameters

### -param hDevice: 
### -param hCryptoSession: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also