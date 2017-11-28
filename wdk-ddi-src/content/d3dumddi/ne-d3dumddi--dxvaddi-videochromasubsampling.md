---
UID: NE.d3dumddi._DXVADDI_VIDEOCHROMASUBSAMPLING
title: DXVADDI_VIDEOCHROMASUBSAMPLING
author: windows-driver-content
description: The DXVADDI_VIDEOCHROMASUBSAMPLING enumeration type contains values that identify the chroma encoding scheme for Y'Cb'Cr' data.
old-location: display\dxvaddi_videochromasubsampling.htm
old-project: display
ms.assetid: 697b6ac2-9d25-42ad-aac5-44754f19bf2c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOCHROMASUBSAMPLING
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

# DXVADDI_VIDEOCHROMASUBSAMPLING enumeration



## -description
<p>The DXVADDI_VIDEOCHROMASUBSAMPLING enumeration type contains values that identify the chroma encoding scheme for Y'Cb'Cr' data. </p>


## -syntax

````
typedef enum _DXVADDI_VIDEOCHROMASUBSAMPLING { 
  DXVADDI_VideoChromaSubsamplingMask                             = 0x0F,
  DXVADDI_VideoChromaSubsampling_Unknown                         = 0,
  DXVADDI_VideoChromaSubsampling_ProgressiveChroma               = 0x8,
  DXVADDI_VideoChromaSubsampling_Horizontally_Cosited            = 0x4,
  DXVADDI_VideoChromaSubsampling_Vertically_Cosited              = 0x2,
  DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes  = 0x1,
  DXVADDI_VideoChromaSubsampling_MPEG2                           = DXVADDI_VideoChromaSubsampling_Horizontally_Cosited | DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes,
  DXVADDI_VideoChromaSubsampling_MPEG1                           = DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes,
  DXVADDI_VideoChromaSubsampling_DV_PAL                          = DXVADDI_VideoChromaSubsampling_Horizontally_Cosited | DXVADDI_VideoChromaSubsampling_Vertically_Cosited,
  DXVADDI_VideoChromaSubsampling_Cosited                         = DXVADDI_VideoChromaSubsampling_Horizontally_Cosited | DXVADDI_VideoChromaSubsampling_Vertically_Cosited | DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes
} DXVADDI_VIDEOCHROMASUBSAMPLING;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_VideoChromaSubsamplingMask"></a><a id="dxvaddi_videochromasubsamplingmask"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLINGMASK"></a><b>DXVADDI_VideoChromaSubsamplingMask</b>

<dd>
<p>The video chroma subsampling mask. The first four (0x0F) bits of a DWORD can be used to specify video chroma subsampling.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_Unknown"></a><a id="dxvaddi_videochromasubsampling_unknown"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_UNKNOWN"></a><b>DXVADDI_VideoChromaSubsampling_Unknown</b>

<dd>
<p>The video chroma subsampling is not specified.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_ProgressiveChroma"></a><a id="dxvaddi_videochromasubsampling_progressivechroma"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_PROGRESSIVECHROMA"></a><b>DXVADDI_VideoChromaSubsampling_ProgressiveChroma</b>

<dd>
<p>The video chroma subsampling is progressive.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_Horizontally_Cosited"></a><a id="dxvaddi_videochromasubsampling_horizontally_cosited"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_HORIZONTALLY_COSITED"></a><b>DXVADDI_VideoChromaSubsampling_Horizontally_Cosited</b>

<dd>
<p>Chroma samples are aligned on multiples of the luma samples horizontally.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_Vertically_Cosited"></a><a id="dxvaddi_videochromasubsampling_vertically_cosited"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_VERTICALLY_COSITED"></a><b>DXVADDI_VideoChromaSubsampling_Vertically_Cosited</b>

<dd>
<p>Chroma samples are aligned on multiples of the luma samples vertically.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes"></a><a id="dxvaddi_videochromasubsampling_vertically_alignedchromaplanes"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_VERTICALLY_ALIGNEDCHROMAPLANES"></a><b>DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes</b>

<dd>
<p>The Pb and Pr (or Cb and Cr) planes have the same phase alignment. This value can be set only to 0 in the <b>VideoChromaSubsampling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure if the data is vertically cosited.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_MPEG2"></a><a id="dxvaddi_videochromasubsampling_mpeg2"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_MPEG2"></a><b>DXVADDI_VideoChromaSubsampling_MPEG2</b>

<dd>
<p>A bitwise OR of the <b>DXVADDI_VideoChromaSubsampling_Horizontally_Cosited</b> and <b>DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes</b> values that are used with 4:2:0 data.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_MPEG1"></a><a id="dxvaddi_videochromasubsampling_mpeg1"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_MPEG1"></a><b>DXVADDI_VideoChromaSubsampling_MPEG1</b>

<dd>
<p>The <b>DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes</b> value that is used with 4:2:0 data.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_DV_PAL"></a><a id="dxvaddi_videochromasubsampling_dv_pal"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_DV_PAL"></a><b>DXVADDI_VideoChromaSubsampling_DV_PAL</b>

<dd>
<p>A bitwise OR of the <b>DXVADDI_VideoChromaSubsampling_Horizontally_Cosited</b> and <b>DXVADDI_VideoChromaSubsampling_Vertically_Cosited</b> values that are used with 4:2:0 data.</p>
</dd>

### -field <a id="DXVADDI_VideoChromaSubsampling_Cosited"></a><a id="dxvaddi_videochromasubsampling_cosited"></a><a id="DXVADDI_VIDEOCHROMASUBSAMPLING_COSITED"></a><b>DXVADDI_VideoChromaSubsampling_Cosited</b>

<dd>
<p>A bitwise OR of the <b>DXVADDI_VideoChromaSubsampling_Horizontally_Cosited</b>, and <b>DXVADDI_VideoChromaSubsampling_Vertically_Cosited</b>, and <b>DXVADDI_VideoChromaSubsampling_Vertically_AlignedChromaPlanes</b> values that are used with 4:4:4, 4:2:2, and 4:1:1 data.</p>
</dd>
</dl>

## -remarks
<p>A bitwise OR of the values of DXVADDI_VIDEOCHROMASUBSAMPLING can be used to create a value in the <b>VideoChromaSubsampling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Cosite variations indicate that the chroma samples are aligned with the luma samples. Typically, 4:2:0 data with chroma is aligned in one or more directions with the luma data. Note that 4:4:4, 4:2:2, and 4:1:1 data are always cosited in both directions. </p>

<p>A bitwise OR of the values of DXVADDI_VIDEOCHROMASUBSAMPLING can be used to create a value in the <b>VideoChromaSubsampling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Cosite variations indicate that the chroma samples are aligned with the luma samples. Typically, 4:2:0 data with chroma is aligned in one or more directions with the luma data. Note that 4:4:4, 4:2:2, and 4:1:1 data are always cosited in both directions. </p>

<p>A bitwise OR of the values of DXVADDI_VIDEOCHROMASUBSAMPLING can be used to create a value in the <b>VideoChromaSubsampling</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Cosite variations indicate that the chroma samples are aligned with the luma samples. Typically, 4:2:0 data with chroma is aligned in one or more directions with the luma data. Note that 4:4:4, 4:2:2, and 4:1:1 data are always cosited in both directions. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOCHROMASUBSAMPLING enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
