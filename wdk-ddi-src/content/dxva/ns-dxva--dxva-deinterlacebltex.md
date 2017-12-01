---
UID: NS.dxva._DXVA_DeinterlaceBltEx
title: DXVA_DeinterlaceBltEx
author: windows-driver-content
description: The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate-converted video with any supplied video substreams, and for writing the combined output to a destination surface.
old-location: display\dxva_deinterlacebltex.htm
old-project: display
ms.assetid: dbc32410-119f-4172-8d2a-7d41e8b64ae4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_DeinterlaceBltEx, DXVA_DeinterlaceBltEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_DeinterlaceBltEx
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

# DXVA_DeinterlaceBltEx structure



## -description
<p>The DXVA_DeinterlaceBltEx structure describes parameters for deinterlace or frame-rate conversion, for combining the deinterlaced or frame-rate-converted video with any supplied video substreams, and for writing the combined output to a destination surface. </p>


## -syntax

````
typedef struct _DXVA_DeinterlaceBltEx {
  DWORD             Size;
  DXVA_AYUVsample2  BackgroundColor;
  RECT              rcTarget;
  REFERENCE_TIME    rtTarget;
  DWORD             NumSourceSurfaces;
  FLOAT             Alpha;
  DXVA_VideoSample2 Source[MAX_DEINTERLACE_SURFACES];
  DWORD             DestinationFormat;
  DWORD             DestinationFlags;
} DXVA_DeinterlaceBltEx;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of the structure, in bytes.</p>
</dd>

### -field <b>BackgroundColor</b>

<dd>
<p>Specifies a <a href="..\dxva\ns-dxva--dxva-ayuvsample2.md">DXVA_AYUVsample2</a> structure that identifies background color and opacity level. For Windows Server 2003 with SP1 and Windows XP with SP2, the opacity level is not used and should be ignored by the driver.</p>
</dd>

### -field <b>rcTarget</b>

<dd>
<p>Specifies a pointer to a <a href="display.rect">RECT</a> structure that describes the location within the destination surface to which the output image is written. Note that the output image is restricted to the pixels within the <b>rcTarget</b> rectangle--that is, every pixel within this rectangle must be written to; pixels outside this rectangle must not be modified. </p>
</dd>

### -field <b>rtTarget</b>

<dd>
<p>Identifies the location of the output frame within the sequence of input frames. If only deinterlacing is performed, the target time should coincide with either the starting display time of a sample, as defined in the <a href="..\dxva\ns-dxva--dxva-videosample2.md">DXVA_VideoSample2</a> structure, or the midpoint between the starting display time and the ending display time. For more information, see Remarks.</p>
<p>If a frame-rate conversion is requested, the <b>rtTarget</b> time can be different from any of the <b>rtStart</b> times of the samples.</p>
</dd>

### -field <b>NumSourceSurfaces</b>

<dd>
<p>Specifies the number of valid surfaces passed in the <b>Source</b> array.</p>
</dd>

### -field <b>Alpha</b>

<dd>
<p>Specifies the planar-transparency value of the output image as it is written to the destination surface. For Windows Server 2003 with SP1 and Windows XP with SP2, this value is always 1.0F, which indicates that the overall image is opaque and that no alpha blending on the overall image is required.</p>
</dd>

### -field <b>Source</b>

<dd>
<p>Specifies an array of DXVA_VideoSample2 structures that describe the input samples that are required for the deinterlacing, frame-rate conversion, and substream-compositing operations. For information about how input samples are arranged in this array, see <a href="https://msdn.microsoft.com/99110b1a-1511-44f5-a4bb-a5e38fd41fff">Input Buffer Order</a>.</p>
</dd>

### -field <b>DestinationFormat</b>

<dd>
<p>Specifies format information for the destination surface. For Windows Server 2003 with SP1 and Windows XP with SP2, this member is set to 0.</p>
</dd>

### -field <b>DestinationFlags</b>

<dd>
<p>Specifies a collection of flags that indicate changes in the current destination surface from the previous destination surface. This member is a bitwise-OR of one or more of the flags in the <a href="..\dxva\ne-dxva--dxva-destinationflags.md">DXVA_DestinationFlags</a> enumeration type.</p>
</dd>
</dl>

## -remarks
<p>The render sends the DXVA_DeinterlaceBltEx structure to the accelerator to specify the deinterlace or frame-rate conversion parameters for bit-block transfers. </p>

<p>When a single frame is being created from one field in a sample, as defined in the <a href="..\dxva\ns-dxva--dxva-videosample2.md">DXVA_VideoSample2</a> structure, <b>rtTarget</b> should be the starting display time for that field. If you have two fields in one sample and want to deinterlace both, <a href="display.dxva_deinterlacebobdeviceclass_deinterlacebltex">DeinterlaceBltEx</a> will be called twice. The first time <i>DeinterlaceBltEx</i> is called, <b>rtTarget</b> will be the starting display time. The second time <i>DeinterlaceBltEx</i> is called, <b>rtTarget</b> will be the midpoint between the starting display time and the ending display time. In other words, for the first call, <b>rtTarget</b> = <b>rtStart</b>. For the second call, <b>rtTarget</b> = (<b>rtStart</b> + <b>rtEnd</b>) / 2.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
</td>
</tr>
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
<a href="..\dxva\ns-dxva--dxva-deinterlacecaps.md">DXVA_DeinterlaceCaps</a>
</dt>
<dt>
<a href="..\dxva\ne-dxva--dxva-destinationflags.md">DXVA_DestinationFlags</a>
</dt>
<dt>
<a href="..\dxva\ns-dxva--dxva-videosample2.md">DXVA_VideoSample2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_DeinterlaceBltEx structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
