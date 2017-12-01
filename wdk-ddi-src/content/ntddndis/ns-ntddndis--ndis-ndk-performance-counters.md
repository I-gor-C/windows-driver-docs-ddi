---
UID: NS.ntddndis._NDIS_NDK_PERFORMANCE_COUNTERS
title: NDIS_NDK_PERFORMANCE_COUNTERS
author: windows-driver-content
description: The NDIS_NDK_PERFORMANCE_COUNTERS structure contains the NDK performance counters.
old-location: netvista\ndis_ndk_performance_counters.htm
old-project: netvista
ms.assetid: DA752989-B49B-4832-8821-8B45AB3304CD
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_NDK_PERFORMANCE_COUNTERS, NDIS_NDK_PERFORMANCE_COUNTERS, *PNDIS_NDK_PERFORMANCE_COUNTERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NDK_PERFORMANCE_COUNTERS
req.alt-loc: ntddndis.h
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

# NDIS_NDK_PERFORMANCE_COUNTERS structure



## -description
<p>The <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure contains the NDK performance counters. </p>


## -syntax

````
typedef struct _NDIS_NDK_PERFORMANCE_COUNTERS {
  ULONG64 Connect;
  ULONG64 Accept;
  ULONG64 ConnectFailure;
  ULONG64 ConnectionError;
  ULONG64 ActiveConnection;
  ULONG64 Reserved01;
  ULONG64 Reserved02;
  ULONG64 Reserved03;
  ULONG64 Reserved04;
  ULONG64 Reserved05;
  ULONG64 Reserved06;
  ULONG64 Reserved07;
  ULONG64 Reserved08;
  ULONG64 Reserved09;
  ULONG64 Reserved10;
  ULONG64 Reserved11;
  ULONG64 Reserved12;
  ULONG64 Reserved13;
  ULONG64 Reserved14;
  ULONG64 Reserved15;
  ULONG64 Reserved16;
  ULONG64 Reserved17;
  ULONG64 Reserved18;
  ULONG64 Reserved19;
  ULONG64 Reserved20;
  ULONG64 CQError;
  ULONG64 RDMAInOctets;
  ULONG64 RDMAOutOctets;
  ULONG64 RDMAInFrames;
  ULONG64 RDMAOutFrames;
} NDIS_NDK_PERFORMANCE_COUNTERS, *PNDIS_NDK_PERFORMANCE_COUNTERS;
````


## -struct-fields
<dl>

### -field <b>Connect</b>

<dd>
<p>The number of outbound connections established. In a bitmask of counters (for example, <b>MissingCounterMask</b> member of the <a href="..\ntddndis\ns-ntddndis--ndis-ndk-capabilities.md">NDIS_NDK_CAPABILITIES</a> structure), this is counter 0.</p>
</dd>

### -field <b>Accept</b>

<dd>
<p>The number of inbound <i>RDMA</i> connections established. In a bitmask of counters (for example, <b>MissingCounterMask</b> member of the <a href="..\ntddndis\ns-ntddndis--ndis-ndk-capabilities.md">NDIS_NDK_CAPABILITIES</a> structure), this is counter 1.</p>
</dd>

### -field <b>ConnectFailure</b>

<dd>
<p>The  number of inbound and outbound <i>RDMA</i> connect attempts that  failed. In a bitmask of counters, this is counter 2.</p>
</dd>

### -field <b>ConnectionError</b>

<dd>
<p>The number of established connections with  an error before a consumer disconnected the connection. In a bitmask of counters, this is counter 3.</p>
</dd>

### -field <b>ActiveConnection</b>

<dd>
<p>The number of  active <i>RDMA</i> connections. In a bitmask of counters, this is counter 4.</p>
</dd>

### -field <b>Reserved01</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved02</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved03</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved04</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved05</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved06</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved07</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved08</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved09</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved10</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved11</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved12</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved13</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved14</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved15</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved16</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved17</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved18</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved19</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved20</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>CQError</b>

<dd>
<p>The number of <i>RDMA</i> completion queue (CQs) that went into an error state. In a bitmask of counters, this is counter 25.</p>
</dd>

### -field <b>RDMAInOctets</b>

<dd>
<p>The number of bytes  for all incoming <i>RDMA</i> traffic. This should include additional layer two protocol overhead.  In a bitmask of counters, this is counter 26.</p>
</dd>

### -field <b>RDMAOutOctets</b>

<dd>
<p>The number of bytes  for all outgoing <i>RDMA</i> traffic.  This should include additional layer two protocol overhead.  In a bitmask of counters, this is counter 27.</p>
</dd>

### -field <b>RDMAInFrames</b>

<dd>
<p>The number, in frames,  of layer two frames that carry incoming <i>RDMA</i> traffic. In a bitmask of counters, this is counter 28.</p>
</dd>

### -field <b>RDMAOutFrames</b>

<dd>
<p>The number, in frames,  of layer two frames that carry outgoing <i>RDMA</i> traffic. In a bitmask of counters, this is counter 29.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure is used in the <b>CounterSet</b>  member of the <a href="..\ntddndis\ns-ntddndis--ndis-ndk-statistics-info.md">NDIS_NDK_STATISTICS_INFO</a> structure. </p>

<p>NDK providers are required to support all the performance counters that are included
    in the <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure. However, in the rare case that
    a provider cannot support a counter due to extreme implementation difficulties,
    the provider must indicate any unsupported counters with the mask value for the
    counter which it cannot support. The <b>MissingCounterMask</b>  parameter of the <a href="..\ntddndis\ns-ntddndis--ndis-ndk-capabilities.md">NDIS_NDK_CAPABILITIES</a> structure specifies a bitmask that identifies counters that an NDK provider does not support.</p>

<p>All <b>ReservedXX</b> counters must be set to zero by providers and are ignored by NDIS. The term <i>RDMA</i> refers to all NDKPI and NDSPI activity as well as activity through any other RDMA programming interface that might be exposed by the provider. All providers must report the NDKPI and NDSPI activity with these counters, but reporting activity for other RDMA programming interfaces is not a strict requirement. The term <i>RDMA traffic</i> for the RDMA in, out, byte, and frame counters refers to all RDMA activity originating from NDKPI, NDSPI, and other RDMA programming interfaces (if any). This includes reads and writes (that is, direct data placement) as well as sends and receives. This also should also include all of the associated layer two protocol overhead. That is, <i>RDMA traffic</i> on an NDK-capable adapter includes all traffic through the adapter except for traffic that is  delivered through the standard NDIS send and receive interface and TCP chimney by NDIS protocol drivers.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
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
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ndk-capabilities.md">NDIS_NDK_CAPABILITIES</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-ndk-statistics-info.md">NDIS_NDK_STATISTICS_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NDK_PERFORMANCE_COUNTERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
