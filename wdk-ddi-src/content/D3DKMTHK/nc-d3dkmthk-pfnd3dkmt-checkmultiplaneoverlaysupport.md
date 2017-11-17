---
UID: NC.d3dkmthk.PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT
title: PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtcheckmultiplaneoverlaysupport.htm
ms.assetid: CD354937-4383-4418-9BF8-34D78FCFC118
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTCheckMultiPlaneOverlaySupport
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
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
req.iface: 
---

# PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT callback



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -prototype

````
PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT D3DKMTCheckMultiPlaneOverlaySupport;

EXTERN_C _Check_return_ NTSTATUS APIENTRY* D3DKMTCheckMultiPlaneOverlaySupport(
  _Inout_ const D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT *pMPOSupport
)
{ ... }
````


## -parameters
<dl>

### -param <i>pMPOSupport</i> [in, out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
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
</table>