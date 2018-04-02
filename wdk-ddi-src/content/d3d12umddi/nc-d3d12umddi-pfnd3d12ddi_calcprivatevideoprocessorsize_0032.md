---
UID: NC:d3d12umddi.PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032
title: PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032
author: windows-driver-content
description: Used to calculate the size of a video processor.
old-location: display\pfnd3d12ddi_calcprivatevideoprocessorsize_0032.htm
old-project: display
ms.assetid: 7CE581B5-A6B5-4108-A678-554221386636
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032, PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032 entry point [Display Devices], d3d12umddi/PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032, display.pfnd3d12ddi_calcprivatevideoprocessorsize_0032
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
-	PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032 callback function
Used to calculate the size of a video processor.

## Syntax

```
PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032 Pfnd3d12ddiCalcprivatevideoprocessorsize0032;

SIZE_T Pfnd3d12ddiCalcprivatevideoprocessorsize0032(
  D3D12DDI_HDEVICE hDrvDevice,
  CONST D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032 *pArgs
)
{...}
```

## Parameters

`hDrvDevice`

The hardware device being processed.

`*pArgs`

The arguments used to create a video processor.


## Return Value

Returns the size of the video processor in bytes.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h |