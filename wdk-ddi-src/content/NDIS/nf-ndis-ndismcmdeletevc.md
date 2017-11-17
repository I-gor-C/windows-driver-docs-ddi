---
UID: NF.ndis.NdisMCmDeleteVc
title: NdisMCmDeleteVc
author: windows-driver-content
description: NdisMCmDeleteVc destroys a caller-created VC.
old-location: netvista\ndismcmdeletevc.htm
ms.assetid: b55d0995-efd8-4a61-85e9-970559e21a88
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMCmDeleteVc (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMCmDeleteVc (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmDeleteVc
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_MCM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisMCmDeleteVc
req.iface: 
---

# NdisMCmDeleteVc function



## -description
<p><b>NdisMCmDeleteVc</b> destroys a caller-created VC.</p>


## -syntax

````
NDIS_STATUS NdisMCmDeleteVc(
  _In_ NDIS_HANDLE NdisVcHandle
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle identifying the VC to be deleted. The caller originally obtained this handle
     from 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562812">NdisMCmCreateVc</a>.</p>
</dd>
</dl>

## -returns
<p><b>NdisMCmDeleteVc</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS deleted the VC.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p>The VC is still active, so it could not be deleted.</p>

<p> </p>

## -remarks
<p>When an MCM driver calls 
    <b>NdisMCmDeleteVc</b>, there must be no outstanding calls on the given VC and that VC must have been
    deactivated. To meet these requirements implies that the MCM driver has already called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562818">NdisMCmDeactivateVc</a> with the given 
    <i>NdisVcHandle</i> successfully.</p>

<p>Only the driver that created a particular VC can delete that VC. A call to 
    <b>NdisMCmDeleteVc</b> causes NDIS to call the 
    <a href="https://msdn.microsoft.com/d761270f-bf77-441e-834c-9ac7fb3d350f">ProtocolCoDeleteVc</a> function of the
    client with which the caller shares the 
    <i>NdisVcHandle</i> .</p>

<p>When 
    <b>NdisMCmDeleteVc</b> returns control, the 
    <i>NdisVcHandle</i> is no longer valid. The MCM driver can release the resources it allocated to maintain
    state about the deleted VC or prepare them for reuse in a subsequent incoming-call notification after it
    calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562812">NdisMCmCreateVc</a>.</p>

<p>The driver writer determines whether an MCM driver has an (internal) 
    <a href="https://msdn.microsoft.com/ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4">MiniportCoDeleteVc</a> function that the
    driver calls in the context of tearing down connections for outgoing and incoming calls.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDeleteVc</b>. Stand-alone call managers and clients, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCoDeleteVc</b> instead.</p>

<p>When an MCM driver calls 
    <b>NdisMCmDeleteVc</b>, there must be no outstanding calls on the given VC and that VC must have been
    deactivated. To meet these requirements implies that the MCM driver has already called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562818">NdisMCmDeactivateVc</a> with the given 
    <i>NdisVcHandle</i> successfully.</p>

<p>Only the driver that created a particular VC can delete that VC. A call to 
    <b>NdisMCmDeleteVc</b> causes NDIS to call the 
    <a href="https://msdn.microsoft.com/d761270f-bf77-441e-834c-9ac7fb3d350f">ProtocolCoDeleteVc</a> function of the
    client with which the caller shares the 
    <i>NdisVcHandle</i> .</p>

<p>When 
    <b>NdisMCmDeleteVc</b> returns control, the 
    <i>NdisVcHandle</i> is no longer valid. The MCM driver can release the resources it allocated to maintain
    state about the deleted VC or prepare them for reuse in a subsequent incoming-call notification after it
    calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562812">NdisMCmCreateVc</a>.</p>

<p>The driver writer determines whether an MCM driver has an (internal) 
    <a href="https://msdn.microsoft.com/ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4">MiniportCoDeleteVc</a> function that the
    driver calls in the context of tearing down connections for outgoing and incoming calls.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDeleteVc</b>. Stand-alone call managers and clients, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCoDeleteVc</b> instead.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff553362">NdisMCmDeleteVc (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMCmDeleteVc (NDIS 5.1)</b>) in
   Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547967">Irql_MCM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/ed9b6ad1-059b-47d9-b1f7-10d498c5d2d4">MiniportCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562818">NdisMCmDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562812">NdisMCmCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d761270f-bf77-441e-834c-9ac7fb3d350f">ProtocolCoDeleteVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmDeleteVc function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
