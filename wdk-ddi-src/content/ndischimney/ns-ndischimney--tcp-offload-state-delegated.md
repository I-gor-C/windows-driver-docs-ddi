---
UID: NS.ndischimney._TCP_OFFLOAD_STATE_DELEGATED
title: TCP_OFFLOAD_STATE_DELEGATED
author: windows-driver-content
description: The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state object.
old-location: netvista\tcp_offload_state_delegated.htm
old-project: netvista
ms.assetid: ab16cfa1-24f6-434a-a687-07e19172f185
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TCP_OFFLOAD_STATE_DELEGATED, TCP_OFFLOAD_STATE_DELEGATED, *PTCP_OFFLOAD_STATE_DELEGATED
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
req.alt-api: TCP_OFFLOAD_STATE_DELEGATED
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

# TCP_OFFLOAD_STATE_DELEGATED structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state
  object.</p>


## -syntax

````
typedef struct _TCP_OFFLOAD_STATE_DELEGATED {
  OFFLOAD_STATE_HEADER         Header;
  TCP_OFFLOAD_CONNECTION_STATE State;
  USHORT                       Flags;
  ULONG                        RcvNxt;
  ULONG                        RcvWnd;
  ULONG                        SndUna;
  ULONG                        SndNxt;
  ULONG                        SndMax;
  ULONG                        SndWnd;
  ULONG                        MaxSndWnd;
  ULONG                        SendWL1;
  ULONG                        CWnd;
  ULONG                        SsThresh;
  USHORT                       SRtt;
  USHORT                       RttVar;
  ULONG                        TsRecent;
  ULONG                        TsRecentAge;
  ULONG                        TsTime;
  ULONG                        TotalRT;
  UCHAR                        DupAckCount;
  UCHAR                        SndWndProbeCount;
  struct {
    UCHAR ProbeCount;
    ULONG TimeoutDelta;
  } KeepAlive;
  struct {
    UCHAR Count;
    ULONG TimeoutDelta;
  } Retransmit;
  union {
    struct {
      PNET_BUFFER_LIST SendDataHead;
      PNET_BUFFER_LIST SendDataTail;
    };
    ULONG  SendBacklogSize;
  };
  union {
    PNET_BUFFER_LIST BufferedData;
    ULONG            ReceiveBacklogSize;
  };
} TCP_OFFLOAD_STATE_DELEGATED, *PTCP_OFFLOAD_STATE_DELEGATED;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a> structure. NDIS
     sets the 
     <b>Length</b> member of 
     <b>Header</b> to the size, in bytes, of the TCP_OFFLOAD_STATE_DELEGATED structure. The 
     <b>RecognizedOptions</b> member of 
     <b>Header</b> is reserved.</p>
</dd>

### -field <b>State</b>

<dd>
<p>The current state of the TCP connection (see RFC 793) as one of the following
     TCP_OFFLOAD_CONNECTION_STATE values:
     </p>
<p></p>
<dl>

### -field <a id="TcpConnectionClosed"></a><a id="tcpconnectionclosed"></a><a id="TCPCONNECTIONCLOSED"></a><b>TcpConnectionClosed</b>

<dd>
<p>No connection state.</p>
</dd>

### -field <a id="TcpConnectionListen"></a><a id="tcpconnectionlisten"></a><a id="TCPCONNECTIONLISTEN"></a><b>TcpConnectionListen</b>

<dd>
<p>Waiting for a connection request from any remote TCP and port.</p>
</dd>

### -field <a id="TcpConnectionSynSent"></a><a id="tcpconnectionsynsent"></a><a id="TCPCONNECTIONSYNSENT"></a><b>TcpConnectionSynSent</b>

<dd>
<p>Waiting for a matching connection request after having sent a connection request.</p>
</dd>

### -field <a id="TcpConnectionSynRcvd"></a><a id="tcpconnectionsynrcvd"></a><a id="TCPCONNECTIONSYNRCVD"></a><b>TcpConnectionSynRcvd</b>

<dd>
<p>Waiting for a confirming connection request acknowledgment after having both received and sent a
       connection request.</p>
</dd>

### -field <a id="TcpConnectionEstablished"></a><a id="tcpconnectionestablished"></a><a id="TCPCONNECTIONESTABLISHED"></a><b>TcpConnectionEstablished</b>

<dd>
<p>An open connection: data received can be delivered to the user. The normal state for the data
       transfer phase of the connection.</p>
</dd>

### -field <a id="TcpConnectionFinWait1"></a><a id="tcpconnectionfinwait1"></a><a id="TCPCONNECTIONFINWAIT1"></a><b>TcpConnectionFinWait1</b>

<dd>
<p>Waiting for a connection termination request from the remote TCP, or an acknowledgment of the
       connection termination request that was previously sent.</p>
</dd>

### -field <a id="TcpConnectionFinWait2"></a><a id="tcpconnectionfinwait2"></a><a id="TCPCONNECTIONFINWAIT2"></a><b>TcpConnectionFinWait2</b>

<dd>
<p>Waiting for a connection termination request from the remote TCP.</p>
</dd>

### -field <a id="TcpConnectionCloseWait"></a><a id="tcpconnectionclosewait"></a><a id="TCPCONNECTIONCLOSEWAIT"></a><b>TcpConnectionCloseWait</b>

<dd>
<p>Waiting for a connection termination request from the local user.</p>
</dd>

### -field <a id="TcpConnectionClosing"></a><a id="tcpconnectionclosing"></a><a id="TCPCONNECTIONCLOSING"></a><b>TcpConnectionClosing</b>

<dd>
<p>Waiting for a connection termination request acknowledgment from the remote TCP.</p>
</dd>

### -field <a id="TcpConnectionLastAck"></a><a id="tcpconnectionlastack"></a><a id="TCPCONNECTIONLASTACK"></a><b>TcpConnectionLastAck</b>

<dd>
<p>Waiting for an acknowledgment of the connection termination request previously sent to the
       remote TCP, which includes an acknowledgment of its connection termination request.</p>
</dd>

### -field <a id="TcpConnectionTimeWait"></a><a id="tcpconnectiontimewait"></a><a id="TCPCONNECTIONTIMEWAIT"></a><b>TcpConnectionTimeWait</b>

<dd>
<p>Waiting for enough time to pass to ensure that the remote TCP received the acknowledgment of its
       connection termination request.</p>
</dd>
</dl>
<p> Note that the host stack can offload a TCP connection when the connection is in any state
     except 
     <b>TcpConnectionClosed</b>, 
     <b>TcpConnectionListen</b>, 
     <b>TcpConnectionSynRcvd</b>, 
     </p>
<p><b>TcpConnectionSynSent</b>, or 
     <b>TcpConnectionTimeWait</b> state. The host stack can query, update, invalidate, or terminate a TCP
     connection regardless of the connection state.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>RcvNxt</b>

<dd>
<p>The sequence number for the next receive segment (see RCV.NEXT in RFC 793).</p>
</dd>

### -field <b>RcvWnd</b>

<dd>
<p>The receive window size, in bytes (see RCV.WND in RFC 793).</p>
</dd>

### -field <b>SndUna</b>

<dd>
<p>The sequence number for the first byte of unacknowledged data (see SND.UNA in RFC 793). For more information, see <a href="NULL">Send Data That Contains Data to Be Retransmitted</a>.</p>
</dd>

### -field <b>SndNxt</b>

<dd>
<p>The sequence number for the next byte to send on the connection (see SND.NXT in RFC 793). For more information, see <a href="NULL">Send Data That Contains Data to Be Retransmitted</a>.</p>
</dd>

### -field <b>SndMax</b>

<dd>
<p>The maximum sequence number that has been sent on the connection. For more information, see <a href="NULL">Send Data That Contains Data to Be Retransmitted</a>.</p>
</dd>

### -field <b>SndWnd</b>

<dd>
<p>The send window size, in bytes (see SND.WND in RFC 793).</p>
</dd>

### -field <b>MaxSndWnd</b>

<dd>
<p>The maximum send window size, in bytes (see RFC 813).</p>
</dd>

### -field <b>SendWL1</b>

<dd>
<p>The segment sequence number used for the last window update (see SND.WL1 in RFC 793).</p>
</dd>

### -field <b>CWnd</b>

<dd>
<p>The congestion window size, in bytes (see cwnd in RFC 2581).</p>
</dd>

### -field <b>SsThresh</b>

<dd>
<p>The slow start threshold, in bytes (see ssthresh in RFC 2581).</p>
</dd>

### -field <b>SRtt</b>

<dd>
<p>The smoothed round-trip time, in clock ticks (see SRTT in RFCs 793 and 2988). Maintained on a per
     connection basis because it takes into account path, host, and sometimes application behavior.</p>
</dd>

### -field <b>RttVar</b>

<dd>
<p>The round trip time variation, in clock ticks (see RTTVAR in RFC 2988).</p>
</dd>

### -field <b>TsRecent</b>

<dd>
<p>The timestamp value to send in the next ACK (see TS.Recent in RFC 1323)</p>
</dd>

### -field <b>TsRecentAge</b>

<dd>
<p>The length of time, in clock ticks, since the most recent timestamp was received (see RFC
     1323).</p>
</dd>

### -field <b>TsTime</b>

<dd>
<p>The current value of the adjusted timestamp.</p>
</dd>

### -field <b>TotalRT</b>

<dd>
<p>The total time, in clock ticks, that has been spent retransmitting the current TCP segment.</p>
</dd>

### -field <b>DupAckCount</b>

<dd>
<p>The number of ACKs that have been accepted for the same sequence number (see RFC 1323).</p>
</dd>

### -field <b>SndWndProbeCount</b>

<dd>
<p>The current send window probe round. For a description of the send window probe round, see 
     <a href="NULL">Persist Timer</a>.</p>
</dd>

### -field <b>KeepAlive</b>

<dd>
<p>This member is a union that consists of the following members:</p>
<dl>

### -field <b>ProbeCount</b>

<dd>
<p>The number of keepalive probes that have been sent that have not received a response (see RFC
      1122).</p>
</dd>

### -field <b>TimeoutDelta</b>

<dd>
<p>The time remaining, in clock ticks, until the next keepalive timeout (see RFC 1122). Note that a
      value of -1 immediately after the TCP connection was offloaded indicates that the keepalive timer was
      not running when the connection was offloaded. If the offload target's keepalive timer is not running,
      the offload target should return -1 in this member when responding to a call to the
      MiniportQueryOffload function or the MiniportTerminateOffload function.</p>
</dd>
</dl>
</dd>

### -field <b>Retransmit</b>

<dd>
<p>This member is a union that consists of the following members:</p>
<dl>

### -field <b>Count</b>

<dd>
<p>The number of retransmits that have been sent (see RFC 2581).</p>
</dd>

### -field <b>TimeoutDelta</b>

<dd>
<p>The time, in clock ticks, remaining until the next retransmit timeout (see RFC 2581). Note that a
      value of -1 immediately after the TCP connection was offloaded indicates that the retransmit timer was
      not running when the connection was offloaded. The retransmit timer was not running because there was
      no outstanding send data on the connection when the connection was offloaded. If the offload target's
      retransmit timer is not running, the offload target should return -1 in this member when responding to
      a call to the MiniportQueryOffload function or the MiniportTerminateOffload function.</p>
</dd>
</dl>
</dd>

### -field <b>SendDataHead</b>

<dd>
<p>A pointer to a 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. This
       NET_BUFFER_LIST structure is in the linked list that is pointed to by the 
       <b>NetBufferListChain</b> member of the 
       <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that immediately precedes the
       TCP_OFFLOAD_STATE_DELEGATED structure. If the 
       <b>NetBufferListChain</b> pointer is <b>NULL</b>, 
       <b>SendDataHead</b> is not significant.
       </p>
<p>The 
       <b>SendDataHead</b> pointer points to the first NET_BUFFER_LIST structure whose NET_BUFFER structure
       has buffered the send data associated with it.</p>
<p>This variable is used only in an initiate offload or terminate offload operation. For more
       information about how this variable is used, see 
       <a href="NULL">Handling Outstanding Send Data During and After an Offload Operation</a> and 
       <a href="NULL">Handling Outstanding Send Data During a Terminate Offload Operation</a>.</p>
</dd>

### -field <b>SendDataTail</b>

<dd>
<p>A pointer to a 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. This
       NET_BUFFER_LIST structure is in the linked list that is pointed to by the NetBufferListChain member of
       the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure that immediately precedes the
       TCP_OFFLOAD_STATE_DELEGATED structure. If the NetBufferListChain pointer is <b>NULL</b>, SendDataTail is not
       significant.
       </p>
<p>The SendDataTail pointer points to the last NET_BUFFER_LIST structure whose NET_BUFFER structure
       has buffered the send data associated with it.</p>
<p>This variable is used only in an initiate offload or terminate offload operation. For more
       information about how this variable is used, see 
       <a href="netvista.handling_outstanding_send_data_during_and_after_an_offload_operation">Handling Outstanding Send Data During and After an Offload
       Operation</a> and 
       <a href="netvista.handling_outstanding_send_data_during_a_terminate_offload_operation">Handling Outstanding Send Data During a Terminate Offload
       Operation</a>
</p>
</dd>

### -field <b>SendBacklogSize</b>

<dd>
<p>The offload target specifies this value to indicate the number of data bytes that the host stack
       should have outstanding at the offload target for optimum performance. (This is the number of send
       bytes that have been passed to the offload target but that have not yet been completed by the offload
       target.) The specific variables and algorithm that the offload target uses to calculate the send
       backlog size are implementation-specific. The send backlog size can be a function of the roundtrip
       time (RTT) for the connection, the interface bandwidth, and other parameters. An offload target could,
       for example, use the minimum of the bandwidth/delay product and the advertised received window. Note
       however, that the send backlog size does not vary according to the number of data bytes that are
       currently posted for transmission on the connection.</p>
<p>The host stack can query the TCP delegated state for the connection to obtain the send backlog
       size. In addition, the offload target can indicate a change in the send backlog size by calling the 
       <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">
       NdisTcpOffloadEventHandler</a> function.</p>
<p>If the offload target does not support the send-backlog-size feature, it must write a value of
       0xFFFFFFFF to 
       <b>SendBacklogSize</b> when the TCP-delegated state for the connection is queried. The 
       <b>SendBacklogSize</b> variable is not used in the terminate offload operation.</p>
</dd>

### -field <b>BufferedData</b>

<dd>
<p>A pointer to buffered receive data. The host stack can pass such data to the offload target when
      offloading a TCP connection. (For more information, see 
      <a href="NULL">Handling Buffered Receive Data During and After an Offload Operation</a>.) The
      offload target can pass such data to the host stack when uploading a TCP connection. (For more
      information, see 
      <a href="NULL">Handling Buffered Receive Data During a Terminate Offload Operation</a>.)</p>
</dd>

### -field <b>ReceiveBacklogSize</b>

<dd>
<p>The offload target specifies this value to indicate the number of receive data bytes that are
      buffered in the offload target for the offloaded TCP connection. The host stack can query the TCP
      delegated state for the connection to obtain this value. The host stack uses this value to post one or
      more receive requests on the connection that are large enough to hold all of the buffered data.
      </p>
<p>If the offload target does not support the receive backlog size feature, it should write a value of
      0xFFFFFFFF to 
      <b>ReceiveBacklogSize</b> .</p>
</dd>
</dl>

## -remarks
<p>The host stack provides initial values for the TCP delegated variables when it offloads these
    variables to the offload target. After it is offloaded, the TCP delegated variables are owned and
    maintained by the offload target. Only the offload target can change the value of an offloaded TCP
    delegated variable. The offload target does not notify the host stack of changes to the values of
    offloaded TCP delegated variables. However, the host stack can query the value of offloaded TCP delegated
    variables, which causes NDIS to call the offload target's 
    <a href="..\ndischimney\nc-ndischimney-w-query-offload-handler.md">MiniportQueryOffload</a> function.
    When the host stack terminates the offload of the TCP connection state object by causing NDIS to call the
    offload target's 
    <a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">
    MiniportTerminateOffload</a> function, the offload target passes the value of the TCP delegated
    variables in the terminated TCP connection state object back to the host stack.</p>

<p>When passed to an offload target, a TCP_OFFLOAD_STATE_DELEGATED structure is associated with an 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure, which contains a header that is formatted as an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure. The
    Revision member of the NDIS_OBJECT_HEADER structure, in this case, specifies the revision number of the
    TCP_OFFLOAD_STATE_DELEGATED structure.</p>

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
<a href="..\ndischimney\nc-ndischimney-w-query-offload-handler.md">MiniportQueryOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">MiniportTerminateOffload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570937">TCP_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570938">TCP_OFFLOAD_STATE_CONST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20TCP_OFFLOAD_STATE_DELEGATED structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
