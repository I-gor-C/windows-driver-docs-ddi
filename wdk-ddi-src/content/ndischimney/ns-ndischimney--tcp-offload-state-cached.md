---
UID: NS.ndischimney._TCP_OFFLOAD_STATE_CACHED
title: TCP_OFFLOAD_STATE_CACHED
author: windows-driver-content
description: The TCP_OFFLOAD_STATE_CACHED structure contains the cached variables of a TCP connection state object.
old-location: netvista\tcp_offload_state_cached.htm
old-project: netvista
ms.assetid: 953154eb-e6f3-4013-a68f-1a358953c7ad
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TCP_OFFLOAD_STATE_CACHED, TCP_OFFLOAD_STATE_CACHED, *PTCP_OFFLOAD_STATE_CACHED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TCP_OFFLOAD_STATE_CACHED
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
req.iface: 
---

# TCP_OFFLOAD_STATE_CACHED structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The TCP_OFFLOAD_STATE_CACHED structure contains the cached variables of a TCP connection state
  object.</p>


## -syntax

````
typedef struct _TCP_OFFLOAD_STATE_CACHED {
  OFFLOAD_STATE_HEADER Header;
  USHORT               Flags;
  ULONG                InitialRcvWnd;
  ULONG                RcvIndicationSize;
  UCHAR                KaProbeCount;
  ULONG                KaTimeout;
  ULONG                KaInterval;
  ULONG                MaxRT;
  ULONG                FlowLabel  :20;
  UCHAR                TtlOrHopLimit;
  UCHAR                TosOrTrafficClass;
  UCHAR                UserPriority  :3;
} TCP_OFFLOAD_STATE_CACHED, *PTCP_OFFLOAD_STATE_CACHED;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a> structure. NDIS
     sets the 
     <b>Length</b> member of 
     <b>Header</b> to the size, in bytes, of the TCP_OFFLOAD_STATE_CACHED structure. The 
     <b>RecognizedOptions</b> member of 
     <b>Header</b> is reserved.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitmask that can be set to zero or any of the following flags, combined with bitwise OR: 
     </p>
<p></p>
<dl>

### -field <a id="TCP_FLAG_KEEP_ALIVE_ENABLED"></a><a id="tcp_flag_keep_alive_enabled"></a>TCP_FLAG_KEEP_ALIVE_ENABLED

<dd>
<p>The host stack sets this flag to enable the keepalive option on the connection. The host stack
       clears this flag to disable the keepalive option on the connection. For more information about the
       keepalive option, see RFC 1122.</p>
</dd>

### -field <a id="TCP_FLAG_NAGLING_ENABLED"></a><a id="tcp_flag_nagling_enabled"></a>TCP_FLAG_NAGLING_ENABLED

<dd>
<p>The host stack sets this flag to enable the Nagle algorithm on the connection. The host stack
       clears this flag to disable the Nagle algorithm on the connection. For more information about the
       Nagle algorithm, see RFC 896.</p>
</dd>

### -field <a id="TCP_FLAG_KEEP_ALIVE_RESTART"></a><a id="tcp_flag_keep_alive_restart"></a>TCP_FLAG_KEEP_ALIVE_RESTART

<dd>
<p>The host stack sets this flag to cause the offload target to reset its keepalive timer to
       zero.</p>
</dd>

### -field <a id="TCP_FLAG_MAX_RT_RESTART"></a><a id="tcp_flag_max_rt_restart"></a>TCP_FLAG_MAX_RT_RESTART

<dd>
<p>The host stack sets this flag to cause the offload target to reset the TotalRT variable in the
       TCP delegated state for the connection to zero.</p>
</dd>

### -field <a id="TCP_FLAG_UPDATE_RCV_WND"></a><a id="tcp_flag_update_rcv_wnd"></a>TCP_FLAG_UPDATE_RCV_WND

<dd>
<p>The host stack sets this flag to indicate that the default receive window size (InitialRcvWnd in
       the TCP_OFFLOAD_STATE_CACHED structure) has changed. If the value of InitialRcvWnd differs from the
       offload target's currrent receive window size (RcvWnd in the TCP_OFFLOAD_STATE_DELEGATED structure),
       the offload target must advertise a new receive window size to the peer.</p>
</dd>
</dl>
</dd>

### -field <b>InitialRcvWnd</b>

<dd>
<p>The default receive window (from socket option SO_RCVBUF).</p>
</dd>

### -field <b>RcvIndicationSize</b>

<dd>
<p>When non-<b>NULL</b>, the optimum number of data bytes that the offload target should supply in a single
     call to the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">
     NdisTcpOffloadReceiveHandler</a> function. This number, which is typically between tens and hundreds
     of bytes, is a suggestion--not a requirement. The offload target can indicate more or less than 
     <b>RcvIndicationSize</b> data bytes. However, for optimum performance, the offload target should indicate
     
     <b>RcvIndicationSize</b> data bytes. For more information, see 
     <b>
     NdisTcpOffloadReceiveHandler</b>.
     </p>
<p>When <b>NULL</b>, 
     <b>RcvIndicationSize</b> is unspecified. In this case, the offload target should ignore 
     <b>RcvIndicationSize</b> and indicate as much data as possible in calls to the 
     <i>NdisTcpOffloadReceiveHandler</i> function.</p>
</dd>

### -field <b>KaProbeCount</b>

<dd>
<p>The number of keepalive probes that the offload target should send to determine whether a TCP
     connection is intact (see RFC 1122).</p>
</dd>

### -field <b>KaTimeout</b>

<dd>
<p>This member specifies, in clock ticks, the timeout interval for inactivity before sending a
     keepalive probe (see RFC 1122).</p>
</dd>

### -field <b>KaInterval</b>

<dd>
<p>This member specifies, in clock ticks, the timeout after which to retransmit a keepalive frame if
     no response is received to a keepalive probe (see RFC 1122).</p>
</dd>

### -field <b>MaxRT</b>

<dd>
<p>This member specifies, in clock ticks, the maximum time that the offload target should spend
     retransmitting a segment. If the value of 
     <b>MaxRT</b> is non-zero, 
     <b>MaxRT</b> overrides 
     <b>TcpMaximumRetransmissions</b> in the 
     <a href="netvista.ndis_task_tcp_connection_offload">
     NDIS_TASK_TCP_CONNECTION_OFFLOAD</a> structure. The default value for is 
     <b>MaxRT</b> is zero, which means that 
     <b>TcpMaximumRetransmissions</b> sets the maximum number of times that the offload target should
     retransmit a segment on a TCP connection. If the value of 
     <b>MaxRT</b> is FFFFFFFF (or -1), there is no limit on the maximum number of retransmissions. When 
     <b>MaxRT</b> is nonzero, the offload target should reset the 
     <b>TotalRT</b> variable in the TCP delegated state for the connection. 
     <b>TotalRT</b> indicates the total time, in clock ticks, that the offload target has spent retransmitting
     the current TCP segment.</p>
</dd>

### -field <b>FlowLabel</b>

<dd>
<p>This member marks host-labeled packets for special handling by intervening routers--for example,
     nondefault QoS or "real-time" service (see RFC 2460). This variable is set through a socket option and
     can vary during the lifetime of the TCP connection. This variable is only meaningful if the TCP
     connection is over IPv6.</p>
</dd>

### -field <b>TtlOrHopLimit</b>

<dd>
<p>If the TCP connection is over IPv4, then this member specifies the time to live (see RFC 791).
     This variable is set through a socket option and can vary during the lifetime of the TCP connection. 
     </p>
<p>If the TCP connection is over IPv6, then this member specifies the number of routers that the packet
     can pass through (see RFC 2460). This variable is set through a socket option and can vary during the
     lifetime of the TCP connection.</p>
</dd>

### -field <b>TosOrTrafficClass</b>

<dd>
<p>If the TCP connection is over IPv4, then this member specifies the type of service for routing a
     packet (see RFC 2474). This variable is set through a socket option and can vary during the lifetime of
     the TCP connection. 
     </p>
<p>If the TCP connection is over IPv6, then this member prioritizes values for packets according to
     traffic types, indicating how willing the sender is to have the packets discarded (see RFC 2460). This
     variable is set through a socket option and can vary during the lifetime of the TCP
     connection.</p>
</dd>

### -field <b>UserPriority</b>

<dd>
<p>A 3-bit priority value. If the offload target supports 802.1p packet information, it must insert
     this priority value into the 
     <a href="https://msdn.microsoft.com/70dedf56-0591-4296-ad29-df3c48d06987">tag header</a> of all packets that it transmits
     on the offloaded TCP connection. If the offload target does not support 802.1p packet information, it
     should ignore 
     <b>UserPriority</b> . For more information about supporting 802.1p packet information, see 
     <a href="netvista.802_1q_and_802_1p_processing_on_an_offloaded_tcp_connection">802.1Q
     and 802.1p Processing on an Offloaded TCP Connection</a>.</p>
</dd>
</dl>

## -remarks
<p>Cached variables are owned and maintained by the host stack. An offload target must not change the
    value of a cached variable unless requested to do so by the host stack. If the value of a cached variable
    changes, the host stack requests an update of the variable, which causes NDIS to call the offload
    target's 
    <a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a> function.
    When the host stack terminates the offload of one or more state objects by causing NDIS to call the
    offload target's 
    <a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">
    MiniportTerminateOffload</a> function, the offload target does not return the value of offloaded
    constant variables to the host stack.</p>

<p>Note that if an offloaded TCP connection's TCP_FLAG_MAX_RT_RESTART flag is set, the offload target
    must:</p>

<p>Reset that connection's delegated KeepaliveProbeCount variable when the host stack updates that
      connection's cached KaProbeCount variable.</p>

<p>Reset that connection's delegated KeepaliveTimeoutDelta variable when the host stack updates that
      connection's cached KaTimeout and/or KaInterval variables.</p>

<p>When passed to an offload target, a TCP_OFFLOAD_STATE_CACHED structure is associated with an 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure, which contains a header that is formatted as an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure. The 
    <b>Revision</b> member of the NDIS_OBJECT_HEADER structure, in this case, specifies the revision number of
    the TCP_OFFLOAD_STATE_CACHED structure.</p>

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
<a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">MiniportTerminateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570938">TCP_OFFLOAD_STATE_CONST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570939">TCP_OFFLOAD_STATE_DELEGATED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20TCP_OFFLOAD_STATE_CACHED structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
