---
UID: NF:ndis.NdisMCmRegisterSapComplete
title: NdisMCmRegisterSapComplete macro
author: windows-driver-content
description: NdisMCmRegisterSapComplete returns the final status of a client's request, for which the MCM driver's ProtocolCmRegisterSap function previously returned NDIS_STATUS_PENDING, to register a SAP.
old-location: netvista\ndismcmregistersapcomplete.htm
old-project: netvista
ms.assetid: 53f94e25-ca6c-4230-8447-d36774322dc7
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: NdisMCmRegisterSapComplete macro [Network Drivers Starting with Windows Vista], NdisMCmRegisterSapComplete, condis_mcm_ref_4b7dfebf-1828-41cd-9645-0fc6774cc9a8.xml, netvista.ndismcmregistersapcomplete, ndis/NdisMCmRegisterSapComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCmRegisterSapComplete   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCmRegisterSapComplete   (NDIS 5.1)) in Windows XP.
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
-	NdisMCmRegisterSapComplete
product: Windows
targetos: Windows
req.typenames: "*PNDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE"
---


# NdisMCmRegisterSapComplete function
<b>NdisMCmRegisterSapComplete</b> returns the final status of a client's request, for which the MCM driver's
  
  <a href="..\ndis\nc-ndis-protocol_cm_reg_sap.md">ProtocolCmRegisterSap</a> function
  previously returned NDIS_STATUS_PENDING, to register a SAP.

## Syntax

````
VOID NdisMCmRegisterSapComplete(
  [in] NDIS_STATUS Status,
  [in] NDIS_HANDLE NdisSapHandle,
  [in] NDIS_HANDLE CallMgrSapContext
);
````

## Parameters

`_S_`

TBD

`_H_`

TBD

`_C_`

TBD


## Return Value

None

## Remarks

An MCM driver must call 
    <b>NdisMCmRegisterSapComplete</b> if its 
    <a href="..\ndis\nc-ndis-protocol_cm_reg_sap.md">ProtocolCmRegisterSap</a> function
    returned NDIS_STATUS_PENDING when it was called with the given 
    <i>NdisSapHandle</i> . The call to 
    <b>NdisMCmRegisterSapComplete</b> causes NDIS to call the client's 
    <a href="..\ndis\nc-ndis-protocol_cl_register_sap_complete.md">
    ProtocolClRegisterSapComplete</a> function.

If the MCM driver sets 
    <i>Status</i> to anything other than NDIS_STATUS_SUCCESS, it should consider the 
    <i>NdisSapHandle</i> invalid when 
    <b>NdisMCmRegisterSapComplete</b> returns control. After failing a SAP registration, the CM can release or
    reuse the per-SAP context area, if any, that it already allocated. NDIS also releases its context for the
    SAP if the MCM driver fails the registration.

Only connection-oriented miniport drivers that provide integrated call-management support can call 
    <b>NdisMCmRegisterSapComplete</b>. Stand-alone call managers, which register themselves with NDIS as
    protocol drivers, call 
    <b>NdisCmRegisterSapComplete</b> instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCmRegisterSapComplete   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCmRegisterSapComplete   (NDIS 5.1)) in Windows XP.  |
| **Target Platform** | Desktop |
| **Header** | ndis.h (include Ndis.h) |
| **Library** | ndis.h |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_MCM_Function |

## See Also

<a href="..\ndis\nf-ndis-ndisallocatefromnpagedlookasidelist.md">
   NdisAllocateFromNPagedLookasideList</a>



<a href="..\ndis\nc-ndis-protocol_cm_reg_sap.md">ProtocolCmRegisterSap</a>



<a href="..\ndis\nf-ndis-ndismcmdispatchincomingcall.md">NdisMCmDispatchIncomingCall</a>



<a href="..\ndis\nf-ndis-ndisclregistersap.md">NdisClRegisterSap</a>



<a href="..\ndis\nc-ndis-protocol_cl_register_sap_complete.md">
   ProtocolClRegisterSapComplete</a>



<a href="..\ndis\nf-ndis-ndiscmregistersapcomplete.md">NdisCmRegisterSapComplete</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCmRegisterSapComplete macro%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>