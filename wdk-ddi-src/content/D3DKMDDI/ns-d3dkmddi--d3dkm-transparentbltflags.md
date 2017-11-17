---
UID: NS.d3dkmddi._D3DKM_TRANSPARENTBLTFLAGS
title: D3DKM_TRANSPARENTBLTFLAGS
author: windows-driver-content
description: The D3DKM_TRANSPARENTBLTFLAGS structure specifies the display adapter's ability to perform a hardware-accelerated bit-block transfer (bitblt) with transparency.
old-location: display\d3dkm_transparentbltflags.htm
ms.assetid: 8ac87e6e-bc24-45fe-b0c5-d253dd03da16
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKM_TRANSPARENTBLTFLAGS
req.alt-loc: d3dkmddi.h
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
ms.keywords: D3DKM_TRANSPARENTBLTFLAGS, D3DKM_TRANSPARENTBLTFLAGS
req.iface: 
---

# D3DKM_TRANSPARENTBLTFLAGS structure



## -description
<p>The D3DKM_TRANSPARENTBLTFLAGS structure specifies the display adapter's ability to perform a hardware-accelerated bit-block transfer (bitblt) with transparency.</p>


## -syntax

````
typedef struct _D3DKM_TRANSPARENTBLTFLAGS {
  union {
    struct {
      UINT HonorAlpha  :1;
    };
    UINT   Value;
  };
} D3DKM_TRANSPARENTBLTFLAGS;
````


## -struct-fields
<dl>

### -field <b>HonorAlpha</b>

<dd>
<p>[in] A UINT value that specifies in a hardware-accelerated transparent bit-block transfer whether the alpha channel should be used during comparison:</p>
<dl>
<dd>
<p>1 = The display adapter does not ignore the alpha channel when it compares the reference color with the source color.</p>
</dd>
<dd>
<p>0 = The display adapter ignores the alpha channel when it compares the reference color with the source color.</p>
</dd>
</dl>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>Value</b>

<dd>
<p>[in] A member in the union that D3DKM_TRANSPARENTBLTFLAGS contains. This member can hold a 32-bit value that specifies the display adapter's ability to perform hardware-accelerated bit-block transfer with transparency.</p>
</dd>
</dl>

## -remarks
<p>For more information about how to use the members of this structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561091">DXGK_GDIARG_TRANSPARENTBLT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKM_TRANSPARENTBLTFLAGS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
