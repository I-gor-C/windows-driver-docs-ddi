---
UID: NS.d3dkmthk._D3DKMT_OPENNTHANDLEFROMNAME
title: D3DKMT_OPENNTHANDLEFROMNAME
author: windows-driver-content
description: Describes information that is required to open an NT handle to the process from a graphics adapter name.
old-location: display\d3dkmt_opennthandlefromname.htm
old-project: display
ms.assetid: 34f70519-7905-4a16-bd07-db3592b05890
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_OPENNTHANDLEFROMNAME, D3DKMT_OPENNTHANDLEFROMNAME
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
req.alt-api: D3DKMT_OPENNTHANDLEFROMNAME
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

# D3DKMT_OPENNTHANDLEFROMNAME structure



## -description
<p>Describes information that is required to open an NT handle to the process from a graphics adapter name.</p>


## -syntax

````
typedef struct _D3DKMT_OPENNTHANDLEFROMNAME {
  DWORD             dwDesiredAccess;
  OBJECT_ATTRIBUTES *pObjAttrib;
  HANDLE            hNtHandle;
} D3DKMT_OPENNTHANDLEFROMNAME;
````


## -struct-fields
<dl>

### -field dwDesiredAccess

<dd>
<p>[in] Specifies read and write access for the resource.</p>
</dd>

### -field pObjAttrib

<dd>
<p>[in] A pointer to an <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that specifies attributes of the adapter, including its name.</p>
</dd>

### -field hNtHandle

<dd>
<p>[out] An NT handle to the process.</p>
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