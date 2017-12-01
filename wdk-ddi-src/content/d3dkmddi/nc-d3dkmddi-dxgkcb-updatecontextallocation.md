---
UID: NC.d3dkmddi.DXGKCB_UPDATECONTEXTALLOCATION
title: DXGKCB_UPDATECONTEXTALLOCATION
author: windows-driver-content
description: DxgkCbUpdateContextAllocation is used to update the content of a context allocation.
old-location: display\dxgkcbupdatecontextallocation.htm
old-project: display
ms.assetid: 708A33C2-9620-4259-845A-2F862B6F209B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkCbUpdateContextAllocation
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
req.irql: 
req.iface: 
---

# DXGKCB_UPDATECONTEXTALLOCATION callback



## -description
<p><b>DxgkCbUpdateContextAllocation</b> is used to update the content of a context allocation. The video memory manager maps the specified allocation in the paging process address space than trigger an <i>UpdateContextAllocation</i> paging operation (<i>DxgkCbUpdateContextAllocation</i>), passing the kernel mode driver the specified driver private data.

The call to <b>DxgkCbUpdateContextAllocation</b> returns when the update to the context allocation is completed.</p>


## -prototype

````
DXGKCB_UPDATECONTEXTALLOCATION DxgkCbUpdateContextAllocation;

NTSTATUS APIENTRY DxgkCbUpdateContextAllocation(
  _In_ const HANDLE                            hAdapter,
  _In_ const DXGKARGCB_UPDATECONTEXTALLOCATION *pArgs
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle to the display adapter.</p>
</dd>

### -param <i>pArgs</i> [in]

<dd>
<p>The <a href="..\d3dkmddi\ns-d3dkmddi--dxgkargcb-updatecontextallocation.md">DXGKARGCB_UPDATECONTEXTALLOCATION</a> structure that describes the operation.</p>
</dd>
</dl>

## -returns
<p>
      Returns <b>STATUS_SUCCESS</b> if it succeeds. Otherwise, it returns one of the error codes defined in <b>Ntstatus.h</b>.</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkargcb-updatecontextallocation.md">DXGKARGCB_UPDATECONTEXTALLOCATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_UPDATECONTEXTALLOCATION callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
