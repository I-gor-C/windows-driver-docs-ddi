---
UID: NF.fwpsk.FwpsInjectTransportSendAsync1
title: FwpsInjectTransportSendAsync1
author: windows-driver-content
description: The FwpsInjectTransportSendAsync1 function injects packet data from the transport, datagram data, or ICMP error layers into the send data path.
old-location: netvista\fwpsinjecttransportsendasync1.htm
ms.assetid: 74d91e43-d58a-4c2c-bfc9-4b0829a5f9f8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectTransportSendAsync1
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsInjectTransportSendAsync1
req.iface: 
---

# FwpsInjectTransportSendAsync1 function



## -description
<p>The 
  <b>FwpsInjectTransportSendAsync1</b> function injects packet data from the transport, datagram data, or ICMP
  error layers into the send data path. This function differs from the previous version
  (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551188">FwpsInjectTransportSendAsync0</a>) in that it takes an updated parameters structure as an argument.</p>


## -syntax

````
NTSTATUS NTAPI FwpsInjectTransportSendAsync1(
  _In_     HANDLE                      injectionHandle,
  _In_opt_ HANDLE                      injectionContext,
  _In_     UINT64                      endpointHandle,
  _In_     UINT32                      flags,
  _In_opt_ FWPS_TRANSPORT_SEND_PARAMS1 *sendArgs,
  _In_     ADDRESS_FAMILY              addressFamily,
  _In_     COMPARTMENT_ID              compartmentId,
  _Inout_  NET_BUFFER_LIST             *netBufferList,
  _In_     FWPS_INJECT_COMPLETE0       completionFn,
  _In_opt_ HANDLE                      completionContext
);
````


## -parameters
<dl>

### -param <i>injectionHandle</i> [in]

<dd>
<p>An injection handle that was previously created by a call to the 
     <a href="https://msdn.microsoft.com/61cee8ef-1070-46d4-a541-94a9f09b593b">
     FwpsInjectionHandleCreate0</a> function.</p>
</dd>

### -param <i>injectionContext</i> [in, optional]

<dd>
<p>An optional handle to the injection context. If specified, it can be obtained by calling the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551202">FwpsQueryPacketInjectionState0</a> function when the packet injection state 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> is
     <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>.</p>
</dd>

### -param <i>endpointHandle</i> [in]

<dd>
<p>A handle that indicates the stack transport endpoint in the send data path into which the packet
     is to be injected. This endpoint handle is provided to a callout through the 
     <b>transportEndpointHandle</b> member of the 
     <a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. Callout
     drivers should use the provided handle to inject cloned packets back into the data path as soon as
     possible, before the socket associated with the stack endpoint is closed and the handle becomes no
     longer valid.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>This parameter is reserved. Callout drivers must set this parameter to zero.</p>
</dd>

### -param <i>sendArgs</i> [in, optional]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/8d5653e4-a755-4066-b25a-f8f589821412">
     FWPS_TRANSPORT_SEND_PARAMS1</a> structure that specifies the properties of the current outbound
     packet. This parameter can be <b>NULL</b> only if the net buffer list to be injected contains an IP header (for
     example, if the packet is sent through a raw socket).</p>
</dd>

### -param <i>addressFamily</i> [in]

<dd>
<p>One of the following address families:
     </p>
<p></p>
<dl>

### -param <a id="AF_INET"></a><a id="af_inet"></a>AF_INET

<dd>
<p>The IPv4 address family.</p>
</dd>

### -param <a id="AF_INET6"></a><a id="af_inet6"></a>AF_INET6

<dd>
<p>The IPv6 address family.</p>
</dd>
</dl>
</dd>

### -param <i>compartmentId</i> [in]

<dd>
<p>The identifier of the routing compartment into which the packet data is injected, specified as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff542009">COMPARTMENT_ID</a> type. This identifier is provided
     to a callout through the 
     <b>compartmentId</b> member of the 
     <a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function. If the 
     <b>compartmentId</b> member is available to callouts, FWPS_METADATA_FIELD_COMPARTMENT_ID will be set in
     the 
     <b>currentMetadataValues</b> member. Otherwise, set this parameter to UNSPECIFIED_COMPARTMENT_ID.</p>
</dd>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that describes
     the packet data that is being injected. A callout driver allocates a <b>NET_BUFFER_LIST</b> structure to use to
     inject packet data by calling either the 
     <a href="https://msdn.microsoft.com/72759748-fac6-45b9-9a81-ab71e6e7c3ef">
     FwpsAllocateCloneNetBufferList0</a> function or the 
     <a href="https://msdn.microsoft.com/d7f2d3c0-f2c9-4624-b3e1-9fbbf64c7186">
     FwpsAllocateNetBufferAndNetBufferList0</a> function.</p>
</dd>

### -param <i>completionFn</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a> callout function provided by
     the callout driver. The filter engine calls this function after the packet data, described by the 
     <i>netBufferList</i> parameter, has been injected into the network stack.</p>
</dd>

### -param <i>completionContext</i> [in, optional]

<dd>
<p>A pointer to a callout driver-provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsInjectTransportSendAsync1</b> function returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The packet data injection was initiated successfully. The filter engine will call the completion
       function after the filter engine has completed injecting the packet data into the network stack, or
       when an error occurred subsequently. In case of an error, the 
       <b>Status</b> member of the completed 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure will indicate
       the reason for failure.</p><dl>
<dt><b>STATUS_FWP_TCPIP_NOT_READY</b></dt>
</dl><p>The TCP/IP network stack is not ready to accept injection of packet data.</p><dl>
<dt><b>STATUS_FWP_INJECT_HANDLE_CLOSING</b></dt>
</dl><p>The injection handle is being closed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
     function to inject packet data from the transport, datagram data, or
    ICMP error layers into the send data path. At these layers, the IP header might no<b>FwpsInjectTransportSendAsync1</b>t yet be formed, and
    when IPsec policy is active, the packet data is not encrypted or signed. Therefore, this function is
    ideal to use for packet inspection in an IPsec-enabled environment.</p>

<p>This function can execute asynchronously.</p>

<p>If the return value is not <b>STATUS_SUCCESS</b>, the completion function will not be called. In this case,
    the net buffer list pointed to by 
    <i>netBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>.</p>

<p>Callout drivers normally inject data into the network stack when they modify packet data. For more
    information about how a callout driver can modify packet data, see 
    <a href="NULL">Callout Driver Operations</a>.</p>

<p>The injected packet can be indicated to the callout driver again. To prevent infinite looping, the
    driver should first call the 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a> function before calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function, and permit
    packets that have the injection state 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> set to
    <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>.</p>

<p>The 
    <i>endpointHandle</i> parameter and members declared in the 
    
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552423">FWPS_TRANSPORT_SEND_PARAMS1</a> structure pointed to by the 
    <i>sendArgs</i> parameter are provided to callouts from the following network layers:</p>

<p>
<dl>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>
</dd>
</dl>
</p><dl>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>
</dd>
</dl><p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>

<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>

<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>

<p>The datagram belongs to a raw socket if both of the following are true: <ul>
<li>The <b>currentMetadataValues</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure has the <b>FWPS_METADATA_FIELD_IP_HEADER_SIZE</b> flag set.</li>
<li>The <b>ipHeaderSize</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure is greater than zero.</li>
</ul>
</p>

<p>At the following network layers, if the datagram belongs to a raw socket, you'll need to copy the <b>headerIncludeHeader</b> and <b>headerIncludeHeaderLength</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure into the corresponding member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552423">FWPS_TRANSPORT_SEND_PARAMS1</a> structure that the <i>sendArgs</i> parameter points to:<ul>
<li>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</li>
<li>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</li>
</ul>
</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>A callout driver calls the 
     function to inject packet data from the transport, datagram data, or
    ICMP error layers into the send data path. At these layers, the IP header might no<b>FwpsInjectTransportSendAsync1</b>t yet be formed, and
    when IPsec policy is active, the packet data is not encrypted or signed. Therefore, this function is
    ideal to use for packet inspection in an IPsec-enabled environment.</p>

<p>This function can execute asynchronously.</p>

<p>If the return value is not <b>STATUS_SUCCESS</b>, the completion function will not be called. In this case,
    the net buffer list pointed to by 
    <i>netBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>.</p>

<p>Callout drivers normally inject data into the network stack when they modify packet data. For more
    information about how a callout driver can modify packet data, see 
    <a href="NULL">Callout Driver Operations</a>.</p>

<p>The injected packet can be indicated to the callout driver again. To prevent infinite looping, the
    driver should first call the 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a> function before calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function, and permit
    packets that have the injection state 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> set to
    <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>.</p>

<p>The 
    <i>endpointHandle</i> parameter and members declared in the 
    
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552423">FWPS_TRANSPORT_SEND_PARAMS1</a> structure pointed to by the 
    <i>sendArgs</i> parameter are provided to callouts from the following network layers:</p>

<p>
<dl>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>
</dd>
</dl>
</p><dl>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>
</dd>
<dd>
<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>
</dd>
</dl><p>FWPS_LAYER_OUTBOUND_TRANSPORT_V4</p>

<p>FWPS_LAYER_OUTBOUND_TRANSPORT_V6</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4</p>

<p>FWPS_LAYER_OUTBOUND_ICMP_ERROR_V6</p>

<p>The datagram belongs to a raw socket if both of the following are true: <ul>
<li>The <b>currentMetadataValues</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure has the <b>FWPS_METADATA_FIELD_IP_HEADER_SIZE</b> flag set.</li>
<li>The <b>ipHeaderSize</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure is greater than zero.</li>
</ul>
</p>

<p>At the following network layers, if the datagram belongs to a raw socket, you'll need to copy the <b>headerIncludeHeader</b> and <b>headerIncludeHeaderLength</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure into the corresponding member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552423">FWPS_TRANSPORT_SEND_PARAMS1</a> structure that the <i>sendArgs</i> parameter points to:<ul>
<li>
<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</li>
<li>
<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>
</li>
</ul>
</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V4 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

<p>FWPS_LAYER_DATAGRAM_DATA_V6 (when outbound direction is specified with FWP_DIRECTION_OUTBOUND)</p>

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
<p>Available starting with  Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c03656ec-f0fe-49f5-8a04-2d26ef23c50a">completionFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552423">FWPS_TRANSPORT_SEND_PARAMS1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/72759748-fac6-45b9-9a81-ab71e6e7c3ef">
   FwpsAllocateCloneNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d7f2d3c0-f2c9-4624-b3e1-9fbbf64c7186">
   FwpsAllocateNetBufferAndNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551188">FwpsInjectTransportSendAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
   FwpsQueryPacketInjectionState0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectTransportSendAsync1 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
