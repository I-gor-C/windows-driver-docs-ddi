---
UID: NC:d3d10umddi.PFND3D11_1DDI_GETVIDEOPROCESSORCAPS
title: PFND3D11_1DDI_GETVIDEOPROCESSORCAPS
author: windows-driver-content
description: Queries the capabilities of a specified video processor.
old-location: display\getvideoprocessorcaps.htm
old-project: display
ms.assetid: 5ffb4f6e-41c6-4d15-8995-a398b9976822
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_GETVIDEOPROCESSORCAPS, d3d10umddi/pfnGetVideoProcessorCaps, display.getvideoprocessorcaps, pfnGetVideoProcessorCaps, pfnGetVideoProcessorCaps callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3d10umddi.h
api_name:
-	pfnGetVideoProcessorCaps
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_GETVIDEOPROCESSORCAPS callback function
Queries the capabilities of a specified video processor.

## Syntax

```
PFND3D11_1DDI_GETVIDEOPROCESSORCAPS Pfnd3d111DdiGetvideoprocessorcaps;

void Pfnd3d111DdiGetvideoprocessorcaps(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSORENUM,
  D3D11_1DDI_VIDEO_PROCESSOR_CAPS *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSORENUM`



`*`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/38c27502-7e8a-45a1-8a7c-315300502480">CreateVideoProcessorEnum</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh450968">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>