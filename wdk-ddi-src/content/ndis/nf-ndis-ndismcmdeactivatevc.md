---
UID: NF.ndis.NdisMCmDeactivateVc
title: NdisMCmDeactivateVc
author: windows-driver-content
description: NdisMCmDeactivateVc notifies NDIS that there will be no further transfers on a particular active VC.
old-location: netvista\ndismcmdeactivatevc.htm
old-project: netvista
ms.assetid: e18f6326-621e-4bed-aa82-b326f3b1422d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMCmDeactivateVc
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMCmDeactivateVc (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMCmDeactivateVc (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmDeactivateVc
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
req.iface: 
---

# NdisMCmDeactivateVc function



## -description
<p><b>NdisMCmDeactivateVc</b> notifies NDIS that there will be no further transfers on a particular active
  VC.</p>


## -syntax

````
NDIS_STATUS NdisMCmDeactivateVc(
  _In_ NDIS_HANDLE NdisVcHandle
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle identifying the VC. This handle was supplied by NDIS to the MCM driver either
     when it called 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562812">NdisMCmCreateVc</a> for an incoming call or
     when its 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function set up
     the VC for a client-initiated outgoing call.</p>
</dd>
</dl>

## -returns
<p><b>NdisMCmDeactivateVc</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS marked the VC as inactive.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p>The VC is already deactivated, so this call is redundant.</p>

<p> </p>

## -remarks
<p>An MCM driver calls 
    <b>NdisMCmDeactivateVc</b> as an essential step in closing a call, usually after the packet exchange with
    network components that tears down the connection.</p>

<p>A successful call to 
    <b>NdisMCmDeactivateVc</b> allows the MCM driver to discard the current call parameters for transfers on
    the VC, possibly reinitializing them to miniport driver-determined default values. However, if the VC is
    reactivated subsequently for another call, the client will supply new call parameters to the miniport
    driver.</p>

<p>The 
    <i>NdisVcHandle</i> passed to 
    <b>NdisMCmDeactivateVc</b> remains valid after VC deactivation is completed. The deactivation of any VC
    allows its creator to reinitialize the VC for reuse or to destroy it:</p>

<p>Following VC deactivation and the closing of the call, a client can reuse a VC that it originally
      created to make another call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>, or it can call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>, thereby causing a call
      to the MCM driver's 
      <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function.</p>

<p>Following VC deactivation and the closing of the call, an MCM driver can reuse a VC that it
      originally created to indicate another incoming call to the same client with 
      <a href="..\ndis\nf-ndis-ndismcmdispatchincomingcall.md">
      NdisMCmDispatchIncomingCall</a>, or it can call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562819">NdisMCmDeleteVc</a>.</p>

<p>The driver writer determines whether an MCM driver has an (internal) 
    <i>MiniportCoDeactivateVc</i> function that the driver calls in the context of tearing down connections
    for outgoing and incoming calls.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDeactivateVc</b>. Stand-alone call managers, which register themselves with NDIS as protocol
    drivers, call 
    <b>NdisCmDeactivateVc</b> instead.</p>

<p>An MCM driver calls 
    <b>NdisMCmDeactivateVc</b> as an essential step in closing a call, usually after the packet exchange with
    network components that tears down the connection.</p>

<p>A successful call to 
    <b>NdisMCmDeactivateVc</b> allows the MCM driver to discard the current call parameters for transfers on
    the VC, possibly reinitializing them to miniport driver-determined default values. However, if the VC is
    reactivated subsequently for another call, the client will supply new call parameters to the miniport
    driver.</p>

<p>The 
    <i>NdisVcHandle</i> passed to 
    <b>NdisMCmDeactivateVc</b> remains valid after VC deactivation is completed. The deactivation of any VC
    allows its creator to reinitialize the VC for reuse or to destroy it:</p>

<p>Following VC deactivation and the closing of the call, a client can reuse a VC that it originally
      created to make another call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>, or it can call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>, thereby causing a call
      to the MCM driver's 
      <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function.</p>

<p>Following VC deactivation and the closing of the call, an MCM driver can reuse a VC that it
      originally created to indicate another incoming call to the same client with 
      <a href="..\ndis\nf-ndis-ndismcmdispatchincomingcall.md">
      NdisMCmDispatchIncomingCall</a>, or it can call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562819">NdisMCmDeleteVc</a>.</p>

<p>The driver writer determines whether an MCM driver has an (internal) 
    <i>MiniportCoDeactivateVc</i> function that the driver calls in the context of tearing down connections
    for outgoing and incoming calls.</p>

<p>Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDeactivateVc</b>. Stand-alone call managers, which register themselves with NDIS as protocol
    drivers, call 
    <b>NdisCmDeactivateVc</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/83192574-5734-40ec-b388-b686568bc800">NdisMCmDeactivateVc (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMCmDeactivateVc (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="..\ndis\nc-ndis-miniport-co-deactivate-vc.md">MiniportCoDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561657">NdisCmDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562792">NdisMCmActivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562819">NdisMCmDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562830">NdisMCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-close-call.md">ProtocolCmCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmDeactivateVc function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
