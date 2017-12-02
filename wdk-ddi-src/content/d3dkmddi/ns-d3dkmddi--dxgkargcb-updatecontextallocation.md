---
UID: NS.d3dkmddi._DXGKARGCB_UPDATECONTEXTALLOCATION
title: DXGKARGCB_UPDATECONTEXTALLOCATION
author: windows-driver-content
description: DXGKARGCB_UPDATECONTEXTALLOCATION contains the data used to call DxgkCbUpdateContextAllocation.
old-location: display\dxgkargcb_updatecontextallocation.htm
old-project: display
ms.assetid: 07BFCA6C-4E75-4BB5-9F6A-22E1FFAFFF6F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARGCB_UPDATECONTEXTALLOCATION, DXGKARGCB_UPDATECONTEXTALLOCATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARGCB_UPDATECONTEXTALLOCATION
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGKARGCB_UPDATECONTEXTALLOCATION structure



## -description
<p><b>DXGKARGCB_UPDATECONTEXTALLOCATION</b> contains the data used to call <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-updatecontextallocation.md">DxgkCbUpdateContextAllocation</a>.</p>


## -syntax

````
typedef struct _DXGKARGCB_UPDATECONTEXTALLOCATION {
  HANDLE hAllocation;
  PVOID  pPrivateDriverData;
  UINT   PrivateDriverDataSize;
} DXGKARGCB_UPDATECONTEXTALLOCATION;
````


## -struct-fields
<dl>

### -field hAllocation

<dd>
<p>Handle to the context allocation being updated. The allocation defines a physical adapter in a linked display adapter link.</p>
</dd>

### -field pPrivateDriverData

<dd>
<p>Pointer to a private driver data buffer to be passed to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-updatecontextallocation.md">DxgkCbUpdateContextAllocation</a> paging operation.</p>
</dd>

### -field PrivateDriverDataSize

<dd>
<p>Specify the size of the driver private data.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-updatecontextallocation.md">DxgkCbUpdateContextAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARGCB_UPDATECONTEXTALLOCATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
