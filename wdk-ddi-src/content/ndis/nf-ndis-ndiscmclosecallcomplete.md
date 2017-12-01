---
UID: NF.ndis.NdisCmCloseCallComplete
title: NdisCmCloseCallComplete
author: windows-driver-content
description: NdisCmCloseCallComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to tear down a call.
old-location: netvista\ndiscmclosecallcomplete.htm
old-project: netvista
ms.assetid: caf248e0-ec9a-4c85-86f7-f35c715c6e39
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisCmCloseCallComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisCmCloseCallComplete (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisCmCloseCallComplete (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmCloseCallComplete
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
req.iface: 
---

# NdisCmCloseCallComplete function



## -description
<p><b>NdisCmCloseCallComplete</b> returns the final status of a client's request, for which the call manager
  previously returned NDIS_STATUS_PENDING, to tear down a call.</p>


## -syntax

````
VOID NdisCmCloseCallComplete(
  _In_     NDIS_STATUS Status,
  _In_     NDIS_HANDLE NdisVcHandle,
  _In_opt_ NDIS_HANDLE NdisPartyHandle
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client's request that the CM close the connection, either
     NDIS_STATUS_SUCCESS or any CM-determined NDIS_STATUS_<i>XXX</i> except NDIS_STATUS_PENDING.</p>
</dd>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle to the VC for the call. This handle was supplied by NDIS when the VC was
     originally created, whether by the call manager or client, with 
     <a href="..\ndis\nf-ndis-ndiscocreatevc.md">NdisCoCreateVc</a>. More recently, the call
     manager obtained this handle from its per-VC state designated by the 
     <i>CallMgrVcContext</i> passed as an input parameter to its 
     <a href="..\ndis\nc-ndis-protocol-cm-close-call.md">
     ProtocolCmCloseCall</a> function.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in, optional]

<dd>
<p>Specifies either <b>NULL</b> if the 
     <i>NdisVcHandle</i> represents a point-to-point VC or the handle to the last remaining party on a
     multipoint connection, which the CM obtained from its per-party state designated by the 
     <i>CallMgrPartyContext</i> passed as an input parameter to its 
     <i>ProtocolCmCloseCall</i> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a stand-alone call manager's 
    <i>ProtocolCmCloseCall</i> function returns NDIS_STATUS_PENDING, the CM must call 
    <b>NdisCmCloseCallComplete</b> subsequently to notify the client and NDIS that its attempt to break the
    connection has completed, whether successfully or with an error. A call to 
    <b>NdisCmCloseCallComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">
    ProtocolClCloseCallComplete</a> function.</p>

<p>If it passes NDIS_STATUS_SUCCESS as the 
    <i>Status</i>, the call manager should consider the 
    <i>NdisVcHandle</i> (and 
    <i>NdisPartyHandle</i>, if any) unusable for transfers over the network as soon as it calls 
    <b>NdisCmCloseCallComplete</b>. If the call manager originally created the VC, it should call 
    <a href="..\ndis\nf-ndis-ndiscodeletevc.md">NdisCoDeleteVc</a> with the same 
    <i>NdisVcHandle</i> that it just passed to 
    <b>NdisCmCloseCallComplete</b>. If the client created this VC, the call manager can expect a call to its 
    <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function with the
    
    <i>ProtocolVcContext</i>, where it has the same 
    <i>NdisVcHandle</i>, as an input parameter.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmCloseCallComplete</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmCloseCallComplete</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/6fecc788-da38-4348-b580-e9e6be99598f">NdisCmCloseCallComplete (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCmCloseCallComplete (NDIS
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
<a href="devtest.ndis_irql_callmanager_function">Irql_CallManager_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmclosecallcomplete.md">NdisMCmCloseCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscodeletevc.md">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">ProtocolClCloseCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmCloseCallComplete function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
