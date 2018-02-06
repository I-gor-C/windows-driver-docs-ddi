---
UID: NC:d3d12umddi.PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021
title: PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021
author: windows-driver-content
description: The pfnCalcPrivateVideoProcessorSize callback function calculates the size of the private video processor.
old-location: display\pfnd3d12ddi_calcprivatevideoprocessorsize.htm
old-project: display
ms.assetid: F1ED5176-4F50-44DA-96B3-5E133A236461
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.pfnd3d12ddi_calcprivatevideoprocessorsize, pfnCalcPrivateVideoProcessorSize callback function [Display Devices], pfnCalcPrivateVideoProcessorSize, PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021, PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021, d3d12umddi/pfnCalcPrivateVideoProcessorSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	D3d12umddi.h
apiname:
-	pfnCalcPrivateVideoProcessorSize
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021 callback function
The <i>pfnCalcPrivateVideoProcessorSize</i> callback function calculates the size of the private video processor.

## Syntax

```
PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021 Pfnd3d12ddiCalcprivatevideoprocessorsize0021;

SIZE_T Pfnd3d12ddiCalcprivatevideoprocessorsize0021(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0021 *pArgs
)
{...}
```

## Parameters

`hDrvDevice`

The handler of a device.

`*pArgs`

The arguments used to create a video processor.


## Return Value

None

## Remarks

The  runtime allocates memory for storing the driver CPU object that represents the video processor.  This method is used to calculate the driver object size.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |