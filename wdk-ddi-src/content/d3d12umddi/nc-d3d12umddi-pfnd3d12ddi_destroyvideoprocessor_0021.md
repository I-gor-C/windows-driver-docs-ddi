---
UID : NC:d3d12umddi.PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021
title : PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021
author : windows-driver-content
description : The pfnDestroyVideoProcessor callback function destroys a video processor.
old-location : display\pfnd3d12ddi_destroyvideoprocessor.htm
old-project : display
ms.assetid : 93C1FA5F-064F-41AC-B854-FF59A5CC172C
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnd3d12ddi_destroyvideoprocessor, pfnDestroyVideoProcessor callback function [Display Devices], pfnDestroyVideoProcessor, PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021, PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021, d3d12umddi/pfnDestroyVideoProcessor
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021 callback function
The <i>pfnDestroyVideoProcessor</i> callback function destroys a video processor.

## Syntax

```
PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021 Pfnd3d12ddiDestroyvideoprocessor0021;

void Pfnd3d12ddiDestroyvideoprocessor0021(
  D3D12DDI_HDEVICE hDrvDevice,
  D3D12DDI_HVIDEOPROCESSOR_0020 hDrvVideoProcessor
)
{...}
```

## Parameters

`hDrvDevice`

The handle of a device driver.

`hDrvVideoProcessor`

The handle of a video processor.


## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |