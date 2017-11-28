---
UID: NE.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_CONTENT
title: D3DKMDT_VIDPN_PRESENT_PATH_CONTENT
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration is used to indicate the type of content that is displayed on a VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_content.htm
old-project: display
ms.assetid: 29423933-c3cf-4fe4-b79c-f82718163a23
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_CONTENT
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration is used to indicate the type of content that is displayed on a VidPN present path.</p>


## -syntax

````
typedef enum _D3DKMDT_VIDPN_PRESENT_PATH_CONTENT { 
  D3DKMDT_VPPC_UNINITIALIZED  = 0,
  D3DKMDT_VPPC_GRAPHICS       = 1,
  D3DKMDT_VPPC_VIDEO          = 2,
  D3DKMDT_VPPC_NOTSPECIFIED   = 255
} D3DKMDT_VIDPN_PRESENT_PATH_CONTENT;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_VPPC_UNINITIALIZED"></a><a id="d3dkmdt_vppc_uninitialized"></a><b>D3DKMDT_VPPC_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_VIDPN_PRESENT_PATH_CONTENT has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_VPPC_GRAPHICS"></a><a id="d3dkmdt_vppc_graphics"></a><b>D3DKMDT_VPPC_GRAPHICS</b>

<dd>
<p>Indicates that the path displays graphics content.</p>
</dd>

### -field <a id="D3DKMDT_VPPC_VIDEO"></a><a id="d3dkmdt_vppc_video"></a><b>D3DKMDT_VPPC_VIDEO</b>

<dd>
<p>Indicates that the path displays video content.</p>
</dd>

### -field <a id="D3DKMDT_VPPC_NOTSPECIFIED"></a><a id="d3dkmdt_vppc_notspecified"></a><b>D3DKMDT_VPPC_NOTSPECIFIED</b>

<dd>
<p>Indicates that no content type has been specified.</p>
</dd>
</dl>

## -remarks
<p>The <b>Content</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration.</p>

<p>The <b>Content</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration.</p>

<p>The <b>Content</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_CONTENT enumeration.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>