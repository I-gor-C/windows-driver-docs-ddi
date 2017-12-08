---
UID: NS.D3DKMTHK._D3DKMT_UNPINDIRECTFLIPRESOURCES
title: _D3DKMT_UNPINDIRECTFLIPRESOURCES
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_unpindirectflipresources.htm
old-project: display
ms.assetid: c875a30c-41e4-478c-b8b0-c1fb32672915
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DKMT_UNPINDIRECTFLIPRESOURCES, D3DKMT_UNPINDIRECTFLIPRESOURCES
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
req.alt-api: D3DKMT_UNPINDIRECTFLIPRESOURCES
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

# _D3DKMT_UNPINDIRECTFLIPRESOURCES structure



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef struct _D3DKMT_UNPINDIRECTFLIPRESOURCES {
  D3DKMT_HANDLE hDevice;
  UINT          ResourceCount;
  D3DKMT_HANDLE *pResourceList;
} D3DKMT_UNPINDIRECTFLIPRESOURCES;
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