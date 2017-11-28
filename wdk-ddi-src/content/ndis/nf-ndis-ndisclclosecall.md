---
UID: NF.ndis.NdisClCloseCall
title: NdisClCloseCall
author: windows-driver-content
description: NdisClCloseCall requests that a call on the specified VC be torn down.
old-location: netvista\ndisclclosecall.htm
old-project: netvista
ms.assetid: 4d1a7451-8c0f-4df8-85c5-14aaaa9afd94
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisClCloseCall
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisClCloseCall (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisClCloseCall (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClCloseCall
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
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

# NdisClCloseCall function



## -description
<p><b>NdisClCloseCall</b> requests that a call on the specified VC be torn down.</p>


## -syntax

````
NDIS_STATUS NdisClCloseCall(
  _In_     NDIS_HANDLE NdisVcHandle,
  _In_opt_ NDIS_HANDLE NdisPartyHandle,
  _In_opt_ PVOID       Buffer,
  _In_     UINT        Size
);
````


## -parameters
<dl>

### -param <i>NdisVcHandle</i> [in]

<dd>
<p>Handle to the VC of the call being closed or disconnected. This handle was supplied by NDIS when
     the VC was originally created with 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>, whether by the client in
     preparation for making an outgoing call or by the call manager in preparation for dispatching an
     incoming call to the client.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in, optional]

<dd>
<p>Handle to the last party to be dropped on a multipoint VC or <b>NULL</b>. If this is a multipoint VC, the
     client obtained this handle either from a preceding call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>.</p>
</dd>

### -param <i>Buffer</i> [in, optional]

<dd>
<p>Pointer to a caller-allocated buffer containing any data to be transmitted to the party on the
     remote node when the connection is closed. Depending on the underlying medium, this pointer can be
     <b>NULL</b>.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size, in bytes, at 
     <i>Buffer</i>, zero if 
     <i>Buffer</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>When 
     <b>NdisClCloseCall</b> returns anything other than NDIS_STATUS_PENDING, the client should make an
     internal call to its 
     <a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">
     ProtocolClCloseCallComplete</a> function. Otherwise, NDIS calls the client's 
     <i>ProtocolClCloseCallComplete</i> function when this operation is completed.</p>

## -remarks
<p>Clients usually call 
    <b>NdisClCloseCall</b> in any one of the following circumstances:</p>

<p>To close an established call, whether the call was initiated by the client with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> or was offered by a remote
      peer and accepted by the client's 
      <a href="..\ndis\nc-ndis-protocol-cl-incoming-call.md">
      ProtocolClIncomingCall</a> function.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">
      ProtocolClIncomingCloseCall</a> function to tear down an established call.</p>

<p>This occurs when the remote party closes an incoming call that the remote party originally initiated
      and that the client accepted. For client-initiated outgoing calls, this occurs either when the remote
      party closes the point-to-point connection on the remote node or when the last remaining party on a
      multipoint VC closes the call on the remote node.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-make-call-complete.md">
      ProtocolClMakeCallComplete</a> function to tear down a client-initiated attempt to make an outgoing
      call.</p>

<p>This occurs if the call manager has modified the client-specified call parameters passed to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> and the client finds these
      modifications unacceptable.</p>

<p>From the 
      <i>ProtocolClIncomingQoSChange</i> function to tear down an established call.</p>

<p>This occurs if a QoS change proposed by the other party on the VC is unacceptable to the client.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-modify-call-qos-complete.md">
      ProtocolClModifyCallQoSComplete</a> function to tear down an established call.</p>

<p>This occurs if a client-proposed QoS change on the VC is not accepted and the CM-modified QoS
      returned to 
      <i>ProtocolClModifyCallQoSComplete</i> is unacceptable to the client.</p>

<p>Before calling 
    <b>NdisClCloseCall</b>, a protocol must ensure that all its outstanding send packets have been returned
    to its 
    <a href="..\ndis\nc-ndis-protocol-co-send-net-buffer-lists-complete.md">
    ProtocolCoSendNetBufferListsComplete</a> function. (Packets sent via 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561728">NdisCoSendNetBufferLists</a> are
    always returned asynchronously to 
    <i>ProtocolCoSendNetBufferListsComplete</i>.) After calling 
    <b>NdisClCloseCall</b>, a protocol must not call 
    <b>NdisCoSendNetBufferLists</b> to send
    packets on the VC referenced by 
    <b>NdisClCloseCall</b>.</p>

<p>A client's call to 
    <b>NdisClCloseCall</b> causes NDIS to mark the 
    <i>NdisVcHandle</i> as closing and to call the CM's 
    <a href="..\ndis\nc-ndis-protocol-cm-close-call.md">ProtocolCmCloseCall</a> function.</p>

<p>To tear down an established call on a client-created multipoint VC, the client must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> one or more times to
    release all but the last party on the VC 
    before it calls 
    <b>NdisClCloseCall</b>. The call manager will fail any client's request to close a multipoint call if the
    given VC still has more than one party connected. The 
    <i>NdisPartyHandle</i> passed to 
    <b>NdisClCloseCall</b> can be any valid handle that the client obtained from its preceding calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> with the given 
    <i>NdisVcHandle</i> .</p>

<p>As remote parties to a client-initiated multipoint call request that their connections be closed, NDIS
    calls that client's 
    <i>ProtocolClDropParty</i> function as long as more than one outstanding party exists on the
    client-created multipoint VC. When the last remaining remote party closes its connection, NDIS calls the
    client's 
    <a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">
    ProtocolClIncomingCloseCall</a> function instead. Consequently, the 
    <i>ProtocolClIncomingCloseCall</i> function of any client that sets up multipoint connections must
    identify the last remaining party on its multipoint VCs and pass the appropriate 
    <i>NdisPartyHandle</i> to 
    <b>NdisClCloseCall</b>.</p>

<p>After the client releases an 
    <i>NdisPartyHandle</i> with 
    <b>NdisClCloseCall</b>, it can release (or reinitialize for reuse) the resources for the per-party state
    it was maintaining. However, the client cannot release or reuse its per-VC resources in a similar manner
    on completion of the operation it initiated with 
    <b>NdisClCloseCall</b> because the 
    <i>NdisVcHandle</i>, which cannot be reused to make another call because it is marked as closing, is
    still valid until the VC is destroyed. Either the client must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> if it created the VC for an
    outgoing call before it releases or reinitializes its per-VC resources, or the client must defer the
    release or reinitialization of these resources until its 
    <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function is
    called.</p>

<p>Clients usually call 
    <b>NdisClCloseCall</b> in any one of the following circumstances:</p>

<p>To close an established call, whether the call was initiated by the client with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> or was offered by a remote
      peer and accepted by the client's 
      <a href="..\ndis\nc-ndis-protocol-cl-incoming-call.md">
      ProtocolClIncomingCall</a> function.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">
      ProtocolClIncomingCloseCall</a> function to tear down an established call.</p>

<p>This occurs when the remote party closes an incoming call that the remote party originally initiated
      and that the client accepted. For client-initiated outgoing calls, this occurs either when the remote
      party closes the point-to-point connection on the remote node or when the last remaining party on a
      multipoint VC closes the call on the remote node.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-make-call-complete.md">
      ProtocolClMakeCallComplete</a> function to tear down a client-initiated attempt to make an outgoing
      call.</p>

<p>This occurs if the call manager has modified the client-specified call parameters passed to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> and the client finds these
      modifications unacceptable.</p>

<p>From the 
      <i>ProtocolClIncomingQoSChange</i> function to tear down an established call.</p>

<p>This occurs if a QoS change proposed by the other party on the VC is unacceptable to the client.</p>

<p>From the 
      <a href="..\ndis\nc-ndis-protocol-cl-modify-call-qos-complete.md">
      ProtocolClModifyCallQoSComplete</a> function to tear down an established call.</p>

<p>This occurs if a client-proposed QoS change on the VC is not accepted and the CM-modified QoS
      returned to 
      <i>ProtocolClModifyCallQoSComplete</i> is unacceptable to the client.</p>

<p>Before calling 
    <b>NdisClCloseCall</b>, a protocol must ensure that all its outstanding send packets have been returned
    to its 
    <a href="..\ndis\nc-ndis-protocol-co-send-net-buffer-lists-complete.md">
    ProtocolCoSendNetBufferListsComplete</a> function. (Packets sent via 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561728">NdisCoSendNetBufferLists</a> are
    always returned asynchronously to 
    <i>ProtocolCoSendNetBufferListsComplete</i>.) After calling 
    <b>NdisClCloseCall</b>, a protocol must not call 
    <b>NdisCoSendNetBufferLists</b> to send
    packets on the VC referenced by 
    <b>NdisClCloseCall</b>.</p>

<p>A client's call to 
    <b>NdisClCloseCall</b> causes NDIS to mark the 
    <i>NdisVcHandle</i> as closing and to call the CM's 
    <a href="..\ndis\nc-ndis-protocol-cm-close-call.md">ProtocolCmCloseCall</a> function.</p>

<p>To tear down an established call on a client-created multipoint VC, the client must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> one or more times to
    release all but the last party on the VC 
    before it calls 
    <b>NdisClCloseCall</b>. The call manager will fail any client's request to close a multipoint call if the
    given VC still has more than one party connected. The 
    <i>NdisPartyHandle</i> passed to 
    <b>NdisClCloseCall</b> can be any valid handle that the client obtained from its preceding calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a> with the given 
    <i>NdisVcHandle</i> .</p>

<p>As remote parties to a client-initiated multipoint call request that their connections be closed, NDIS
    calls that client's 
    <i>ProtocolClDropParty</i> function as long as more than one outstanding party exists on the
    client-created multipoint VC. When the last remaining remote party closes its connection, NDIS calls the
    client's 
    <a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">
    ProtocolClIncomingCloseCall</a> function instead. Consequently, the 
    <i>ProtocolClIncomingCloseCall</i> function of any client that sets up multipoint connections must
    identify the last remaining party on its multipoint VCs and pass the appropriate 
    <i>NdisPartyHandle</i> to 
    <b>NdisClCloseCall</b>.</p>

<p>After the client releases an 
    <i>NdisPartyHandle</i> with 
    <b>NdisClCloseCall</b>, it can release (or reinitialize for reuse) the resources for the per-party state
    it was maintaining. However, the client cannot release or reuse its per-VC resources in a similar manner
    on completion of the operation it initiated with 
    <b>NdisClCloseCall</b> because the 
    <i>NdisVcHandle</i>, which cannot be reused to make another call because it is marked as closing, is
    still valid until the VC is destroyed. Either the client must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> if it created the VC for an
    outgoing call before it releases or reinitializes its per-VC resources, or the client must defer the
    release or reinitialization of these resources until its 
    <a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a> function is
    called.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff550852">NdisClCloseCall (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisClCloseCall (NDIS 5.1)</b>) in
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547996">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561728">NdisCoSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-close-call-complete.md">ProtocolClCloseCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-close-call.md">ProtocolClIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">ProtocolClIncomingDropParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-call-qos-change.md">
   ProtocolClIncomingCallQoSChange</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-make-call-complete.md">ProtocolClMakeCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-modify-call-qos-complete.md">
   ProtocolClModifyCallQoSComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-close-call.md">ProtocolCmCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-send-net-buffer-lists-complete.md">
   ProtocolCoSendNetBufferListsComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClCloseCall function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
