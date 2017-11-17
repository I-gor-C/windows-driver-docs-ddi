---
UID: NC.d3d12umddi.PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020
title: PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020
author: windows-driver-content
description: 
ms.assetid: 77eecc38-20cb-47f6-a5f7-ee0c9a2af15a
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

# PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020 Pfnd3d12ddiGetSupportedExtendedFeatureVersions0020; 

// Definition

HRESULT Pfnd3d12ddiGetSupportedExtendedFeatureVersions0020 
(
	D3D12DDI_HDEVICE hDevice
	D3D12DDI_FEATURE_0020 Feature
	UINT32 *puFeatureVersions
	UINT32 *pFeatureVersions
)
{...}

PFND3D12DDI_GET_SUPPORTED_EXTENDED_FEATURE_VERSIONS_0020 


```

## -parameters

### -param hDevice: 
### -param Feature: 
### -param *puFeatureVersions: 
### -param *pFeatureVersions: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also