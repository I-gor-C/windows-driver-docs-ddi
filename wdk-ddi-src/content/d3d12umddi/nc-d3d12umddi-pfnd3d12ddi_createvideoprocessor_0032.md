---
UID: NC:d3d12umddi.PFND3D12DDI_CREATEVIDEOPROCESSOR_0032
title: PFND3D12DDI_CREATEVIDEOPROCESSOR_0032
author: windows-driver-content
description: Used to create a video processor.
old-location: display\pfnd3d12ddi_createvideoprocessor_0032_.htm
old-project: display
ms.assetid: 64E9EDF7-0B98-4D8A-BB2B-D336622558D0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D12DDI_CREATEVIDEOPROCESSOR_0032, PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 callback function [Display Devices], d3d12umddi/PFND3D12DDI_CREATEVIDEOPROCESSOR_0032, display.pfnd3d12ddi_createvideoprocessor_0032_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d12umddi.h
api_name:
-	PFND3D12DDI_CREATEVIDEOPROCESSOR_0032
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 callback function
Used to create a video processor.

## Syntax

```
PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 Pfnd3d12ddiCreatevideoprocessor0032;

HRESULT Pfnd3d12ddiCreatevideoprocessor0032(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032 *pArgs,
  D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`

The arguments used to create a video processor.

`hDrvVideoProcessor`

The video processor.


## Return Value

Returns STATUS_SUCCESS if completed successfully.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |