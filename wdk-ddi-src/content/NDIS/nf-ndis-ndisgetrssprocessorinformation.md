---
UID: NF.ndis.NdisGetRssProcessorInformation
title: NdisGetRssProcessorInformation
author: windows-driver-content
description: The NdisGetRssProcessorInformation function retrieves information about the set of processors that a miniport driver must use for receive side scaling (RSS).
old-location: netvista\ndisgetrssprocessorinformation.htm
ms.assetid: 0da022d5-7294-4780-bab8-119ff6385abf
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
req.alt-api: NdisGetRssProcessorInformation
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisGetRssProcessorInformation
req.iface: 
---

# NdisGetRssProcessorInformation function



## -description
<p>The 
  <b>NdisGetRssProcessorInformation</b> function retrieves information about the set of processors that a
  miniport driver must use for receive side scaling (RSS).</p>


## -syntax

````
NDIS_STATUS NdisGetRssProcessorInformation(
  _In_      NDIS_HANDLE              NdisHandle,
  _Out_opt_ PNDIS_RSS_PROCESSOR_INFO RssProcessorInfo,
  _Inout_   PSIZE_T                  Size
);
````


## -parameters
<dl>

### -param <i>NdisHandle</i> [in]

<dd>
<p>An NDIS instance handle that was obtained during caller initialization. NDIS drivers can use the
     handles from the following functions:
     </p>
<dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</p>
</dd>
</dl>
</dd>

### -param <i>RssProcessorInfo</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer where NDIS puts the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff567274">NDIS_RSS_PROCESSOR_INFO</a> structure
     and an array of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff567271">NDIS_RSS_PROCESSOR</a> structures that
     contain information about the RSS processor set. The caller provides the length of the buffer in the 
     <i>Size</i> parameter.</p>
</dd>

### -param <i>Size</i> [in, out]

<dd>
<p>A pointer to a value that is the size, in bytes, of the buffer that the caller provided. When the
     function returns, this member contains either the amount of data that NDIS put in the buffer or the
     required size of the buffer if the buffer was too short.</p>
</dd>
</dl>

## -returns
<p><b>NdisGetRssProcessorInformation</b> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl><p>The size that was specified in 
       <i>Size</i> parameter was too small. In this case, NDIS provides the required buffer size in the 
       <i>Size</i> parameter.</p>

<p> </p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisGetRssProcessorInformation</b> function to retrieve information about the receive side scaling
    (RSS) processors on the local computer.</p>

<p>RSS-capable miniport drivers that support MSI-X call 
    <b>NdisGetRssProcessorInformation</b> in their 
    <a href="https://msdn.microsoft.com/8bddb6c5-367c-4862-bdb8-4974015750da">
    MiniportFilterResourceRequirements</a> function. Miniport drivers set the interrupt affinity of the
    allocated MSI-X messages to the RSS processors that are specified in the 
    <b>RssProcessors</b> member of the 
    <i>RssProcessorInfo</i> parameter.</p>

<p>NDIS drivers call the 
    <b>NdisGetRssProcessorInformation</b> function to retrieve information about the receive side scaling
    (RSS) processors on the local computer.</p>

<p>RSS-capable miniport drivers that support MSI-X call 
    <b>NdisGetRssProcessorInformation</b> in their 
    <a href="https://msdn.microsoft.com/8bddb6c5-367c-4862-bdb8-4974015750da">
    MiniportFilterResourceRequirements</a> function. Miniport drivers set the interrupt affinity of the
    allocated MSI-X messages to the RSS processors that are specified in the 
    <b>RssProcessors</b> member of the 
    <i>RssProcessorInfo</i> parameter.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/8bddb6c5-367c-4862-bdb8-4974015750da">
   MiniportFilterResourceRequirements</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567271">NDIS_RSS_PROCESSOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567274">NDIS_RSS_PROCESSOR_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisGetRssProcessorInformation function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
