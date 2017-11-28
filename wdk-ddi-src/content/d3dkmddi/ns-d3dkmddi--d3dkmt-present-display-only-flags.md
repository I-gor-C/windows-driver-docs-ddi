---
UID: NS.d3dkmddi._D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
title: D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
author: windows-driver-content
description: Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.
old-location: display\d3dkmt_present_display_only_flags.htm
old-project: display
ms.assetid: a45dfdeb-06d2-49c8-a6e1-f42a43857492
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS, D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS
req.alt-loc: D3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS structure



## -description
<p>Indicates how a kernel mode display-only driver (KMDOD) is to perform a present operation.</p>


## -syntax

````
typedef struct _D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS {
  union {
    struct {
      UINT Rotate  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS;
````


## -struct-fields
<dl>

### -field <b>Rotate</b>

<dd>
<p>[in] A UINT value that specifies whether to rotate the presentation data to match the current orientation of the screen during the presentation bit-block transfer (bitblt). The current orientation of the screen is set in the <b>Rotation</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure, which is set in the <b>ContentTransformation</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure for the video present path.</p>
<p>The KMDOD should rotate the data only if the <b>Rotate</b> bit-field flag is set. Even if the KMDOD determines that the current orientation of the screen is rotated from the presentation data and <b>Rotate</b> is not set, the KMDOD should not rotate the data.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero.</p>
<p>Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFF) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that <b>D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS</b> contains that can hold a 32-bit value that identifies the type of present operation to perform.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
