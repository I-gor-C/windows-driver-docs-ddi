---
UID: NS.dxva._DXVA_DeinterlaceBlt
title: DXVA_DeinterlaceBlt
author: windows-driver-content
description: The DXVA_DeinterlaceBlt structure is sent by the VMR to the accelerator to specify the deinterlace or frame-rate conversion parameters for bit-block transfers.
old-location: display\dxva_deinterlaceblt.htm
old-project: display
ms.assetid: 0512a825-9cec-4ca0-9686-df5b3d2b216b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_DeinterlaceBlt, DXVA_DeinterlaceBlt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_DeinterlaceBlt
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

# DXVA_DeinterlaceBlt structure



## -description
<p>The DXVA_DeinterlaceBlt structure is sent by the VMR to the accelerator to specify the deinterlace or frame-rate conversion parameters for bit-block transfers.</p>


## -syntax

````
typedef struct _DXVA_DeinterlaceBlt {
  DWORD            Size;
  DWORD            Reserved;
  REFERENCE_TIME   rtTarget;
  RECT             DstRect;
  RECT             SrcRect;
  DWORD            NumSourceSurfaces;
  FLOAT            Alpha;
  DXVA_VideoSample Source[MAX_DEINTERLACE_SURFACES];
} DXVA_DeinterlaceBlt;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of this structure in bytes.</p>
</dd>

### -field <b>Reserved</b>

<dd></dd>

### -field <b>rtTarget</b>

<dd>
<p>Identifies the location of the output frame within the sequence of input frames. If only deinterlacing is performed, the target time should coincide with either the starting display time of a reference sample, as defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564085">DXVA_VideoSample</a> structure, or the midpoint between the starting display time and the ending display time. For more information, see Remarks.</p>
<p>If a frame rate conversion is requested, the <b>rtTarget</b> time can be different from any of the <b>rtStart</b> times of the reference samples.</p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that describes the upper left and lower right points of a rectangle on the destination surface. These points define the area in which the bit-block transfer should occur and its position on the destination surface.</p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that describes the upper left and lower right points of a rectangle on the source surface. These points define the area of the source data for the bit-block transfer and its position on the source surface.</p>
</dd>

### -field <b>NumSourceSurfaces</b>

<dd>
<p>Specifies the number of valid surfaces passed in the <b>Source</b> array.</p>
</dd>

### -field <b>Alpha</b>

<dd>
<p>Specifies the transparency of the output image as it is written to the destination surface. A value of  0.0F indicates transparent. A value of 1.0F indicates opaque.</p>
</dd>

### -field <b>Source</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff564085">DXVA_VideoSample</a> structures that specify the reference input samples needed for this deinterlacing or frame-rate conversion operation.</p>
</dd>
</dl>

## -remarks
<p>When creating a single frame from one field in a sample, as defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564085">DXVA_VideoSample</a> structure, <b>rtTarget</b> should be the starting display time for that field. If you have two fields in one sample and want to deinterlace both, <a href="display.dxva_deinterlacebobdeviceclass_deinterlaceblt">DeinterlaceBlt</a> will be called twice. The first time <i>DeinterlaceBlt</i> is called, <b>rtTarget</b> will be the starting display time. The second time <i>DeinterlaceBlt</i> is called, <b>rtTarget</b> will be the midpoint between the starting display time and the ending display time. In other words, for the first call, <b>rtTarget</b> = <b>rtStart</b>. For the second call, <b>rtTarget</b> = (<b>rtStart</b> + <b>rtEnd</b>) / 2.</p>

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
<a href="display.dxva_deinterlacebobdeviceclass_deinterlaceblt">DeinterlaceBlt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564085">DXVA_VideoSample</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563939">DXVA_DeinterlaceCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_DeinterlaceBlt structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
