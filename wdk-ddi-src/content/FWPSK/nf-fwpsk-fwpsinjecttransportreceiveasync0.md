---
UID: NF.fwpsk.FwpsInjectTransportReceiveAsync0
title: FwpsInjectTransportReceiveAsync0
author: windows-driver-content
description: The FwpsInjectTransportReceiveAsync0 function injects packet data from the transport, datagram data, or ICMP error layers into the receive data path.Note  FwpsInjectTransportReceiveAsync0 is a specific version of FwpsInjectTransportReceiveAsync.
old-location: netvista\fwpsinjecttransportreceiveasync0.htm
ms.assetid: 0809a013-9977-44fc-b800-576b4fd983e8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectTransportReceiveAsync0
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
ms.keywords: FwpsInjectTransportReceiveAsync0
req.iface: 
---

# FwpsInjectTransportReceiveAsync0 function



## -description
<p>The 
  <b>FwpsInjectTransportReceiveAsync0</b> function injects packet data from the transport, datagram data, or
  ICMP error layers into the receive data path.</p>


## -syntax

````
NTSTATUS NTAPI FwpsInjectTransportReceiveAsync0(
  _In_       HANDLE                injectionHandle,
  _In_opt_   HANDLE                injectionContext,
  _Reserved_ PVOID                 reserved,
  _In_       UINT32                flags,
  _In_       ADDRESS_FAMILY        addressFamily,
  _In_       COMPARTMENT_ID        compartmentId,
  _In_       IF_INDEX              interfaceIndex,
  _In_       IF_INDEX              subInterfaceIndex,
  _Inout_    NET_BUFFER_LIST       *netBufferList,
  _In_       FWPS_INJECT_COMPLETE0 completionFn,
  _In_opt_   HANDLE                completionContext
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

### -param <i>reserved</i> 

<dd>
<p>Reserved. Callout drivers must set this parameter to zero.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>Reserved. Callout drivers must set this parameter to zero.</p>
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
     <b>compartmentId</b> member is available to callouts, <b>FWPS_METADATA_FIELD_COMPARTMENT_ID</b> will be set in
     the 
     <b>currentMetadataValues</b> member. Otherwise, set this parameter to <b>UNSPECIFIED_COMPARTMENT_ID</b>.</p>
</dd>

### -param <i>interfaceIndex</i> [in]

<dd>
<p>The index of the interface on which the original packet data was received. A callout driver should
     use the value of the interface index that is passed as one of the incoming data values to its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function for this
     parameter if the packet is to be injected into the same interface where the original packet was
     indicated.</p>
</dd>

### -param <i>subInterfaceIndex</i> [in]

<dd>
<p>The index of the subinterface on which the original packet data was received. A callout driver
     should use the value of the subinterface index that is passed as one of the incoming data values to its 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function for this
     parameter if the packet is to be injected into the same subinterface where the original packet was
     indicated.</p>
</dd>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that describes
     the packet data that is being injected. A callout driver allocates a <b>NET_BUFFER_LIST</b> structure to use to
     inject packet data by calling either the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551134">FwpsAllocateCloneNetBufferList0</a> function or the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a> function. The <b>NET_BUFFER_LIST</b> structure must begin with an
     IP header.</p>
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
<p>A pointer to a callout driver–provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsInjectTransportReceiveAsync0</b> function returns one of the following <b>NTSTATUS</b> codes.</p><dl>
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
    <b>FwpsInjectTransportReceiveAsync0</b> function to inject packet data from the transport, datagram data,
    or ICMP error layers into the receive data path. This function can execute asynchronously. Callout
    drivers normally inject data into the network stack when modifying packet data. For more information
    about how a callout driver can modify packet data, see 
    <a href="NULL">Callout Driver Operations</a>.</p>

<p>If a callout driver modified a packet that it will inject with 
    <b>FwpsInjectTransportReceiveAsync0</b>, it should call the 
    <a href="https://msdn.microsoft.com/badb7e91-1d5f-42c3-973b-c7d756d24a01">
    FwpsConstructIpHeaderForTransportPacket0</a> function to correct the IP and upper-level protocol (TCP,
    UDP, and ICMP) checksums. The 
    <i>headerIncludeHeaderSize</i> parameter of 
    <b>FwpsConstructIpHeaderForTransportPacket0</b> should be the same value as the 
    <b>ipHeaderSize</b> member of the 
    <a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
    FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the <i>inMetaValues</i> parameter of the
    callout driver's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>

<p>If the return value is not <b>STATUS_SUCCESS</b>, the completion function will not be called. In this case,
    the net buffer list pointed to by 
    <i>netBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/0d0dea63-de0d-4421-b123-ce31ac6af1d9">
    FwpsFreeCloneNetBufferList0</a>.</p>

<p>If the original inbound packet data had been subject to IPsec policy enforcement when it was
    originally processed by the transport layer, the cloned packet injected by this function will bypass
    IPsec verification when it reenters the network stack. Locally generated inbound packets that use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a> function also bypass IPsec verification.</p>

<p>To allow IPsec to process inbound packets first, the callout that inspects the transport layer data
    must have a lower value of 
    <b>subLayerWeight</b> in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a> structure than the universal
    sublayer. In addition, the callout driver must not intercept tunnel-mode packets for which the
    combination of 
    <a href="https://msdn.microsoft.com/ac5994a7-411c-47f2-ba1d-2d49c727de8d">
    FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0</a> members (
    <b>isTunnelMode</b> &amp;&amp; !
    <b>isDeTunneled</b> ) is returned by the 
    <a href="https://msdn.microsoft.com/c3391615-963b-4916-9280-ce782269692c">
    FwpsGetPacketListSecurityInformation0</a> function. The callout driver must wait for the packet to be
    detunneled and then should intercept it at the transport layer or at a forward layer.</p>

<p>This function can be called from one of the following transport layers if the
    <b>FWPS_METADATA_FIELD_ALE_CLASSIFY_REQUIRED</b> metadata flag is not set:</p><dl>
<dd>
<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V6</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_DATAGRAM_DATA_V4</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>
</dd>
<dd>
<p><b>FWPS_LAYER_DATAGRAM_DATA_V6</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</b></p>
</dd>
</dl><p><b>FWPS_LAYER_INBOUND_TRANSPORT_V4</b></p>

<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V6</b></p>

<p><b>FWPS_LAYER_DATAGRAM_DATA_V4</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>

<p><b>FWPS_LAYER_DATAGRAM_DATA_V6</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>

<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</b></p>

<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</b></p>

<p>Otherwise, this function should be called from the following Application Layer Enforcement (ALE) layers
    after a pended ALE operation was initiated with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551199">FwpsPendOperation0</a> and has completed
    with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a>:</p><dl>
<dd>
<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</b></p>
</dd>
</dl><p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</b></p>

<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</b></p>

<p>A net buffer list to be injected must be passed to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a> function as the 
    <i>netBufferList</i> argument.</p>

<p>The injected packet can be indicated to the callout driver again. To prevent infinite looping, the
    driver should first call the 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a> function before proceeding with a call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function, and the driver
    should permit packets that have the injection state 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> set to
    <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b> to pass through unaltered.</p>

<p>A callout driver calls the 
    <b>FwpsInjectTransportReceiveAsync0</b> function to inject packet data from the transport, datagram data,
    or ICMP error layers into the receive data path. This function can execute asynchronously. Callout
    drivers normally inject data into the network stack when modifying packet data. For more information
    about how a callout driver can modify packet data, see 
    <a href="NULL">Callout Driver Operations</a>.</p>

<p>If a callout driver modified a packet that it will inject with 
    <b>FwpsInjectTransportReceiveAsync0</b>, it should call the 
    <a href="https://msdn.microsoft.com/badb7e91-1d5f-42c3-973b-c7d756d24a01">
    FwpsConstructIpHeaderForTransportPacket0</a> function to correct the IP and upper-level protocol (TCP,
    UDP, and ICMP) checksums. The 
    <i>headerIncludeHeaderSize</i> parameter of 
    <b>FwpsConstructIpHeaderForTransportPacket0</b> should be the same value as the 
    <b>ipHeaderSize</b> member of the 
    <a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
    FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the <i>inMetaValues</i> parameter of the
    callout driver's 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function.</p>

<p>If the return value is not <b>STATUS_SUCCESS</b>, the completion function will not be called. In this case,
    the net buffer list pointed to by 
    <i>netBufferList</i> must be freed by a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a> or 
    <a href="https://msdn.microsoft.com/0d0dea63-de0d-4421-b123-ce31ac6af1d9">
    FwpsFreeCloneNetBufferList0</a>.</p>

<p>If the original inbound packet data had been subject to IPsec policy enforcement when it was
    originally processed by the transport layer, the cloned packet injected by this function will bypass
    IPsec verification when it reenters the network stack. Locally generated inbound packets that use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551135">FwpsAllocateNetBufferAndNetBufferList0</a> function also bypass IPsec verification.</p>

<p>To allow IPsec to process inbound packets first, the callout that inspects the transport layer data
    must have a lower value of 
    <b>subLayerWeight</b> in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a> structure than the universal
    sublayer. In addition, the callout driver must not intercept tunnel-mode packets for which the
    combination of 
    <a href="https://msdn.microsoft.com/ac5994a7-411c-47f2-ba1d-2d49c727de8d">
    FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0</a> members (
    <b>isTunnelMode</b> &amp;&amp; !
    <b>isDeTunneled</b> ) is returned by the 
    <a href="https://msdn.microsoft.com/c3391615-963b-4916-9280-ce782269692c">
    FwpsGetPacketListSecurityInformation0</a> function. The callout driver must wait for the packet to be
    detunneled and then should intercept it at the transport layer or at a forward layer.</p>

<p>This function can be called from one of the following transport layers if the
    <b>FWPS_METADATA_FIELD_ALE_CLASSIFY_REQUIRED</b> metadata flag is not set:</p><dl>
<dd>
<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V6</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_DATAGRAM_DATA_V4</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>
</dd>
<dd>
<p><b>FWPS_LAYER_DATAGRAM_DATA_V6</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</b></p>
</dd>
</dl><p><b>FWPS_LAYER_INBOUND_TRANSPORT_V4</b></p>

<p><b>FWPS_LAYER_INBOUND_TRANSPORT_V6</b></p>

<p><b>FWPS_LAYER_DATAGRAM_DATA_V4</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>

<p><b>FWPS_LAYER_DATAGRAM_DATA_V6</b> (when inbound direction is specified with <b>FWP_DIRECTION_INBOUND</b>)</p>

<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V4</b></p>

<p><b>FWPS_LAYER_INBOUND_ICMP_ERROR_V6</b></p>

<p>Otherwise, this function should be called from the following Application Layer Enforcement (ALE) layers
    after a pended ALE operation was initiated with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551199">FwpsPendOperation0</a> and has completed
    with a call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a>:</p><dl>
<dd>
<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</b></p>
</dd>
<dd>
<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</b></p>
</dd>
</dl><p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V4</b></p>

<p><b>FWPS_LAYER_ALE_AUTH_RECV_ACCEPT_V6</b></p>

<p>A net buffer list to be injected must be passed to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a> function as the 
    <i>netBufferList</i> argument.</p>

<p>The injected packet can be indicated to the callout driver again. To prevent infinite looping, the
    driver should first call the 
    <a href="https://msdn.microsoft.com/785d99a5-a8c9-4763-bdd4-e26f604f6be7">
    FwpsQueryPacketInjectionState0</a> function before proceeding with a call to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function, and the driver
    should permit packets that have the injection state 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a> set to
    <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b> to pass through unaltered.</p>

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
<p>Available starting with Windows Vista.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552391">FWPS_FILTER_CONDITION0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fba7eb60-0d19-4bfd-b484-2e615d3e9237">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552408">FWPS_PACKET_INJECTION_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ac5994a7-411c-47f2-ba1d-2d49c727de8d">
   FWPS_PACKET_LIST_INBOUND_IPSEC_INFORMATION0</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551152">FwpsCompleteOperation0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551172">FwpsFreeNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551170">FwpsFreeCloneNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c3391615-963b-4916-9280-ce782269692c">
   FwpsGetPacketListSecurityInformation0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551180">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551181">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551185">FwpsInjectNetworkSendAsync0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551199">FwpsPendOperation0</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectTransportReceiveAsync0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
