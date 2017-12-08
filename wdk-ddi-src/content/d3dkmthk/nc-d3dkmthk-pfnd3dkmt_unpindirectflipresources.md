---
UID: NC.d3dkmthk.PFND3DKMT_UNPINDIRECTFLIPRESOURCES
title: PFND3DKMT_UNPINDIRECTFLIPRESOURCES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtunpindirectflipresources.htm
old-project: display
ms.assetid: cfbcf6b4-b1e7-4565-856a-585d7d0d187d
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_TARGETMODE_DETAIL_TIMING, DXGK_TARGETMODE_DETAIL_TIMING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTUnpinDirectFlipResources
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

# PFND3DKMT_UNPINDIRECTFLIPRESOURCES callback



## -description
Reserved for system use. Do not use in your driver.


## -prototype

````
PFND3DKMT_UNPINDIRECTFLIPRESOURCES D3DKMTUnpinDirectFlipResources;

_Check_return_ NTSTATUS APIENTRY* D3DKMTUnpinDirectFlipResources(
  _In_ const D3DKMT_UNPINDIRECTFLIPRESOURCES *pResources
)
{ ... }
````


## -parameters

### -param pResources [in]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012
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