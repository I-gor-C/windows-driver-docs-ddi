---
UID: NF.ndis.NdisMOidRequestComplete
title: NdisMOidRequestComplete
author: windows-driver-content
description: Miniport drivers call the NdisMOidRequestComplete function to return the final status of an OID request for which the driver's MiniportOidRequest function returned NDIS_STATUS_PENDING.
old-location: netvista\ndismoidrequestcomplete.htm
ms.assetid: 30d060d0-05a3-42b5-b5ff-2f2b12873ca9
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMOidRequestComplete
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: DoubleComplete, DoubleCompleteWorkItem, Irql_OID_Function, NdisMNetPnPEventInOIDRequest, NdisOidComplete, NdisOidDoubleComplete, NdisOidDoubleRequest, NdisTimedOidComplete, WlanAssociation, WlanDisassociation, WlanTimedConnectRequest, WlanTimedLinkQuality, WlanTimedScan
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisMOidRequestComplete
req.iface: 
---

# NdisMOidRequestComplete function



## -description
<p>Miniport drivers call the 
  <b>NdisMOidRequestComplete</b> function to return the final status of an OID request for which the driver's 
  <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function returned
  NDIS_STATUS_PENDING.</p>


## -syntax

````
VOID NdisMOidRequestComplete(
  _In_ NDIS_HANDLE       MiniportAdapterHandle,
  _In_ PNDIS_OID_REQUEST OidRequest,
  _In_ NDIS_STATUS       Status
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>A miniport adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>OidRequest</i> [in]

<dd>
<p>A pointer to a buffer that is formatted as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure. The miniport
     driver obtained this pointer as an input parameter to its 
     <i>MiniportOidRequest</i> function.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>The final status of the request operation, either NDIS_STATUS_SUCCESS,
     NDIS_STATUS_REQUEST_ABORTED, or any driver-determined NDIS_STATUS_<i>XXX</i><u>except</u> NDIS_STATUS_PENDING. For more information about OID status values, see 
     <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A miniport driver that returns NDIS_STATUS_PENDING from its 
    <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function must
    call 
    <b>NdisMOidRequestComplete</b> after the miniport driver has finished the request operation.</p>

<p>A call to 
    <b>NdisMOidRequestComplete</b> causes a call to the request complete function (see 
    <a href="https://msdn.microsoft.com/2c383523-7d9c-4f1b-8df1-5cb4cc3562d6">ProtocolRequestComplete</a>, 
    <a href="https://msdn.microsoft.com/2706577e-ba03-4347-9672-7303752ec0fe">ProtocolOidRequestComplete</a>,
    
    <a href="https://msdn.microsoft.com/2dba21d8-512b-4a1a-9cf9-0240c94a69a0">FilterOidRequestComplete</a>) of
    the overlying driver that called the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a> function.</p>

<p>A miniport driver that returns NDIS_STATUS_PENDING from its 
    <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function must
    call 
    <b>NdisMOidRequestComplete</b> after the miniport driver has finished the request operation.</p>

<p>A call to 
    <b>NdisMOidRequestComplete</b> causes a call to the request complete function (see 
    <a href="https://msdn.microsoft.com/2c383523-7d9c-4f1b-8df1-5cb4cc3562d6">ProtocolRequestComplete</a>, 
    <a href="https://msdn.microsoft.com/2706577e-ba03-4347-9672-7303752ec0fe">ProtocolOidRequestComplete</a>,
    
    <a href="https://msdn.microsoft.com/2dba21d8-512b-4a1a-9cf9-0240c94a69a0">FilterOidRequestComplete</a>) of
    the overlying driver that called the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544922">DoubleComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544924">DoubleCompleteWorkItem</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547990">Irql_OID_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975120">NdisMNetPnPEventInOIDRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305115">NdisOidComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305116">NdisOidDoubleComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305117">NdisOidDoubleRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305120">NdisTimedOidComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305122">WlanAssociation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305124">WlanDisassociation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305127">WlanTimedConnectRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305128">WlanTimedLinkQuality</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305129">WlanTimedScan</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563710">NdisOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2c383523-7d9c-4f1b-8df1-5cb4cc3562d6">ProtocolRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2706577e-ba03-4347-9672-7303752ec0fe">ProtocolOidRequestComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2dba21d8-512b-4a1a-9cf9-0240c94a69a0">FilterOidRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMOidRequestComplete function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
