---
UID: NF.ndis.NdisMCmNotifyCloseAddressFamily
title: NdisMCmNotifyCloseAddressFamily
author: windows-driver-content
description: The NdisMCmNotifyCloseAddressFamily function notifies NDIS that a specified address family (AF) that is associated with a miniport call manager (MCM) should be closed and NDIS should notify any affected CoNDIS clients.
old-location: netvista\ndismcmnotifycloseaddressfamily.htm
old-project: netvista
ms.assetid: 47b0b1da-e29b-45cc-921b-69d630670b44
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMCmNotifyCloseAddressFamily
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
req.alt-api: NdisMCmNotifyCloseAddressFamily
req.alt-loc: ndis.h
req.ddi-compliance: Irql_MCM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisMCmNotifyCloseAddressFamily function



## -description
<p>The 
  <b>NdisMCmNotifyCloseAddressFamily</b> function notifies NDIS that a specified address family (AF) that is
  associated with a miniport call manager (MCM) should be closed and NDIS should notify any affected CoNDIS
  clients.</p>


## -syntax

````
NDIS_STATUS NdisMCmNotifyCloseAddressFamily(
  _In_ NDIS_HANDLE NdisAfHandle
);
````


## -parameters
<dl>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>A handle that identifies the AF that NDIS should close. NDIS supplied this handle to the MCM's 
     <a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisMCmNotifyCloseAddressFamily</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS successfully closed the address family.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>NDIS is handling this request asynchronously, and it will call the MCM's 
       <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
       ProtocolCmNotifyCloseAfComplete</a> function when the close operation is complete.</p><dl>
<dt><b>NDIS_STATUS_<i>XXX</i></b></dt>
</dl><p>NDIS failed the request for some NDIS or client driver-determined reason.</p>

<p> </p>

## -remarks
<p>MCMs, which register as NDIS miniport drivers by calling the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function, can call the 
    <b>NdisMCmNotifyCloseAddressFamily</b> function. Stand-alone call managers instead call the 
    <a href="..\ndis\nf-ndis-ndiscmnotifycloseaddressfamily.md">
    NdisCmNotifyCloseAddressFamily</a> function.</p>

<p>To close an AF for a miniport adapter, the MCM should call 
    <b>NdisMCmNotifyCloseAddressFamily</b> from its 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function. NDIS
    subsequently calls the 
    <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">
    ProtocolClNotifyCloseAf</a> function of the client that has the specified AF open.</p>

<p>If 
    <b>NdisMCmNotifyCloseAddressFamily</b> returns NDIS_STATUS_PENDING, NDIS calls the MCM's 
    <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
    ProtocolCmNotifyCloseAfComplete</a> function after the client completes the AF close operation.</p>

<p>MCMs, which register as NDIS miniport drivers by calling the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function, can call the 
    <b>NdisMCmNotifyCloseAddressFamily</b> function. Stand-alone call managers instead call the 
    <a href="..\ndis\nf-ndis-ndiscmnotifycloseaddressfamily.md">
    NdisCmNotifyCloseAddressFamily</a> function.</p>

<p>To close an AF for a miniport adapter, the MCM should call 
    <b>NdisMCmNotifyCloseAddressFamily</b> from its 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function. NDIS
    subsequently calls the 
    <a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">
    ProtocolClNotifyCloseAf</a> function of the client that has the specified AF open.</p>

<p>If 
    <b>NdisMCmNotifyCloseAddressFamily</b> returns NDIS_STATUS_PENDING, NDIS calls the MCM's 
    <a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
    ProtocolCmNotifyCloseAfComplete</a> function after the client completes the AF close operation.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547967">Irql_MCM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndiscmnotifycloseaddressfamily.md">
   NdisCmNotifyCloseAddressFamily</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-notify-close-af.md">ProtocolClNotifyCloseAf</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-notify-close-af-complete.md">
   ProtocolCmNotifyCloseAfComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-open-af.md">ProtocolCmOpenAf</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmNotifyCloseAddressFamily function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
