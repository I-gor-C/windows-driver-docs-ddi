---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW
title: PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW
author: windows-driver-content
description: Creates a resource view for a video processor. This view defines the output sample for the video processing operation.
old-location: display\createvideoprocessoroutputview.htm
old-project: display
ms.assetid: 619695dc-8525-4200-a0c2-8ce0fb1010ed
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.createvideoprocessoroutputview, CreateVideoProcessorOutputView callback function [Display Devices], CreateVideoProcessorOutputView, PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW, PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW, d3d10umddi/CreateVideoProcessorOutputView
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	D3d10umddi.h
apiname:
-	CreateVideoProcessorOutputView
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
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

The Direct3D runtime calls <i>CreateVideoProcessorOutputView</i> after it has called the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessoroutputviewsize.md">CalcPrivateVideoProcessorOutputViewSize</a>   to determine the size in bytes for the private data that the driver requires for the video processor output view. The runtime allocates the memory for this private data for the driver. The driver uses this memory to store private data that is related to the video processor output view.

When the runtime  calls <i>CreateVideoProcessorOutputView</i>, it passes the handle to the private data memory in the <i>hView</i> parameter. This handle is actually a pointer to the memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivatevideoprocessoroutputviewsize.md">CalcPrivateVideoProcessorOutputViewSize</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createvideodecoderoutputview.md">D3D11_1DDIARG_CREATEVIDEODECODEROUTPUTVIEW</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CREATEVIDEOPROCESSOROUTPUTVIEW callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>