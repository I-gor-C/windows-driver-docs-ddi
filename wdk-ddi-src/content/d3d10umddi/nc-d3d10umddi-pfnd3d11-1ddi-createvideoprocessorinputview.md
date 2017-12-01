---
UID: NC.d3d10umddi.PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW
title: PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW
author: windows-driver-content
description: Creates a resource view for a video processor. This view defines the input sample for the video processing operation.
old-location: display\createvideoprocessorinputview.htm
old-project: display
ms.assetid: f3942c53-e366-41c5-9f43-d093fa6b6ed6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
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
req.alt-api: CreateVideoProcessorInputView
req.alt-loc: D3d10umddi.h
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
req.iface: 
---

# PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW callback



## -description
<p>Creates a resource view for a video processor. This view defines the input sample for the video processing operation.</p>


## -prototype

````
PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW CreateVideoProcessorInputView;

HRESULT APIENTRY* CreateVideoProcessorInputView(
  _In_       D3D10DDI_HDEVICE                            hDevice,
  _In_ const D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW *pView,
  _In_       D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW         hView,
  _In_       D3D11_1DDI_HRTVIDEOPROCESSORINPUTVIEW       hRTView
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).

</p>
</dd>

### -param <i>pView</i> [in]

<dd>
<p>A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessorinputview.md">D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW</a> structure. This structure specifies the attributes of the video processor input view to be created.</p>
</dd>

### -param <i>hView</i> [in]

<dd>
<p>A handle to the driver's private data for the video processor input view. For more information, see the Remarks section.</p>
</dd>

### -param <i>hRTView</i> [in]

<dd>
<p>A handle to the video processor input that the driver should use when it calls back into the Direct3D runtime.</p>
</dd>
</dl>

## -returns
<p><b>CreateVideoProcessorInputView</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The video processor input view was created successfully.</p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p>The graphics adapter was removed.</p><dl>
<dt><b>DXGI_ERROR_UNSUPPORTED</b></dt>
</dl><p>The D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW contained incorrect or unsupported data. For example, the driver should return <b>DXGI_ERROR_UNSUPPORTED</b> if the <b>FourCC</b> member specified an unsupported code value.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
        Memory was not available to complete the operation.</p>

<p> </p>

## -remarks
<p>The Direct3D runtime calls <i>CreateVideoProcessorInputView</i> after it has called the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorinputviewsize.md">CalcPrivateVideoProcessorInputViewSize</a>   to determine the size in bytes for the private data that the driver requires for the video processor input view. The runtime allocates the memory for this private data for the driver. The driver uses this memory to store private data that is related to the video processor input view.</p>

<p>When the runtime  calls <i>CreateVideoProcessorInputView</i>, it passes the handle to the private data memory in the <i>hView</i> parameter. This handle is actually a pointer to the memory. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-calcprivatevideoprocessorinputviewsize.md">CalcPrivateVideoProcessorInputViewSize</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddiarg-createvideoprocessorinputview.md">D3D11_1DDIARG_CREATEVIDEOPROCESSORINPUTVIEW</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CREATEVIDEOPROCESSORINPUTVIEW callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
