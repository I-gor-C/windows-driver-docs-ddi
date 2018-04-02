---
UID: NF:ndis.NdisMCmDispatchIncomingDropParty
title: NdisMCmDispatchIncomingDropParty macro
author: windows-driver-content
description: NdisMCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC.
old-location: netvista\ndismcmdispatchincomingdropparty.htm
old-project: netvista
ms.assetid: 4549b6f4-5138-4724-959c-a36b38c319fd
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NdisMCmDispatchIncomingDropParty, NdisMCmDispatchIncomingDropParty macro [Network Drivers Starting with Windows Vista], condis_mcm_ref_1a170d75-7913-4068-b047-206b531d42c6.xml, ndis/NdisMCmDispatchIncomingDropParty, netvista.ndismcmdispatchincomingdropparty
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
req.lib: 
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndis.h
api_name:
-	NdisMCmDispatchIncomingDropParty
product:
- Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisMCmDispatchIncomingDropParty function
<b>NdisMCmDispatchIncomingDropParty</b> notifies a client that it should remove a particular party on a
  multipoint VC.

## Syntax

```
void NdisMCmDispatchIncomingDropParty(
   _S_,
   _H_,
   _B_,
   _Z_
);
```

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
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>.

However, an MCM driver also can call 
    <b>NdisMCmDispatchIncomingDropParty</b> with a driver-determined 
    <i>CloseStatus</i> at the behest of the network itself if abnormal network conditions occur, such as the
    failure of a switch on the path between the local client and one or more client(s) on an established
    multipoint connection.

A call to 
    <b>NdisMCmDispatchIncomingDropParty</b> causes NDIS to call the client's 
    <a href="https://msdn.microsoft.com/3815ca4b-f4bc-4de9-a28a-5d3ee20bcdd8">
    ProtocolClIncomingDropParty</a> function.

If the 
    <i>NdisPartyHandle</i> identifies the last remaining party on the given VC, the MCM driver calls 
    <a href="https://msdn.microsoft.com/843050e1-a1ec-4313-b527-529c4ff6ca07">
    NdisMCmDispatchIncomingCloseCall</a>, rather than 
    <b>NdisMCmDispatchIncomingDropParty</b>.

Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmDispatchIncomingDropParty</b>. Stand-alone call managers, which register themselves with NDIS
    as protocol drivers, call 
    <b>NdisCmDispatchIncomingDropParty</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       NdisMCmDispatchIncomingDropParty (NDIS 5.1)) in Windows XP.  |
| **Target Platform** | Desktop |
| **Header** | ndis.h (include Ndis.h) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_MCM_Function |

## See Also

<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>



<a href="https://msdn.microsoft.com/9dce2b0a-1d0c-4c87-a32f-8bf72bb91cfe">
   NdisCmDispatchIncomingDropParty</a>



<a href="https://msdn.microsoft.com/843050e1-a1ec-4313-b527-529c4ff6ca07">
   NdisMCmDispatchIncomingCloseCall</a>



<a href="https://msdn.microsoft.com/3815ca4b-f4bc-4de9-a28a-5d3ee20bcdd8">ProtocolClIncomingDropParty</a>