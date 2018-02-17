---
UID: NC:d3dumddi.PFND3DDDI_CREATEVIDEOPROCESSDEVICE
title: PFND3DDDI_CREATEVIDEOPROCESSDEVICE
author: windows-driver-content
description: The CreateVideoProcessDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) video processing device that is used to process video (for example, to deinterlace the video and adjust ProcAmp properties of the video).
old-location: display\createvideoprocessdevice.htm
old-project: display
ms.assetid: 3149c7d9-0bf7-4355-8f15-821cf6b92f0a
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.createvideoprocessdevice, CreateVideoProcessDevice callback function [Display Devices], CreateVideoProcessDevice, PFND3DDDI_CREATEVIDEOPROCESSDEVICE, PFND3DDDI_CREATEVIDEOPROCESSDEVICE, d3dumddi/CreateVideoProcessDevice, UserModeDisplayDriver_Functions_2f8b832f-db45-4f76-ab8f-5ba94f818933.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3dumddi.h
apiname:
-	CreateVideoProcessDevice
product: Windows
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

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createvideoprocessdevice.md">CreateVideoProcessDevice</a> could not allocate the required memory for it to complete.

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

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_destroyvideoprocessdevice.md">DestroyVideoProcessDevice</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createvideoprocessdevice.md">D3DDDIARG_CREATEVIDEOPROCESSDEVICE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATEVIDEOPROCESSDEVICE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>