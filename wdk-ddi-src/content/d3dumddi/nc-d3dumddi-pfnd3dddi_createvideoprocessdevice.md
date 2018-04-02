---
UID: NC:d3dumddi.PFND3DDDI_CREATEVIDEOPROCESSDEVICE
title: PFND3DDDI_CREATEVIDEOPROCESSDEVICE
author: windows-driver-content
description: The CreateVideoProcessDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processing device that is used to process video (for example, to deinterlace the video and adjust ProcAmp properties of the video).
old-location: display\createvideoprocessdevice.htm
old-project: display
ms.assetid: 3149c7d9-0bf7-4355-8f15-821cf6b92f0a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateVideoProcessDevice, CreateVideoProcessDevice callback function [Display Devices], PFND3DDDI_CREATEVIDEOPROCESSDEVICE, UserModeDisplayDriver_Functions_2f8b832f-db45-4f76-ab8f-5ba94f818933.xml, d3dumddi/CreateVideoProcessDevice, display.createvideoprocessdevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
-	CreateVideoProcessDevice
product:
- Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_CREATEVIDEOPROCESSDEVICE callback function
The <b>CreateVideoProcessDevice</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processing device that is used to process video (for example, to deinterlace the video and adjust ProcAmp properties of the video).

## Syntax

```
PFND3DDDI_CREATEVIDEOPROCESSDEVICE Pfnd3dddiCreatevideoprocessdevice;

HRESULT Pfnd3dddiCreatevideoprocessdevice(
  HANDLE hDevice,
  D3DDDIARG_CREATEVIDEOPROCESSDEVICE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>CreateVideoProcessDevice</b> returns one of the following values:

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
The video processing device is successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542977">D3DDDIARG_CREATEVIDEOPROCESSDEVICE</a>



<a href="https://msdn.microsoft.com/dc0f8dba-afdd-47f4-ba7f-72c510e80052">DestroyVideoProcessDevice</a>