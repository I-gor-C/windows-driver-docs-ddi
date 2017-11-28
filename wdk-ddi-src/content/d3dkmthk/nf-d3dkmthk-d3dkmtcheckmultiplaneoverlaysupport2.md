---
UID: NF.d3dkmthk.D3DKMTCheckMultiPlaneOverlaySupport2
title: D3DKMTCheckMultiPlaneOverlaySupport2
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtcheckmultiplaneoverlaysupport2.htm
old-project: display
ms.assetid: FD1F6A41-07AA-406F-85AD-E71C482325B0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTCheckMultiPlaneOverlaySupport2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTCheckMultiPlaneOverlaySupport2
req.alt-loc: GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: GDI32.lib
req.dll: GDI32.dll
req.irql: 
req.iface: 
---

# D3DKMTCheckMultiPlaneOverlaySupport2 function



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTCheckMultiPlaneOverlaySupport2(
  _Inout_ D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT2 *
);
````


## -parameters
<dl>

### -param <i></i> [in, out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>GDI32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>GDI32.dll</dt>
</dl>
</td>
</tr>
</table>