---
UID: NE.dxva._DXVA_VideoProcessCaps
title: DXVA_VideoProcessCaps
author: windows-driver-content
description: The DXVA_VideoProcessCaps enumeration identifies operations that can be performed concurrently with the requested deinterlace.
old-location: display\dxva_videoprocesscaps.htm
old-project: display
ms.assetid: 225da110-cd59-4803-bde8-26e275b3ddbd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_GAMMA_CONTROL_CAPABILITIES, DXGI_GAMMA_CONTROL_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_VideoProcessCaps
req.alt-loc: dxva.h
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

# DXVA_VideoProcessCaps enumeration



## -description
<p>The DXVA_VideoProcessCaps enumeration identifies operations that can be performed concurrently with the requested deinterlace. </p>


## -syntax

````
typedef enum _DXVA_VideoProcessCaps { 
  DXVA_VideoProcess_None                = 0x0000,
  DXVA_VideoProcess_YUV2RGB             = 0x0001,
  DXVA_VideoProcess_StretchX            = 0x0002,
  DXVA_VideoProcess_StretchY            = 0x0004,
  DXVA_VideoProcess_AlphaBlend          = 0x0008,
  DXVA_VideoProcess_SubRects            = 0x0010,
  DXVA_VideoProcess_SubStreams          = 0x0020,
  DXVA_VideoProcess_SubStreamsExtended  = 0x0040,
  DXVA_VideoProcess_YUV2RGBExtended     = 0x0080,
  DXVA_VideoProcess_AlphaBlendExtended  = 0x0100
} DXVA_VideoProcessCaps;
````


## -enum-fields
<dl>

### -field <a id="DXVA_VideoProcess_None"></a><a id="dxva_videoprocess_none"></a><a id="DXVA_VIDEOPROCESS_NONE"></a><b>DXVA_VideoProcess_None</b>

<dd>
<p>Indicates that the deinterlace hardware can only perform basic deinterlace operations. That is, deinterlace operations that are not combined with other operations, like-color conversion, alpha blend, stretch, subsection, or substream. </p>
</dd>

### -field <a id="DXVA_VideoProcess_YUV2RGB"></a><a id="dxva_videoprocess_yuv2rgb"></a><a id="DXVA_VIDEOPROCESS_YUV2RGB"></a><b>DXVA_VideoProcess_YUV2RGB</b>

<dd>
<p>Indicates that the deinterlace hardware can convert video from the YUV color space to the RGB color space. The RGB format will have at least 8 bits of precision for each color component. If possible, a buffer copy within the VMR can be avoided. All drivers should be able to support this operation for the bob deinterlace mode. 
</p>
<p>Not used with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.</p>
</dd>

### -field <a id="DXVA_VideoProcess_StretchX"></a><a id="dxva_videoprocess_stretchx"></a><a id="DXVA_VIDEOPROCESS_STRETCHX"></a><b>DXVA_VideoProcess_StretchX</b>

<dd>
<p>Indicates that aspect ratio correction can be performed simultaneously as the video is being deinterlaced if the deinterlacer is able to stretch or shrink horizontally. The enumerator should be supported for the bob deinterlace mode.</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.
</p>
</dd>

### -field <a id="DXVA_VideoProcess_StretchY"></a><a id="dxva_videoprocess_stretchy"></a><a id="DXVA_VIDEOPROCESS_STRETCHY"></a><b>DXVA_VideoProcess_StretchY</b>

<dd>
<p>Indicates that aspect ratio adjustment is combined with a general picture resizing operation to scale the video image.</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.
</p>
</dd>

### -field <a id="DXVA_VideoProcess_AlphaBlend"></a><a id="dxva_videoprocess_alphablend"></a><a id="DXVA_VIDEOPROCESS_ALPHABLEND"></a><b>DXVA_VideoProcess_AlphaBlend</b>

<dd>
<p>Indicates that the VMR will not perform a buffer copy when an alpha value is changed. It is rare that applications alter the constant alpha value associated with the video stream, so this is a low priority feature. The enumerator should be supported for the bob deinterlace mode.
</p>
<p>Not used with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.
</p>
</dd>

### -field <a id="DXVA_VideoProcess_SubRects"></a><a id="dxva_videoprocess_subrects"></a><a id="DXVA_VIDEOPROCESS_SUBRECTS"></a><b>DXVA_VideoProcess_SubRects</b>

<dd>
<p>Indicates that the deinterlace hardware can deinterlace just a subrectangle region of the video image to the specified destination position. This is useful if the video image must be cropped before being processed further as the size of the output frame is reduced. </p>
</dd>

### -field <a id="DXVA_VideoProcess_SubStreams"></a><a id="dxva_videoprocess_substreams"></a><a id="DXVA_VIDEOPROCESS_SUBSTREAMS"></a><b>DXVA_VideoProcess_SubStreams</b>

<dd>
<p>Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.
</p>
<p>Indicates that the deinterlace hardware can combine video substreams with the video stream.
</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.</p>
</dd>

### -field <a id="DXVA_VideoProcess_SubStreamsExtended"></a><a id="dxva_videoprocess_substreamsextended"></a><a id="DXVA_VIDEOPROCESS_SUBSTREAMSEXTENDED"></a><b>DXVA_VideoProcess_SubStreamsExtended</b>

<dd>
<p>Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.
</p>
<p>Indicates that necessary color adjustments can be made to the source video streams and substreams. These adjustments are indicated in the extended color data, as the video is deinterlaced, composited with the substreams, and written to the destination surface.</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.</p>
</dd>

### -field <a id="DXVA_VideoProcess_YUV2RGBExtended"></a><a id="dxva_videoprocess_yuv2rgbextended"></a><a id="DXVA_VIDEOPROCESS_YUV2RGBEXTENDED"></a><b>DXVA_VideoProcess_YUV2RGBExtended</b>

<dd>
<p>Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.
</p>
<p>Indicates a color-space-conversion operation can be performed as the deinterlaced and composited pixels are written to the destination surface using the extended color information that is specified for the source and destination surfaces.
</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.</p>
</dd>

### -field <a id="DXVA_VideoProcess_AlphaBlendExtended"></a><a id="dxva_videoprocess_alphablendextended"></a><a id="DXVA_VIDEOPROCESS_ALPHABLENDEXTENDED"></a><b>DXVA_VideoProcess_AlphaBlendExtended</b>

<dd>
<p>Windows Server 2003 SP1 and later and Windows XP SP2 and later versions only.
</p>
<p>Indicates that an alpha-blend operation can be performed with the destination surface when the deinterlaced and composited pixels are written to the destination surface. The driver must handle background color based on the alpha value of the <b>Alpha</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563915">DXVA_DeinterlaceBltEx</a> structure. When the alpha value is 1.0f, the background color is drawn opaque (without transparency). When the alpha value is 0.0f, the background should not be drawn (transparent).</p>
<p>Must use with the <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> function.
</p>
</dd>
</dl>

## -remarks
<p>Occasionally, the aspect ratio adjustment performed by <b>DXVA_VideoProcess_AlphaBlend</b> is combined with a general picture resizing operation to scale the video image within an application-defined composition space, which is rare and not an essential feature. It is best if the scaling needed for resizing the video to fit into the application window can be done simultaneously to the scaling needed for deinterlacing, which avoids cumulative artifacts. </p>

<p>Color space conversion performed by <b>DXVA_VideoProcess_YUV2RGB</b> is particularly useful within the VMR if it is combined with any (and ideally, all) of the following enumerators: <b>DXVA_VideoProcess_StretchX</b>, <b>DXVA_VideoProcess_StretchY</b>, and <b>DXVA_VideoProcess_AlphaBlend</b>. There is no requirement to convert from the RGB color space to the YUV color space.</p>

<p>Occasionally, the aspect ratio adjustment performed by <b>DXVA_VideoProcess_AlphaBlend</b> is combined with a general picture resizing operation to scale the video image within an application-defined composition space, which is rare and not an essential feature. It is best if the scaling needed for resizing the video to fit into the application window can be done simultaneously to the scaling needed for deinterlacing, which avoids cumulative artifacts. </p>

<p>Color space conversion performed by <b>DXVA_VideoProcess_YUV2RGB</b> is particularly useful within the VMR if it is combined with any (and ideally, all) of the following enumerators: <b>DXVA_VideoProcess_StretchX</b>, <b>DXVA_VideoProcess_StretchY</b>, and <b>DXVA_VideoProcess_AlphaBlend</b>. There is no requirement to convert from the RGB color space to the YUV color space.</p>

<p>Occasionally, the aspect ratio adjustment performed by <b>DXVA_VideoProcess_AlphaBlend</b> is combined with a general picture resizing operation to scale the video image within an application-defined composition space, which is rare and not an essential feature. It is best if the scaling needed for resizing the video to fit into the application window can be done simultaneously to the scaling needed for deinterlacing, which avoids cumulative artifacts. </p>

<p>Color space conversion performed by <b>DXVA_VideoProcess_YUV2RGB</b> is particularly useful within the VMR if it is combined with any (and ideally, all) of the following enumerators: <b>DXVA_VideoProcess_StretchX</b>, <b>DXVA_VideoProcess_StretchY</b>, and <b>DXVA_VideoProcess_AlphaBlend</b>. There is no requirement to convert from the RGB color space to the YUV color space.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563939">DXVA_DeinterlaceCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_VideoProcessCaps enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
