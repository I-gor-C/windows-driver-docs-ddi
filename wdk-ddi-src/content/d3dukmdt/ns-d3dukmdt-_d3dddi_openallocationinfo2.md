---
UID: NS.D3DUKMDT._D3DDDI_OPENALLOCATIONINFO2
title: _D3DDDI_OPENALLOCATIONINFO2
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dddi_openallocationinfo2.htm
old-project: display
ms.assetid: 5C439C23-75B1-422C-850D-6980CC89539B
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _D3DDDI_OPENALLOCATIONINFO2, D3DDDI_OPENALLOCATIONINFO2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_OPENALLOCATIONINFO2
req.alt-loc: D3dukmdt.h
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

# _D3DDDI_OPENALLOCATIONINFO2 structure



## -description
Reserved for system use. Do not use in your driver.


## -syntax

````
typedef struct _D3DDDI_OPENALLOCATIONINFO2 {
  D3DKMT_HANDLE          hAllocation;
  const VOID             *pPrivateDriverData;
  UINT                   PrivateDriverDataSize;
  D3DGPU_VIRTUAL_ADDRESS GpuVirtualAddress;
  ULONG_PTR              Reserved[6];
} D3DDDI_OPENALLOCATIONINFO2;
````


## -struct-fields

### -field hAllocation


### -field pPrivateDriverData


### -field PrivateDriverDataSize


### -field GpuVirtualAddress


### -field Reserved


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 7
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2008
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dukmdt.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>