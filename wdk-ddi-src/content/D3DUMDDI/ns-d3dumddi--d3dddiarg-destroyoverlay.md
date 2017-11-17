---
UID: NS.d3dumddi._D3DDDIARG_DESTROYOVERLAY
title: D3DDDIARG_DESTROYOVERLAY
author: windows-driver-content
description: The D3DDDIARG_DESTROYOVERLAY structure contains a handle to the overlay to disable.
old-location: display\d3dddiarg_destroyoverlay.htm
ms.assetid: a468205c-288c-49d5-ab14-0ee39dca7b7c
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
req.alt-api: D3DDDIARG_DESTROYOVERLAY
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
ms.keywords: D3DDDIARG_DESTROYOVERLAY, D3DDDIARG_DESTROYOVERLAY
req.iface: 
---

# D3DDDIARG_DESTROYOVERLAY structure



## -description
<p>The D3DDDIARG_DESTROYOVERLAY structure contains a handle to the overlay to disable.</p>


## -syntax

````
typedef struct _D3DDDIARG_DESTROYOVERLAY {
  HANDLE hOverlay;
} D3DDDIARG_DESTROYOVERLAY;
````


## -struct-fields
<dl>

### -field <b>hOverlay</b>

<dd>
<p>[in] A handle to the overlay to disable.</p>
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
<a href="https://msdn.microsoft.com/63004d19-e2cd-462c-8fa5-ea4dd6e29735">DestroyOverlay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DESTROYOVERLAY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
