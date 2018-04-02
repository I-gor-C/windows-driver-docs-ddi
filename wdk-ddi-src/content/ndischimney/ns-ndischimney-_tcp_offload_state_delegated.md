---
UID: NS:ndischimney._TCP_OFFLOAD_STATE_DELEGATED
title: "_TCP_OFFLOAD_STATE_DELEGATED"
author: windows-driver-content
description: The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state object.
old-location: netvista\tcp_offload_state_delegated.htm
old-project: netvista
ms.assetid: ab16cfa1-24f6-434a-a687-07e19172f185
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PTCP_OFFLOAD_STATE_DELEGATED, PTCP_OFFLOAD_STATE_DELEGATED, PTCP_OFFLOAD_STATE_DELEGATED structure pointer [Network Drivers Starting with Windows Vista], TCP_OFFLOAD_STATE_DELEGATED, TCP_OFFLOAD_STATE_DELEGATED structure [Network Drivers Starting with Windows Vista], _TCP_OFFLOAD_STATE_DELEGATED, ndischimney/PTCP_OFFLOAD_STATE_DELEGATED, ndischimney/TCP_OFFLOAD_STATE_DELEGATED, netvista.tcp_offload_state_delegated, tcp_chim_struct_e835c163-e154-4b9c-b1bb-b658376fd89d.xml"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndischimney.h
api_name:
-	TCP_OFFLOAD_STATE_DELEGATED
product:
- Windows
targetos: Windows
req.typenames: TCP_OFFLOAD_STATE_DELEGATED, *PTCP_OFFLOAD_STATE_DELEGATED
---

# _TCP_OFFLOAD_STATE_DELEGATED structure
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]

The TCP_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a TCP connection state
  object.

## Syntax
```
typedef struct _TCP_OFFLOAD_STATE_DELEGATED {
  OFFLOAD_STATE_HEADER         Header;
  TCP_OFFLOAD_CONNECTION_STATE State;
  USHORT                       Flags;
  ULONG                        RcvNxt;
  ULONG                        RcvWnd;
  ULONG                        SndUna;
  ULONG                        SndNxt;
  ULONG                        SndMax;
  ULONG                        SndWnd;
  ULONG                        MaxSndWnd;
  ULONG                        SendWL1;
  ULONG                        CWnd;
  ULONG                        SsThresh;
  USHORT                       SRtt;
  USHORT                       RttVar;
  ULONG                        TsRecent;
  ULONG                        TsRecentAge;
  ULONG                        TsTime;
  ULONG                        TotalRT;
  UCHAR                        DupAckCount;
  UCHAR                        SndWndProbeCount;
  struct {
    UCHAR ProbeCount;
    ULONG TimeoutDelta;
  } KeepAlive;
  struct {
    UCHAR Count;
    ULONG TimeoutDelta;
  } Retransmit;
  union {
    struct {
      PNET_BUFFER_LIST SendDataHead;
      PNET_BUFFER_LIST SendDataTail;
    };
    ULONG SendBacklogSize;
  };
  union {
    PNET_BUFFER_LIST BufferedData;
    ULONG            ReceiveBacklogSize;
  };
  ULONG                        DWnd;
} *PTCP_OFFLOAD_STATE_DELEGATED, TCP_OFFLOAD_STATE_DELEGATED;
```

## Members


`Header`

An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a> structure. NDIS
     sets the 
     <b>Length</b> member of 
     <b>Header</b> to the size, in bytes, of the TCP_OFFLOAD_STATE_DELEGATED structure. The 
     <b>RecognizedOptions</b> member of 
     <b>Header</b> is reserved.

`State`

The current state of the TCP connection (see RFC 793) as one of the following
     TCP_OFFLOAD_CONNECTION_STATE values:
     





#### TcpConnectionClosed

No connection state.



#### TcpConnectionListen

Waiting for a connection request from any remote TCP and port.



#### TcpConnectionSynSent

Waiting for a matching connection request after having sent a connection request.



#### TcpConnectionSynRcvd

Waiting for a confirming connection request acknowledgment after having both received and sent a
       connection request.



#### TcpConnectionEstablished

An open connection: data received can be delivered to the user. The normal state for the data
       transfer phase of the connection.



#### TcpConnectionFinWait1

Waiting for a connection termination request from the remote TCP, or an acknowledgment of the
       connection termination request that was previously sent.



#### TcpConnectionFinWait2

Waiting for a connection termination request from the remote TCP.



#### TcpConnectionCloseWait

Waiting for a connection termination request from the local user.



#### TcpConnectionClosing

Waiting for a connection termination request acknowledgment from the remote TCP.



#### TcpConnectionLastAck

Waiting for an acknowledgment of the connection termination request previously sent to the
       remote TCP, which includes an acknowledgment of its connection termination request.



#### TcpConnectionTimeWait

Waiting for enough time to pass to ensure that the remote TCP received the acknowledgment of its
       connection termination request.

 Note that the host stack can offload a TCP connection when the connection is in any state
     except 
     <b>TcpConnectionClosed</b>, 
     <b>TcpConnectionListen</b>, 
     <b>TcpConnectionSynRcvd</b>, 
     

<b>TcpConnectionSynSent</b>, or 
     <b>TcpConnectionTimeWait</b> state. The host stack can query, update, invalidate, or terminate a TCP
     connection regardless of the connection state.

`Flags`

Reserved for system use.

`RcvNxt`

The sequence number for the next receive segment (see RCV.NEXT in RFC 793).

`RcvWnd`

The receive window size, in bytes (see RCV.WND in RFC 793).

`SndUna`

The sequence number for the first byte of unacknowledged data (see SND.UNA in RFC 793). For more information, see <a href="https://msdn.microsoft.com/38039411-1ef8-47a0-9a9a-de9451dc2cc9">Send Data That Contains Data to Be Retransmitted</a>.

`SndNxt`

The sequence number for the next byte to send on the connection (see SND.NXT in RFC 793). For more information, see <a href="https://msdn.microsoft.com/38039411-1ef8-47a0-9a9a-de9451dc2cc9">Send Data That Contains Data to Be Retransmitted</a>.

`SndMax`

The maximum sequence number that has been sent on the connection. For more information, see <a href="https://msdn.microsoft.com/38039411-1ef8-47a0-9a9a-de9451dc2cc9">Send Data That Contains Data to Be Retransmitted</a>.

`SndWnd`

The send window size, in bytes (see SND.WND in RFC 793).

`MaxSndWnd`

The maximum send window size, in bytes (see RFC 813).

`SendWL1`

The segment sequence number used for the last window update (see SND.WL1 in RFC 793).

`CWnd`

The congestion window size, in bytes (see cwnd in RFC 2581).

`SsThresh`

The slow start threshold, in bytes (see ssthresh in RFC 2581).

`SRtt`

The smoothed round-trip time, in clock ticks (see SRTT in RFCs 793 and 2988). Maintained on a per
     connection basis because it takes into account path, host, and sometimes application behavior.

`RttVar`

The round trip time variation, in clock ticks (see RTTVAR in RFC 2988).

`TsRecent`

The timestamp value to send in the next ACK (see TS.Recent in RFC 1323)

`TsRecentAge`

The length of time, in clock ticks, since the most recent timestamp was received (see RFC
     1323).

`TsTime`

The current value of the adjusted timestamp.

`TotalRT`

The total time, in clock ticks, that has been spent retransmitting the current TCP segment.

`DupAckCount`

The number of ACKs that have been accepted for the same sequence number (see RFC 1323).

`SndWndProbeCount`

The current send window probe round. For a description of the send window probe round, see 
     <a href="https://msdn.microsoft.com/b45f5fd7-e80b-4718-9889-9839fa61845a">Persist Timer</a>.

`KeepAlive`

This member is a union that consists of the following members:



#### ProbeCount

The number of keepalive probes that have been sent that have not received a response (see RFC
      1122).



#### TimeoutDelta

The time remaining, in clock ticks, until the next keepalive timeout (see RFC 1122). Note that a
      value of -1 immediately after the TCP connection was offloaded indicates that the keepalive timer was
      not running when the connection was offloaded. If the offload target's keepalive timer is not running,
      the offload target should return -1 in this member when responding to a call to the
      MiniportQueryOffload function or the MiniportTerminateOffload function.

`Retransmit`

This member is a union that consists of the following members:



#### Count

The number of retransmits that have been sent (see RFC 2581).



#### TimeoutDelta

The time, in clock ticks, remaining until the next retransmit timeout (see RFC 2581). Note that a
      value of -1 immediately after the TCP connection was offloaded indicates that the retransmit timer was
      not running when the connection was offloaded. The retransmit timer was not running because there was
      no outstanding send data on the connection when the connection was offloaded. If the offload target's
      retransmit timer is not running, the offload target should return -1 in this member when responding to
      a call to the MiniportQueryOffload function or the MiniportTerminateOffload function.

`DWnd`



## Remarks
The host stack provides initial values for the TCP delegated variables when it offloads these
    variables to the offload target. After it is offloaded, the TCP delegated variables are owned and
    maintained by the offload target. Only the offload target can change the value of an offloaded TCP
    delegated variable. The offload target does not notify the host stack of changes to the values of
    offloaded TCP delegated variables. However, the host stack can query the value of offloaded TCP delegated
    variables, which causes NDIS to call the offload target's 
    <a href="https://msdn.microsoft.com/a583c4cb-53c1-4eff-bcfe-c962f736b1f8">MiniportQueryOffload</a> function.
    When the host stack terminates the offload of the TCP connection state object by causing NDIS to call the
    offload target's 
    <a href="https://msdn.microsoft.com/1b808e3c-2d64-44c9-88d3-0a0311e1dc99">
    MiniportTerminateOffload</a> function, the offload target passes the value of the TCP delegated
    variables in the terminated TCP connection state object back to the host stack.

When passed to an offload target, a TCP_OFFLOAD_STATE_DELEGATED structure is associated with an 
    <a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure, which contains a header that is formatted as an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure. The
    Revision member of the NDIS_OBJECT_HEADER structure, in this case, specifies the revision number of the
    TCP_OFFLOAD_STATE_DELEGATED structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ndischimney.h (include Ndischimney.h) |

## See Also

<a href="https://msdn.microsoft.com/a583c4cb-53c1-4eff-bcfe-c962f736b1f8">MiniportQueryOffload</a>



<a href="https://msdn.microsoft.com/1b808e3c-2d64-44c9-88d3-0a0311e1dc99">MiniportTerminateOffload</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569062">OFFLOAD_STATE_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570937">TCP_OFFLOAD_STATE_CACHED</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff570938">TCP_OFFLOAD_STATE_CONST</a>