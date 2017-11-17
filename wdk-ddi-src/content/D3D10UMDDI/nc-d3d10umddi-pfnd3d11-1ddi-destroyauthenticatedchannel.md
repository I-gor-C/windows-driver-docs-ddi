---
UID: NC.d3d10umddi.PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL
title: PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL
author: windows-driver-content
description: 
ms.assetid: 1a905f15-22ba-4487-b0af-e81a67609e20
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

# PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL Pfnd3d111DdiDestroyauthenticatedchannel; 

// Definition

VOID Pfnd3d111DdiDestroyauthenticatedchannel 
(
	D3D10DDI_HDEVICE hDevice
	D3D11_1DDI_HAUTHCHANNEL hAuthChannel
)
{...}

PFND3D11_1DDI_DESTROYAUTHENTICATEDCHANNEL 


```

## -parameters

### -param hDevice: 
### -param hAuthChannel: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also