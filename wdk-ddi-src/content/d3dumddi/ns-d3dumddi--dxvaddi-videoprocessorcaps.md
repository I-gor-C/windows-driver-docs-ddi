---
UID: NS.d3dumddi._DXVADDI_VIDEOPROCESSORCAPS
title: DXVADDI_VIDEOPROCESSORCAPS
author: windows-driver-content
description: The DXVADDI_VIDEOPROCESSORCAPS structure describes the video processing capabilities of a specific deinterlace mode.
old-location: display\dxvaddi_videoprocessorcaps.htm
old-project: display
ms.assetid: bea6d458-943e-466f-adca-466f26dc3599
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_VIDEOPROCESSORCAPS, DXVADDI_VIDEOPROCESSORCAPS
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
req.alt-api: DXVADDI_VIDEOPROCESSORCAPS
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

# DXVADDI_VIDEOPROCESSORCAPS structure



## -description
<p>The DXVADDI_VIDEOPROCESSORCAPS structure describes the video processing capabilities of a specific deinterlace mode.</p>


## -syntax

````
typedef struct _DXVADDI_VIDEOPROCESSORCAPS {
  D3DDDI_POOL  InputPool;
  UINT         NumForwardRefSamples;
  UINT         NumBackwardRefSamples;
  D3DDDIFORMAT OutputFormat;
  UINT         DeinterlaceTechnology;
  UINT         ProcAmpControlCaps;
  UINT         VideoProcessorOperations;
  UINT         NoiseFilterTechnology;
  UINT         DetailFilterTechnology;
} DXVADDI_VIDEOPROCESSORCAPS;
````


## -struct-fields
<dl>

### -field InputPool

<dd>
<p>[out] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-pool.md">D3DDDI_POOL</a>-typed value that indicates the memory pool from which the interlaced source surfaces should be allocated. </p>
</dd>

### -field NumForwardRefSamples

<dd>
<p>[out] The required number of forward reference samples for the defined deinterlace mode. The samples are in subsequent fields. This value is zero for bob and line blending and can be other values (such as 1, 2, or 3) for adaptive deinterlacing and frame-rate conversion.</p>
</dd>

### -field NumBackwardRefSamples

<dd>
<p>[out] The required backward reference samples for the defined deinterlace mode. The samples are in former fields. This value is zero for bob, 1 for line blending and can be other values (such as 1, 2, or 3) for adaptive deinterlacing and frame-rate conversion.</p>
</dd>

### -field OutputFormat

<dd>
<p>[out] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the uncompressed output frames. Typically, a deinterlace algorithm outputs frames in a pixel format that matches the input sample format. This member ensures that the Video Mixing Renderer (VMR) or other video renderer is able to supply the correct output frame surfaces to the deinterlacing hardware.</p>
<p>Note that if the DXVADDI_VIDEOPROCESS_YUV2RGB value is returned in the <b>VideoProcessorOperations</b> member, the VMR determines that valid output formats are specified by this member as well as an D3DFMT_X8R8G8B8 format.</p>
</dd>

### -field DeinterlaceTechnology

<dd>
<p>[out] A bitwise OR of the following values to indicate the underlying deinterlacing technology that is used to implement the deinterlacing algorithm. The values can be combined as required to most closely match the algorithm's implementation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_UNKNOWN</p>
</td>
<td>
<p>The deinterlacing technology is unknown.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_BOBLINEREPLICATE</p>
</td>
<td>
<p>The deinterlace algorithm creates missing lines by repeating the line either above or below a missing line. This method looks jagged and is not recommended.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_BOBVERTICALSTRETCH</p>
</td>
<td>
<p>A deinterlace algorithm that creates missing lines by vertically stretching each video field by a factor of two by averaging two lines. Slight vertical adjustments are made to ensure that the resulting image does not move up and down.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_BOBVERTICALSTRETCH4TAP</p>
</td>
<td>
<p>A deinterlace algorithm that creates missing lines by vertically stretching each video field by a factor of two by using a [-1, 9, 9, -1] / 16 filter across four lines. Slight vertical adjustments are made to ensure that the resulting image does not move up and down.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_MEDIANFILTERING</p>
</td>
<td>
<p>The pixels in the missing line are recreated by a median filtering operation.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_EDGEFILTERING</p>
</td>
<td>
<p>Pixels in the missing line are recreated by an edge filter. In this process, spatial directional filters are applied to determine the orientation of edges in the picture content, and missing pixels are created by filtering along (rather than across) the detected edges.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_FIELDADAPTIVE</p>
</td>
<td>
<p>Pixels in the missing line are recreated by switching on a field-by-field basis between either spatial or temporal interpolation, depending on the amount of motion.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_PIXELADAPTIVE</p>
</td>
<td>
<p>Pixels in the missing line are recreated by switching on a pixel-by-pixel basis between either spatial or temporal interpolation, depending on the amount of motion.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_MOTIONVECTORSTEERED</p>
</td>
<td>
<p>Objects within a sequence of video fields. The missing pixels are recreated after first aligning the movement axis of the individual objects in the scene to make them parallel with the time axis.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DEINTERLACETECH_INVERSETELECINE</p>
</td>
<td>
<p>A deinterlace algorithm that can undo the 3:2 pull-down process that is used for displaying 24Hz-content on 60Hz-displays, 25Hz-content on 50Hz-displays, or so on.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ProcAmpControlCaps

<dd>
<p>[out] A bitwise OR of the following values to indicate the ProcAmp operations that the hardware supports.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXVADDI_PROCAMP_NONE</p>
</td>
<td>
<p>The hardware does not support any ProcAmp operations.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_PROCAMP_BRIGHTNESS</p>
</td>
<td>
<p>Brightness adjustments to the video image are allowed.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_PROCAMP_CONTRAST</p>
</td>
<td>
<p>Contrast adjustments to the video image are allowed.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_PROCAMP_HUE</p>
</td>
<td>
<p>Hue adjustments to the video image are allowed.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_PROCAMP_SATURATION</p>
</td>
<td>
<p>Saturation adjustments to the video image are allowed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field VideoProcessorOperations

<dd>
<p>[out] A bitwise OR of the following values to indicate which additional video processing operations the hardware can perform concurrently with the requested <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-videoprocessblt.md">VideoProcessBlt</a> operation.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_NONE</p>
</td>
<td>
<p>The hardware cannot perform any more video processing operations.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_YUV2RGB</p>
</td>
<td>
<p>Video conversion from the YUV color space to the RGB color space is allowed. The RGB format that is used has at least 8 bits of precision for each color component. If this operation is possible, a buffer copy within the VMR can be avoided. Note that conversion from the RGB color space to the YUV color space is not required.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_STRETCHX</p>
</td>
<td>
<p>Aspect ratio correction can be performed at the same time as the video is ProcAmp-adjusted if the hardware is able to stretch or shrink horizontally.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_STRETCHY</p>
</td>
<td>
<p>Aspect ratio adjustment is combined with a general picture resizing operation to scale the video image within an application-defined composition space. This operation is rare and not an essential feature. It is best if the scaling that is required for resizing the video to fit into the application window can be done at the same time as the scaling required for ProcAmp adjustment. This type of operation avoids cumulative artifacts.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_ALPHABLEND</p>
</td>
<td>
<p>The VMR does not perform a buffer copy when an alpha value is changed. Applications rarely alter the constant alpha value that is associated with the video stream, so this operation is a low priority feature.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_SUBRECTS</p>
</td>
<td>
<p>The video processing device can operate on a subrectangle region of the video image. This operation is useful if the video image must be cropped before being processed further as the size of the output frame is reduced.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_SUBSTREAMS</p>
</td>
<td>
<p>The video processing device can combine video substreams with the video stream.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_SUBSTREAMSEXTENDED</p>
</td>
<td>
<p>Necessary color adjustments can be made to the source video streams and substreams. These adjustments are indicated in the extended color data, as the video is deinterlaced, composited with the substreams, and written to the destination surface.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_YUV2RGBEXTENDED</p>
</td>
<td>
<p>A color-space-conversion operation can be performed as the deinterlaced and composited pixels are written to the destination surface by using the extended color information that is specified for the source and destination surfaces.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_ALPHABLENDEXTENDED</p>
</td>
<td>
<p>An alpha-blend operation can be performed with the destination surface when the deinterlaced and composited pixels are written to the destination surface. The driver must handle background color based on the alpha value of the <b>Alpha</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-videoprocessblt.md">D3DDDIARG_VIDEOPROCESSBLT</a> structure. When the alpha value is 1.0, the background color is drawn opaque (without transparency). When the alpha value is 0.0, the background should not be drawn (transparent).</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_CONSTRICTION</p>
</td>
<td>
<p>The video processing device can temporarily reduce the output frame to a size that the <b>ConstrictionSize</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-videoprocessblt.md">D3DDDIARG_VIDEOPROCESSBLT</a> structure specifies.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_NOISEFILTER</p>
</td>
<td>
<p>The video processing device can perform noise filtering operations on the video stream.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_DETAILFILTER</p>
</td>
<td>
<p>The video processing device can perform detail filtering operations on the video stream.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_PLANARALPHA</p>
</td>
<td>
<p>The video processing device can apply a constant alpha blend to the entire video stream (plane) while it mixes the video stream and substreams together. The <b>Alpha</b> member of D3DDDIARG_VIDEOPROCESSBLT specifies the alpha value.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_LINEARSCALING</p>
</td>
<td>
<p>The video processing device can linearly scale the video stream.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_GAMMACOMPENSATED</p>
</td>
<td>
<p>The video processing device can perform gamma conversion on the video stream.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_VIDEOPROCESS_MAINTAINSORIGINALFIELDDATA</p>
</td>
<td>
<p>The video processing device can maintain the original field data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field NoiseFilterTechnology

<dd>
<p>[out] A bitwise OR of the following values to indicate the underlying technology that is used to implement noise filtering. The values can be combined as required to most closely match the noise-filter implementation. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_UNSUPPORTED</p>
</td>
<td>
<p>No noise-filter technology is supported.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_UNKNOWN</p>
</td>
<td>
<p>The noise-filter technology is unknown.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_MEDIAN</p>
</td>
<td>
<p>The video processing device uses median noise filtering.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_TEMPORAL</p>
</td>
<td>
<p>The video processing device uses temporal noise filtering.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_BLOCKNOISE</p>
</td>
<td>
<p>The video processing device uses block noise filtering.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_NOISEFILTERTECH_MOSQUITONOISE</p>
</td>
<td>
<p>The video processing device uses mosquito noise filtering.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field DetailFilterTechnology

<dd>
<p>[out] A bitwise OR of the following values to indicate the underlying technology that is used to implement detail filtering. The values can be combined as required to most closely match the detail-filter implementation.  </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXVADDI_DETAILFILTERTECH_UNSUPPORTED</p>
</td>
<td>
<p>No detail-filter technology is supported.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DETAILFILTERTECH_UNKNOWN</p>
</td>
<td>
<p>The detail-filter technology is unknown.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DETAILFILTERTECH_EDGE</p>
</td>
<td>
<p>The video processing device uses edge detail filtering.</p>
</td>
</tr>
<tr>
<td>
<p>DXVADDI_DETAILFILTERTECH_SHARPENING</p>
</td>
<td>
<p>The video processing device uses sharpening detail filtering.</p>
</td>
</tr>
</table>
<p> </p>
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
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-pool.md">D3DDDI_POOL</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi--d3dddicaps-type.md">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-videoprocessblt.md">D3DDDIARG_VIDEOPROCESSBLT</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videoprocessorinput.md">DXVADDI_VIDEOPROCESSORINPUT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getcaps.md">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOPROCESSORCAPS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
