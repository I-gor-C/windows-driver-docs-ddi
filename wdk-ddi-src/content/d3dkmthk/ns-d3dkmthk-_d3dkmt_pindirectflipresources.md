---
UID: NS.D3DKMTHK._D3DKMT_PINDIRECTFLIPRESOURCES
title: _D3DKMT_PINDIRECTFLIPRESOURCES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_pindirectflipresources.htm
old-project: display
ms.assetid: c5c79876-a9b5-44fa-9545-3995118520d0
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_PINDIRECTFLIPRESOURCES, D3DKMT_PINDIRECTFLIPRESOURCES
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
---

# _D3DKMT_PINDIRECTFLIPRESOURCES structure



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef struct _D3DKMT_PINDIRECTFLIPRESOURCES {
  D3DKMT_HANDLE hDevice;
  UINT          ResourceCount;
  D3DKMT_HANDLE *pResourceList;
} D3DKMT_PINDIRECTFLIPRESOURCES;
````


## -struct-fields

### -field hDevice


### -field ResourceCount


### -field pResourceList


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
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>