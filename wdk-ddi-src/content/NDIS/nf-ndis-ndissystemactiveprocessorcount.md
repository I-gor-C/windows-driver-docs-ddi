---
UID: NF.ndis.NdisSystemActiveProcessorCount
title: NdisSystemActiveProcessorCount
author: windows-driver-content
description: The NdisSystemActiveProcessorCount function returns the number of currently active processors in the local computer.
old-location: netvista\ndissystemactiveprocessorcount.htm
ms.assetid: 7ddb54eb-9f20-4cb9-8488-5f2806d23430
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.1. For NDIS 6.20 and later, use NdisGroupActiveProcessorCount instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSystemActiveProcessorCount
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
ms.keywords: NdisSystemActiveProcessorCount
req.iface: 
---

# NdisSystemActiveProcessorCount function



## -description
<p>The 
  <b>NdisSystemActiveProcessorCount</b> function returns the number of currently active processors in the
  local computer.</p>


## -syntax

````
ULONG NdisSystemActiveProcessorCount(
   PKAFFINITY ActiveProcessors
);
````


## -parameters
<dl>

### -param <i>ActiveProcessors</i> 

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>-typed variable that receives a bitmap
     that represents the set of currently active processors. In a hot-add environment, this bitmap can change
     during runtime.</p>
</dd>
</dl>

## -returns
<p><b>NdisSystemActiveProcessorCount</b> returns the number of currently active processors in the local
     computer.</p>

## -remarks
<p>An NDIS driver might call the 
    <b>NdisSystemActiveProcessorCount</b> function during initialization before it allocates resources.</p>

<p><b>NdisSystemActiveProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/4369ad33-ba4a-45db-9a41-e77d6c55da53">
    KeQueryActiveProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemActiveProcessorCount</b> returns can change at runtime on SKUs that support hot-add CPU
    functionality.</p>

<p>The Windows Server 2008 Enterprise operating system and the Windows Server 2008 Datacenter operating
    system support 
    <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">dynamic hardware
    partitioning</a>. As part of dynamic hardware partitioning, Windows Server 2008 supports hot-add
    operations for CPUs at runtime. In a hot-add CPU environment, the number of processors might not remain
    constant during runtime.</p>

<p>An NDIS driver might call the 
    <b>NdisSystemActiveProcessorCount</b> function during initialization before it allocates resources.</p>

<p><b>NdisSystemActiveProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/4369ad33-ba4a-45db-9a41-e77d6c55da53">
    KeQueryActiveProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemActiveProcessorCount</b> returns can change at runtime on SKUs that support hot-add CPU
    functionality.</p>

<p>The Windows Server 2008 Enterprise operating system and the Windows Server 2008 Datacenter operating
    system support 
    <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">dynamic hardware
    partitioning</a>. As part of dynamic hardware partitioning, Windows Server 2008 supports hot-add
    operations for CPUs at runtime. In a hot-add CPU environment, the number of processors might not remain
    constant during runtime.</p>

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
<p>Supported in NDIS 6.1. For NDIS 6.20 and later, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562685">NdisGroupActiveProcessorCount</a> instead.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552985">KeQueryActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562685">NdisGroupActiveProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564579">NdisSystemProcessorCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSystemActiveProcessorCount function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
