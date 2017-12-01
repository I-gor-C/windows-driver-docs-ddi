---
UID: NF.ndis.NdisCoOidRequestComplete
title: NdisCoOidRequestComplete
author: windows-driver-content
description: The NdisCoOidRequestComplete function returns the final status of an OID request that a CoNDIS client's or stand-alone call manager's ProtocolCoOidRequest function previously returned NDIS_STATUS_PENDING for.
old-location: netvista\ndiscooidrequestcomplete.htm
old-project: netvista
ms.assetid: ba4a22a1-ad48-43f1-96f5-dee5d76e49cb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisCoOidRequestComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCoOidRequestComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Connection_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisCoOidRequestComplete function



## -description
<p>The 
  <b>NdisCoOidRequestComplete</b> function returns the final status of an OID request that a CoNDIS client's
  or stand-alone call manager's 
  <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a> function
  previously returned NDIS_STATUS_PENDING for.</p>


## -syntax

````
VOID NdisCoOidRequestComplete(
  _In_     NDIS_HANDLE       NdisAfHandle,
  _In_opt_ NDIS_HANDLE       NdisVcHandle,
  _In_opt_ NDIS_HANDLE       NdisPartyHandle,
  _In_     PNDIS_OID_REQUEST OidRequest,
  _In_     NDIS_STATUS       Status
);
````


## -parameters
<dl>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>An address family (AF) handle that NDIS passed to the client or stand-alone call manager's 
     <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">
     ProtocolCoOidRequest</a> function.</p>
</dd>

### -param <i>NdisVcHandle</i> [in, optional]

<dd>
<p>A virtual connection (VC) handle that NDIS passed to the client or stand-alone call manager's 
     <i>ProtocolCoOidRequest</i> function. A <b>NULL</b> value for this parameter indicates that the request is not
     VC-specific. This parameter is <b>NULL</b> if the caller of the 
     <a href="..\ndis\nf-ndis-ndiscooidrequest.md">NdisCoOidRequest</a> or 
     <a href="..\ndis\nf-ndis-ndismcmoidrequest.md">NdisMCmOidRequest</a> function specified a
     <b>NULL</b> VC handle.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in, optional]

<dd>
<p>A party handle that NDIS passed to the client or stand-alone call manager's 
     <i>ProtocolCoOidRequest</i> function. A <b>NULL</b> value for this parameter indicates that the request is not
     party-specific. This parameter is <b>NULL</b> if the caller of the 
     <b>NdisCoOidRequest</b> or 
     <b>NdisMCmOidRequest</b> function specified a <b>NULL</b> party handle.</p>
</dd>

### -param <i>OidRequest</i> [in]

<dd>
<p>A pointer to a buffer that is formatted as an 
     <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure. The caller of
     the 
     <b>NdisCoOidRequest</b> or 
     <b>NdisMCmOidRequest</b> function supplied this buffer.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The final status of the request operation, either NDIS_STATUS_SUCCESS, or any driver-determined
     NDIS_STATUS_<i>XXX</i> status value 
     except NDIS_STATUS_PENDING.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A CoNDIS protocol driver that returns NDIS_STATUS_PENDING from its 
    <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a> function must
    call 
    <b>NdisCoOidRequestComplete</b> after the protocol driver has finished the request operation.</p>

<p>After a driver calls 
    <b>NdisCoOidRequestComplete</b>, NDIS calls the 
    <a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
    ProtocolCoOidRequestComplete</a> function of the driver that originally called the 
    <a href="..\ndis\nf-ndis-ndiscooidrequest.md">NdisCoOidRequest</a> or 
    <a href="..\ndis\nf-ndis-ndismcmoidrequest.md">NdisMCmOidRequest</a> function.</p>

<p>Only clients and stand-alone call managers, which register themselves with NDIS as protocol drivers,
    can call 
    <b>NdisCoOidRequestComplete</b>. Miniport call managers (MCMs) call the 
    <a href="..\ndis\nf-ndis-ndismcmoidrequestcomplete.md">
    NdisMCmOidRequestComplete</a> function or 
    <a href="..\ndis\nf-ndis-ndismcooidrequestcomplete.md">
    NdisMCoOidRequestComplete</a> instead, depending on whether the MCM driver's 
    <a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a> or 
    <a href="..\ndis\nc-ndis-miniport-co-oid-request.md">MiniportCoOidRequest</a> function,
    respectively, handled the client's request.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_connection_function">Irql_Connection_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-co-oid-request.md">MiniportCoOidRequest</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscooidrequest.md">NdisCoOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmoidrequest.md">NdisMCmOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmoidrequestcomplete.md">NdisMCmOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcooidrequestcomplete.md">NdisMCoOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-oid-request.md">ProtocolCoOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-oid-request-complete.md">
   ProtocolCoOidRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCoOidRequestComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
