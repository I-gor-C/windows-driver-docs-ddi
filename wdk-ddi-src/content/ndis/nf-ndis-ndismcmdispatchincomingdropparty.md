---
UID: NF.ndis.NdisMCmDispatchIncomingDropParty
title: NdisMCmDispatchIncomingDropParty macro
author: windows-driver-content
description: NdisMCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC.
old-location: netvista\ndismcmdispatchincomingdropparty.htm
old-project: netvista
ms.assetid: 4549b6f4-5138-4724-959c-a36b38c319fd
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisMCmDispatchIncomingDropParty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCmDispatchIncomingDropParty
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
req.irql: <= DISPATCH_LEVEL
---

# NdisMCmDispatchIncomingDropParty macro



## -description
<b>NdisMCmDispatchIncomingDropParty</b> notifies a client that it should remove a particular party on a
  multipoint VC.



## -syntax

````
VOID NdisMCmDispatchIncomingDropParty(
  [in]           NDIS_STATUS DropStatus,
  [in]           NDIS_HANDLE NdisPartyHandle,
  [in, optional] PVOID       Buffer,
  [in]           UINT        Size
);
````


## -parameters

### -param DropStatus [in]

Indicates the reason this party is being dropped, usually NDIS_STATUS_SUCCESS if the remote party
     simply requested that its connection be closed.


### -param NdisPartyHandle [in]

Specifies the handle that identifies the party to be dropped from the multipoint VC, which must
     have other parties that are still connected. The MCM driver originally obtained this handle as an input
     parameter to its 
     <a href="..\ndis\nc-ndis-protocol_cm_add_party.md">ProtocolCmAddParty</a> function.


### -param Buffer [in, optional]

Pointer to a caller-allocated resident buffer containing additional protocol-specific data
     received from the remote party, if any. Depending on the underlying medium, this pointer can be
     <b>NULL</b>.


### -param Size [in]

Specifies the size in bytes of the buffer, zero if 
     <i>Buffer</i> is <b>NULL</b>.


## -remarks
In the course of normal network operations, an MCM driver calls 
    <b>NdisMCmDispatchIncomingDropParty</b> with the 
    <i>CloseStatus</i> set to NDIS_STATUS_SUCCESS because a remote client on a multipoint connection has
    called 
    <a href="netvista.ndisclclosecall">NdisClCloseCall</a>.

However, an MCM driver also can call 
    <b>NdisMCmDispatchIncomingDropParty</b> with a driver-determined 
    <i>CloseStatus</i> at the behest of the network itself if abnormal network conditions occur, such as the
    failure of a switch on the path between the local client and one or more client(s) on an established
    multipoint connection.

A call to 
    <b>NdisMCmDispatchIncomingDropParty</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol_cl_incoming_drop_party.md">
    ProtocolClIncomingDropParty</a> function.

If the 
    <i>NdisPartyHandle</i> identifies the last remaining party on the given VC, the MCM driver calls 
    <a href="netvista.ndismcmdispatchincomingclosecall">
    NdisMCmDispatchIncomingCloseCall</a>, rather than 
    <b>NdisMCmDispatchIncomingDropParty</b>.

Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDispatchIncomingDropParty</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmDispatchIncomingDropParty</b> instead.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/0d445263-b1cb-4e83-8144-54740445e431">
   NdisMCmDispatchIncomingDropParty (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>
   NdisMCmDispatchIncomingDropParty (NDIS 5.1)</b>) in Windows XP.

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
<a href="devtest.ndis_irql_mcm_function">Irql_MCM_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="netvista.ndiscldropparty">NdisClDropParty</a>
</dt>
<dt>
<a href="netvista.ndiscmdispatchincomingdropparty">
   NdisCmDispatchIncomingDropParty</a>
</dt>
<dt>
<a href="netvista.ndismcmdispatchincomingclosecall">
   NdisMCmDispatchIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_incoming_drop_party.md">ProtocolClIncomingDropParty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmDispatchIncomingDropParty macro%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

