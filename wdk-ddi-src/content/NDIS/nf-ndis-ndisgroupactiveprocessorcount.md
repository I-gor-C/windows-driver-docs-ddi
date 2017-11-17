---
UID: NF.ndis.NdisGroupActiveProcessorCount
title: NdisGroupActiveProcessorCount
author: windows-driver-content
description: The NdisGroupActiveProcessorCount function returns the number of processors that are currently active in a specified group.
old-location: netvista\ndisgroupactiveprocessorcount.htm
ms.assetid: d6631aa7-e3ba-4768-a55a-6a66d1ee84c6
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisGroupActiveProcessorCount
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
ms.keywords: NdisGroupActiveProcessorCount
req.iface: 
---

# NdisGroupActiveProcessorCount function



## -description
<p>The 
  <b>NdisGroupActiveProcessorCount</b> function returns the number of processors that are currently active in
  a specified group.</p>


## -syntax

````
ULONG NdisGroupActiveProcessorCount(
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
<p><b>NdisGroupActiveProcessorCount</b> returns a ULONG value for the number of processors that are active
      in the group that is specified in the 
      <i>Group</i> parameter. The number of processors is a zero-based value.</p>

<p>If the 
      <i>Group</i> parameter is ALL_PROCESSOR_GROUPS, 
      <b>NdisGroupActiveProcessorCount</b> returns the number of active processors in the local computer.</p>

## -remarks
<p>An NDIS driver might call the 
    <b>NdisGroupActiveProcessorCount</b> function during initialization before it allocates resources.</p>

<p>The processor count that 
    <a href="https://msdn.microsoft.com/92a50a96-8bfb-4d5d-8f24-dd29794e55b1">
    NdisGroupActiveProcessorMask</a> returns can change at runtime on SKUs that support hot-add
    functionality for CPUs.</p>

<p>To obtain an active affinity mask, call the 
    <a href="https://msdn.microsoft.com/92a50a96-8bfb-4d5d-8f24-dd29794e55b1">
    NdisGroupActiveProcessorMask</a> function.</p>

<p>To obtain the maximum number of processors in a group, call the 
    <a href="https://msdn.microsoft.com/545a5014-aa07-49ee-92b7-2ae95f4ce785">
    NdisGroupMaxProcessorCount</a> function.</p>

<p>An NDIS driver might call the 
    <b>NdisGroupActiveProcessorCount</b> function during initialization before it allocates resources.</p>

<p>The processor count that 
    <a href="https://msdn.microsoft.com/92a50a96-8bfb-4d5d-8f24-dd29794e55b1">
    NdisGroupActiveProcessorMask</a> returns can change at runtime on SKUs that support hot-add
    functionality for CPUs.</p>

<p>To obtain an active affinity mask, call the 
    <a href="https://msdn.microsoft.com/92a50a96-8bfb-4d5d-8f24-dd29794e55b1">
    NdisGroupActiveProcessorMask</a> function.</p>

<p>To obtain the maximum number of processors in a group, call the 
    <a href="https://msdn.microsoft.com/545a5014-aa07-49ee-92b7-2ae95f4ce785">
    NdisGroupMaxProcessorCount</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562687">NdisGroupActiveProcessorMask</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562689">NdisGroupMaxProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
   NdisSystemActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564579">NdisSystemProcessorCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGroupActiveProcessorCount function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
