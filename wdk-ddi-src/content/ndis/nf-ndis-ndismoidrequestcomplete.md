---
UID: NF.ndis.NdisMOidRequestComplete
title: NdisMOidRequestComplete function
author: windows-driver-content
description: Miniport drivers call the NdisMOidRequestComplete function to return the final status of an OID request for which the driver's MiniportOidRequest function returned NDIS_STATUS_PENDING.
old-location: netvista\ndismoidrequestcomplete.htm
old-project: netvista
ms.assetid: 30d060d0-05a3-42b5-b5ff-2f2b12873ca9
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisMOidRequestComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
---

# NdisMOidRequestComplete function



## -description
Miniport drivers call the 
  <b>NdisMOidRequestComplete</b> function to return the final status of an OID request for which the driver's 
  <a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a> function returned
  NDIS_STATUS_PENDING.



## -syntax

````
VOID NdisMOidRequestComplete(
  _In_ NDIS_HANDLE       MiniportAdapterHandle,
  _In_ PNDIS_OID_REQUEST OidRequest,
  _In_ NDIS_STATUS       Status
);
````


## -parameters

### -param MiniportAdapterHandle [in]

A miniport adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of the 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">
     MiniportInitializeEx</a> function.


### -param OidRequest [in]

A pointer to a buffer that is formatted as an 
     <a href="netvista.ndis_oid_request">NDIS_OID_REQUEST</a> structure. The miniport
     driver obtained this pointer as an input parameter to its 
     <i>MiniportOidRequest</i> function.


### -param Status [in]

The final status of the request operation, either NDIS_STATUS_SUCCESS,
     NDIS_STATUS_REQUEST_ABORTED, or any driver-determined NDIS_STATUS_<i>XXX</i><u>except</u> NDIS_STATUS_PENDING. For more information about OID status values, see 
     <a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a>.


## -returns
None


## -remarks
A miniport driver that returns NDIS_STATUS_PENDING from its 
    <a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a> function must
    call 
    <b>NdisMOidRequestComplete</b> after the miniport driver has finished the request operation.

A call to 
    <b>NdisMOidRequestComplete</b> causes a call to the request complete function (see 
    <a href="https://msdn.microsoft.com/2c383523-7d9c-4f1b-8df1-5cb4cc3562d6">ProtocolRequestComplete</a>, 
    <a href="..\ndis\nc-ndis-protocol_oid_request_complete.md">ProtocolOidRequestComplete</a>,
    
    <a href="..\ndis\nc-ndis-filter_oid_request_complete.md">FilterOidRequestComplete</a>) of
    the overlying driver that called the 
    <a href="netvista.ndisoidrequest">NdisOidRequest</a> function.


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
Supported in NDIS 6.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_doublecomplete">DoubleComplete</a>, <a href="devtest.ndis_doublecompleteworkitem">DoubleCompleteWorkItem</a>, <a href="devtest.ndis_irql_oid_function">Irql_OID_Function</a>, <a href="devtest.ndis_ndismnetpnpeventinoidrequest">NdisMNetPnPEventInOIDRequest</a>, <a href="devtest.ndis_ndisoidcomplete">NdisOidComplete</a>, <a href="devtest.ndis_ndisoiddoublecomplete">NdisOidDoubleComplete</a>, <a href="devtest.ndis_ndisoiddoublerequest">NdisOidDoubleRequest</a>, <a href="devtest.ndis_ndistimedoidcomplete">NdisTimedOidComplete</a>, <a href="devtest.ndis_wlanassociation">WlanAssociation</a>, <a href="devtest.ndis_wlandisassociation">WlanDisassociation</a>, <a href="devtest.ndis_wlantimedconnectrequest">WlanTimedConnectRequest</a>, <a href="devtest.ndis_wlantimedlinkquality">WlanTimedLinkQuality</a>, <a href="devtest.ndis_wlantimedscan">WlanTimedScan</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_oid_request.md">MiniportOidRequest</a>
</dt>
<dt>
<a href="netvista.ndis_oid_request">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="netvista.ndisoidrequest">NdisOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2c383523-7d9c-4f1b-8df1-5cb4cc3562d6">ProtocolRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_oid_request_complete.md">ProtocolOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter_oid_request_complete.md">FilterOidRequestComplete</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMOidRequestComplete function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

