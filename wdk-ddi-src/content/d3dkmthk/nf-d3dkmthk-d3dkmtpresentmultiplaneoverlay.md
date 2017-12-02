---
UID: NF.d3dkmthk.D3DKMTPresentMultiPlaneOverlay
title: D3DKMTPresentMultiPlaneOverlay
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmtpresentmultiplaneoverlay.htm
old-project: display
ms.assetid: 62993166-9630-4395-8649-078f0de40647
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTPresentMultiPlaneOverlay
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTPresentMultiPlaneOverlay
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

# D3DKMTPresentMultiPlaneOverlay function



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
EXTERN_C _Check_return_ NTSTATUS APIENTRY D3DKMTPresentMultiPlaneOverlay(
  _In_ const D3DKMT_PRESENT_MULTIPLANE_OVERLAY *pPresent
);
````


## -parameters
<dl>

### -param pPresent [in]

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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>