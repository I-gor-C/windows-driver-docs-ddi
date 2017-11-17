---
UID: NC.d3d12umddi.PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020
title: PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020
author: windows-driver-content
description: 
ms.assetid: a8fdae5b-2eb0-4ac9-a666-2a5309e04507
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

# PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020 Pfnd3d12ddiEnableExtendedFeature0020; 

// Definition

HRESULT Pfnd3d12ddiEnableExtendedFeature0020 
(
	D3D12DDI_HDEVICE hDevice
	D3D12DDI_FEATURE_0020 Feature
	UINT32 FeatureVersion
)
{...}

PFND3D12DDI_ENABLE_EXTENDED_FEATURE_0020 


```

## -parameters

### -param hDevice: 
### -param Feature: 
### -param FeatureVersion: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also