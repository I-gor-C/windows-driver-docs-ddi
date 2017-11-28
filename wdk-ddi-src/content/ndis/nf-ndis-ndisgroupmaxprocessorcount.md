---
UID: NF.ndis.NdisGroupMaxProcessorCount
title: NdisGroupMaxProcessorCount
author: windows-driver-content
description: The NdisGroupMaxProcessorCount function determines the maximum number of processors in a specified processor group.
old-location: netvista\ndisgroupmaxprocessorcount.htm
old-project: netvista
ms.assetid: 545a5014-aa07-49ee-92b7-2ae95f4ce785
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisGroupMaxProcessorCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGroupMaxProcessorCount
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisGroupMaxProcessorCount function



## -description
<p>The 
  <b>NdisGroupMaxProcessorCount</b> function determines the maximum number of processors in a specified
  processor group.</p>


## -syntax

````
ULONG NdisGroupMaxProcessorCount(
   USHORT Group
);
````


## -parameters
<dl>

### -param <i>Group</i> 

<dd>
<p>A USHORT value that identifies a processor group in the local computer system.</p>
</dd>
</dl>

## -returns
<p><b>NdisGroupMaxProcessorCount</b> returns a ULONG value for the maximum number of processors that are
      included in the group that is specified in the 
      <i>Group</i> parameter. The number of processors is a zero-based value.</p>

<p>If the 
      <i>Group</i> parameter is ALL_PROCESSOR_GROUPS, 
      <b>NdisGroupMaxProcessorCount</b> returns the maximum number of processors in the local computer.</p>

## -remarks
<p>An NDIS driver might call the 
    <b>NdisGroupMaxProcessorCount</b> function during initialization before it allocates resources.</p>

<p>The processor count can change at runtime on SKUs that support hot-add functionality for CPUs. To
    obtain an active processor count, call the 
    <a href="..\ndis\nf-ndis-ndisgroupactiveprocessorcount.md">
    NdisGroupActiveProcessorCount</a> function.</p>

<p>An NDIS driver might call the 
    <b>NdisGroupMaxProcessorCount</b> function during initialization before it allocates resources.</p>

<p>The processor count can change at runtime on SKUs that support hot-add functionality for CPUs. To
    obtain an active processor count, call the 
    <a href="..\ndis\nf-ndis-ndisgroupactiveprocessorcount.md">
    NdisGroupActiveProcessorCount</a> function.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="..\ndis\nf-ndis-ndisgroupactiveprocessorcount.md">
   NdisGroupActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564579">NdisSystemProcessorCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGroupMaxProcessorCount function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
