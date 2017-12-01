---
UID: NS.d3dkmddi._DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
title: DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
author: windows-driver-content
description: The DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure contains a D3DKMDT_VIDPN_PRESENT_PATH structure, which contains arguments for the DxgkDdiUpdateActiveVidPnPresentPath function.
old-location: display\dxgkarg_updateactivevidpnpresentpath.htm
old-project: display
ms.assetid: 6a4d43fd-f118-4424-93e8-57f72b56f929
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH, DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH
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
req.iface: 
---

# DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure



## -description
<p>The DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure contains a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure, which contains arguments for the <a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a> function.</p>


## -syntax

````
typedef struct _DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH {
  D3DKMDT_VIDPN_PRESENT_PATH VidPnPresentPathInfo;
} DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH;
````


## -struct-fields
<dl>

### -field <b>VidPnPresentPathInfo</b>

<dd>
<p>A <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path.md">D3DKMDT_VIDPN_PRESENT_PATH</a> structure that contains the arguments required by <a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a>.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiupdateactivevidpnpresentpath">DxgkDdiUpdateActiveVidPnPresentPath</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_UPDATEACTIVEVIDPNPRESENTPATH structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
