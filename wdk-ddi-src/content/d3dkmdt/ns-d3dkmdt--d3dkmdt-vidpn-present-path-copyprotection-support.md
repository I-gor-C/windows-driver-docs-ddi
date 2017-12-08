---
UID: NS.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT
title: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure is used to indicate the types of copy protection that are supported by a particular VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_copyprotection_support.htm
old-project: display
ms.assetid: 2b0c7428-bc88-461c-ab72-daccf02606da
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT,
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
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT
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

# D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure is used to indicate the types of copy protection that are supported by a particular VidPN present path.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT {
  UINT NoProtection  :1;
  UINT MacroVisionApsTrigger  :1;
  UINT MacroVisionFull  :1;
  UINT Reserved  :29;
} D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT;
````


## -struct-fields
<dl>

### -field NoProtection

<dd>
<p>The path is not capable of providing any copy protection.</p>
</dd>

### -field MacroVisionApsTrigger

<dd>
<p>The path is capable of providing Rovi (formerly Macrovision) analog protection support (APS). </p>
</dd>

### -field MacroVisionFull

<dd>
<p>The path is capable of providing full Rovi (formerly Macrovision) copy protection.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>The <b>CopyProtectionSupport</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path-copyprotection.md">D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION</a> structure is a D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_SUPPORT structure.</p>

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