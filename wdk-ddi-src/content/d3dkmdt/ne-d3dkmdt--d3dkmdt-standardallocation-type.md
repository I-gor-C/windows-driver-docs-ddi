---
UID: NE.d3dkmdt._D3DKMDT_STANDARDALLOCATION_TYPE
title: D3DKMDT_STANDARDALLOCATION_TYPE
author: windows-driver-content
description: The D3DKMDT_STANDARDALLOCATION_TYPE enumeration type contains values that identify particular types of surfaces.
old-location: display\d3dkmdt_standardallocation_type.htm
old-project: display
ms.assetid: b86029c5-9d59-4cd0-81bd-cafb8db2fdfd
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
req.alt-api: D3DKMDT_STANDARDALLOCATION_TYPE
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

# D3DKMDT_STANDARDALLOCATION_TYPE enumeration



## -description
<p>The D3DKMDT_STANDARDALLOCATION_TYPE enumeration type contains values that identify particular types of surfaces.</p>


## -syntax

````
typedef enum _D3DKMDT_STANDARDALLOCATION_TYPE { 
  D3DKMDT_STANDARDALLOCATION_SHAREDPRIMARYSURFACE  = 1,
  D3DKMDT_STANDARDALLOCATION_SHADOWSURFACE         = 2,
  D3DKMDT_STANDARDALLOCATION_STAGINGSURFACE        = 3,
  D3DKMDT_STANDARDALLOCATION_GDISURFACE            = 4
} D3DKMDT_STANDARDALLOCATION_TYPE;
````


## -enum-fields
<dl>

### -field D3DKMDT_STANDARDALLOCATION_SHAREDPRIMARYSURFACE

<dd>
<p>Indicates that the surface is a shared primary surface, which is opened by multiple applications that all require direct central processing unit (CPU) access to it.</p>
</dd>

### -field D3DKMDT_STANDARDALLOCATION_SHADOWSURFACE

<dd>
<p>Indicates that the surface is a shadow surface.</p>
</dd>

### -field D3DKMDT_STANDARDALLOCATION_STAGINGSURFACE

<dd>
<p>Indicates that the surface is a staging surface.</p>
</dd>

### -field D3DKMDT_STANDARDALLOCATION_GDISURFACE

<dd>
<p>Indicates that the surface is used for GDI hardware acceleration and Desktop Windows Manager (DWM) redirection.</p>
<p>This constant value is available beginning with Windows 7.</p>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-createallocation.md">DXGKARG_CREATEALLOCATION</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-shadowsurfacedata.md">D3DKMDT_SHADOWSURFACEDATA</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-stagingsurfacedata.md">D3DKMDT_STAGINGSURFACEDATA</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-sharedprimarysurfacedata.md">D3DKMDT_SHAREDPRIMARYSURFACEDATA</a>
</dt>
<dt>
<a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_STANDARDALLOCATION_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
