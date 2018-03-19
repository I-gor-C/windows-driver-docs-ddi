---
UID: NC:d3dumddi.PFND3DDDI_VIDEOPROCESSBLT
title: PFND3DDDI_VIDEOPROCESSBLT
author: windows-driver-content
description: The VideoProcessBlt function processes a video frame by using the specified Microsoft DirectX Video Accelerator (VA) video processing device.
old-location: display\videoprocessblt.htm
old-project: display
ms.assetid: 719465dd-4547-491c-ab30-ae63bba1b72c
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3DDDI_VIDEOPROCESSBLT, UserModeDisplayDriver_Functions_23e47fd3-a838-4b56-82c3-7894d2b173a1.xml, VideoProcessBlt, VideoProcessBlt callback function [Display Devices], d3dumddi/VideoProcessBlt, display.videoprocessblt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows Vista.
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3dumddi.h
api_name:
-	VideoProcessBlt
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_VIDEOPROCESSBLT callback function
The <i>VideoProcessBlt</i> function processes a video frame by using the specified Microsoft DirectX Video Accelerator (VA) video processing device.

## Syntax

```
PFND3DDDI_VIDEOPROCESSBLT Pfnd3dddiVideoprocessblt;

HRESULT Pfnd3dddiVideoprocessblt(
  HANDLE hDevice,
  CONST D3DDDIARG_VIDEOPROCESSBLT *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<i>VideoProcessBlt</i> returns one of the following values:

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
The DirectX VA video processing operation is successfully performed.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">
<i>VideoProcessBlt</i> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows Vista.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicefuncs.md">D3DDDI_DEVICEFUNCS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_videoprocessblt.md">D3DDDIARG_VIDEOPROCESSBLT</a>