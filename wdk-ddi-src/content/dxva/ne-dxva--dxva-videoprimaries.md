---
UID: NE.dxva._DXVA_VideoPrimaries
title: DXVA_VideoPrimaries
author: windows-driver-content
description: The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used.
old-location: display\dxva_videoprimaries.htm
old-project: display
ms.assetid: 8aa6ba31-aec0-4a92-ad0e-6c19b796e398
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
req.alt-api: DXVA_VideoPrimaries
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

# DXVA_VideoPrimaries enumeration



## -description
<p>The DXVA_VideoPrimaries enumeration type contains enumerators that identify the color primaries, which state which RGB basis functions are used.</p>


## -syntax

````
typedef enum _DXVA_VideoPrimaries { 
  DXVA_VideoPrimariesShift           = (DXVA_ExtColorData_ShiftBase + 14),
  DXVA_VideoPrimariesMask            = DXVAColorMask(5, DXVA_VideoPrimariesShift),
  DXVA_VideoPrimaries_Unknown        = 0,
  DXVA_VideoPrimaries_reserved       = 1,
  DXVA_VideoPrimaries_BT709          = 2,
  DXVA_VideoPrimaries_BT470_2_SysM   = 3,
  DXVA_VideoPrimaries_BT470_2_SysBG  = 4,
  DXVA_VideoPrimaries_SMPTE170M      = 5,
  DXVA_VideoPrimaries_SMPTE240M      = 6,
  DXVA_VideoPrimaries_EBU3213        = 7,
  DXVA_VideoPrimaries_SMPTE_C        = 8
} DXVA_VideoPrimaries;
````


## -enum-fields
<dl>

### -field DXVA_VideoPrimariesShift

<dd>
<p>Specifies to shift bits by 22 positions (DXVA_ExtColorData_ShiftBase + 14, or 8 + 14).</p>
</dd>

### -field DXVA_VideoPrimariesMask

<dd>
<p>Specifies the color primaries mask. 5 (0x07C00000) bits of a DWORD can be used to specify color primaries.</p>
</dd>

### -field DXVA_VideoPrimaries_Unknown

<dd>
<p>Specifies that color primaries are not specified. The default is BT709.</p>
</dd>

### -field DXVA_VideoPrimaries_reserved

<dd>
<p>Reserved.</p>
</dd>

### -field DXVA_VideoPrimaries_BT709

<dd>
<p>Specifies BT709 primaries (including sRGB, scRGB).</p>
</dd>

### -field DXVA_VideoPrimaries_BT470_2_SysM

<dd>
<p>Specifies BT470-2 SysM primaries, which are the original NTSC primaries. </p>
</dd>

### -field DXVA_VideoPrimaries_BT470_2_SysBG

<dd>
<p>Specifies BT470-2 SysBG primaries. </p>
</dd>

### -field DXVA_VideoPrimaries_SMPTE170M

<dd>
<p>Specifies SMPTE170M primaries, which are rarely used analog NTSC primaries (also known as SMPTE RP 145).</p>
</dd>

### -field DXVA_VideoPrimaries_SMPTE240M

<dd>
<p>Specifies SMPTE240M primaries. </p>
</dd>

### -field DXVA_VideoPrimaries_EBU3213

<dd>
<p>Specifies EBU3213 primaries. </p>
</dd>

### -field DXVA_VideoPrimaries_SMPTE_C

<dd>
<p>Specifies SMPTE_C primaries, which are analog '79 NTSC primaries.</p>
</dd>
</dl>

## -remarks
<p>One of the enumerators of DXVA_VideoPrimaries can be specified in the <b>VideoPrimaries</b> member of the <a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_VideoPrimaries enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
