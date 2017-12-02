---
UID: NE.dxva._DXVA_VideoTransferFunction
title: DXVA_VideoTransferFunction
author: windows-driver-content
description: The DXVA_VideoTransferFunction enumeration type contains enumerators that identify the conversion function from R'G'B' to RGB.
old-location: display\dxva_videotransferfunction.htm
old-project: display
ms.assetid: 2ed04fd0-685d-4b5a-a23f-337a14506f8b
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
req.alt-api: DXVA_VideoTransferFunction
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

# DXVA_VideoTransferFunction enumeration



## -description
<p>The DXVA_VideoTransferFunction enumeration type contains enumerators that identify the conversion function from R'G'B' to RGB.</p>


## -syntax

````
typedef enum _DXVA_VideoTransferFunction { 
  DXVA_VideoTransFuncShift          = (DXVA_ExtColorData_ShiftBase + 19),
  DXVA_VideoTransFuncMask           = DXVAColorMask(5, DXVA_VideoTransFuncShift),
  DXVA_VideoTransFunc_Unknown       = 0,
  DXVA_VideoTransFunc_10            = 1,
  DXVA_VideoTransFunc_18            = 2,
  DXVA_VideoTransFunc_20            = 3,
  DXVA_VideoTransFunc_22            = 4,
  DXVA_VideoTransFunc_22_709        = 5,
  DXVA_VideoTransFunc_22_240M       = 6,
  DXVA_VideoTransFunc_22_8bit_sRGB  = 7,
  DXVA_VideoTransFunc_28            = 8
} DXVA_VideoTransferFunction;
````


## -enum-fields
<dl>

### -field DXVA_VideoTransFuncShift

<dd>
<p>Specifies to shift bits by 27 positions (DXVA_ExtColorData_ShiftBase + 19, or 8 + 19).</p>
</dd>

### -field DXVA_VideoTransFuncMask

<dd>
<p>Specifies the video transfer function mask. 5 (0xF8000000) bits of a DWORD can be used to specify the video transfer function.</p>
</dd>

### -field DXVA_VideoTransFunc_Unknown

<dd>
<p>Specifies that the video transfer function is not specified. The default is 22_8bit_sRGB if required for a computation.</p>
</dd>

### -field DXVA_VideoTransFunc_10

<dd>
<p>Specifies linear RGB conversion (corresponds to gamma = 1.0).</p>
</dd>

### -field DXVA_VideoTransFunc_18

<dd>
<p>Specifies true 1.8 gamma. That is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>

### -field DXVA_VideoTransFunc_20

<dd>
<p>Specifies true 2.0 gamma. That is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>

### -field DXVA_VideoTransFunc_22

<dd>
<dl>

### -field Specifies true 2.2 gamma. That is, L' = pow(L, 1/gamma) for L=0..1.


### -field The BT470-2 SysM primaries (DXVA_VideoPrimaries enumeration type) use gamma 2.2.

</dl>
</dd>

### -field DXVA_VideoTransFunc_22_709

<dd>
<dl>

### -field Specifies gamma 2.2 curve with a linear range in the low range. 


### -field The BT709, SMPTE296M, SMPTE170M, BT470, and SMPTE274M primaries (DXVA_VideoPrimaries enumeration type) use this video transfer function. 

</dl>
</dd>

### -field DXVA_VideoTransFunc_22_240M

<dd>
<dl>

### -field Specifies gamma 2.2 curve with a linear range in the low range. 


### -field The SMPTE240M and interim 274M primaries (DXVA_VideoPrimaries enumeration type) use this video transfer function. 

</dl>
</dd>

### -field DXVA_VideoTransFunc_22_8bit_sRGB

<dd>
<p>Specifies gamma 2.4 curve with a linear range in the low range, which makes it match an accurate 2.2 gamma 8 bit curve. </p>
</dd>

### -field DXVA_VideoTransFunc_28

<dd>
<p>Specifies true 2.8 gamma. That is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>
</dl>

## -remarks
<p>One of the enumerators of DXVA_VideoTransferFunction can be specified in the <b>VideoTransferFunction</b> member of the <a href="..\dxva\ns-dxva--dxva-extendedformat.md">DXVA_ExtendedFormat</a> structure.</p>

<p>DXVA_VideoTransferFunction corresponds to the gamma function of the data. Some transfer functions have corrections to account for 8 bit integer quantization effects.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_VideoTransferFunction enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
