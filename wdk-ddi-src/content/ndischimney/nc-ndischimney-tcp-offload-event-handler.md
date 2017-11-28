---
UID: NC.ndischimney.TCP_OFFLOAD_EVENT_HANDLER
title: TCP_OFFLOAD_EVENT_HANDLER
author: windows-driver-content
description: NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisTcpOffloadEventHandler function.
old-location: netvista\protocoltcpoffloadevent.htm
old-project: netvista
ms.assetid: b64c0f9e-aa3d-43c5-bdf5-c40cae3929e3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BINARY_DATA, BINARY_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolTcpOffloadEvent
req.alt-loc: Ndischimney.h
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

# TCP_OFFLOAD_EVENT_HANDLER callback



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>NDIS calls a protocol driver's or intermediate driver's 
  <i>ProtocolIndicateOffloadEvent</i> function to post an indication that was initiated by an underlying
  driver's or offload target's call to the 
  <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">
  NdisTcpOffloadEventHandler</a> function.</p>


## -prototype

````
TCP_OFFLOAD_EVENT_HANDLER ProtocolTcpOffloadEvent;

VOID ProtocolTcpOffloadEvent(
  _In_ PVOID OffloadContext,
  _In_ ULONG EventType,
  _In_ ULONG EventSpecificInformation
)
{ ... }
````


## -parameters
<dl>

### -param <i>OffloadContext</i> [in]

<dd>
<p>A pointer to the protocol or intermediate driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566705">NDIS_OFFLOAD_HANDLE</a> structure for the
     TCP connection on which the indication is being made. The protocol or intermediate driver supplied this
     pointer as an input parameter to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562743">NdisInitiateOffload</a> function when
     offloading the connection.</p>
</dd>

### -param <i>EventType</i> [in]

<dd>
<p>The event being indicated as one of the following TCP_OFFLOAD_EVENT_TYPE values:
     </p>
<p></p>
<dl>

### -param <a id="TcpIndicateDisconnect"></a><a id="tcpindicatedisconnect"></a><a id="TCPINDICATEDISCONNECT"></a><b>TcpIndicateDisconnect</b>

<dd>
<p>Indicates that the remote host initiated a graceful disconnect by sending a FIN segment on the
       connection.</p>
</dd>

### -param <a id="TcpIndicateRetrieve"></a><a id="tcpindicateretrieve"></a><a id="TCPINDICATERETRIEVE"></a><b>TcpIndicateRetrieve</b>

<dd>
<p>Indicates that the offload target is requesting the host stack to terminate the offload of a TCP
       connection.</p>
</dd>

### -param <a id="TcpIndicateAbort"></a><a id="tcpindicateabort"></a><a id="TCPINDICATEABORT"></a><b>TcpIndicateAbort</b>

<dd>
<p>Indicates that the remote host initiated an abortive disconnect by sending an acceptable RST
       segment on the connection.</p>
</dd>

### -param <a id="TcpIndicateSendBacklogChange"></a><a id="tcpindicatesendbacklogchange"></a><a id="TCPINDICATESENDBACKLOGCHANGE"></a><b>TcpIndicateSendBacklogChange</b>

<dd>
<p>Indicates a change in the preferred send backlog size.</p>
</dd>
</dl>
</dd>

### -param <i>EventSpecificInformation</i> [in]

<dd>
<p>Specifies additional information about the event being indicated as follows:
     </p>
<p></p>
<dl>

### -param <a id="TcpIndicateDisconnect"></a><a id="tcpindicatedisconnect"></a><a id="TCPINDICATEDISCONNECT"></a><b>TcpIndicateDisconnect</b>

<dd>
<p>Not meaningful.</p>
</dd>

### -param <a id="TcpIndicateRetrieve"></a><a id="tcpindicateretrieve"></a><a id="TCPINDICATERETRIEVE"></a><b>TcpIndicateRetrieve</b>

<dd>
<p>Indicates the reason for the upload request as a TCP_UPLOAD_REASON value. For more information,
       see 
       <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">
       NdisTcpOffloadEventHandler</a>.</p>
</dd>

### -param <a id="TcpIndicateAbort"></a><a id="tcpindicateabort"></a><a id="TCPINDICATEABORT"></a><b>TcpIndicateAbort</b>

<dd>
<p>Not meaningful.</p>
</dd>

### -param <a id="TcpIndicateSendBacklogChange"></a><a id="tcpindicatesendbacklogchange"></a><a id="TCPINDICATESENDBACKLOGCHANGE"></a><b>TcpIndicateSendBacklogChange</b>

<dd>
<p>Specifies the optimum number of send data bytes that the host stack should have outstanding at
       the offload target in order to achieve the best data throughput.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To propagate the indication to the overlying driver or host stack, the intermediate driver calls the 
    <b>NdisTcpOffloadEventHandler</b> function. The intermediate driver passes the following parameters to the
    
    <b>NdisTcpOffloadEventHandler</b> function:</p>

<p>The 
      <b>NdisOffloadHandle</b> that the offload target stored in its context for the offloaded TCP connection.
      For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The 
      <i>EventType</i> that NDIS passed to the intermediate driver's 
      <i>ProtocolTcpOffloadEvent</i> function.</p>

<p>The 
      <i>EventSpecificInformation</i> that NDIS passed to the intermediate driver's 
      <i>ProtocolTcpOffloadEvent</i> function.</p>

<p>To propagate the indication to the overlying driver or host stack, the intermediate driver calls the 
    <b>NdisTcpOffloadEventHandler</b> function. The intermediate driver passes the following parameters to the
    
    <b>NdisTcpOffloadEventHandler</b> function:</p>

<p>The 
      <b>NdisOffloadHandle</b> that the offload target stored in its context for the offloaded TCP connection.
      For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The 
      <i>EventType</i> that NDIS passed to the intermediate driver's 
      <i>ProtocolTcpOffloadEvent</i> function.</p>

<p>The 
      <i>EventSpecificInformation</i> that NDIS passed to the intermediate driver's 
      <i>ProtocolTcpOffloadEvent</i> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564595">NdisTcpOffloadEventHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20TCP_OFFLOAD_EVENT_HANDLER callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
