---
UID: NS.d3dumddi._D3DDDIARG_UNLOCKASYNC
title: D3DDDIARG_UNLOCKASYNC
author: windows-driver-content
description: The D3DDDIARG_UNLOCKASYNC structure describes a resource or a surface within the resource to unlock.
old-location: display\d3dddiarg_unlockasync.htm
old-project: display
ms.assetid: 27d4a7fa-ac2a-4049-8c9f-5ac9338c70b3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_UNLOCKASYNC, D3DDDIARG_UNLOCKASYNC
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
req.alt-api: D3DDDIARG_UNLOCKASYNC
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

# D3DDDIARG_UNLOCKASYNC structure



## -description
<p>The D3DDDIARG_UNLOCKASYNC structure describes a resource or a surface within the resource to unlock. </p>


## -syntax

````
typedef struct _D3DDDIARG_UNLOCKASYNC {
  HANDLE                  hResource;
  UINT                    SubResourceIndex;
  D3DDDI_UNLOCKASYNCFLAGS Flags;
} D3DDDIARG_UNLOCKASYNC;
````


## -struct-fields
<dl>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to the resource to be unlocked. </p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>[in] The zero-based index into the resource that <b>hResource</b> specifies. This index indicates the subresource or surface to be unlocked.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544676">D3DDDI_UNLOCKASYNCFLAGS</a> structure that indicates, in bit-field flags, how to unlock the resource.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockasync.md">UnlockAsync</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_UNLOCKASYNC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
