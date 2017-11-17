---
UID: NC.d3d10umddi.PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
title: PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
author: windows-driver-content
description: 
ms.assetid: b7695f2a-30b3-490b-bc74-967cbf3173e0
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

# PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE Pfnd3d111DdiCalcprivateauthenticatedchannelsize; 

// Definition

SIZE_T Pfnd3d111DdiCalcprivateauthenticatedchannelsize 
(
	D3D10DDI_HDEVICE hDevice
	CONST D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL *pCreateData
)
{...}

PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE 


```

## -parameters

### -param hDevice: 
### -param *pCreateData: 



## -returns

Returns SIZE_T that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also