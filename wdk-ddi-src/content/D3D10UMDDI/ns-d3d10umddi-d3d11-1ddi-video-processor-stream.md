---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_STREAM
title: D3D11_1DDI_VIDEO_PROCESSOR_STREAM
author: windows-driver-content
description: Contains stream-level data for the VideoProcessorBlt function.
old-location: display\d3d11_1ddi_video_processor_stream.htm
ms.assetid: 7edbe37b-ea45-4d37-908c-25c840e4cd74
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_STREAM
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
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_STREAM, D3D11_1DDI_VIDEO_PROCESSOR_STREAM
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_STREAM structure



## -description
<p>Contains stream-level data for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a> function.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_PROCESSOR_STREAM {
  BOOL                                Enable;
  UINT                                OutputIndex;
  UINT                                InputFrameOrField;
  UINT                                PastFrames;
  UINT                                FutureFrames;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW *pPastSurfaces;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW hInputSurface;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW *pFutureSurfaces;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW *pPastSurfacesRight;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW hInputSurfaceRight;
  D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW *pFutureSurfacesRight;
} D3D11_1DDI_VIDEO_PROCESSOR_STREAM;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>Specifies whether this input stream is enabled. If the value is <b>TRUE</b>, the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a> function blits this stream to the output surface. Otherwise, this stream is not blitted.</p>
<p>The maximum number of streams that can be enabled at one time is given in the <b>MaxInputStreams</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450968">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a> structure.</p>
</dd>

### -field <b>OutputIndex</b>

<dd>
<p>The zero-based index number of the output frame.</p>
</dd>

### -field <b>InputFrameOrField</b>

<dd>
<p>The zero-based index number of the input frame or field.</p>
</dd>

### -field <b>PastFrames</b>

<dd>
<p>The number of past reference frames.</p>
</dd>

### -field <b>FutureFrames</b>

<dd>
<p>The number of future reference frames.</p>
</dd>

### -field <b>pPastSurfaces</b>

<dd>
<p>A <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to an array of  pointers, allocated by the caller. This array contains the past reference frames for the video processing operation. The number of elements in the array is equal to <b>PastFrames</b>.</p>
</dd>

### -field <b>hInputSurface</b>

<dd>
<p>A <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to the surface that contains the current input frame.</p>
</dd>

### -field <b>pFutureSurfaces</b>

<dd>
<p>A <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to an array of pointers, allocated by the caller. This array contains the future reference frames for the video processing operation. The number of elements in the array is equal to <b>FutureFrames</b>.</p>
</dd>

### -field <b>pPastSurfacesRight</b>

<dd>
<p>If the stereo 3-D format is <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_SEPARATE</b>, this member is a <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to an array of   pointers that contains the past reference frames for the right view. The number of elements in the array is equal to <b>PastFrames</b>.</p>
<p>For any other stereo 3-D format, set this member to <b>NULL</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh439817">VideoProcessorSetStreamStereoFormat</a>.



</p>
</dd>

### -field <b>hInputSurfaceRight</b>

<dd>
<p>If the stereo 3-D format is <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_SEPARATE</b>, this member is a <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to the current input frame for the right view.</p>
<p>For any other stereo 3-D format, set this member to <b>NULL</b>. 

 

</p>
</dd>

### -field <b>pFutureSurfacesRight</b>

<dd>
<p>If the stereo 3-D format is <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_SEPARATE</b>, this member is a <b>D3D11_1DDI_HVIDEOPROCESSORINPUTVIEW</b> pointer to an array of  pointers that contains the future reference frames for the right view. The number of elements in the array is equal to <b>FutureFrames</b>.</p>
<p>

For any other stereo 3-D format, set this member to <b>NULL</b>. 

</p>
</dd>
</dl>

## -remarks
<p>If the stereo 3-D format is <b>D3D11_1DDI_VIDEO_PROCESSOR_STEREO_FORMAT_SEPARATE</b>, the <b>pPastSurfaces</b>, <b>pInputSurface</b>, and <b>pFutureSurfaces</b> members contain the left view.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450968">D3D11_1DDI_VIDEO_PROCESSOR_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451703">VideoProcessorBlt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439817">VideoProcessorSetStreamStereoFormat</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_PROCESSOR_STREAM structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
