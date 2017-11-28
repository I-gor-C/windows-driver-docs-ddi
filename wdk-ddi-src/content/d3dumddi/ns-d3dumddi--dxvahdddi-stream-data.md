---
UID: NS.d3dumddi._DXVAHDDDI_STREAM_DATA
title: DXVAHDDDI_STREAM_DATA
author: windows-driver-content
description: The DXVAHDDDI_STREAM_DATA structure describes an input stream that is processed.
old-location: display\dxvahdddi_stream_data.htm
old-project: display
ms.assetid: 3b8fc849-8794-4dab-af28-a1c0dfd859d3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVAHDDDI_STREAM_DATA, DXVAHDDDI_STREAM_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_STREAM_DATA is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_STREAM_DATA
req.alt-loc: d3dumddi.h
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

# DXVAHDDDI_STREAM_DATA structure



## -description
<p>The DXVAHDDDI_STREAM_DATA structure describes an input stream that is processed. </p>


## -syntax

````
typedef struct _DXVAHDDDI_STREAM_DATA {
  BOOL              Enable;
  UINT              OutputIndex;
  UINT              InputFrameOrField;
  UINT              PastFrames;
  UINT              FutureFrames;
  DXVAHDDDI_SURFACE *pPastSurfaces;
  DXVAHDDDI_SURFACE InputSurface;
  DXVAHDDDI_SURFACE *pFutureSurfaces;
} DXVAHDDDI_STREAM_DATA;
````


## -struct-fields
<dl>

### -field <b>Enable</b>

<dd>
<p>[in] A Boolean value that specifies whether the input stream is enabled. The number of input streams that the runtime enables must not be more than the number, which the driver sets in the <b>MaxStreamStates</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a> structure.  </p>
</dd>

### -field <b>OutputIndex</b>

<dd>
<p>[in] A zero-based cyclic frame index number of the output frames that are composed. </p>
</dd>

### -field <b>InputFrameOrField</b>

<dd>
<p>[in] A zero-based frame number of the input frames or fields that are processed.</p>
</dd>

### -field <b>PastFrames</b>

<dd>
<p>[in] The number of past reference frames. This number must not be more than the number that the driver sets in the <b>PastFrames</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563109">DXVAHDDDI_VPCAPS</a> structure.  </p>
</dd>

### -field <b>FutureFrames</b>

<dd>
<p>[in] The number of future reference frames. This number must not be more than the number that the driver sets in the <b>FutureFrames</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563109">DXVAHDDDI_VPCAPS</a> structure.  </p>
</dd>

### -field <b>pPastSurfaces</b>

<dd>
<p>[in] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563106">DXVAHDDDI_SURFACE</a> structures that describe the past reference surfaces. </p>
</dd>

### -field <b>InputSurface</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563106">DXVAHDDDI_SURFACE</a> structure that describes the input surface. </p>
</dd>

### -field <b>pFutureSurfaces</b>

<dd>
<p>[in] An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563106">DXVAHDDDI_SURFACE</a> structures that describe the future reference surfaces. </p>
</dd>
</dl>

## -remarks
<p>The driver must allocate the surfaces that the <b>pPastSurfaces</b>, <b>InputSurface</b>, and <b>pFutureSurfaces</b> members specify in the pool type, which the driver sets in the <b>InputPool</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a> structure, and with one of the following surface types; otherwise, the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-videoprocessblthd.md">VideoProcessBltHD</a> function returns an error.</p>

<p>A video surface that is created with the DXVAHD_SURFACE_TYPE_VIDEO_INPUT or DXVAHD_SURFACE_TYPE_VIDEO_INPUT_PRIVATE type. </p>

<p>A decode render target surface that is created with the DXVA2_VideoDecodeRenderTarget type. </p>

<p>An off-screen plain surface. </p>

<p>The <b>OutputIndex</b> member is a zero-based cyclic number that indicates the frame index number of the output. The driver uses this output-index information to perform the video processing in a certain pattern or cycle, especially when the driver performs deinterlacing, frame-rate conversion, and inverse telecine. For example, with the following output-index pattern, the driver performs the indicated video processing:</p>

<p>Progressive format at normal and half rate:  </p>

<p>OutputIndex = 0, 0,...</p>

<p>Progressive format at 2/1 custom rate (double frame-rate conversion, OutputFrames=2):  </p>

<p>OutputIndex = 0, 1, 0, 1,...</p>

<p>Interlaced format at normal rate:  </p>

<p>OutputIndex = 0, 1, 0, 1,... (0: first field, 1: second field)</p>

<p>Interlaced format at half rate:  </p>

<p>OutputIndex = 0, 0,... (for example, first and second fields are blended to one frame)</p>

<p>Interlaced at 4/5 custom rate (3:2 inverse telecine, OutputFrames=4):  </p>

<p>OutputIndex = 0, 1, 2, 3, 0, 1, 2, 3,... (0:A, 1:B, 2:C, 3:D film frame) </p>

<p>The <b>InputFrameOrField</b> member is a zero-based number that indicates the frame or the field number of the input surface. For example, with the following input-frame-or-field number, the driver can perform the indicated video processing: </p>

<p>Progressive format and interlaced format at normal rate:  </p>

<p>InputFrameOrField = 0, 1, 2,...</p>

<p>Progressive format and interlaced format at half rate:  </p>

<p>InputFrameOrField = 0, 2, 4,...</p>

<p>Interlaced format at 4/5 custom rate (3:2 inverse telecine, OutputFrames=4 and InputFrameOrField=10):  </p>

<p>InputFrameOrField = 0, 0, 0, 0, 10, 10, 10, 10, 20, 20, 20, 20,...</p>

<p>Interlaced format at 4/15 custom rate (8:7 inverse telecine, OutputFrames=2 and InputFrameOrField=15):  </p>

<p>InputFrameOrField = 0, 0, 15, 15, 30, 30,...</p>

<p>The application should cause both the <b>OutputIndex</b> and <b>InputFrameOrField</b> members to reset when either the frame format or the output rate is changed so that the driver can reset its internal processing state. For more information about changing frame format or output rate, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563081">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a>.</p>

<p>However, if the driver switches between normal and half rate (values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563061">DXVAHDDDI_OUTPUT_RATE</a> enumeration), the driver should not require the reset. </p>

<p>If both the <b>OutputIndex</b> and <b>InputFrameOrField</b> members remain unchanged at the next process time, the driver determines that the frame is unchanged (for example, paused) in the stream processing. Therefore, the driver can optimize the frame by using cached data.</p>

<p>The driver should fallback to a less intensive video processing method as less reference frames are provided. The driver should fallback to Bob de-interlacing when no reference samples are provided.</p>

<p>An application can provide less past and future reference frames than the reference frames that the driver requests. For example, an application can provide less reference frames in the following conditions:</p>

<p>At the beginning or at the end of the frame sequence. </p>

<p>Transition between progressive and interlaced. </p>

<p>Normal or half rate progressive stream. </p>

<p>Sub-video streams that do not require high quality de-interlacing. </p>

<p>While throttling the reference frames to recover from frame drops and to keep up the frame rate. </p>

<p>Frame dropping from the input (for example, frame drops in the decoder). </p>

<p>Both the past and the future reference frames are provided in the  <b>pPastSurfaces</b> and <b>pFutureSurfaces</b> array members in temporal order from older to newer frames continuously. For example, the order of the elements in the arrays are as shown in the following example:</p><dl>
<dd>
<p><b>pPastSurfaces</b> [] = {..., T-3, T-2, T-1}</p>
</dd>
<dd>
<p><b>InputSurface</b> = T</p>
</dd>
<dd>
<p><b>pFutureSurfaces</b> [] = {T+1, T+2, T+3,...}</p>
</dd>
</dl><p><b>pPastSurfaces</b> [] = {..., T-3, T-2, T-1}</p>

<p><b>InputSurface</b> = T</p>

<p><b>pFutureSurfaces</b> [] = {T+1, T+2, T+3,...}</p>

<p>The input and reference frames change location from the future location to the past location through the current location as the <b>OutputIndex</b> and <b>InputFrameOrField</b> members increment. For example, the input surface changes as the <b>OutputIndex</b> and <b>InputFrameOrField</b> increment when the driver performs the following video processing:</p>

<p>Progressive format at normal rate:  </p>

<p>OutputIndex = 0, 0, 0,... </p>

<p>InputFrameOrField = 0, 1, 2,...</p>

<p>InputSurface = T, T+1, T+2,...</p>

<p>Interlaced format at normal rate:  </p>

<p>OutputIndex = 0, 1, 0, 1, 0, 1,... </p>

<p>InputFrameOrField = 0, 1, 2, 3, 4, 5,...</p>

<p>InputSurface = T, T, T+1, T+1, T+2, T+2,...</p>

<p>Interlaced format at half rate:  </p>

<p>OutputIndex = 0, 0, 0,... </p>

<p>InputFrameOrField = 0, 2, 4,...</p>

<p>InputSurface = T, T+1, T+2,...</p>

<p>Interlaced format at 4/5 custom rate (3:2 inverse telecine, OutputFrames=4 and InputFrameOrField=10):  </p>

<p>OutputIndex = 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3,... </p>

<p>InputFrameOrField = 0, 0, 0, 0, 10, 10, 10, 10, 20, 20, 20, 20,...</p>

<p>InputSurface = T, T, T, T, T+5, T+5, T+5, T+5, T+10, T+10, T+10, T+10,... </p>

<p>Interlaced format at 4/15 custom rate (8:7 inverse telecine, OutputFrames=2 and InputFrameOrField=15):  </p>

<p>OutputIndex = 0, 1, 0, 1, 0, 1,... </p>

<p>InputFrameOrField = 0, 0, 15, 15, 30, 30,...</p>

<p>InputSurface = T, T, T+7, T+7, T+15, T+15,...  (note that T+7 frame contains 15th field) </p>

<p>The following pseudo-code example shows the interaction between the application (APP) and the driver (DRV) while performing Inverse Telecine (IVTC) on 3:2 pull-down, 30 frames (60 fields) per second interlaced content:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_STREAM_DATA is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563061">DXVAHDDDI_OUTPUT_RATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563081">DXVAHDDDI_STREAM_STATE_FRAME_FORMAT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563092">DXVAHDDDI_STREAM_STATE_OUTPUT_RATE_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563106">DXVAHDDDI_SURFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563109">DXVAHDDDI_VPCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563113">DXVAHDDDI_VPDEVCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-dxvahd-videoprocessblthd.md">VideoProcessBltHD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVAHDDDI_STREAM_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
