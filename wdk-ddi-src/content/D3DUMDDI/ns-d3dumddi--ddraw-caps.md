---
UID: NS.d3dumddi._DDRAW_CAPS
title: DDRAW_CAPS
author: windows-driver-content
description: The DDRAW_CAPS structure describes general Microsoft DirectDraw capabilities that the user-mode display driver supports.
old-location: display\ddraw_caps.htm
ms.assetid: 023e3780-bc88-446b-b235-8853807fb05a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDRAW_CAPS
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
ms.keywords: DDRAW_CAPS, DDRAW_CAPS
req.iface: 
---

# DDRAW_CAPS structure



## -description
<p>The DDRAW_CAPS structure describes general Microsoft DirectDraw capabilities that the user-mode display driver supports.</p>


## -syntax

````
typedef struct _DDRAW_CAPS {
  UINT Caps;
  UINT Caps2;
  UINT CKeyCaps;
  UINT FxCaps;
  UINT MaxVideoPorts;
} DDRAW_CAPS;
````


## -struct-fields
<dl>

### -field <b>Caps</b>

<dd>
<p>[out] A valid bitwise OR of the following general capability bits that the driver supports.</p>
<table>
<tr>
<th>Capability bit</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDRAW_CAPS_ZBLTS</p>
</td>
<td>
<p>Z-buffers can be used in bit-block transfer (bitblt) operations.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS_COLORKEY</p>
</td>
<td>
<p>Some form of color key can be used in either overlay or bitblt operations. For more specific color key capability information, see the <b>CKeyCaps</b> member.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS_BLTDEPTHFILL</p>
</td>
<td>
<p>Z-buffers can be depth-filled in bitblt operations.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Caps2</b>

<dd>
<p>[out] A valid bitwise OR of more of the following general capability bits that the driver supports.</p>
<table>
<tr>
<th>Capability bit</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDRAW_CAPS2_VIDEOPORT</p>
</td>
<td>
<p>A hardware video port can be used.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS2_CANDROPZ16BIT</p>
</td>
<td>
<p>Sixteen-bit RGBZ values can be converted into 16-bit RGB values. (The system does not support 8-bit conversions.)</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS2_FLIPINTERVAL</p>
</td>
<td>
<p>The driver responds to the <b>Flip</b> bit-field flag.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS2_FLIPNOVSYNC</p>
</td>
<td>
<p>The driver responds to the <b>FlipWithNoWait</b> bit-field flag.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CAPS2_DYNAMICTEXTURES</p>
</td>
<td>
<p>The driver supports dynamic textures.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CKeyCaps</b>

<dd>
<p>[out] A valid bitwise OR of the following color key capability bits that the driver supports.</p>
<table>
<tr>
<th>Capability bit</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDRAW_CKEYCAPS_SRCBLT</p>
</td>
<td>
<p>Transparent bit-block transfers can be performed with a color key that identifies bits of the source surface that are copied to the destination surface.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_CKEYCAPS_DESTBLT</p>
</td>
<td>
<p>Transparent bit-block transfers (bitblts) can be performed with a color key that identifies the replaceable bits of the destination surface.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>FxCaps</b>

<dd>
<p>[out] A valid bitwise OR of the following stretching and effects capability bits that the driver supports.</p>
<table>
<tr>
<th>Capability bit</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDRAW_FXCAPS_BLTMIRRORLEFTRIGHT</p>
</td>
<td>
<p>Bit-block transfers (bitblts) that flip the contents of the source surface to the destination surface horizontally along the center axis can be performed.</p>
</td>
</tr>
<tr>
<td>
<p>DDRAW_FXCAPS_BLTMIRRORUPDOWN</p>
</td>
<td>
<p>Bit-block transfers (bitblts) that flip the contents of the source surface to the destination surface vertically along the center axis can be performed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MaxVideoPorts</b>

<dd>
<p>[out] The maximum number of video ports that the device supports.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543148">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544132">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDRAW_CAPS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
