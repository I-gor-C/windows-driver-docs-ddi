---
UID: NF.ndis.NdisClModifyCallQoS
title: NdisClModifyCallQoS function
author: windows-driver-content
description: NdisClModifyCallQoS requests a change in the quality of service on a connection.
old-location: netvista\ndisclmodifycallqos.htm
old-project: netvista
ms.assetid: c31449a6-e275-480c-83ea-8575fda73cd9
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisClModifyCallQoS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisClModifyCallQoS (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisClModifyCallQoS (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClModifyCallQoS
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
---

# NdisClModifyCallQoS function



## -description
<b>NdisClModifyCallQoS</b> requests a change in the quality of service on a connection.



## -syntax

````
NDIS_STATUS NdisClModifyCallQoS(
  _In_ NDIS_HANDLE         NdisVcHandle,
  _In_ PCO_CALL_PARAMETERS CallParameters
);
````


## -parameters

### -param NdisVcHandle [in]

Specifies the handle to the VC for which the client wants to modify the QoS. The client originally
     obtained this handle by calling 
     <a href="netvista.ndiscocreatevc">NdisCoCreateVc</a>, and, more recently,
     retrieved this handle from its per-VC state area.


### -param CallParameters [in]

Pointer to a structure of type CO_CALL_PARAMETERS that specifies the new QoS requested by the
     caller.


## -returns
When 
     <b>NdisClModifyCallQoS</b> returns anything other than NDIS_STATUS_PENDING, the client should make an
     internal call to its 
     <a href="..\ndis\nc-ndis-protocol_cl_modify_call_qos_complete.md">
     ProtocolClModifyCallQoSComplete</a> function. Otherwise, NDIS calls the client's 
     <i>ProtocolClModifyCallQoSComplete</i> function when this operation is completed.


## -remarks
A call to 
    <b>NdisClModifyCallQoS</b> causes NDIS to call the CM's 
    <a href="..\ndis\nc-ndis-protocol_cm_modify_qos_call.md">
    ProtocolCmModifyCallQoS</a> function, which, in turn, calls 
    <a href="netvista.ndiscmactivatevc">NdisCmActivateVc</a> to notify the underlying
    miniport driver to change the call parameters if the requested QoS change can be made.

If the call manager does not accept the client's proposed QoS change, the client either can continue
    using the unchanged QoS for the call or can tear down the call. If the client and call manager cannot
    agree on the QoS for a particular call, the creator of the VC is responsible for initiating the teardown
    of the VC.


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
   <a href="https://msdn.microsoft.com/a4c237f6-cefc-41a7-900a-d38b4fa01c3b">NdisClModifyCallQoS (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisClModifyCallQoS (NDIS
   5.1)</b>) in Windows XP.

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
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="devtest.ndis_irql_protocol_driver_function">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_co_activate_vc.md">MiniportCoActivateVc</a>
</dt>
<dt>
<a href="netvista.ndisclclosecall">NdisClCloseCall</a>
</dt>
<dt>
<a href="netvista.ndiscmmodifycallqoscomplete">NdisCmModifyCallQoSComplete</a>
</dt>
<dt>
<a href="netvista.ndiscocreatevc">NdisCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_modify_call_qos_complete.md">
   ProtocolClModifyCallQoSComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cm_modify_qos_call.md">ProtocolCmModifyCallQoS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClModifyCallQoS function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

