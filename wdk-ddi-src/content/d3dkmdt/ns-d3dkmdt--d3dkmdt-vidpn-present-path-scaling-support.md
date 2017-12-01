---
UID: NS.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
title: D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure is used to indicate the types of scaling (and centering) that are supported by a particular VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_scaling_support.htm
old-project: display
ms.assetid: 44b7f841-40e5-4d7d-adca-b70b4a8ef55c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT, D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT
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
req.irql: 
req.iface: 
---

# D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure is used to indicate the types of scaling (and centering) that are supported by a particular VidPN present path.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT {
  UINT Identity  :1;
  UINT Centered  :1;
  UINT Stretched  :1;
  UINT AspectRatioCenteredMax  :1;
  UINT Custom  :1;
} D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT;
````


## -struct-fields
<dl>

### -field <b>Identity</b>

<dd>
<p>The path is capable of displaying content with no transformation.</p>
</dd>

### -field <b>Centered</b>

<dd>
<p>The path is capable of displaying centered content.</p>
</dd>

### -field <b>Stretched</b>

<dd>
<p>The path is capable of displaying scaled content.</p>
</dd>

### -field <b>AspectRatioCenteredMax</b>

<dd>
<p>The path is capable of scaling source content to fit the target while preserving the aspect ratio of the source.</p>
<p>This member is available beginning with Windows 7.</p>
</dd>

### -field <b>Custom</b>

<dd>
<p>The path is capable of displaying one or more scaling modes that are not described by other members of this structure.</p>
</dd>
</dl>

## -remarks
<p>The <b>ScalingSupport</b> member of a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path-transformation.md">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure.</p>

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
<a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-vidpn-present-path-scaling.md">D3DKMDT_VIDPN_PRESENT_PATH_SCALING</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path-transformation.md">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDPN_PRESENT_PATH_SCALING_SUPPORT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
