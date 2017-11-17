---
UID: NC.d3d12umddi.PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020
title: PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020
author: windows-driver-content
description: 
ms.assetid: 5263a88d-fc7d-4d8a-9ecc-fc8654057b40
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

# PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020 Pfnd3d12ddiGetSupportedExtendedFeatures0020; 

// Definition

HRESULT Pfnd3d12ddiGetSupportedExtendedFeatures0020 
(
	D3D12DDI_HDEVICE hDevice
	UINT32 *puFeatures
	D3D12DDI_FEATURE_0020 *pFeatures
)
{...}

PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURES_0020 


```

## -parameters

### -param hDevice: 
### -param *puFeatures: 
### -param *pFeatures: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also