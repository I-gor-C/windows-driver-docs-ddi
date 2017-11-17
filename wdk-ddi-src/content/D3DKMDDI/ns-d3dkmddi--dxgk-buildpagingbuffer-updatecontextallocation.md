---
UID: NS.d3dkmddi._DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION
title: DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION
author: windows-driver-content
description: DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION describes an operation used to update the content of a context or device allocation.
old-location: display\dxgk_buildpagingbuffer_updatecontextallocation.htm
ms.assetid: DA23251C-E901-48A0-9B58-458622DE8CF0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION
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
ms.keywords: DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION, DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION
req.iface: 
---

# DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION structure



## -description
<p><b>DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION</b> describes an operation used to update the content of a context or device allocation.</p>


## -syntax

````
typedef struct _DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION {
  D3DGPU_VIRTUAL_ADDRESS ContextAllocation;
  UINT64                 ContextAllocationSize;
  PVOID                  pDriverPrivateData;
  UINT                   DriverPrivateDataSize;
} DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION;
````


## -struct-fields
<dl>

### -field <b>ContextAllocation</b>

<dd>
<p>A GPU virtual address in the paging process scratch area for the context allocation being updated.</p>
</dd>

### -field <b>ContextAllocationSize</b>

<dd>
<p>The size of the context allocation.</p>
</dd>

### -field <b>pDriverPrivateData</b>

<dd>
<p>A pointer to the driver-private data that was passed in the call to <a href="https://msdn.microsoft.com/708A33C2-9620-4259-845A-2F862B6F209B">DxgkCbUpdateContextAllocation</a>.</p>
</dd>

### -field <b>DriverPrivateDataSize</b>

<dd>
<p>The size of the driver-private data.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557540">DXGKARG_BUILDPAGINGBUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/708A33C2-9620-4259-845A-2F862B6F209B">DxgkCbUpdateContextAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BUILDPAGINGBUFFER_UPDATECONTEXTALLOCATION structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
