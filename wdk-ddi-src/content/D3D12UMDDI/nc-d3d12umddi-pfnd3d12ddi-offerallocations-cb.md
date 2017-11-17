---
UID: NC.d3d12umddi.PFND3D12DDI_OFFERALLOCATIONS_CB
title: PFND3D12DDI_OFFERALLOCATIONS_CB
author: windows-driver-content
description: 
ms.assetid: 25413bd4-4567-4a20-8b6c-8b47d00f87fb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
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

# PFND3D12DDI_OFFERALLOCATIONS_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_OFFERALLOCATIONS_CB Pfnd3d12ddiOfferallocationsCb; 

// Definition

HRESULT Pfnd3d12ddiOfferallocationsCb 
(
	D3D12DDI_HRTDEVICE hRTDevice
	CONST D3D12DDICB_OFFERALLOCATIONS *
)
{...}

PFND3D12DDI_OFFERALLOCATIONS_CB 


```

## -parameters

### -param hRTDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also