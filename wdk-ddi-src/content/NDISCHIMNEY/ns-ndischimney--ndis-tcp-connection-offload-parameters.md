---
UID: NS.ndischimney._NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS
title: NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS
author: windows-driver-content
description: The NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure provides TCP chimney offload information in the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OIDs:
old-location: netvista\ndis_tcp_connection_offload_parameters.htm
ms.assetid: f8d3f971-2abc-425d-9929-518f093262a7
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS
req.alt-loc: ndischimney.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS, NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS, *PNDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS
req.iface: 
---

# NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure provides TCP chimney offload information in the 
  <a href="netvista.oid_tcp_connection_offload_parameters">
  OID_TCP_CONNECTION_OFFLOAD_PARAMETERS</a> OIDs:</p>


## -syntax

````
typedef struct _NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS {
  NDIS_OBJECT_HEADER         Header;
  NDIS_OFFLOAD_ENCAPSULATION Encapsulation;
  ULONG                      TicksPerSecond;
  UCHAR                      TcpAckFrequency;
  UCHAR                      TcpDelayedAckTicks;
  UCHAR                      TcpMaximumRetransmissions;
  UCHAR                      TcpDoubtReachabilityRetransmissions;
  ULONG                      TcpSwsPreventionTicks;
  ULONG                      TcpDuplicateAckThreshold;
  ULONG                      TcpPushTicks;
  ULONG                      NceStaleTicks;
#if (NDIS_SUPPORT_NDIS61)
  ULONG                      CongestionAlgorithm  :4;
#endif 
} NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS, *PNDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to 
     <b>NDIS_OBJECT_TYPE_DEFAULT</b>, the 
     <b>Revision</b> member to 
     <b>NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS_ 1</b>, and the 
     <b>Size</b> member to 
     <code>sizeof(NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS)</code>.</p>
</dd>

### -field <b>Encapsulation</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/19013ffa-6bb5-4a77-b85b-c32fb0bf0530">
     NDIS_OFFLOAD_ENCAPSULATION</a> structure that contains encapsulation settings for TCP chimney
     offload.</p>
</dd>

### -field <b>TicksPerSecond</b>

<dd>
<p>A ULONG value that the TCP/IP driver stack sets to specify how many ticks of the host's clock
     equal one second. The default value is 1000 (that is, 1 tick = 1 millisecond). An offload target must
     support this member.</p>
</dd>

### -field <b>TcpAckFrequency</b>

<dd>
<p>A UCHAR value that the TCP/IP driver stack sets to specify the maximum number of segments that the
     offload target can receive before the target sends an ACK. An offload target must support this
     member.</p>
</dd>

### -field <b>TcpDelayedAckTicks</b>

<dd>
<p>A UCHAR value that the TCP/IP driver stack sets to specify how many ticks, starting from the
     reception of a segment, that the offload target should wait for additional receive segments before the
     target sends an ACK. An offload target uses this value to initialize its delayed-ACK timer. An offload
     target must support this member.</p>
</dd>

### -field <b>TcpMaximumRetransmissions</b>

<dd>
<p>A UCHAR value that the TCP/IP driver stack sets to specify the maximum number of times that the
     offload target should retransmit a segment on a TCP connection. When the retransmit counter for a TCP
     connection exceeds this limit, the offload target can call the 
     <a href="https://msdn.microsoft.com/b62e8a07-fe7b-4c52-8795-19e4bb889b6e">
     NdisTcpOffloadEventHandler</a> function with an 
     <b>EventType</b> parameter of 
     <b>TcpIndicateRetrieve</b> to request that the TCP/IP driver stack terminate the
     offload of the connection. An offload target must support this member.</p>
</dd>

### -field <b>TcpDoubtReachabilityRetransmissions</b>

<dd>
<p>A UCHAR value that the TCP/IP driver stack sets to specify the maximum number of times that the
     offload target should retransmit a segment before the target indicates to the TCP/IP driver stack that
     the reachability of a neighbor is in doubt. For more information about this indication, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563619">NdisMOffloadEventIndicate</a>. An
     offload target should support this member.</p>
</dd>

### -field <b>TcpSwsPreventionTicks</b>

<dd>
<p>A ULONG value that the TCP/IP driver stack sets to specify the number of ticks for the offload
     target's silly window syndrome (SWS) send and receive timers. When the SWS send timer times out, the
     offload target sends a partial segment. When the SWS receive timer times out, the offload target sends a
     window update. An offload target should support this member.</p>
</dd>

### -field <b>TcpDuplicateAckThreshold</b>

<dd>
<p>A ULONG value that the TCP/IP driver stack sets to specify the number of duplicate acknowledgments
     that the offload target must receive before the target performs a fast retransmission. An offload target
     must support this member.</p>
</dd>

### -field <b>TcpPushTicks</b>

<dd>
<p>A ULONG value that the TCP/IP driver stack sets to specify the number of ticks that an offload
     target must wait before the target completes a pre-posted receive buffer. This interval starts
     immediately after the offload target places the first byte in the pre-posted receive buffer. An offload
     target uses this value to initialize its push timer. An offload target must support this member.</p>
</dd>

### -field <b>NceStaleTicks</b>

<dd>
<p>A ULONG value that the TCP/IP driver stack sets to indicate the number of ticks of inactivity that
     make a neighbor state object stale. An offload target must support this member.</p>
</dd>

### -field <b>CongestionAlgorithm</b>

<dd>
<p>Reserved for future use.
     </p>
<p>If you are an independent hardware vendor (IHV) and you want to implement nondefault congestion
     control algorithms, for example Compound TCP, contact Microsoft at 
     <a href="mailto:offloadt@microsoft.com">External TCP Offload Triage</a>.</p>
</dd>
</dl>

## -remarks
<p>In NDIS 6.0 and later versions, the NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure specifies the
    current or requested parameters that a miniport adapter provides for TCP chimney offload.</p>

<p>To specify various offload parameter settings, NDIS and overlying drivers supply an
    NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure when they set the 
    <a href="netvista.oid_tcp_connection_offload_parameters">
    OID_TCP_CONNECTION_OFFLOAD_PARAMETERS</a> OID.</p>

<p>To obtain the current settings of various offload parameters, NDIS and overlying drivers query
    OID_TCP_CONNECTION_OFFLOAD_PARAMETERS. The miniport driver returns the current settings in the
    NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure.</p>

<p>The 
    <b>Encapsulation</b> member of NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS defines the TCP
    chimney offload encapsulation settings for the miniport adapter. For more information, see the 
    <a href="netvista.full_tcp_offload">NDIS 6.0 TCP chimney offload
    documentation</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Full TCP Offload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566702">NDIS_OFFLOAD_ENCAPSULATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563619">NdisMOffloadEventIndicate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564595">NdisTcpOffloadEventHandler</a>
</dt>
<dt>
<a href="netvista.oid_tcp_connection_offload_parameters">
   OID_TCP_CONNECTION_OFFLOAD_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
