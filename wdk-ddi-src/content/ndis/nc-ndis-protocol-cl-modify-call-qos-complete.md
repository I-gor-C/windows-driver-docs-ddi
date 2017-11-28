---
UID: NC.ndis.PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE
title: PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE
author: windows-driver-content
description: The ProtocolClModifyCallQoSComplete function is used by connection-oriented NDIS clients that can modify the quality of service on a connection dynamically.
old-location: netvista\protocolclmodifycallqoscomplete.htm
old-project: netvista
ms.assetid: 0d925862-49af-4579-b877-c9a033e73be0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   ProtocolClModifyCallQoSComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   ProtocolClModifyCallQoSComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClModifyCallQoSComplete
req.alt-loc: Ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE callback



## -description
<p>The 
  <i>ProtocolClModifyCallQoSComplete</i> function is used by connection-oriented NDIS clients that can modify
  the quality of service on a connection dynamically. Such clients must have 
  <i>ProtocolClModifyCallQoSComplete</i> functions to complete the asynchronous operations that they initate
  with 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a>. Otherwise, such a
  protocol driver's registered 
  <i>ProtocolClModifyCallQoSComplete</i> function can simply return control.</p>


## -prototype

````
PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE ProtocolClModifyCallQoSComplete;

VOID ProtocolClModifyCallQoSComplete(
  _In_ NDIS_STATUS         Status,
  _In_ NDIS_HANDLE         ProtocolVcContext,
  _In_ PCO_CALL_PARAMETERS CallParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client's asynchronous request to modify the call parameters for
     this VC as one of the following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The QoS was modified as requested by the client.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>NDIS or the call manager could not modify the QoS because one of them could not allocate
       sufficient resources dynamically.</p>
</dd>

### -param <a id="NDIS_STATUS_INVALID_DATA"></a><a id="ndis_status_invalid_data"></a>NDIS_STATUS_INVALID_DATA

<dd>
<p>The call parameters that the client supplied to 
       <b>NdisClModifyCallQoS</b> were invalid.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>The call manager could not change the QoS because of a failure on the network or in another
       connection-oriented network component.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX"></a><a id="ndis_status_xxx"></a>NDIS_STATUS_<i>XXX</i>

<dd>
<p>The call manager failed to change the QoS, and NDIS propagated the CM-determined failure status
       to the client.</p>
</dd>
</dl>
</dd>

### -param <i>ProtocolVcContext</i> [in]

<dd>
<p>Specifies the handle to the client's per-VC context area, which the client originally supplied to
     NDIS when it called 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> to set up the VC for its
     outgoing call request or from its 
     <i>ProtocolCoCreateVc</i> function if the client accepted an incoming call on this VC.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to a buffered CO_CALL_PARAMETERS structure containing the client-specified QoS change it
     requested, or, possibly, the original QoS for this VC established when the connection was activated,
     which the call manager has restored.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClModifyCallQoSComplete</i> indicates that the call manager has completed processing of a
    client-initiated request to change the quality of service on an active VC. For example, if the underlying
    network medium supports dynamic QoS changes, a client can request modifications at any time on an active
    VC.</p>

<p>If the client's call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> succeeds, 
    <i>ProtocolClModifyCallQoSComplete</i> can accept the QoS change by simply returning control. Otherwise, 
    <i>ProtocolClModifyCallQoSComplete</i> can engage in further negotiation with the call manager as long as
    the client's developer places some reasonable limit on the number of possible renegotiations.
    Alternatively, 
    <i>ProtocolClModifyCallQoSComplete</i> can simply tear down the call with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a> whenever the call manager
    rejects a request to change the QoS and the previously established QoS has become unacceptable to the
    client.</p>

<p>To define a <i>ProtocolClModifyCallQoSComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClModifyCallQoSComplete</i> function that is named "MyClModifyCallQoSComplete", use the <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A call to 
    <i>ProtocolClModifyCallQoSComplete</i> indicates that the call manager has completed processing of a
    client-initiated request to change the quality of service on an active VC. For example, if the underlying
    network medium supports dynamic QoS changes, a client can request modifications at any time on an active
    VC.</p>

<p>If the client's call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> succeeds, 
    <i>ProtocolClModifyCallQoSComplete</i> can accept the QoS change by simply returning control. Otherwise, 
    <i>ProtocolClModifyCallQoSComplete</i> can engage in further negotiation with the call manager as long as
    the client's developer places some reasonable limit on the number of possible renegotiations.
    Alternatively, 
    <i>ProtocolClModifyCallQoSComplete</i> can simply tear down the call with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a> whenever the call manager
    rejects a request to change the QoS and the previously established QoS has become unacceptable to the
    client.</p>

<p>To define a <i>ProtocolClModifyCallQoSComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClModifyCallQoSComplete</i> function that is named "MyClModifyCallQoSComplete", use the <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/4efa0174-902e-4056-8dc6-1ad7b2fc5090">
   ProtocolClModifyCallQoSComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>
   ProtocolClModifyCallQoSComplete (NDIS 5.1)</i>) in Windows XP.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561679">NdisCmModifyCallQoSComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563545">NdisMCmModifyCallQoSComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-modify-qos-call.md">ProtocolCmModifyCallQoS</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
