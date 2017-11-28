---
UID: NF.ndis.NdisCmDispatchCallConnected
title: NdisCmDispatchCallConnected
author: windows-driver-content
description: NdisCmDispatchCallConnected notifies NDIS and the client that data transfers can begin on a VC that the call manager created for an incoming call initiated on a remote node.
old-location: netvista\ndiscmdispatchcallconnected.htm
old-project: netvista
ms.assetid: c5fcca82-ab8f-4ea9-86df-295f43fe7afa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisCmDispatchCallConnected
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisCmDispatchCallConnected
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisCmDispatchCallConnected
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmDispatchCallConnected
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

# NdisCmDispatchCallConnected function



## -description
<p><b>NdisCmDispatchCallConnected</b> notifies NDIS and the client that data transfers can begin on a VC that
  the call manager created for an 
  <i>incoming</i> call initiated on a remote node.</p>


## -syntax

````
VOID NdisCmDispatchCallConnected(
  _In_ NDIS_HANDLE NdisVcHandle
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Specifies the handle to the VC that represents the connection, which was created with 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> when the call manager's 
     <a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
     ProtocolCoReceiveNetBufferLists</a> function was notified of the incoming call.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A stand-alone CM's 
    <a href="..\ndis\nc-ndis-protocol-cm-incoming-call-complete.md">
    ProtocolCmIncomingCallComplete</a> function calls 
    <b>NdisCmDispatchCallConnected</b> to complete the final handshake for an incoming call from a remote
    node, which the client has already accepted.</p>

<p>A call to 
    <b>NdisCmDispatchCallConnected</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-call-connected.md">
    ProtocolClCallConnected</a> function.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDispatchCallConnected</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmDispatchCallConnected</b> instead.</p>

<p>A stand-alone CM's 
    <a href="..\ndis\nc-ndis-protocol-cm-incoming-call-complete.md">
    ProtocolCmIncomingCallComplete</a> function calls 
    <b>NdisCmDispatchCallConnected</b> to complete the final handshake for an incoming call from a remote
    node, which the client has already accepted.</p>

<p>A call to 
    <b>NdisCmDispatchCallConnected</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-call-connected.md">
    ProtocolClCallConnected</a> function.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDispatchCallConnected</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmDispatchCallConnected</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/5eaf6b28-8f43-4216-962c-d5dd36fc4d56">NdisCmDispatchCallConnected
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisCmDispatchCallConnected
   (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561664">NdisCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562826">NdisMCmDispatchCallConnected</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-call-connected.md">ProtocolClCallConnected</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-incoming-call-complete.md">
   ProtocolCmIncomingCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
   ProtocolCoReceiveNetBufferLists</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmDispatchCallConnected function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
