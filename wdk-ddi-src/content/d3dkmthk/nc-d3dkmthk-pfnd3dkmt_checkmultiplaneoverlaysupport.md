---
UID: NC.d3dkmthk.PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT
title: PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtcheckmultiplaneoverlaysupport.htm
old-project: display
ms.assetid: CD354937-4383-4418-9BF8-34D78FCFC118
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_TARGETMODE_DETAIL_TIMING, DXGK_TARGETMODE_DETAIL_TIMING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
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
---

# PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT callback



## -description
Reserved for system use. Do not use in your driver.


## -prototype

````
PFND3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT D3DKMTCheckMultiPlaneOverlaySupport;

EXTERN_C _Check_return_ NTSTATUS APIENTRY* D3DKMTCheckMultiPlaneOverlaySupport(
  _Inout_ const D3DKMT_CHECKMULTIPLANEOVERLAYSUPPORT *pMPOSupport
)
{ ... }
````


## -parameters

### -param pMPOSupport [in, out]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>