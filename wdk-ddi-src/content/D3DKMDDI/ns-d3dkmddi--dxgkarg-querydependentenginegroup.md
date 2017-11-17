---
UID: NS.d3dkmddi._DXGKARG_QUERYDEPENDENTENGINEGROUP
title: DXGKARG_QUERYDEPENDENTENGINEGROUP
author: windows-driver-content
description: Describes all nodes on the physical display adapter (engine) that are to be queried when the display port driver's GPU scheduler calls the DxgkDdiQueryDependentEngineGroup function to query node dependencies.
old-location: display\dxgkarg_querydependentenginegroup.htm
ms.assetid: 6b1d6465-83bd-42c4-be1f-d7a2cfb74483
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_QUERYDEPENDENTENGINEGROUP
req.alt-loc: D3dkmddi.h
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
ms.keywords: DXGKARG_QUERYDEPENDENTENGINEGROUP, DXGKARG_QUERYDEPENDENTENGINEGROUP
req.iface: 
---

# DXGKARG_QUERYDEPENDENTENGINEGROUP structure



## -description
<p>Describes all nodes on the physical display adapter (engine) that are to be queried when the display port driver's GPU scheduler calls the <a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a> function to query node dependencies.</p>


## -syntax

````
typedef struct _DXGKARG_QUERYDEPENDENTENGINEGROUP {
  UINT      NodeOrdinal;
  UINT      EngineOrdinal;
  ULONGLONG DependentNodeOrdinalMask;
} DXGKARG_QUERYDEPENDENTENGINEGROUP;
````


## -struct-fields
<dl>

### -field <b>NodeOrdinal</b>

<dd>
<p>[in] An index of a node within the physical adapter defined by   the <b>EngineOrdinal</b> member that is being queried in a call to <a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>.</p>
</dd>

### -field <b>EngineOrdinal</b>

<dd>
<p>[in] An index that defines the physical adapter in a linked display adapter (LDA) configuration that the node defined by <b>NodeOrdinal</b> belongs to.</p>
</dd>

### -field <b>DependentNodeOrdinalMask</b>

<dd>
<p>[out] The bitmask that describes all dependent nodes that will be affected by a reset operation.</p>
</dd>
</dl>

## -remarks
<p>The index value <b>EngineOrdinal</b> is assumed to be identical for all dependent nodes.</p>

<p>See Remarks of  <a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a> for a discussion of how to compute the bitmask in the <b>DependentNodeOrdinalMask</b> member.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/5BC4F94C-2B45-44E2-8BBF-B455BB864A29">TDR changes in Windows 8</a>.</p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/42040ffc-40a3-4794-805c-7a165c47c8c9">DxgkDdiQueryDependentEngineGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9c2097b2-5742-422c-a650-7efff2484970">DxgkDdiResetEngine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_QUERYDEPENDENTENGINEGROUP structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
