---
UID: NS.d3dumddi._DXVADDI_EXTENDEDFORMAT
title: DXVADDI_EXTENDEDFORMAT
author: windows-driver-content
description: The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame.
old-location: display\dxvaddi_extendedformat.htm
old-project: display
ms.assetid: e4f863bd-12ec-489d-a6e0-6b9242fbb0b0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_EXTENDEDFORMAT, DXVADDI_EXTENDEDFORMAT
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
req.alt-api: DXVADDI_EXTENDEDFORMAT
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

# DXVADDI_EXTENDEDFORMAT structure



## -description
<p>The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame. </p>


## -syntax

````
typedef struct _DXVADDI_EXTENDEDFORMAT {
  union {
    struct {
      UINT SampleFormat  :8;
      UINT VideoChromaSubsampling  :4;
      UINT NominalRange  :3;
      UINT VideoTransferMatrix  :3;
      UINT VideoLighting  :4;
      UINT VideoPrimaries  :5;
      UINT VideoTransferFunction  :5;
    };
    UINT   Value;
  };
} DXVADDI_EXTENDEDFORMAT;
````


## -struct-fields
<dl>

### -field <b>SampleFormat</b>

<dd>
<p>[in] A UINT value that specifies how a video frame is sampled. The eight bits are defined by one of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-sampleformat.md">DXVADDI_SAMPLEFORMAT</a> enumeration type.</p>
</dd>

### -field <b>VideoChromaSubsampling</b>

<dd>
<p>[in] The chroma encoding scheme for Y'Cb'Cr' data. The four bits are defined by a bitwise OR of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-videochromasubsampling.md">DXVADDI_VIDEOCHROMASUBSAMPLING</a> enumeration type. </p>
</dd>

### -field <b>NominalRange</b>

<dd>
<p>[in] A UINT value that specifies whether sample data includes headroom (that is, values beyond 1.0 white) and toeroom (that is, superblacks below the reference 0.0 black). The three bits are defined by one of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-nominalrange.md">DXVADDI_NOMINALRANGE</a> enumeration type. </p>
</dd>

### -field <b>VideoTransferMatrix</b>

<dd>
<p>[in] The conversion matrix from Y'Cb'Cr' to (studio) R'G'B'. The three bits are defined by one of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-videotransfermatrix.md">DXVADDI_VIDEOTRANSFERMATRIX</a> enumeration type. </p>
</dd>

### -field <b>VideoLighting</b>

<dd>
<p>[in] Lighting conditions for viewing video. The four bits are defined by one of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-videolighting.md">DXVADDI_VIDEOLIGHTING</a> enumeration type. </p>
</dd>

### -field <b>VideoPrimaries</b>

<dd>
<p>[in] Color primaries, which state which RGB basis functions are used. The five bits are defined by one of the values in the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-videoprimaries.md">DXVADDI_VIDEOPRIMARIES</a> enumeration type. </p>
</dd>

### -field <b>VideoTransferFunction</b>

<dd>
<p>[in] The conversion function from R'G'B' to RGB. The five bits are defined by the <a href="..\d3dumddi\ne-d3dumddi--dxvaddi-videotransferfunction.md">DXVADDI_VIDEOTRANSFERFUNCTION</a> enumeration type. </p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that describes the extended format of the video frame.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-videodesc.md">DXVADDI_VIDEODESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_EXTENDEDFORMAT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
