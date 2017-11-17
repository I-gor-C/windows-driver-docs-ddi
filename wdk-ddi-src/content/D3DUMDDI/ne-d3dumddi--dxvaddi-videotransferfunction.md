---
UID: NE.d3dumddi._DXVADDI_VIDEOTRANSFERFUNCTION
title: DXVADDI_VIDEOTRANSFERFUNCTION
author: windows-driver-content
description: The DXVADDI_VIDEOTRANSFERFUNCTION enumeration type contains values that identify the conversion function from R'G'B' to RGB.
old-location: display\dxvaddi_videotransferfunction.htm
ms.assetid: 8d798afe-dc75-4cd0-aad7-1f9824bdcf00
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOTRANSFERFUNCTION
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# DXVADDI_VIDEOTRANSFERFUNCTION enumeration



## -description
<p>The DXVADDI_VIDEOTRANSFERFUNCTION enumeration type contains values that identify the conversion function from R'G'B' to RGB.</p>


## -syntax

````
typedef enum _DXVADDI_VIDEOTRANSFERFUNCTION { 
  DXVADDI_VideoTransFuncMask      = 0x001f,
  DXVADDI_VideoTransFunc_Unknown  = 0,
  DXVADDI_VideoTransFunc_10       = 1,
  DXVADDI_VideoTransFunc_18       = 2,
  DXVADDI_VideoTransFunc_20       = 3,
  DXVADDI_VideoTransFunc_22       = 4,
  DXVADDI_VideoTransFunc_709      = 5,
  DXVADDI_VideoTransFunc_240M     = 6,
  DXVADDI_VideoTransFunc_sRGB     = 7,
  DXVADDI_VideoTransFunc_28       = 8
} DXVADDI_VIDEOTRANSFERFUNCTION;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_VideoTransFuncMask"></a><a id="dxvaddi_videotransfuncmask"></a><a id="DXVADDI_VIDEOTRANSFUNCMASK"></a><b>DXVADDI_VideoTransFuncMask</b>

<dd>
<p>Specifies the video transfer function mask. The first 5 (0x001F) bits of a DWORD can be used to specify the video transfer function.</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_Unknown"></a><a id="dxvaddi_videotransfunc_unknown"></a><a id="DXVADDI_VIDEOTRANSFUNC_UNKNOWN"></a><b>DXVADDI_VideoTransFunc_Unknown</b>

<dd>
<p>Specifies that the video transfer function is not specified. The default is 22_8bit_sRGB if required for a computation.</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_10"></a><a id="dxvaddi_videotransfunc_10"></a><a id="DXVADDI_VIDEOTRANSFUNC_10"></a><b>DXVADDI_VideoTransFunc_10</b>

<dd>
<p>Specifies linear RGB conversion (corresponds to gamma = 1.0).</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_18"></a><a id="dxvaddi_videotransfunc_18"></a><a id="DXVADDI_VIDEOTRANSFUNC_18"></a><b>DXVADDI_VideoTransFunc_18</b>

<dd>
<p>Specifies true 1.8 gamma--that is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_20"></a><a id="dxvaddi_videotransfunc_20"></a><a id="DXVADDI_VIDEOTRANSFUNC_20"></a><b>DXVADDI_VideoTransFunc_20</b>

<dd>
<p>Specifies true 2.0 gamma--that is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_22"></a><a id="dxvaddi_videotransfunc_22"></a><a id="DXVADDI_VIDEOTRANSFUNC_22"></a><b>DXVADDI_VideoTransFunc_22</b>

<dd>
<p>Specifies true 2.2 gamma--that is, L' = pow(L, 1/gamma) for L=0..1. </p>
<p>The BT470-2 SysM primaries (that is, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562951">DXVADDI_VIDEOPRIMARIES</a> enumeration type) use gamma 2.2.</p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_709"></a><a id="dxvaddi_videotransfunc_709"></a><a id="DXVADDI_VIDEOTRANSFUNC_709"></a><b>DXVADDI_VideoTransFunc_709</b>

<dd>
<p>Specifies gamma 2.2 curve with a linear range in the low range. </p>
<p>The BT709, SMPTE296M, SMPTE170M, BT470, and SMPTE274M primaries (that is, the DXVADDI_VIDEOPRIMARIES enumeration type) use this video transfer function. </p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_240M"></a><a id="dxvaddi_videotransfunc_240m"></a><a id="DXVADDI_VIDEOTRANSFUNC_240M"></a><b>DXVADDI_VideoTransFunc_240M</b>

<dd>
<p>Specifies gamma 2.2 curve with a linear range in the low range. </p>
<p>The SMPTE240M and interim 274M primaries (that is, the DXVADDI_VIDEOPRIMARIES enumeration type) use this video transfer function. </p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_sRGB"></a><a id="dxvaddi_videotransfunc_srgb"></a><a id="DXVADDI_VIDEOTRANSFUNC_SRGB"></a><b>DXVADDI_VideoTransFunc_sRGB</b>

<dd>
<p>Specifies gamma 2.4 curve with a linear range in the low range, which makes it match an accurate 2.2 gamma 8-bit curve. </p>
</dd>

### -field <a id="DXVADDI_VideoTransFunc_28"></a><a id="dxvaddi_videotransfunc_28"></a><a id="DXVADDI_VIDEOTRANSFUNC_28"></a><b>DXVADDI_VideoTransFunc_28</b>

<dd>
<p>Specifies true 2.8 gamma--that is, L' = pow(L, 1/gamma) for L=0..1.</p>
</dd>
</dl>

## -remarks
<p>One of the values of DXVADDI_VIDEOTRANSFERFUNCTION can be specified in the <b>VideoTransferFunction</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>DXVADDI_VIDEOTRANSFERFUNCTION corresponds to the gamma function of the data. Some transfer functions have corrections to account for 8-bit integer quantization effects.</p>

<p>The following constants can also be used for gamma function:</p>

<p>One of the values of DXVADDI_VIDEOTRANSFERFUNCTION can be specified in the <b>VideoTransferFunction</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>DXVADDI_VIDEOTRANSFERFUNCTION corresponds to the gamma function of the data. Some transfer functions have corrections to account for 8-bit integer quantization effects.</p>

<p>The following constants can also be used for gamma function:</p>

<p>One of the values of DXVADDI_VIDEOTRANSFERFUNCTION can be specified in the <b>VideoTransferFunction</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562904">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

<p>DXVADDI_VIDEOTRANSFERFUNCTION corresponds to the gamma function of the data. Some transfer functions have corrections to account for 8-bit integer quantization effects.</p>

<p>The following constants can also be used for gamma function:</p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562951">DXVADDI_VIDEOPRIMARIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOTRANSFERFUNCTION enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
