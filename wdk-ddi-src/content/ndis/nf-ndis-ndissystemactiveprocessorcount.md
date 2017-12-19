---
UID: NF.ndis.NdisSystemActiveProcessorCount
title: NdisSystemActiveProcessorCount function
author: windows-driver-content
description: The NdisSystemActiveProcessorCount function returns the number of currently active processors in the local computer.
old-location: netvista\ndissystemactiveprocessorcount.htm
old-project: NetVista
ms.assetid: 7ddb54eb-9f20-4cb9-8488-5f2806d23430
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisSystemActiveProcessorCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
---

# NdisSystemActiveProcessorCount function



## -description
The 
  <b>NdisSystemActiveProcessorCount</b> function returns the number of currently active processors in the
  local computer.



## -syntax

````
ULONG NdisSystemActiveProcessorCount(
   PKAFFINITY ActiveProcessors
);
````


## -parameters

### -param ActiveProcessors 

A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>-typed variable that receives a bitmap
     that represents the set of currently active processors. In a hot-add environment, this bitmap can change
     during runtime.


## -returns
<b>NdisSystemActiveProcessorCount</b> returns the number of currently active processors in the local
     computer.


## -remarks
An NDIS driver might call the 
    <b>NdisSystemActiveProcessorCount</b> function during initialization before it allocates resources.

<b>NdisSystemActiveProcessorCount</b> is similar to the 
    <a href="kernel.kequeryactiveprocessorcount">
    KeQueryActiveProcessorCount</a> function.

The value that 
    <b>NdisSystemActiveProcessorCount</b> returns can change at runtime on SKUs that support hot-add CPU
    functionality.

The Windows Server 2008 Enterprise operating system and the Windows Server 2008 Datacenter operating
    system support 
    <a href="https://msdn.microsoft.com/1b6a1dc5-ec32-4bb9-acaf-14db284b4a0e">dynamic hardware
    partitioning</a>. As part of dynamic hardware partitioning, Windows Server 2008 supports hot-add
    operations for CPUs at runtime. In a hot-add CPU environment, the number of processors might not remain
    constant during runtime.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.1. For NDIS 6.20 and later, use <a href="netvista.ndisgroupactiveprocessorcount">NdisGroupActiveProcessorCount</a> instead.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>
</dt>
<dt>
<a href="kernel.kequeryactiveprocessorcount">KeQueryActiveProcessorCount</a>
</dt>
<dt>
<a href="netvista.ndisgroupactiveprocessorcount">NdisGroupActiveProcessorCount</a>
</dt>
<dt>
<a href="netvista.ndissystemprocessorcount">NdisSystemProcessorCount</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisSystemActiveProcessorCount function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

