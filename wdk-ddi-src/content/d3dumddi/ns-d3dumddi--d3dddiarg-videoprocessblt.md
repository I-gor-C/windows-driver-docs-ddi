---
UID: NS.d3dumddi._D3DDDIARG_VIDEOPROCESSBLT
title: D3DDDIARG_VIDEOPROCESSBLT
author: windows-driver-content
description: The D3DDDIARG_VIDEOPROCESSBLT structure describes a Microsoft DirectX Video Acceleration (VA) video processing operation to perform.
old-location: display\d3dddiarg_videoprocessblt.htm
old-project: display
ms.assetid: 24e4115f-cd21-46e7-aacc-9b66e7513b9e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_VIDEOPROCESSBLT, D3DDDIARG_VIDEOPROCESSBLT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_VIDEOPROCESSBLT
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

# D3DDDIARG_VIDEOPROCESSBLT structure



## -description
<p>The D3DDDIARG_VIDEOPROCESSBLT structure describes a Microsoft DirectX Video Acceleration (VA) video processing operation to perform.</p>


## -syntax

````
typedef struct _D3DDDIARG_VIDEOPROCESSBLT {
  REFERENCE_TIME               TargetFrame;
  HANDLE                       hVideoProcess;
  RECT                         TargetRect;
  SIZE                         ConstrictionSize;
  UINT                         StreamingFlags;
  DXVADDI_AYUVSAMPLE16         BackgroundColor;
  DXVADDI_EXTENDEDFORMAT       DestFormat;
  DXVADDI_VIDEOPROCESSBLTFLAGS DestFlags;
  DXVADDI_PROCAMPVALUES        ProcAmpValues;
  DXVADDI_FIXED32              Alpha;
  DXVADDI_FILTERVALUES         NoiseFilterLuma;
  DXVADDI_FILTERVALUES         NoiseFilterChroma;
  DXVADDI_FILTERVALUES         DetailFilterLuma;
  DXVADDI_FILTERVALUES         DetailFilterChroma;
  DXVADDI_VIDEOSAMPLE          *pSrcSurfaces;
  UINT                         NumSrcSurfaces;
} D3DDDIARG_VIDEOPROCESSBLT;
````


## -struct-fields
<dl>

### -field TargetFrame

<dd>
<p>[in] A REFERENCE_TIME value that identifies the location of the output frame within the sequence of input frames. If only deinterlacing is performed, the target time should coincide with either the starting display time of a sample, as defined by the <b>Start</b> member in the <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videosample.md">DXVADDI_VIDEOSAMPLE</a> structure, or the midpoint between the starting display time and the ending display time. </p>
<p>If a frame rate conversion is requested, the time in <b>TargetFrame</b> can be different from any of the times in the <b>Start</b> members of the samples.</p>
</dd>

### -field hVideoProcess

<dd>
<p>[in] A handle to the DirectX VA video processing device. The user-mode display driver returns this handle in a call to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md">CreateVideoProcessDevice</a> function.</p>
</dd>

### -field TargetRect

<dd>
<p>[in] A pointer to a <a href="display.rect">RECT</a> structure that describes the location within the destination surface to which the output image is written. Note that the output image is restricted to the pixels within the rectangle that is pointed to by <b>TargetRect</b>. That is, every pixel within this rectangle must be written to; pixels outside this rectangle must not be modified. </p>
</dd>

### -field ConstrictionSize

<dd>
<p>[in] A <a href="display.size">SIZE</a> structure that specifies, for protected content, the size to reduce the output image to. <b>ConstrictionSize</b> should be from (1, 1) to (width, height) of the target rectangle that is specified in the <b>TargetRect</b> member. <b>ConstrictionSize</b> should be (0, 0) to represent no constriction.</p>
<p>For example, consider video that natively has 1920 x 1080 pixels and that is displayed full screen on a 1920 x 1080-resolution monitor for which output protection is unsupported. If the video content specifies a rule that only 854 x 480 pixels of original information can be displayed, the driver must reduce the original image from 1920 x 1080 to 854 x 480 and then stretch the image again to 1920 x 1080. In this example, the SIZE structure in the <b>ConstrictionSize</b> member would specify a size of 854 x 480 pixels.</p>
</dd>

### -field StreamingFlags

<dd>
<p>[in] A UINT value that identifies streaming flags. Currently, no streaming flags are defined.</p>
</dd>

### -field BackgroundColor

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-ayuvsample16.md">DXVADDI_AYUVSAMPLE16</a> structure that identifies background color. </p>
</dd>

### -field DestFormat

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-extendedformat.md">DXVADDI_EXTENDEDFORMAT</a> structure that identifies extended format information for the destination surface. </p>
</dd>

### -field DestFlags

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessbltflags.md">DXVADDI_VIDEOPROCESSBLTFLAGS</a> structure that identifies changes in the current destination surface from the previous destination surface.</p>
</dd>

### -field ProcAmpValues

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-procampvalues.md">DXVADDI_PROCAMPVALUES</a> structure that specifies ProcAmp adjustment data that is output to the destination surface.</p>
</dd>

### -field Alpha

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-fixed32.md">DXVADDI_FIXED32</a> structure that specifies the planar-transparency value of the output image as it is written to the destination surface. When the alpha value is 1.0, the background color is drawn opaque (without transparency and alpha blending). When the alpha value is 0.0, the background should not be drawn (transparent).</p>
</dd>

### -field NoiseFilterLuma

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-filtervalues.md">DXVADDI_FILTERVALUES</a> structure that specifies the luma noise filter.</p>
</dd>

### -field NoiseFilterChroma

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-filtervalues.md">DXVADDI_FILTERVALUES</a> structure that specifies the chroma noise filter.</p>
</dd>

### -field DetailFilterLuma

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-filtervalues.md">DXVADDI_FILTERVALUES</a> structure that specifies the luma detail filter.</p>
</dd>

### -field DetailFilterChroma

<dd>
<p>[in] A <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-filtervalues.md">DXVADDI_FILTERVALUES</a> structure that specifies the chroma detail filter.</p>
</dd>

### -field pSrcSurfaces

<dd>
<p>[in] An array of <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videosample.md">DXVADDI_VIDEOSAMPLE</a> structures that describe the input samples that are required for the deinterlacing, frame-rate conversion, and substream compositing operations. For more information about how input samples are arranged in this array, see <a href="https://msdn.microsoft.com/99110b1a-1511-44f5-a4bb-a5e38fd41fff">Input Buffer Order</a>.</p>
</dd>

### -field NumSrcSurfaces

<dd>
<p>[in] The number of input samples in the array at <b>pSrcSurfaces</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md">CreateVideoProcessDevice</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-ayuvsample8.md">DXVADDI_AYUVSAMPLE8</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-extendedformat.md">DXVADDI_EXTENDEDFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-procampvalues.md">DXVADDI_PROCAMPVALUES</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessbltflags.md">DXVADDI_VIDEOPROCESSBLTFLAGS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videosample.md">DXVADDI_VIDEOSAMPLE</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessblt.md">VideoProcessBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_VIDEOPROCESSBLT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
