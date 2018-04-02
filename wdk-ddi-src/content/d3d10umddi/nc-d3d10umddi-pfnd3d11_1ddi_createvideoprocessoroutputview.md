---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW
title: PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW
author: windows-driver-content
description: Creates a resource view for a video processor. This view defines the output sample for the video processing operation.
old-location: display\createvideoprocessoroutputview.htm
old-project: display
ms.assetid: 619695dc-8525-4200-a0c2-8ce0fb1010ed
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateVideoProcessorOutputView, CreateVideoProcessorOutputView callback function [Display Devices], PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW, d3d10umddi/CreateVideoProcessorOutputView, display.createvideoprocessoroutputview
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
-	CreateVideoProcessorOutputView
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW callback function
Creates a resource view for a video processor. This view defines the output sample for the video processing operation.

## Syntax

```
PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW Pfnd3d111DdiCreatevideoprocessoroutputview;

HRESULT Pfnd3d111DdiCreatevideoprocessoroutputview(
   D3D10DDI_HDEVICE,
  CONST D3D11_1DDIARG_CREATEVIDEOPROCESSOROUTPUTVIEW *,
   D3D11_1DDI_HVIDEOPROCESSOROUTPUTVIEW,
   D3D11_1DDI_HRTVIDEOPROCESSOROUTPUTVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D11_1DDI_HVIDEOPROCESSOROUTPUTVIEW`



`D3D11_1DDI_HRTVIDEOPROCESSOROUTPUTVIEW`




## Return Value

<i>CreateVideoProcessorOutputView</i> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The video processor output view was created successfully.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl>
</td>
<td width="60%">
The graphics adapter was removed.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

        Memory was not available to complete the operation.

</td>
</tr>
</table>

## Remarks

The Direct3D runtime calls <i>CreateVideoProcessorOutputView</i> after it has called the driver's <a href="https://msdn.microsoft.com/2cf09e91-e83b-47ae-bf34-037dc01d7e80">CalcPrivateVideoProcessorOutputViewSize</a>   to determine the size in bytes for the private data that the driver requires for the video processor output view. The runtime allocates the memory for this private data for the driver. The driver uses this memory to store private data that is related to the video processor output view.

When the runtime  calls <i>CreateVideoProcessorOutputView</i>, it passes the handle to the private data memory in the <i>hView</i> parameter. This handle is actually a pointer to the memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/2cf09e91-e83b-47ae-bf34-037dc01d7e80">CalcPrivateVideoProcessorOutputViewSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh406312">D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW</a>