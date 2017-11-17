---
UID: NS.d3dkmddi._DXGK_PHYSICALADAPTERCAPS
title: DXGK_PHYSICALADAPTERCAPS
author: windows-driver-content
description: The DXGK_PHYSICALADAPTERCAPS structure is used to report details of a physical adapter.
old-location: display\dxgk_physicaladaptercaps.htm
ms.assetid: 8D075473-605F-4B75-BB02-5B182EEB3B5F
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
req.alt-api: DXGK_PHYSICALADAPTERCAPS
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
ms.keywords: DXGK_PHYSICALADAPTERCAPS, DXGK_PHYSICALADAPTERCAPS
req.iface: 
---

# DXGK_PHYSICALADAPTERCAPS structure



## -description
<p>The <b>DXGK_PHYSICALADAPTERCAPS</b> structure is used to report details of a physical adapter.</p>


## -syntax

````
typedef struct _DXGK_PHYSICALADAPTERCAPS {
  WORD                      NumExecutionNodes;
  WORD                      PagingNodeIndex;
  HANDLE                    DxgkPhysicalAdapterHandle;
  DXGK_PHYSICALADAPTERFLAGS Flags;
  UINT                      VPRPagingNode;
} DXGK_PHYSICALADAPTERCAPS;
````


## -struct-fields
<dl>

### -field <b>NumExecutionNodes</b>

<dd>
<p>The number of execution nodes in the physical adapter.</p>
</dd>

### -field <b>PagingNodeIndex</b>

<dd>
<p>Index of the paging node for the physical adapter.</p>
</dd>

### -field <b>DxgkPhysicalAdapterHandle</b>

<dd>
<p>Handle, which is passed to the kernel mode driver as <b>DXGKRNL_INTERFACE::DeviceHandle</b> in <a href="https://msdn.microsoft.com/ffacbb39-2581-4207-841d-28ce57fbc64d">DxgkDdiStartDevice</a>. </p>
</dd>

### -field <b>Flags</b>

<dd>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="Flags.IoMmuSupported"></a><a id="flags.iommusupported"></a><a id="FLAGS.IOMMUSUPPORTED"></a><dl>

### -field <b>Flags.IoMmuSupported</b>


### -field <b>TRUE</b>

</dl>
</td>
<td width="60%">
<p>The adapter supports <i>IoMmu</i>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Flags.GpuMmuSupported"></a><a id="flags.gpummusupported"></a><a id="FLAGS.GPUMMUSUPPORTED"></a><dl>

### -field <b>Flags.GpuMmuSupported</b>


### -field <b>TRUE</b>

</dl>
</td>
<td width="60%">
<p>The adapter supports <i>GpuMmu</i>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Flags.MovePagingSupported"></a><a id="flags.movepagingsupported"></a><a id="FLAGS.MOVEPAGINGSUPPORTED"></a><dl>

### -field <b>Flags.MovePagingSupported</b>


### -field <b>TRUE</b>

</dl>
</td>
<td width="60%">
<p>The adapter supports move paging.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="Flags.VPRPagingContextRequired"></a><a id="flags.vprpagingcontextrequired"></a><a id="FLAGS.VPRPAGINGCONTEXTREQUIRED"></a><dl>

### -field <b>Flags.VPRPagingContextRequired</b>


### -field <b>TRUE</b>

</dl>
</td>
<td width="60%">
<p>The adapter requires the index of the VPR paging node.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>VPRPagingNode</b>

<dd>
<p>Index of the node to be used for move paging in  the VPR.</p>
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