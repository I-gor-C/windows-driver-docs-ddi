---
UID: NS.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT
title: D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT structure is used to indicate the angles of rotation that are supported by a particular VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_rotation_support.htm
old-project: display
ms.assetid: f60cd2cf-23b6-4fed-8548-d0483fb17fe1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT, D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT
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
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT
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

# D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT structure



## -description
<p>The <b>D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT</b> structure is used to indicate the angles of rotation that are supported by a particular VidPN present path.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT {
  UINT Identity  :1;
  UINT Rotate90  :1;
  UINT Rotate180  :1;
  UINT Rotate270  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3_PATH_INDEPENDENT_ROTATION)
  UINT Offset0  :1;
  UINT Offset90  :1;
  UINT Offset180  :1;
  UINT Offset270  :1;
#endif 
} D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT;
````


## -struct-fields
<dl>

### -field <b>Identity</b>

<dd>
<p>The path is capable of displaying content with no rotation.</p>
</dd>

### -field <b>Rotate90</b>

<dd>
<p>The path is capable of displaying content that is rotated 90 degrees.</p>
</dd>

### -field <b>Rotate180</b>

<dd>
<p>The path is capable of displaying content that is rotated 180 degrees.</p>
</dd>

### -field <b>Rotate270</b>

<dd>
<p>The path is capable of displaying content that is rotated 270 degrees.</p>
</dd>

### -field <b>Offset0</b>

<dd>
<p>The path adds no rotational offset. For more info, see <a href="display.supporting_rotation_in_a_display_miniport_driver#clone-mode_requirements#clone-mode_requirements">Clone-mode requirements starting with Windows 8.1 Update</a>.</p>
<p>Supported starting with Windows 8.1 Update.</p>
</dd>

### -field <b>Offset90</b>

<dd>
<p>The path adds a rotational offset of 90 degrees. For more info, see <a href="display.supporting_rotation_in_a_display_miniport_driver#clone-mode_requirements#clone-mode_requirements">Clone-mode requirements starting with Windows 8.1 Update</a>.</p>
<p>Supported starting with Windows 8.1 Update.</p>
</dd>

### -field <b>Offset180</b>

<dd>
<p>The path adds a rotational offset of 180 degrees. For more info, see <a href="display.supporting_rotation_in_a_display_miniport_driver#clone-mode_requirements#clone-mode_requirements">Clone-mode requirements starting with Windows 8.1 Update</a>.</p>
<p>Supported starting with Windows 8.1 Update.</p>
</dd>

### -field <b>Offset270</b>

<dd>
<p>The path adds a rotational offset of 270 degrees. For more info, see <a href="display.supporting_rotation_in_a_display_miniport_driver#clone-mode_requirements#clone-mode_requirements">Clone-mode requirements starting with Windows 8.1 Update</a>.</p>
<p>Supported starting with Windows 8.1 Update.</p>
</dd>
</dl>

## -remarks
<p>The <b>RotationSupport</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546719">D3DKMDT_VIDPN_PRESENT_PATH_TRANSFORMATION</a> structure is a <b>D3DKMDT_VIDPN_PRESENT_PATH_ROTATION_SUPPORT</b> structure.</p>

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