---
UID: NC:d3d10umddi.PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION
title: PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION
author: windows-driver-content
description: Returns the private state data for a video processor stream to an application.
old-location: display\videoprocessorgetstreamextension.htm
old-project: display
ms.assetid: e2c91e9c-f8ab-48ba-b98a-332cb0ac7077
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION, d3d10umddi/pfnVideoProcessorGetStreamExtension, display.videoprocessorgetstreamextension, pfnVideoProcessorGetStreamExtension, pfnVideoProcessorGetStreamExtension callback function [Display Devices]
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
-	pfnVideoProcessorGetStreamExtension
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION callback function
Returns the private state data for a video processor stream to an application.

## Syntax

```
PFND3D11_1DDI_VIDEOPROCESSORGETSTREAMEXTENSION Pfnd3d111DdiVideoprocessorgetstreamextension;

HRESULT Pfnd3d111DdiVideoprocessorgetstreamextension(
   D3D10DDI_HDEVICE,
   D3D11_1DDI_HVIDEOPROCESSOR,
   UINT,
  CONST GUID *,
   UINT,
  void *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11_1DDI_HVIDEOPROCESSOR`



`UINT`



`*`



`UINT`



`*`




## Return Value

<b>VideoProcessorGetStreamExtension</b> returns one of the following values:

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

        The display miniport driver cannot set the requested private state data for the video processor.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>
</td>
<td width="60%">
Parameters were validated and determined to be incorrect.


</td>
</tr>
</table>

## Remarks

The Microsoft Direct3D runtime does not validate any parameter data before it calls the  <b>VideoProcessorGetStreamExtension</b> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideoprocessor.md">CreateVideoProcessor</a>