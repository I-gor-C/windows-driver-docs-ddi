---
UID: NS.d3dkmthk._D3DKMT_UMD_DRIVER_VERSION
title: D3DKMT_UMD_DRIVER_VERSION
author: windows-driver-content
description: Indicates the version number of the user-mode driver.
old-location: display\d3dkmt_umd_driver_version.htm
old-project: display
ms.assetid: 0661a65d-5129-49f6-9400-70b8c8e8245f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_UMD_DRIVER_VERSION, D3DKMT_UMD_DRIVER_VERSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_UMD_DRIVER_VERSION
req.alt-loc: D3dkmthk.h
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

# D3DKMT_UMD_DRIVER_VERSION structure



## -description
<p>Indicates the version number of the user-mode driver.</p>


## -syntax

````
typedef struct _D3DKMT_UMD_DRIVER_VERSION {
  LARGE_INTEGER DriverVersion;
} D3DKMT_UMD_DRIVER_VERSION;
````


## -struct-fields
<dl>

### -field DriverVersion

<dd>
<p>The user-mode driver version.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>