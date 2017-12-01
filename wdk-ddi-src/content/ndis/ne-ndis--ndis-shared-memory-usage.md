---
UID: NE.ndis._NDIS_SHARED_MEMORY_USAGE
title: NDIS_SHARED_MEMORY_USAGE
author: windows-driver-content
description: The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.
old-location: netvista\ndis_shared_memory_usage.htm
old-project: netvista
ms.assetid: c46102dd-26ea-459b-8cc2-f7e2d2e2f2ad
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SHARED_MEMORY_USAGE
req.alt-loc: ndis.h
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
req.iface: 
---

# NDIS_SHARED_MEMORY_USAGE enumeration



## -description
<p>The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used.</p>


## -syntax

````
typedef enum _NDIS_SHARED_MEMORY_USAGE { 
  NdisSharedMemoryUsageUndefined,
  NdisSharedMemoryUsageXmit,
  NdisSharedMemoryUsageXmitHeader,
  NdisSharedMemoryUsageXmitData,
  NdisSharedMemoryUsageReceive,
  NdisSharedMemoryUsageReceiveLookahead,
  NdisSharedMemoryUsageReceivePostLookahead,
  NdisSharedMemoryUsageReceiveHeader,
  NdisSharedMemoryUsageReceiveData,
  NdisSharedMemoryUsageOther,
  NdisSharedMemoryUsageMax
} NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE;
````


## -enum-fields
<dl>

### -field <a id="NdisSharedMemoryUsageUndefined"></a><a id="ndissharedmemoryusageundefined"></a><a id="NDISSHAREDMEMORYUSAGEUNDEFINED"></a><b>NdisSharedMemoryUsageUndefined</b>

<dd>
<p>The shared memory application is not defined.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageXmit"></a><a id="ndissharedmemoryusagexmit"></a><a id="NDISSHAREDMEMORYUSAGEXMIT"></a><b>NdisSharedMemoryUsageXmit</b>

<dd>
<p>The shared memory contains transmit data buffers.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageXmitHeader"></a><a id="ndissharedmemoryusagexmitheader"></a><a id="NDISSHAREDMEMORYUSAGEXMITHEADER"></a><b>NdisSharedMemoryUsageXmitHeader</b>

<dd>
<p>The shared memory contains transmit header buffers.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageXmitData"></a><a id="ndissharedmemoryusagexmitdata"></a><a id="NDISSHAREDMEMORYUSAGEXMITDATA"></a><b>NdisSharedMemoryUsageXmitData</b>

<dd>
<p>The shared memory contains transmit data.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageReceive"></a><a id="ndissharedmemoryusagereceive"></a><a id="NDISSHAREDMEMORYUSAGERECEIVE"></a><b>NdisSharedMemoryUsageReceive</b>

<dd>
<p>The shared memory contains receive data buffers.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageReceiveLookahead"></a><a id="ndissharedmemoryusagereceivelookahead"></a><a id="NDISSHAREDMEMORYUSAGERECEIVELOOKAHEAD"></a><b>NdisSharedMemoryUsageReceiveLookahead</b>

<dd>
<p>The shared memory contains receive lookahead buffers.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageReceivePostLookahead"></a><a id="ndissharedmemoryusagereceivepostlookahead"></a><a id="NDISSHAREDMEMORYUSAGERECEIVEPOSTLOOKAHEAD"></a><b>NdisSharedMemoryUsageReceivePostLookahead</b>

<dd>
<p>The shared memory contains received post lookahead information.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageReceiveHeader"></a><a id="ndissharedmemoryusagereceiveheader"></a><a id="NDISSHAREDMEMORYUSAGERECEIVEHEADER"></a><b>NdisSharedMemoryUsageReceiveHeader</b>

<dd>
<p>The shared memory contains receive header information.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageReceiveData"></a><a id="ndissharedmemoryusagereceivedata"></a><a id="NDISSHAREDMEMORYUSAGERECEIVEDATA"></a><b>NdisSharedMemoryUsageReceiveData</b>

<dd>
<p>The shared memory contains receive data.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageOther"></a><a id="ndissharedmemoryusageother"></a><a id="NDISSHAREDMEMORYUSAGEOTHER"></a><b>NdisSharedMemoryUsageOther</b>

<dd>
<p>The shared memory application is not specified.</p>
</dd>

### -field <a id="NdisSharedMemoryUsageMax"></a><a id="ndissharedmemoryusagemax"></a><a id="NDISSHAREDMEMORYUSAGEMAX"></a><b>NdisSharedMemoryUsageMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</p>
</dd>
</dl>

## -remarks
<p>The NDIS_SHARED_MEMORY_USAGE enumeration is used in the 
    <a href="..\ndis\ns-ndis--ndis-shared-memory-parameters.md">
    NDIS_SHARED_MEMORY_PARAMETERS</a> and 
    <a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
    NDIS_SCATTER_GATHER_LIST_PARAMETERS</a> structures.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-scatter-gather-list-parameters.md">
   NDIS_SCATTER_GATHER_LIST_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-shared-memory-parameters.md">NDIS_SHARED_MEMORY_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SHARED_MEMORY_USAGE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
