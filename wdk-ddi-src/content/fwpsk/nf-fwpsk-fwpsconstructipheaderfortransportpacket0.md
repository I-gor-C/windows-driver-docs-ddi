---
UID: NF.fwpsk.FwpsConstructIpHeaderForTransportPacket0
title: FwpsConstructIpHeaderForTransportPacket0
author: windows-driver-content
description: The FwpsConstructIpHeaderForTransportPacket0 function is called by a callout to construct a new IP header or to rebuild a preexisting IP packet header for only one net buffer.Note  FwpsConstructIpHeaderForTransportPacket0 is a specific version of FwpsConstructIpHeaderForTransportPacket. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwpsconstructipheaderfortransportpacket0.htm
old-project: netvista
ms.assetid: badb7e91-1d5f-42c3-973b-c7d756d24a01
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FwpsConstructIpHeaderForTransportPacket0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsConstructIpHeaderForTransportPacket0
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
req.iface: 
---

# FwpsConstructIpHeaderForTransportPacket0 function



## -description
<p>The 
  <b>FwpsConstructIpHeaderForTransportPacket0</b> function is called by a callout to construct a new IP header
  or to rebuild a preexisting IP packet header for only one net buffer.</p>


## -syntax

````
NTSTATUS NTAPI FwpsConstructIpHeaderForTransportPacket0(
  _Inout_          NET_BUFFER_LIST *netBufferList,
  _In_             ULONG           headerIncludeHeaderSize,
  _In_             ADDRESS_FAMILY  addressFamily,
  _In_       const UCHAR           *sourceAddress,
  _In_       const UCHAR           *remoteAddress,
  _In_             IPPROTO         nextProtocol,
  _In_opt_         UINT64          endpointHandle,
  _In_opt_   const WSACMSGHDR      *controlData,
  _In_             ULONG           controlDataLength,
  _In_             UINT32          flags,
  _Reserved_       PVOID           reserved,
  _In_opt_         IF_INDEX        interfaceIndex,
  _In_opt_         IF_INDEX        subInterfaceIndex
);
````


## -parameters
<dl>

### -param netBufferList [in, out]

<dd>
<p>A pointer to a 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure that describes
     the cloned transport layer packet data for which a new IP header is to be constructed or rebuilt. To
     construct a new IP header, locate the offset of the cloned NET_BUFFER_LIST structure at the beginning of
     the transport header. To rebuild a preexisting IP packet header, locate the offset at the beginning of
     the IP header.</p>
</dd>

### -param headerIncludeHeaderSize [in]

<dd>
<p>If the NET_BUFFER_LIST structure pointed to by 
     <i>NetBufferList</i> already contains an IP header, indicates the total size, in bytes, of the existing
     IP header (if it exists). If 
     <i>NetBufferList</i> does not contain an IP header, 
     <i>headerIncludeHeaderSize</i> is zero. Otherwise, the value of this parameter is equal to the 
     <b>ipHeaderSize</b> member of the 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function. Note that
     extension headers for an existing IPv6 header will be removed when this function is called, although
     IPv4 options will be preserved. For more information, see Remarks.</p>
</dd>

### -param addressFamily [in]

<dd>
<p>One of the following address families:
     </p>
<p></p>
<dl>

### -param AF_INET

<dd>
<p>The IPv4 address family.</p>
</dd>

### -param AF_INET6

<dd>
<p>The IPv6 address family.</p>
</dd>
</dl>
</dd>

### -param sourceAddress [in]

<dd>
<p>A pointer to the source IP address that will be part of the IP header to be constructed. For IPv4,
     the address is 4 bytes. For IPv6, the address is 16 bytes. The source address bytes are always in
     network byte order.</p>
</dd>

### -param remoteAddress [in]

<dd>
<p>A pointer to a buffer that specifies the remote IP address that will be part of the IP header to
     be constructed.
     </p>
<p>The buffer can contain an IPv4 address (4 bytes) or an IPv6 address (16 bytes), and the address must
     be specified in network byte order. The IP version must match the 
     <i>addressFamily</i> parameter.</p>
</dd>

### -param nextProtocol [in]

<dd>
<p>Specifies the IPPROTO protocol type of the new IP header to be constructed. For more information
     on the IPPROTO enumeration, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff543744">AF_INET</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff543746">AF_INET6</a>.</p>
</dd>

### -param endpointHandle [in, optional]

<dd>
<p>An optional handle that indicates the stack transport endpoint in the send data path into which
     the packet is to be injected. This endpoint handle is provided to a callout through the 
     <b>transportEndpointHandle</b> member of the 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function.</p>
</dd>

### -param controlData [in, optional]

<dd>
<p>An optional pointer to a buffer that contains socket control data specified by the 
     <b>WSASendMsg</b> function, which is described in the Microsoft Windows SDK documentation. For
     information about the WSACMSGHDR type, see 
     <a href="netvista.cmsghdr">CMSGHDR</a>.
     </p>
<p>If present, socket control data is provided to a callout with the 
     <b>controlData</b> member of the 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> callout function.</p>
<p>If socket control data is not <b>NULL</b>, it must be deep-copied in the callout driver's implementation of
     the 
     <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> function, and the 
     <b>controlData</b> buffer must be kept valid until the injection completion function is
     called.</p>
</dd>

### -param controlDataLength [in]

<dd>
<p>The length, in bytes, of the 
     <i>controlData</i> parameter.</p>
</dd>

### -param flags [in]

<dd>
<p>Reserved. Callout drivers must set this parameter to zero.</p>
</dd>

### -param reserved 

<dd>
<p>Reserved. Callout drivers must set this parameter to <b>NULL</b>.</p>
</dd>

### -param interfaceIndex [in, optional]

<dd>
<p>The index of the interface on which the original packet data was received. A callout driver should use the value of the interface index that is passed as one of the incoming data values to its <a href="netvista.classifyfn">classifyFn</a> callout function for this parameter. This parameter is optional and can be zero.</p>
</dd>

### -param subInterfaceIndex [in, optional]

<dd>
<p>The index of the subinterface on which the original packet data was received. A callout driver
     should use the value of the subinterface index that is passed as one of the incoming data values to its 
     <a href="netvista.classifyfn">classifyFn</a> callout function for this
     parameter if the packet is to be injected into the same subinterface where the original packet was
     indicated. This parameter is optional and can be zero.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsConstructIpHeaderForTransportPacket0</b> function returns one of the following NTSTATUS
     codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A new IP header was successfully constructed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>From a net buffer list cloned at a WFP outbound transport layer (FWPS_LAYER_OUTBOUND_TRANSPORT_Xxx), 
    <b>FwpsConstructIpHeaderForTransportPacket0</b> constructs a new header for each net buffer that is part
    of the net buffer list chain. This function can also be used to rebuild the preexisting IP header of a
    packet, in which case the net buffer list must contain only one net buffer.</p>

<p>This function is useful when the IP header has not yet been created, but the source IP address or the
    source port must be modified from the transport layer. Although it would ordinarily be possible to
    wait to perform such modifications until the packet reaches the Network layer, this cannot be done in an
    IPsec environment in which IP packets are encrypted or digitally signed before they reach the Network
    layer.</p>

<p>The source IP address can be modified to be another locally defined IP address or another address that
    does not exist on the local computer. Packets so modified can then be sent or injected into the receive
    or forwarding data path.</p>

<p>If a nonzero 
    <i>endpointHandle</i> parameter is specified, session states (socket options), if any, associated with the
    socket will be used to construct each new IP header. Similarly, if additional socket options are
    specified with the 
    <i>controlData</i> and 
    <i>controlDataLength</i> parameters, those options will be used to construct each new IP header.</p>

<p>If the input net buffer list was cloned from an inbound WFP transport layer, or if it was created as a
    result of a raw send operation, the net buffers will already contain an IP header. In this case, when
    this function is called, IPv4 options will be preserved in the new IP header, but AH/ESP headers and IPv6
    extension headers will be removed. Because the TCP/IP stack retains AH/ESP headers after IPsec
    processing, packets that have been indicated by WFP and cloned by callouts cannot readily be injected
    into the receive data path. Consequently this function is useful for rebuilding IPsec-processed packets
    that are to be injected into the receive data path with the 
    <a href="..\fwpsk\nf-fwpsk-fwpsinjecttransportreceiveasync0.md">FwpsInjectTransportReceiveAsync0</a> function.</p>

<p>For a header-include session; for example, to filter Generic Routing Encapsulation (GRE) traffic (IP
    protocol 47) sent on a raw socket from outbound transport layers, use the following procedure before you
    call 
    <b>FwpsConstructIpHeaderForTransportPacket0</b>:</p>

<p>Clone the net buffer list by calling the 
      <a href="..\fwpsk\nf-fwpsk-fwpsallocateclonenetbufferlist0.md">
      FwpsAllocateCloneNetBufferList0</a> function.</p>

<p>If the 
      <b>headerIncludeHeaderLength</b> member of the FWPS_INCOMING_METADATA_VALUES0 structure that is pointed
      to by the 
      <a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a> function's 
      <i>inMetaValues</i> parameter is greater than zero, retreat the cloned net buffer list by that amount; for example, by a call to 
      <a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">NdisRetreatNetBufferListDataStart</a>.</p>

<p>Copy the buffer that is pointed to by the 
      <b>headerIncludeHeader</b> member of FWPS_INCOMING_METADATA_VALUES0 into the newly retreated region of
      the cloned net buffer list. The size of the buffer must be equal to the value of 
      <i>headerIncludeHeaderLength</i>.</p>

<p>Call 
      <b>FwpsConstructIpHeaderForTransportPacket0</b> that has the 
      <i>NetBufferList</i> parameter pointing to the cloned net buffer list and the 
      <i>headerIncludeHeaderSize</i> parameter set to the value of 
      <i>headerIncludeHeaderLength</i>.</p>

<p><b>FwpsConstructIpHeaderForTransportPacket0</b> disables large send offload (LSO) and checksum offload
    support for the resulting net buffer list. Full checksums are calculated for upper-level protocols (TCP,
    UDP, and ICMP). The IP checksum is recalculated when the IP header is reconstructed.</p>

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
<p>Available starting with Windows Server 2008.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543744">AF_INET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543746">AF_INET6</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps-callout-classify-fn0.md">classifyFn</a>
</dt>
<dt>
<a href="netvista.cmsghdr">CMSGHDR</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsinjecttransportreceiveasync0.md">
   FwpsInjectTransportReceiveAsync0</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsConstructIpHeaderForTransportPacket0 function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
