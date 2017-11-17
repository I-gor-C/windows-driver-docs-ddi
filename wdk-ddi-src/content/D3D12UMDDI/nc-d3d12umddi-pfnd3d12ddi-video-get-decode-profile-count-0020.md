---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020
title: PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020
author: windows-driver-content
description: 
ms.assetid: 25f6d38f-11e9-49eb-95ba-35e5b1c248ff
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

# PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020 Pfnd3d12ddiVideoGetDecodeProfileCount0020; 

// Definition

UINT Pfnd3d12ddiVideoGetDecodeProfileCount0020 
(
	 D3D12DDI_HDEVICE
	UINT NodeIndex
)
{...}

PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020 


```

## -parameters

### -param D3D12DDI_HDEVICE: 
### -param NodeIndex: 



## -returns

Returns UINT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also