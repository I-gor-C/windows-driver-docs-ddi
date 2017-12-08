---
UID: NS.d3dkmthk._D3DKMT_PINDIRECTFLIPRESOURCES
title: D3DKMT_PINDIRECTFLIPRESOURCES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_pindirectflipresources.htm
old-project: display
ms.assetid: c5c79876-a9b5-44fa-9545-3995118520d0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PINDIRECTFLIPRESOURCES, D3DKMT_PINDIRECTFLIPRESOURCES
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
req.alt-api: D3DKMT_PINDIRECTFLIPRESOURCES
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

# D3DKMT_PINDIRECTFLIPRESOURCES structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _D3DKMT_PINDIRECTFLIPRESOURCES {
  D3DKMT_HANDLE hDevice;
  UINT          ResourceCount;
  D3DKMT_HANDLE *pResourceList;
} D3DKMT_PINDIRECTFLIPRESOURCES;
````


## -struct-fields
<dl>

### -field hDevice

<dd></dd>

### -field ResourceCount

<dd></dd>

### -field pResourceList

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>