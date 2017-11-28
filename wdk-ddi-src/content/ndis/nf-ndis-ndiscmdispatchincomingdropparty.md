---
UID: NF.ndis.NdisCmDispatchIncomingDropParty
title: NdisCmDispatchIncomingDropParty
author: windows-driver-content
description: NdisCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC, usually because the call manager has received a request over the network to close an active multipoint connection.
old-location: netvista\ndiscmdispatchincomingdropparty.htm
old-project: netvista
ms.assetid: 9dce2b0a-1d0c-4c87-a32f-8bf72bb91cfe
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisCmDispatchIncomingDropParty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   NdisCmDispatchIncomingDropParty (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   NdisCmDispatchIncomingDropParty (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisCmDispatchIncomingDropParty
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

# NdisCmDispatchIncomingDropParty function



## -description
<p><b>NdisCmDispatchIncomingDropParty</b> notifies a client that it should remove a particular party on a
  multipoint VC, usually because the call manager has received a request over the network to close an active
  multipoint connection.</p>


## -syntax

````
VOID NdisCmDispatchIncomingDropParty(
  _In_     NDIS_STATUS DropStatus,
  _In_     NDIS_HANDLE NdisPartyHandle,
  _In_opt_ PVOID       Buffer,
  _In_     UINT        Size
);
````


## -parameters
<dl>

### -param <i>DropStatus</i> [in]

<dd>
<p>Indicates the reason this party is being dropped, usually NDIS_STATUS_SUCCESS if the remote party
     simply requested that its connection be closed.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in]

<dd>
<p>Specifies the handle that identifies the party to be dropped from the multipoint VC, which must
     have other parties that are still connected.</p>
</dd>

### -param <i>Buffer</i> [in, optional]

<dd>
<p>Pointer to a caller-allocated resident buffer containing additional protocol-specific data
     received from the remote party, if any. Depending on the underlying medium, this pointer can be
     <b>NULL</b>.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer, zero if 
     <i>Buffer</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>In the course of normal network operations, a stand-alone call manager's 
    <a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
    ProtocolCoReceiveNetBufferLists</a> function calls 
    <b>NdisCmDispatchIncomingDropParty</b> with the 
    <i>CloseStatus</i> set to NDIS_STATUS_SUCCESS because a remote client on a multipoint connection has
    called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>.</p>

<p>However, a call manager also can call 
    <b>NdisCmDispatchIncomingDropParty</b> with a CM-determined 
    <i>CloseStatus</i> at the behest of the network itself if abnormal network conditions occur, such as the
    failure of a switch on the path between the local client and one or more client(s) on an established
    multipoint connection.</p>

<p>A call to 
    <b>NdisCmDispatchIncomingDropParty</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">
    ProtocolClIncomingDropParty</a> function.</p>

<p>If the 
    <i>NdisPartyHandle</i> identifies the last remaining party on the given VC, the CM calls 
    <a href="..\ndis\nf-ndis-ndiscmdispatchincomingclosecall.md">
    NdisCmDispatchIncomingCloseCall</a>, rather than 
    <b>NdisCmDispatchIncomingDropParty</b>.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDispatchIncomingDropParty</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmDispatchIncomingDropParty</b> instead.</p>

<p>In the course of normal network operations, a stand-alone call manager's 
    <a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
    ProtocolCoReceiveNetBufferLists</a> function calls 
    <b>NdisCmDispatchIncomingDropParty</b> with the 
    <i>CloseStatus</i> set to NDIS_STATUS_SUCCESS because a remote client on a multipoint connection has
    called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>.</p>

<p>However, a call manager also can call 
    <b>NdisCmDispatchIncomingDropParty</b> with a CM-determined 
    <i>CloseStatus</i> at the behest of the network itself if abnormal network conditions occur, such as the
    failure of a switch on the path between the local client and one or more client(s) on an established
    multipoint connection.</p>

<p>A call to 
    <b>NdisCmDispatchIncomingDropParty</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">
    ProtocolClIncomingDropParty</a> function.</p>

<p>If the 
    <i>NdisPartyHandle</i> identifies the last remaining party on the given VC, the CM calls 
    <a href="..\ndis\nf-ndis-ndiscmdispatchincomingclosecall.md">
    NdisCmDispatchIncomingCloseCall</a>, rather than 
    <b>NdisCmDispatchIncomingDropParty</b>.</p>

<p>Only stand-alone call managers, which register themselves with NDIS as protocol drivers, can call 
    <b>NdisCmDispatchIncomingDropParty</b>. Connection-oriented miniport drivers that provide integrated
    call-management support call 
    <b>NdisMCmDispatchIncomingDropParty</b> instead.</p>

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
   <a href="https://msdn.microsoft.com/80a5d961-c79b-4222-88c1-ddfd0d3d936f">
   NdisCmDispatchIncomingDropParty (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisCmDispatchIncomingDropParty (NDIS 5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmdispatchincomingclosecall.md">
   NdisCmDispatchIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmdispatchincomingdropparty.md">
   NdisMCmDispatchIncomingDropParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-incoming-drop-party.md">ProtocolClIncomingDropParty</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-receive-net-buffer-lists.md">
   ProtocolCoReceiveNetBufferLists</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisCmDispatchIncomingDropParty function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
