---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION
title: PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION
author: windows-driver-content
description: Returns private state data from a video processor to an application.
old-location: display\videoprocessorgetoutputextension.htm
old-project: display
ms.assetid: 16f314f7-a54b-4c79-9cd6-1472ed454bbe
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION, d3d10umddi/pfnVideoProcessorGetOutputExtension, display.videoprocessorgetoutputextension, pfnVideoProcessorGetOutputExtension, pfnVideoProcessorGetOutputExtension callback function [Display Devices]
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
-	pfnVideoProcessorGetOutputExtension
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION callback function
Returns private state data from a video processor to an application.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORGETOUTPUTEXTENSION Pfnd3d111DdiVideoprocessorgetoutputextension;

HRESULT Pfnd3d111DdiVideoprocessorgetoutputextension(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
  CONST GUID *,
   UINT,
  void *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`*`



`UINT`



`*`




## Return Value

<b>VideoProcessorGetOutputExtension</b> returns one of the following values:

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
The private state data was returned successfully.

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
<dt><b>E_FAIL</b></dt>
</dl>
</td>
<td width="60%">

        The display miniport driver cannot return the requested private state data from the video processor.

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

The Microsoft Direct3D runtime does not validate any parameter data before it calls the  <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_videoprocessorsetoutputextension.md">VideoProcessorSetOutputExtension</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>