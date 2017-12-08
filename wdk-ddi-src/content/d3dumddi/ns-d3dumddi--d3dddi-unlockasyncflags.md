---
UID: NS.d3dumddi._D3DDDI_UNLOCKASYNCFLAGS
title: D3DDDI_UNLOCKASYNCFLAGS
author: windows-driver-content
description: The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource.
old-location: display\d3dddi_unlockasyncflags.htm
old-project: display
ms.assetid: c31e4a4e-7bc7-43a2-8f86-e79012064fa2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_UNLOCKASYNCFLAGS, D3DDDI_UNLOCKASYNCFLAGS
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
req.alt-api: D3DDDI_UNLOCKASYNCFLAGS
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

# D3DDDI_UNLOCKASYNCFLAGS structure



## -description
<p>The D3DDDI_UNLOCKASYNCFLAGS structure identifies how to unlock a resource.</p>


## -syntax

````
typedef struct _D3DDDI_UNLOCKASYNCFLAGS {
  union {
    struct {
      UINT NotifyOnly  :1;
      UINT Reserved  :31;
    };
    UINT   Value;
  };
} D3DDDI_UNLOCKASYNCFLAGS;
````


## -struct-fields
<dl>

### -field NotifyOnly

<dd>
<p>A UINT value that specifies whether the unlock call is for notification only. The Microsoft Direct3D runtime sets <b>NotifyOnly</b> to <b>TRUE</b> when it unlocks runtime-allocated system memory surfaces. </p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field Value

<dd>
<p>A member in the union that is contained in D3DDDI_UNLOCKASYNCFLAGS that can hold one 32-bit value that identifies how to unlock a resource.</p>
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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-unlock.md">D3DDDIARG_UNLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_UNLOCKASYNCFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
