---
UID: NF.ndis.NdisSystemProcessorCount
title: NdisSystemProcessorCount
author: windows-driver-content
description: The NdisSystemProcessorCount function determines whether the caller is running on a uniprocessor or multiprocessor computer.
old-location: netvista\ndissystemprocessorcount.htm
ms.assetid: 17c7b02d-3d32-4056-9baa-2fef74765da3
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use NdisGroupMaxProcessorCount.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSystemProcessorCount
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisSystemProcessorCount
req.iface: 
---

# NdisSystemProcessorCount function



## -description
<p>The 
  <b>NdisSystemProcessorCount</b> function determines whether the caller is running on a uniprocessor or
  multiprocessor computer.</p>


## -syntax

````
CCHAR NdisSystemProcessorCount(void);
````


## -parameters


## -returns
<p><b>NdisSystemProcessorCount</b> returns the number of processors in the computer.</p>

<p><b>NdisSystemProcessorCount</b> returns the number of processors in the computer.</p>

<p><b>NdisSystemProcessorCount</b> returns the number of processors in the computer.</p>

## -remarks
<p>An NDIS driver can call the 
    <b>NdisSystemProcessorCount</b> function to retrieve the maximum number of processors in the local
    computer. To retrieve the number of currently active processors, the driver must call the 
    <a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
    NdisSystemActiveProcessorCount</a> function.</p>

<p><b>NdisSystemProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/bab2c478-4e46-40d9-a4b6-6f322b18ab0a">
    KeQueryMaximumProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemProcessorCount</b> returns does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have
    a statically sized array based on 
    <b>NdisSystemProcessorCount</b> or a dynamically sized array based on 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>To optimize your code based on the number of processors, you must use a resizable structure. In this
    case, use 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>If you are not optimizing and if the data structures that result from using the maximum processor
    count are relatively small, a resizable structure is not necessary. In this case, use 
    <b>NdisSystemProcessorCount</b> to determine the size for a static array.</p>

<p>An NDIS driver can call the 
    <b>NdisSystemProcessorCount</b> function to retrieve the maximum number of processors in the local
    computer. To retrieve the number of currently active processors, the driver must call the 
    <a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
    NdisSystemActiveProcessorCount</a> function.</p>

<p><b>NdisSystemProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/bab2c478-4e46-40d9-a4b6-6f322b18ab0a">
    KeQueryMaximumProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemProcessorCount</b> returns does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have
    a statically sized array based on 
    <b>NdisSystemProcessorCount</b> or a dynamically sized array based on 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>To optimize your code based on the number of processors, you must use a resizable structure. In this
    case, use 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>If you are not optimizing and if the data structures that result from using the maximum processor
    count are relatively small, a resizable structure is not necessary. In this case, use 
    <b>NdisSystemProcessorCount</b> to determine the size for a static array.</p>

<p>An NDIS driver can call the 
    <b>NdisSystemProcessorCount</b> function to retrieve the maximum number of processors in the local
    computer. To retrieve the number of currently active processors, the driver must call the 
    <a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
    NdisSystemActiveProcessorCount</a> function.</p>

<p><b>NdisSystemProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/bab2c478-4e46-40d9-a4b6-6f322b18ab0a">
    KeQueryMaximumProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemProcessorCount</b> returns does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have
    a statically sized array based on 
    <b>NdisSystemProcessorCount</b> or a dynamically sized array based on 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>To optimize your code based on the number of processors, you must use a resizable structure. In this
    case, use 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>If you are not optimizing and if the data structures that result from using the maximum processor
    count are relatively small, a resizable structure is not necessary. In this case, use 
    <b>NdisSystemProcessorCount</b> to determine the size for a static array.</p>

<p>An NDIS driver can call the 
    <b>NdisSystemProcessorCount</b> function to retrieve the maximum number of processors in the local
    computer. To retrieve the number of currently active processors, the driver must call the 
    <a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
    NdisSystemActiveProcessorCount</a> function.</p>

<p><b>NdisSystemProcessorCount</b> is similar to the 
    <a href="https://msdn.microsoft.com/bab2c478-4e46-40d9-a4b6-6f322b18ab0a">
    KeQueryMaximumProcessorCount</a> function.</p>

<p>The value that 
    <b>NdisSystemProcessorCount</b> returns does not change at runtime.</p>

<p>If your code uses an array of buffers, one buffer for each processor, you must decide whether to have
    a statically sized array based on 
    <b>NdisSystemProcessorCount</b> or a dynamically sized array based on 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>To optimize your code based on the number of processors, you must use a resizable structure. In this
    case, use 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564577">NdisSystemActiveProcessorCount</a>.</p>

<p>If you are not optimizing and if the data structures that result from using the maximum processor
    count are relatively small, a resizable structure is not necessary. In this case, use 
    <b>NdisSystemProcessorCount</b> to determine the size for a static array.</p>

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
<p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562689">NdisGroupMaxProcessorCount</a>.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/cd668a59-f74f-427b-880a-9352a7e09fa8">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553042">KeQueryMaximumProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562689">NdisGroupMaxProcessorCount</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7ddb54eb-9f20-4cb9-8488-5f2806d23430">
   NdisSystemActiveProcessorCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSystemProcessorCount function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
