---
UID: NF:ndis.NdisMCmCloseCallComplete
title: NdisMCmCloseCallComplete macro
author: windows-driver-content
description: NdisMCmCloseCallComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to tear down a call.
old-location: netvista\ndismcmclosecallcomplete.htm
old-project: netvista
ms.assetid: 24477865-fb89-4078-99cb-1bf24249c7e2
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NdisMCmCloseCallComplete, NdisMCmCloseCallComplete macro [Network Drivers Starting with Windows Vista], condis_mcm_ref_78d6cea5-8d8c-49d4-ad57-c41eb63d3a4b.xml, ndis/NdisMCmCloseCallComplete, netvista.ndismcmclosecallcomplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCmCloseCallComplete (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCmCloseCallComplete (NDIS   5.1)) in Windows XP.
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
-	NdisMCmCloseCallComplete
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisMCmCloseCallComplete function
<b>NdisMCmCloseCallComplete</b> returns the final status of a client's request, for which the MCM driver
  previously returned NDIS_STATUS_PENDING, to tear down a call.

## Syntax

````
VOID NdisMCmCloseCallComplete(
  [in]           NDIS_STATUS Status,
  [in]           NDIS_HANDLE NdisVcHandle,
  [in, optional] NDIS_HANDLE NdisPartyHandle
);
````

## Parameters

`_S_`

TBD

`_VH_`

TBD

`_PH_`

TBD


## Return Value

None

## Remarks

If an MCM driver's 
    <i>ProtocolCmCloseCall</i> function returns NDIS_STATUS_PENDING, it must call 
    <b>NdisMCmCloseCallComplete</b> subsequently to notify the client and NDIS that its attempt to break the
    connection has completed, whether successfully or with an error. A call to 
    <b>NdisMCmCloseCallComplete</b> causes NDIS to call the client's 
    <i>ProtocolClCloseCallComplete</i> function.

If it passes NDIS_STATUS_SUCCESS as the 
    <i>Status</i>, the MCM driver should consider the 
    <i>NdisVcHandle</i> (and 
    <i>NdisPartyHandle</i>, if any) unusable for transfers over the network as soon as it calls 
    <b>NdisMCmCloseCallComplete</b>. If the MCM driver originally created the VC, it should call 
    <a href="..\ndis\nf-ndis-ndismcmdeletevc.md">NdisMCmDeleteVc</a> with the same 
    <i>NdisVcHandle</i> that it just passed to 
    <b>NdisMCmCloseCallComplete</b>. If the client created this VC, the MCM driver can expect a call to its 
    <a href="..\ndis\nc-ndis-protocol_co_delete_vc.md">ProtocolCoDeleteVc</a> function with the
    
    <i>ProtocolVcContext</i>, designating its per-VC state in which it has stored the same 
    <i>NdisVcHandle</i>, as an input parameter.

Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmCloseCallComplete</b>. Stand-alone call managers, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCmCloseCallComplete</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCmCloseCallComplete (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCmCloseCallComplete (NDIS   5.1)) in Windows XP.  |
| **Target Platform** | Desktop |
| **Header** | ndis.h (include Ndis.h) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_MCM_Function |

## See Also

<a href="..\ndis\nc-ndis-protocol_cl_close_call_complete.md">ProtocolClCloseCallComplete</a>



<a href="..\ndis\nc-ndis-protocol_co_delete_vc.md">ProtocolCoDeleteVc</a>



<a href="..\ndis\nf-ndis-ndiscmclosecallcomplete.md">NdisCmCloseCallComplete</a>



<a href="..\ndis\nf-ndis-ndismcmcreatevc.md">NdisMCmCreateVc</a>



<a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a>



<a href="..\ndis\nf-ndis-ndismcmdeletevc.md">NdisMCmDeleteVc</a>



<a href="..\ndis\nf-ndis-ndismcmdeactivatevc.md">NdisMCmDeactivateVc</a>