---
UID: NF.wdm.KeQueryNodeActiveAffinity
title: KeQueryNodeActiveAffinity
author: windows-driver-content
description: The KeQueryNodeActiveAffinity routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture.
old-location: kernel\kequerynodeactiveaffinity.htm
old-project: kernel
ms.assetid: 49d4c9c7-217f-41b7-b870-886dd78e04a9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: KeQueryNodeActiveAffinity
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryNodeActiveAffinity
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# KeQueryNodeActiveAffinity function



## -description
<p>The <b>KeQueryNodeActiveAffinity</b> routine gets the current processor affinity of a specified node in a multiprocessor system that has a non-uniform memory access (NUMA) architecture.</p>


## -syntax

````
VOID KeQueryNodeActiveAffinity(
  _In_      USHORT          NodeNumber,
  _Out_opt_ PGROUP_AFFINITY Affinity,
  _Out_opt_ PUSHORT         Count
);
````


## -parameters
<dl>

### -param <i>NodeNumber</i> [in]

<dd>
<p>The node number. If a multiprocessor system contains <i>n</i> nodes, the nodes are numbered from 0 to <i>n</i>-1. To obtain the highest node number (<i>n</i>-1) in the system, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553020">KeQueryHighestNodeNumber</a> routine. </p>
</dd>

### -param <i>Affinity</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer into which the routine writes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a> structure. This structure contains the group number of the group that contains the node that is identified by <i>NodeNumber</i>, and an affinity mask that indicates which logical processors in the node are active. You can set this parameter to <b>NULL</b> if you do not need this information. </p>
</dd>

### -param <i>Count</i> [out, optional]

<dd>
<p>A pointer to a location into which the routine writes the number of active processors that are represented in the node affinity mask that is pointed to by <i>Affinity</i>. You can set this parameter to <b>NULL</b> if you do not need this information. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The caller-allocated buffer that is pointed to by the <i>Affinity</i> parameter must be large enough to contain a <b>GROUP_AFFINITY</b> structure. The <b>Mask</b> member of this structure contains an affinity mask that indicates which processors are active. If a processor is active, the corresponding bit in the mask is one. All other bits are zero.</p>

<p>In a NUMA multiprocessor architecture, a node is a collection of processors that share fast access to a region of memory. Memory access is non-uniform because a processor can access the memory in its node faster than it can access the memory in other nodes.</p>

<p>The number of processors in a node cannot exceed the number of bits in the affinity mask in the structure that is pointed to by <i>Affinity</i>. The affinity mask also determines the maximum number of processors in a group.</p>

<p>If, during system initialization, Windows encounters a NUMA hardware node that contains more logical processors than will fit into a group, Windows splits the node into smaller, logical nodes. Each of these nodes does not exceed the maximum group size. The <i>NodeNumber</i> parameter identifies a logical node. To obtain the maximum number of processors per group, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine.</p>

<p>The caller-allocated buffer that is pointed to by the <i>Affinity</i> parameter must be large enough to contain a <b>GROUP_AFFINITY</b> structure. The <b>Mask</b> member of this structure contains an affinity mask that indicates which processors are active. If a processor is active, the corresponding bit in the mask is one. All other bits are zero.</p>

<p>In a NUMA multiprocessor architecture, a node is a collection of processors that share fast access to a region of memory. Memory access is non-uniform because a processor can access the memory in its node faster than it can access the memory in other nodes.</p>

<p>The number of processors in a node cannot exceed the number of bits in the affinity mask in the structure that is pointed to by <i>Affinity</i>. The affinity mask also determines the maximum number of processors in a group.</p>

<p>If, during system initialization, Windows encounters a NUMA hardware node that contains more logical processors than will fit into a group, Windows splits the node into smaller, logical nodes. Each of these nodes does not exceed the maximum group size. The <i>NodeNumber</i> parameter identifies a logical node. To obtain the maximum number of processors per group, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a> routine.</p>

## -requirements
<table>
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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546539">GROUP_AFFINITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553020">KeQueryHighestNodeNumber</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553044">KeQueryMaximumProcessorCountEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeQueryNodeActiveAffinity routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
