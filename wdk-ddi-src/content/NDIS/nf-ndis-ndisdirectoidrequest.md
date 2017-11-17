---
UID: NF.ndis.NdisDirectOidRequest
title: NdisDirectOidRequest
author: windows-driver-content
description: The NdisDirectOidRequest function forwards a direct OID request to the underlying drivers to query the capabilities or status of an adapter or set the state of an adapter.
old-location: netvista\ndisdirectoidrequest.htm
ms.assetid: 771e5761-beea-4a31-9ebe-d65e9157f1f4
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisDirectOidRequest
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisDirectOidRequest
req.iface: 
---

# NdisDirectOidRequest function



## -description
<p>The 
  <b>NdisDirectOidRequest</b> function forwards a direct OID request to the underlying drivers to query the
  capabilities or status of an adapter or set the state of an adapter.</p>


## -syntax

````
NDIS_STATUS NdisDirectOidRequest(
  _In_ NDIS_HANDLE       NdisBindingHandle,
  _In_ PNDIS_OID_REQUEST OidRequest
);
````


## -parameters
<dl>

### -param <i>NdisBindingHandle</i> [in]

<dd>
<p>The handle that the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a> function returns that
     identifies the target miniport adapter on the binding.</p>
</dd>

### -param <i>OidRequest</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure that specifies
     the operation that is requested with a given OID_<i>Xxx</i> code to either query the status of an adapter or to set the state of an adapter.</p>
</dd>
</dl>

## -returns
<p>The underlying driver determines which NDIS_STATUS_<i>XXX</i> code 
     <b>NdisDirectOidRequest</b> returns, but it is usually one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The request operation completed successfully.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>The request is being handled asynchronously, and NDIS will call the caller's 
       <a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
       ProtocolDirectOidRequestComplete</a> function when the request is completed.</p><dl>
<dt><b>NDIS_STATUS_INVALID_OID</b></dt>
</dl><p>The OID_<i>Xxx</i> code that was specified in the 
       <b>Oid</b> member of the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>-structured buffer at 
       <i>OidRequest</i> was invalid or unsupported by the underlying driver.</p><dl>
<dt><b>NDIS_STATUS_INVALID_LENGTH or NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl><p>The value that was specified in the 
       <b>InformationBufferLength</b> member of the NDIS_OID_REQUEST-structured buffer at 
       <i>OidRequest</i> did not match the requirements for the given OID_<i>Xxx</i> code. If the information buffer was too small, the 
       <b>BytesNeeded</b> member contains the correct value for 
       <b>InformationBufferLength</b> on return from 
       <b>NdisDirectOidRequest</b>.</p><dl>
<dt><b>NDIS_STATUS_INVALID_DATA</b></dt>
</dl><p>The data that was supplied at 
       <b>InformationBuffer</b> in the given NDIS_OID_REQUEST structure was invalid for the given OID_<i>Xxx</i> code.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED or NDIS_STATUS_NOT_RECOGNIZED</b></dt>
</dl><p>The underlying driver does not support the requested operation. For 
       <b>NdisDirectOidRequest</b>, NDIS can also return this status if the calling driver has not registered
       a 
       <a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
       ProtocolDirectOidRequestComplete</a> function.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>The request could not be satisfied because of a resource shortage. Typically, this return value
       indicates that an attempt to allocate memory was unsuccessful, but it does not necessarily indicate
       that the same request, submitted later, will be failed for the same reason.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p>The underlying driver attempted the requested operation, typically a set on a NIC, but it
       failed. For example, an attempt to set too many multicast addresses might cause the return of this
       value.</p><dl>
<dt><b>NDIS_STATUS_CLOSING or NDIS_STATUS_CLOSING_INDICATING</b></dt>
</dl><p>The underlying driver failed the requested operation because a close operation is in
       progress.</p><dl>
<dt><b>NDIS_STATUS_RESET_IN_PROGRESS</b></dt>
</dl><p>The underlying miniport driver cannot satisfy the request at this time because it is currently
       resetting the affected NIC. The caller's 
       <a href="https://msdn.microsoft.com/5bc5a24f-5f28-4502-8776-b1cf15fd8283">ProtocolStatusEx</a> function was or
       will be called with NDIS_STATUS_RESET_START to indicate that a reset is in progress. This return value
       does not necessarily indicate that the same request, submitted later, will be failed for the same
       reason.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>This value typically is a non-specific default, returned when none of the more specific
       NDIS_STATUS_<i>Xxx</i> values caused the underlying driver to fail the request.</p>

<p> </p>

## -remarks
<p>The 
    <b>NdisDirectOidRequest</b> function cannot be used for general OID requests. For general OID requests,
    use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a> function instead. 
    <b>NdisDirectOidRequest</b> can be used only for OIDs that NDIS supports for use with the direct OID
    interface. For example, the following OIDs can be used:</p><dl>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_add_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_delete_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_update_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA</a>
</p>
</dd>
</dl><p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_add_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</p>

<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_delete_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</p>

<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_update_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA</a>
</p>

<p>A protocol driver must allocate sufficient memory to hold the information buffer that is associated
    with the specified OID. The driver must also allocate and set up the buffer at the 
    <i>OidRequest</i> parameter before it calls 
    <b>NdisDirectOidRequest</b>. Both buffers must be allocated from nonpaged pool because the underlying
    driver runs at raised IRQL while processing the request.</p>

<p><b>NdisDirectOidRequest</b> forwards a request to underlying drivers or handles the request itself. If the
    next-lower driver is an NDIS intermediate driver, the intermediate driver can call 
    <b>NdisDirectOidRequest</b> with an OID-specific request of its own before completing the request that the
    higher-level driver originally submitted.</p>

<p>A driver that calls 
    <b>NdisDirectOidRequest</b> must register the 
    <a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
    ProtocolDirectOidRequestComplete</a> function.</p>

<p>The direct OID request interface is similar to the general OID request interface. For more information
    about issuing general requests, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a>.</p>

<p>The 
    <b>NdisDirectOidRequest</b> function cannot be used for general OID requests. For general OID requests,
    use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a> function instead. 
    <b>NdisDirectOidRequest</b> can be used only for OIDs that NDIS supports for use with the direct OID
    interface. For example, the following OIDs can be used:</p><dl>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_add_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_delete_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_update_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA</a>
</p>
</dd>
</dl><p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_add_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</p>

<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_delete_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</p>

<p>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_update_sa">
       OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA</a>
</p>

<p>A protocol driver must allocate sufficient memory to hold the information buffer that is associated
    with the specified OID. The driver must also allocate and set up the buffer at the 
    <i>OidRequest</i> parameter before it calls 
    <b>NdisDirectOidRequest</b>. Both buffers must be allocated from nonpaged pool because the underlying
    driver runs at raised IRQL while processing the request.</p>

<p><b>NdisDirectOidRequest</b> forwards a request to underlying drivers or handles the request itself. If the
    next-lower driver is an NDIS intermediate driver, the intermediate driver can call 
    <b>NdisDirectOidRequest</b> with an OID-specific request of its own before completing the request that the
    higher-level driver originally submitted.</p>

<p>A driver that calls 
    <b>NdisDirectOidRequest</b> must register the 
    <a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
    ProtocolDirectOidRequestComplete</a> function.</p>

<p>The direct OID request interface is similar to the general OID request interface. For more information
    about issuing general requests, see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.1 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_add_sa">
   OID_TCP_TASK_IPSEC_OFFLOAD_V2_ADD_SA</a>
</dt>
<dt>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_delete_sa">
   OID_TCP_TASK_IPSEC_OFFLOAD_V2_DELETE_SA</a>
</dt>
<dt>
<a href="netvista.oid_tcp_task_ipsec_offload_v2_update_sa">
   OID_TCP_TASK_IPSEC_OFFLOAD_V2_UPDATE_SA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6b23bbba-1b18-4da7-a45c-68df7c960aad">
   ProtocolDirectOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5bc5a24f-5f28-4502-8776-b1cf15fd8283">ProtocolStatusEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisDirectOidRequest function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
