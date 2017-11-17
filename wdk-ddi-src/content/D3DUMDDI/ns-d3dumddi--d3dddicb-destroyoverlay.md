---
UID: NS.d3dumddi._D3DDDICB_DESTROYOVERLAY
title: D3DDDICB_DESTROYOVERLAY
author: windows-driver-content
description: The D3DDDICB_DESTROYOVERLAY structure contains the handle to the overlay to destroy.
old-location: display\d3dddicb_destroyoverlay.htm
ms.assetid: a7b57177-17d2-42d7-ac4a-3cbd74803d50
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
req.alt-api: D3DDDICB_DESTROYOVERLAY
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
ms.keywords: D3DDDICB_DESTROYOVERLAY, D3DDDICB_DESTROYOVERLAY
req.iface: 
---

# D3DDDICB_DESTROYOVERLAY structure



## -description
<p>The D3DDDICB_DESTROYOVERLAY structure contains the handle to the overlay to destroy.</p>


## -syntax

````
typedef struct _D3DDDICB_DESTROYOVERLAY {
  D3DKMT_HANDLE hKernelOverlay;
} D3DDDICB_DESTROYOVERLAY;
````


## -struct-fields
<dl>

### -field <b>hKernelOverlay</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents the kernel-mode handle that is returned by the <a href="https://msdn.microsoft.com/fbd5b3af-0963-4e41-8be3-41e3e1ecf8bc">pfnCreateOverlayCb</a> function and that identifies the kernel-mode overlay object to destroy. </p>
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
<a href="https://msdn.microsoft.com/fbd5b3af-0963-4e41-8be3-41e3e1ecf8bc">pfnCreateOverlayCb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9fc83bad-c183-4cba-9514-bfe1c676cba5">pfnDestroyOverlayCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_DESTROYOVERLAY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
