---
UID: NE.dxva._DXVA_NominalRange
title: DXVA_NominalRange
author: windows-driver-content
description: The DXVA_NominalRange enumeration type contains enumerators that identify whether sample data includes headroom (values beyond 1.0 white) and toeroom (superblacks below the reference 0.0 black).
old-location: display\dxva_nominalrange.htm
old-project: display
ms.assetid: 9e319f9d-4c24-4dd3-b5a1-b244714c06dc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_GAMMA_CONTROL_CAPABILITIES, DXGI_GAMMA_CONTROL_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_NominalRange
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

# DXVA_NominalRange enumeration



## -description
<p>The DXVA_NominalRange enumeration type contains enumerators that identify whether sample data includes headroom (values beyond 1.0 white) and toeroom (superblacks below the reference 0.0 black). </p>


## -syntax

````
typedef enum _DXVA_NominalRange { 
  DXVA_NominalRangeShift     = (DXVA_ExtColorData_ShiftBase + 4),
  DXVA_NominalRangeMask      = DXVAColorMask(5, DXVA_VideoNominalRangeShift),
  DXVA_NominalRange_Unknown  = 0,
  DXVA_NominalRange_Normal   = 1,
  DXVA_NominalRange_Wide     = 2,
  DXVA_NominalRange_0_255    = 1,
  DXVA_NominalRange_16_235   = 2,
  DXVA_NominalRange_48_208   = 3
} DXVA_NominalRange;
````


## -enum-fields
<dl>

### -field DXVA_NominalRangeShift

<dd>
<p>Specifies to shift bits by 12 positions (DXVA_ExtColorData_ShiftBase + 4, or 8 + 4).</p>
</dd>

### -field DXVA_NominalRangeMask

<dd>
<p>Specifies the nominal range mask. 3 (0x00007000) bits of a DWORD can be used to specify nominal range.</p>
</dd>

### -field DXVA_NominalRange_Unknown

<dd>
<p>Specifies that the nominal range is not specified.</p>
</dd>

### -field DXVA_NominalRange_Normal

<dd>
<p>Specifies that normalized chroma [0..1] maps to [0..255] (8bit) or [0..1023] (10 bit).</p>
</dd>

### -field DXVA_NominalRange_Wide

<dd>
<p>Specifies that normalized chroma [0..1] maps to [16..235] (8bit) or [64..940] (10 bit).</p>
</dd>

### -field DXVA_NominalRange_0_255

<dd>
<p>Specifies that normalized chroma [0..1] maps to [0..255] (8bit) or [0..1023] (10 bit).</p>
</dd>

### -field DXVA_NominalRange_16_235

<dd>
<p>Specifies that normalized chroma [0..1] maps to [16..235] (8bit) or [64..940] (10 bit).</p>
</dd>

### -field DXVA_NominalRange_48_208

<dd>
<p>Specifies that normalized chroma [0..1] maps to [48..208] (8bit) or [192..832] (10 bit).</p>
</dd>
</dl>

## -remarks
<p>One of the enumerators of DXVA_NominalRange can be specified in the <b>NominalRange</b> member of the <a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a> structure.</p>

<p>Wide gamut R'G'B' (that is, blackpoint at 16,16,16 and whitepoint at 235,235,235) must be differentiated from normal <a href="http://go.microsoft.com/fwlink/p/?linkid=10112">sRGB</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This enumeration type applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p>
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
<a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_NominalRange enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
