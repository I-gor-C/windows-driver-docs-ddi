---
UID: NF.ndis.MINIPORT_SYNCHRONOUS_OID_REQUEST
title: MINIPORT_SYNCHRONOUS_OID_REQUEST
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportSynchronousOidRequest callback function to issue a Synchronous OID request.
old-location: netvista\miniport_synchronous_oid_request.htm
old-project: netvista
ms.assetid: 0DDF9CF8-91F6-4D7C-A8E8-FC425BF155CB
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MINIPORT_SYNCHRONOUS_OID_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportSynchronousOidRequest
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# MINIPORT_SYNCHRONOUS_OID_REQUEST function



## -description
<p>NDIS calls a miniport driver's <i>MiniportSynchronousOidRequest</i> callback function to issue a Synchronous OID request.</p>


## -syntax

````
NDIS_STATUS MiniportSynchronousOidRequest(
  _In_ NDIS_HANDLE      MiniportAdapterContext,
  _In_ NDIS_OID_REQUEST *OidRequest
);
````


## -parameters
<dl>

### -param MiniportAdapterContext [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>

### -param OidRequest [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure that contains
     both the buffer and the request packet for the miniport driver to handle. Depending on the request, the
     driver returns requested information in the structure that is provided.</p>
</dd>
</dl>

## -returns
<p><i>MiniportSynchronousOidRequest</i> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The miniport driver set or obtained the data as requested.</p><dl>
<dt><b>NDIS_STATUS_INVALID_OID</b></dt>
</dl><p>The request that 
       <i>OidRequest</i> specified was invalid or not recognized.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The request that 
       <i>OidRequest</i> specified was recognized, but the miniport driver does not support it.</p><dl>
<dt><b>NDIS_STATUS_BUFFER_TOO_SHORT</b></dt>
</dl><p>The buffer that 
       <i>OidRequest</i> supplies was too small to hold the requested data.</p><dl>
<dt><b>NDIS_STATUS_INVALID_LENGTH</b></dt>
</dl><p>The value that was specified in the 
       <b>InformationBufferLength</b> member of the NDIS_OID_REQUEST structure at 
       <i>OidRequest</i> is incorrect for the specified OID_<i>Xxx</i> code.</p><dl>
<dt><b>NDIS_STATUS_INVALID_DATA</b></dt>
</dl><p>One or more of the parameters that were specified for the request at 
       <i>OidRequest</i> were invalid.</p><dl>
<dt><b>NDIS_STATUS_INDICATION_REQUIRED</b></dt>
</dl><p>The miniport driver will provide an OID completion status with a subsequent status indication. A
       miniport driver cannot return NDIS_STATUS_INDICATION_REQUIRED unless the particular OID allows it. To
       determine if this status is allowed, see the OID reference page. For more information about
       NDIS_STATUS_INDICATION_REQUIRED, see 
       <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> and 
       <a href="..\ndis\ns-ndis--ndis-status-indication.md">NDIS_STATUS_INDICATION</a>.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p>After calling the 
       <a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
       MiniportDevicePnPEventNotify</a> function to indicate a surprise removal, NDIS called the driver's 
       <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function. If the
       driver received any OID requests before NDIS calls 
       <i>MiniportHaltEx</i>, it should immediately complete such requests with a status value of
       NDIS_STATUS_NOT_ACCEPTED.</p>

<p>Miniport drivers are not always required to return NDIS_STATUS_NOT_ACCEPTED for all OIDs after a surprise removal, but doing so helps explain why the call failed.</p>

<p> </p>

## -remarks
<p><i>MiniportSynchronousOidRequest</i> is an optional function. A miniport driver registers this function if it handles Synchronous OID requests. The driver specifies the <i>MiniportSynchronousOidRequest</i> entry point when it calls the <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a> function, using the <b>SynchronousOidRequestHandler</b> member of the <a href="..\ndis\ns-ndis--ndis-miniport-driver-characteristics.md">NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a> structure.
</p>

<p>Miniport drivers must not return NDIS_STATUS_PENDING or NDIS_STATUS_REQUEST_ABORTED from MiniportSynchronousOidRequest. Synchronous OID requests cannot be pended or cancelled.</p>

<p>Miniport drivers may return NDIS_STATUS_NOT_ACCEPTED after NDIS calls <a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
       MiniportDevicePnPEventNotify</a> to notify the driver of the device’s surprise removal. However, miniport drivers may still complete the OID request with a different status code, if it is possible to do so. For more info, see each OID’s specific documentation.</p>

<p>Miniport drivers are expected to complete Synchronous OID requests quickly without blocking, waiting, or sleeping. Synchronous OID requests are only used for low-latency operations, and miniport drivers should strive to complete them within several milliseconds. Most OID requests are delivered to <a href="netvista.miniport_oid_request">MiniportOidRequest</a>, which is permitted to pend or wait for longer durations.
</p>

<p>NDIS does not serialize Synchronous OID requests against each other, against other OID requests, against <a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a>, against <a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>, or against power transitions. It is the responsibility of the miniport driver to implement its own synchronization and to fail requests that are delivered at a time when the request cannot be handled successfully.</p>

<p>NDIS does serialize Synchronous OID requests against <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>; NDIS guarantees that no Synchronous OID requests will be active once <i>MiniportHaltEx</i> is invoked.</p>

<p>Miniport drivers that implement NDIS Selective Suspend are incompatible with Synchronous OIDs and must not register a <i>MiniportSynchronousOidRequest</i> handler.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-pause.md">MiniportPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="netvista.miniport_oid_request">MiniportOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
       MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-driver-characteristics.md">NDIS_MINIPORT_DRIVER_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-status-indication.md">NDIS_STATUS_INDICATION</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/synchronous-oid-request-interface-in-ndis-6-80">Synchronous OID Request Interface in NDIS 6.80</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_SYNCHRONOUS_OID_REQUEST function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
