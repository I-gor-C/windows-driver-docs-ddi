---
UID: NF.fwpsk.FwpsInjectForwardAsync0
title: FwpsInjectForwardAsync0 function
author: windows-driver-content
description: The FwpsInjectForwardAsync0 function injects packet data into the forwarding data path.Note  FwpsInjectForwardAsync0 is a specific version of FwpsInjectForwardAsync.
old-location: netvista\fwpsinjectforwardasync0.htm
old-project: netvista
ms.assetid: b7cb70c6-c672-4a29-983c-c73767af72ea
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: FwpsInjectForwardAsync0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsInjectForwardAsync0
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
---

# FwpsInjectForwardAsync0 function



## -description
The 
  <b>FwpsInjectForwardAsync0</b> function injects packet data into the forwarding data path.


## -syntax

````
NTSTATUS NTAPI FwpsInjectForwardAsync0(
  _In_     HANDLE                injectionHandle,
  _In_opt_ HANDLE                injectionContext,
  _In_     UINT32                flags,
  _In_     ADDRESS_FAMILY        addressFamily,
  _In_     COMPARTMENT_ID        compartmentId,
  _In_     IF_INDEX              interfaceIndex,
  _Inout_  NET_BUFFER_LIST       *netBufferList,
  _In_     FWPS_INJECT_COMPLETE0 completionFn,
  _In_opt_ HANDLE                completionContext
);
````


## -parameters

### -param injectionHandle [in]

An injection handle that was previously created by a call to the 
     <a href="netvista.fwpsinjectionhandlecreate0">
     FwpsInjectionHandleCreate0</a> function.

### -param injectionContext [in, optional]

An optional handle to the injection context. If specified, it can be obtained by calling the 
     <a href="netvista.fwpsquerypacketinjectionstate0">
     FwpsQueryPacketInjectionState0</a> function when the packet injection state 
     <a href="netvista.fwps_packet_injection_state">FWPS_PACKET_INJECTION_STATE</a> is
     <b>FWPS_PACKET_INJECTED_BY_SELF</b> or <b>FWPS_PACKET_PREVIOUSLY_INJECTED_BY_SELF</b>.

### -param flags [in]

Reserved. Callout drivers must set this parameter to zero.

### -param addressFamily [in]

One of the following address families:
     


### -param AF_INET

The IPv4 address family.

### -param AF_INET6

The IPv6 address family.
</dd>
</dl>

### -param compartmentId [in]

The identifier of the routing compartment into which the packet data is injected, specified as a 
     <a href="kernel.compartment_id">COMPARTMENT_ID</a> type. This identifier is provided
     to a callout through the 
     <b>compartmentId</b> member of the 
     <a href="netvista.fwps_incoming_metadata_values0">
     FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to the callout driver's 
     <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> callout function. If the 
     <b>compartmentId</b> member is available to callouts, FWPS_METADATA_FIELD_COMPARTMENT_ID will be set in
     the 
     <b>currentMetadataValues</b> member. Otherwise, set this parameter to UNSPECIFIED_COMPARTMENT_ID.

### -param interfaceIndex [in]

The index of the destination interface (on which the packet data is to be sent). The index is a
     32-bit value. A callout driver should use the value of the interface index that is passed as one of the
     incoming data values to its 
     <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> callout function for this
     parameter if the packet is to be injected into the same interface where the original packet was
     indicated.

### -param netBufferList [in, out]

A pointer to a 
     <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure that describes
     the packet data that is being injected. A callout driver allocates a NET_BUFFER_LIST structure to inject
     packet data by calling either the 
     <a href="netvista.fwpsallocateclonenetbufferlist0">
     FwpsAllocateCloneNetBufferList0</a> function or the 
     <a href="netvista.fwpsallocatenetbufferandnetbufferlist0">
     FwpsAllocateNetBufferAndNetBufferList0</a> function. The NET_BUFFER_LIST structure must begin with an
     IP header.

### -param completionFn [in]

A pointer to a 
     <a href="..\fwpsk\nc-fwpsk-fwps_inject_complete0.md">completionFn</a> callout function provided by
     the callout driver. The filter engine calls this function after the packet data, described by the 
     <i>netBufferList</i> parameter, has been injected into the network stack.

### -param completionContext [in, optional]

A pointer to a callout driver-provided context that is passed to the callout function pointed to
     by the 
     <i>completionFn</i> parameter. This parameter is optional and can be <b>NULL</b>.

## -returns
The 
     <b>FwpsInjectForwardAsync0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The packet data injection was initiated successfully. The filter engine will call the completion
       function after the filter engine has completed injecting the packet data into the network stack, or
       when an error occurred subsequently, in which case the 
       <b>Status</b> member of the completed 
       <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure will indicate
       the reason for failure.
<dl>
<dt><b>STATUS_FWP_TCPIP_NOT_READY</b></dt>
</dl>The TCP/IP network stack is not ready to accept injection of packet data.
<dl>
<dt><b>STATUS_FWP_INJECT_HANDLE_CLOSING</b></dt>
</dl>The injection handle is being closed.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 

## -remarks
A callout driver calls the 
    <b>FwpsInjectForwardAsync0</b> function to inject packet data or a packet fragment into the forwarding
    data path.

This function can execute asynchronously. Callout drivers normally inject data into the network stack
    when modifying packet data. For more information about how a callout driver can modify packet data, see 
    <a href="netvista.callout_driver_operations">Callout Driver Operations</a>.

A packet or packet fragment injected with this function will not be indicated to any WFP layer for
    filtering.

If the return value is not STATUS_SUCCESS, the completion function will not be called. In this case,
    the net buffer list pointed to by 
    <i>netBufferList</i> must be freed by a call to 
    <a href="netvista.fwpsfreenetbufferlist0">FwpsFreeNetBufferList0</a> or 
    <a href="netvista.fwpsfreeclonenetbufferlist0">
    FwpsFreeCloneNetBufferList0</a>.

IP packets or fragments can be cloned, modified, and injected back into the network stack. However, a
    fragment group must be reassembled by the callout driver as a single NET_BUFFER_LIST before it can be
    reinjected.

Forward-injected packets do not reenter the forwarding layer. Therefore, they will not be
    reclassified.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows Vista.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a>
</dt>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_inject_complete0.md">completionFn</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="netvista.fwpsallocateclonenetbufferlist0">
   FwpsAllocateCloneNetBufferList0</a>
</dt>
<dt>
<a href="netvista.fwpsallocatenetbufferandnetbufferlist0">
   FwpsAllocateNetBufferAndNetBufferList0</a>
</dt>
<dt>
<a href="netvista.fwpsinjectionhandlecreate0">FwpsInjectionHandleCreate0</a>
</dt>
<dt>
<a href="netvista.fwpsinjectionhandledestroy0">FwpsInjectionHandleDestroy0</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.packet_injection_functions">Packet Injection Functions</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsInjectForwardAsync0 function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>