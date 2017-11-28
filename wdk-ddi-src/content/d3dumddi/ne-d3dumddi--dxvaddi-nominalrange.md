---
UID: NE.d3dumddi._DXVADDI_NOMINALRANGE
title: DXVADDI_NOMINALRANGE
author: windows-driver-content
description: The DXVADDI_NOMINALRANGE enumeration type contains values that identify whether sample data includes headroom (that is, values beyond 1.0 white) and toeroom (that is, superblacks below the reference 0.0 black).
old-location: display\dxvaddi_nominalrange.htm
old-project: display
ms.assetid: f3f5fac9-013c-4739-a29e-c781b34e5289
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
req.alt-api: DXVADDI_NOMINALRANGE
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

# DXVADDI_NOMINALRANGE enumeration



## -description
<p>The DXVADDI_NOMINALRANGE enumeration type contains values that identify whether sample data includes headroom (that is, values beyond 1.0 white) and toeroom (that is, superblacks below the reference 0.0 black). </p>


## -syntax

````
typedef enum _DXVADDI_NOMINALRANGE { 
  DXVADDI_NominalRangeMask      = 0x07,
  DXVADDI_NominalRange_Unknown  = 0,
  DXVADDI_NominalRange_Normal   = 1,
  DXVADDI_NominalRange_Wide     = 2,
  DXVADDI_NominalRange_0_255    = 1,
  DXVADDI_NominalRange_16_235   = 2,
  DXVADDI_NominalRange_48_208   = 3
} DXVADDI_NOMINALRANGE;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_NominalRangeMask"></a><a id="dxvaddi_nominalrangemask"></a><a id="DXVADDI_NOMINALRANGEMASK"></a><b>DXVADDI_NominalRangeMask</b>

<dd>
<p>The nominal range mask. The first 3 (0x07) bits of a DWORD can be used to specify nominal range.</p>
</dd>

### -field <a id="DXVADDI_NominalRange_Unknown"></a><a id="dxvaddi_nominalrange_unknown"></a><a id="DXVADDI_NOMINALRANGE_UNKNOWN"></a><b>DXVADDI_NominalRange_Unknown</b>

<dd>
<p>The nominal range is not specified.</p>
</dd>

### -field <a id="DXVADDI_NominalRange_Normal"></a><a id="dxvaddi_nominalrange_normal"></a><a id="DXVADDI_NOMINALRANGE_NORMAL"></a><b>DXVADDI_NominalRange_Normal</b>

<dd>
<p>Normalized chroma [0..1] maps to [0..255] (8bit) or [0..1023] (10 bit).</p>
</dd>

### -field <a id="DXVADDI_NominalRange_Wide"></a><a id="dxvaddi_nominalrange_wide"></a><a id="DXVADDI_NOMINALRANGE_WIDE"></a><b>DXVADDI_NominalRange_Wide</b>

<dd>
<p>Normalized chroma [0..1] maps to [16..235] (8bit) or [64..940] (10 bit).</p>
</dd>

### -field <a id="DXVADDI_NominalRange_0_255"></a><a id="dxvaddi_nominalrange_0_255"></a><a id="DXVADDI_NOMINALRANGE_0_255"></a><b>DXVADDI_NominalRange_0_255</b>

<dd>
<p>Normalized chroma [0..1] maps explicitly to [0..255] (8bit).</p>
</dd>

### -field <a id="DXVADDI_NominalRange_16_235"></a><a id="dxvaddi_nominalrange_16_235"></a><a id="DXVADDI_NOMINALRANGE_16_235"></a><b>DXVADDI_NominalRange_16_235</b>

<dd>
<p>Normalized chroma [0..1] maps explicitly to [16..235] (8bit).</p>
</dd>

### -field <a id="DXVADDI_NominalRange_48_208"></a><a id="dxvaddi_nominalrange_48_208"></a><a id="DXVADDI_NOMINALRANGE_48_208"></a><b>DXVADDI_NominalRange_48_208</b>

<dd>
<p>Normalized chroma [0..1] maps explicitly to [48..208] (8bit).</p>
</dd>
</dl>

## -remarks
<p>One of the values of DXVADDI_NOMINALRANGE can be specified in the <b>NominalRange</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Wide gamut R'G'B' (that is, blackpoint at 16,16,16 and whitepoint at 235,235,235) must be differentiated from normal <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>.</p>

<p>One of the values of DXVADDI_NOMINALRANGE can be specified in the <b>NominalRange</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Wide gamut R'G'B' (that is, blackpoint at 16,16,16 and whitepoint at 235,235,235) must be differentiated from normal <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>.</p>

<p>One of the values of DXVADDI_NOMINALRANGE can be specified in the <b>NominalRange</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>Wide gamut R'G'B' (that is, blackpoint at 16,16,16 and whitepoint at 235,235,235) must be differentiated from normal <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_NOMINALRANGE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
