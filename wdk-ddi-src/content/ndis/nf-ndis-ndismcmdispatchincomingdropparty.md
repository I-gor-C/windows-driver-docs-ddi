---
UID: NF:ndis.NdisMCmDispatchIncomingDropParty
title: NdisMCmDispatchIncomingDropParty macro
author: windows-driver-content
description: NdisMCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC.
old-location: netvista\ndismcmdispatchincomingdropparty.htm
old-project: netvista
ms.assetid: 4549b6f4-5138-4724-959c-a36b38c319fd
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: NdisMCmDispatchIncomingDropParty, condis_mcm_ref_1a170d75-7913-4068-b047-206b531d42c6.xml, ndis/NdisMCmDispatchIncomingDropParty, netvista.ndismcmdispatchincomingdropparty, NdisMCmDispatchIncomingDropParty macro [Network Drivers Starting with Windows Vista]
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
req.ddi-compliance: Irql_MCM_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: ndis.h
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ndis.h
apiname:
-	NdisMCmDispatchIncomingDropParty
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisMCmDispatchIncomingDropParty function
<b>NdisMCmDispatchIncomingDropParty</b> notifies a client that it should remove a particular party on a
  multipoint VC.

## Syntax

````
VOID NdisMCmDispatchIncomingDropParty(
  [in]           NDIS_STATUS DropStatus,
  [in]           NDIS_HANDLE NdisPartyHandle,
  [in, optional] PVOID       Buffer,
  [in]           UINT        Size
);
````

## Parameters

`_S_`

TBD

`_H_`

TBD

`_B_`

TBD

`_Z_`

TBD


## Return Value

None

## Remarks

In the course of normal network operations, an MCM driver calls 
    <b>NdisMCmDispatchIncomingDropParty</b> with the 
    <i>CloseStatus</i> set to NDIS_STATUS_SUCCESS because a remote client on a multipoint connection has
    called 
    <a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a>.

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
    <a href="..\ndis\nf-ndis-ndismcmdispatchincomingclosecall.md">
    NdisMCmDispatchIncomingCloseCall</a>, rather than 
    <b>NdisMCmDispatchIncomingDropParty</b>.

Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDispatchIncomingDropParty</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmDispatchIncomingDropParty</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows XP. Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows XP. |
| **Target Platform** | Desktop |
| **Header** | ndis.h (include Ndis.h) |
| **Library** | ndis.h |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_MCM_Function |

## See Also

<a href="..\ndis\nf-ndis-ndismcmdispatchincomingclosecall.md">
   NdisMCmDispatchIncomingCloseCall</a>

<a href="..\ndis\nc-ndis-protocol_cl_incoming_drop_party.md">ProtocolClIncomingDropParty</a>

<a href="..\ndis\nf-ndis-ndiscmdispatchincomingdropparty.md">
   NdisCmDispatchIncomingDropParty</a>

<a href="..\ndis\nf-ndis-ndiscldropparty.md">NdisClDropParty</a>

<a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmDispatchIncomingDropParty macro%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>