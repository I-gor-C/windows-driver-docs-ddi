---
UID: NF.ndis.NdisCmDeactivateVc
title: NdisCmDeactivateVc
author: windows-driver-content
description: NdisCmDeactivateVc notifies NDIS and the underlying miniport driver that there will be no further transfers on a particular active VC.
old-location: netvista\ndiscmdeactivatevc.htm
ms.assetid: 141830de-e113-4f42-91f8-8f1cdbf3e32c
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisCmDeactivateVc (NDIS 5.1))
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisCmDeactivateVc (NDIS 5.1))
   in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmDeactivateVc
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_CallManager_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisCmDeactivateVc
req.iface: 
---

# NdisCmDeactivateVc function



## -description
<p><b>NdisCmDeactivateVc</b> notifies NDIS and the underlying miniport driver that there will be no further
  transfers on a particular active VC.</p>


## -syntax

````
NDIS_STATUS NdisCmDeactivateVc(
  _In_ NDIS_HANDLE NdisVcHandle
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle identifying the VC. This handle was supplied by NDIS to the call manager
     either when it called 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> for an incoming call or
     when its 
     <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function set up
     the VC for a client-initiated outgoing call.</p>
</dd>
</dl>

## -returns
<p>When 
     <b>NdisCmDeactivateVc</b> returns anything other than NDIS_STATUS_PENDING, the call manager should make
     an internal call to its 
     <a href="https://msdn.microsoft.com/44ee0e3c-aee9-4e24-9e54-c57248b568b6">
     ProtocolCmDeactivateVcComplete</a> function. Otherwise, NDIS calls the CM's 
     <i>ProtocolCmDeactivateVcComplete</i> function when this operation is completed.</p>

## -remarks
<p>A stand-alone call manager calls 
    <b>NdisCmDeactivateVc</b> as an essential step in closing a call, usually after the packet exchange with
    network components that tears down the call.</p>

<p>A call to 
    <b>NdisCmDeactivateVc</b> causes NDIS to call the underlying miniport driver's 
    <a href="https://msdn.microsoft.com/8c17cec8-d161-47cf-b886-bb8b8d957656">MiniportCoDeactivateVc</a> function,
    which can discard the current call parameters for transfers on the VC, possibly reinitializing them to
    miniport driver-determined default values. If the VC is reactivated subsequently for another call, the
    client or call manager will supply new call parameters to the miniport driver.</p>

<p>The 
    <i>NdisVcHandle</i> passed to 
    <b>NdisCmDeactivateVc</b> remains valid after VC deactivation is completed. The deactivation of any VC
    allows its creator to reinitialize the VC for reuse:</p>

<p>Following VC deactivation and the closing of the call, a client can reuse a VC that it originally
      created to make another call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>.</p>

<p>Following VC deactivation and the closing of the call, a CM can reuse a VC that it originally
      created to indicate another incoming call to the same client with 
      <a href="https://msdn.microsoft.com/2172aeec-8502-414e-9d01-9292c0eb7ce8">
      NdisCmDispatchIncomingCall</a>.</p>

<p>The creator of a particular VC that will not be reused calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> to destroy that VC.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDeactivateVc</b>. Connection-oriented miniport drivers that provide integrated call-management
    support call 
    <b>NdisMCmDeactivateVc</b> instead.</p>

<p>A stand-alone call manager calls 
    <b>NdisCmDeactivateVc</b> as an essential step in closing a call, usually after the packet exchange with
    network components that tears down the call.</p>

<p>A call to 
    <b>NdisCmDeactivateVc</b> causes NDIS to call the underlying miniport driver's 
    <a href="https://msdn.microsoft.com/8c17cec8-d161-47cf-b886-bb8b8d957656">MiniportCoDeactivateVc</a> function,
    which can discard the current call parameters for transfers on the VC, possibly reinitializing them to
    miniport driver-determined default values. If the VC is reactivated subsequently for another call, the
    client or call manager will supply new call parameters to the miniport driver.</p>

<p>The 
    <i>NdisVcHandle</i> passed to 
    <b>NdisCmDeactivateVc</b> remains valid after VC deactivation is completed. The deactivation of any VC
    allows its creator to reinitialize the VC for reuse:</p>

<p>Following VC deactivation and the closing of the call, a client can reuse a VC that it originally
      created to make another call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>.</p>

<p>Following VC deactivation and the closing of the call, a CM can reuse a VC that it originally
      created to indicate another incoming call to the same client with 
      <a href="https://msdn.microsoft.com/2172aeec-8502-414e-9d01-9292c0eb7ce8">
      NdisCmDispatchIncomingCall</a>.</p>

<p>The creator of a particular VC that will not be reused calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> to destroy that VC.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDeactivateVc</b>. Connection-oriented miniport drivers that provide integrated call-management
    support call 
    <b>NdisMCmDeactivateVc</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff550938">NdisCmDeactivateVc (NDIS 5.1)</a>)
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCmDeactivateVc (NDIS 5.1)</b>)
   in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547917">Irql_CallManager_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/8c17cec8-d161-47cf-b886-bb8b8d957656">MiniportCoDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561649">NdisCmActivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562818">NdisMCmDeactivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b5307e1b-3905-4e43-a0b0-0068ba18ef0d">ProtocolCmCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/44ee0e3c-aee9-4e24-9e54-c57248b568b6">
   ProtocolCmDeactivateVcComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmDeactivateVc function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
