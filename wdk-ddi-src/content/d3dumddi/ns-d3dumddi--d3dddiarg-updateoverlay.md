---
UID: NS.d3dumddi._D3DDDIARG_UPDATEOVERLAY
title: D3DDDIARG_UPDATEOVERLAY
author: windows-driver-content
description: The D3DDDIARG_UPDATEOVERLAY structure describes an overlay to modify.
old-location: display\d3dddiarg_updateoverlay.htm
old-project: display
ms.assetid: e49f48fd-f2e8-4ccc-813f-f624e06ab365
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_UPDATEOVERLAY, D3DDDIARG_UPDATEOVERLAY
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
req.alt-api: D3DDDIARG_UPDATEOVERLAY
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

# D3DDDIARG_UPDATEOVERLAY structure



## -description
<p>The D3DDDIARG_UPDATEOVERLAY structure describes an overlay to modify. </p>


## -syntax

````
typedef struct _D3DDDIARG_UPDATEOVERLAY {
  HANDLE             hOverlay;
  D3DDDI_OVERLAYINFO OverlayInfo;
} D3DDDIARG_UPDATEOVERLAY;
````


## -struct-fields
<dl>

### -field <b>hOverlay</b>

<dd>
<p>[in] A handle to the overlay to modify.</p>
</dd>

### -field <b>OverlayInfo</b>

<dd>
<p>[in] A pointer to the <a href="..\d3dumddi\ns-d3dumddi--d3dddi-overlayinfo.md">D3DDDI_OVERLAYINFO</a> structure that describes the modification for the overlay. </p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-updateoverlay.md">UpdateOverlay</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-overlayinfo.md">D3DDDI_OVERLAYINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_UPDATEOVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
