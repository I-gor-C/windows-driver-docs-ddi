---
UID: NC.ndis.PROTOCOL_CM_ACTIVATE_VC_COMPLETE
title: PROTOCOL_CM_ACTIVATE_VC_COMPLETE
author: windows-driver-content
description: The ProtocolCmActivateVcComplete function is required.
old-location: netvista\protocolcmactivatevccomplete.htm
old-project: netvista
ms.assetid: 6ec9e73e-8abd-4d27-b598-6176f2125348
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
   
   ProtocolCmActivateVcComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   ProtocolCmActivateVcComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCmActivateVcComplete
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

# PROTOCOL_CM_ACTIVATE_VC_COMPLETE callback



## -description
<p>The 
  <i>ProtocolCmActivateVcComplete</i> function is required. This function indicates to the call manager that a
  previous call to 
  <b>NdisCoActivateVc</b> has been completed by the miniport driver.</p>


## -prototype

````
PROTOCOL_CM_ACTIVATE_VC_COMPLETE ProtocolCmActivateVcComplete;

VOID ProtocolCmActivateVcComplete(
  _In_ NDIS_STATUS         Status,
  _In_ NDIS_HANDLE         CallMgrVcContext,
  _In_ PCO_CALL_PARAMETERS CallParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status, as indicated by the miniport driver, of the request by the call
     manager to activate a VC.</p>
</dd>

### -param <i>CallMgrVcContext</i> [in]

<dd>
<p>Specifies the handle to a call manager-allocated context area in which the call manager maintains
     its per-VC state. The call manager supplied this handle from its 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to the call parameters as specified by the call manager in a call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561649">NdisCmActivateVc</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When other network components have completed their operations for activating a virtual connection,
    initiated when the call manager called 
    <b>NdisCmActivateVc</b>, NDIS notifies the call manager that the VC has been activated by calling its 
    <i>ProtocolCmActivateVcComplete</i> function. The status of the activation is found in 
    <i>Status</i> . Possible values for 
    <i>Status</i> include, but are not limited to:</p>

<p></p><dl>
<dt><a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS</dt>
<dd>
<p>Indicates that the VC completed successfully and the call manager can continue operations on this
      VC as required by its media.</p>
</dd>
<dt><a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES</dt>
<dd>
<p>Indicates that another component in the activation has failed to activate the virtual connection
      because of a lack of memory or an inability allocate another type of resource.</p>
</dd>
<dt><a id="NDIS_STATUS_NOT_ACCEPTED"></a><a id="ndis_status_not_accepted"></a>NDIS_STATUS_NOT_ACCEPTED</dt>
<dd>
<p>Indicates that an activation is currently pending on the virtual connection. Only one activation
      can be processed at a time for a virtual connection. The request to activate the VC should be tried
      again at a later time.</p>
</dd>
<dt><a id="NDIS_STATUS_CLOSING"></a><a id="ndis_status_closing"></a>NDIS_STATUS_CLOSING</dt>
<dd>
<p>Indicates that a deactivation is pending on the VC and the VC is no longer available for network
      communication until the deactivation has been completed and a successful activation has taken
      place.</p>
</dd>
<dt><a id="NDIS_STATUS_INVALID_DATA"></a><a id="ndis_status_invalid_data"></a>NDIS_STATUS_INVALID_DATA</dt>
<dd>
<p>Indicates that the miniport driver has rejected the call parameters at 
      <i>CallParameters</i> as invalid for the adapter.</p>
</dd>
</dl><p>Indicates that the VC completed successfully and the call manager can continue operations on this
      VC as required by its media.</p>

<p>Indicates that another component in the activation has failed to activate the virtual connection
      because of a lack of memory or an inability allocate another type of resource.</p>

<p>Indicates that an activation is currently pending on the virtual connection. Only one activation
      can be processed at a time for a virtual connection. The request to activate the VC should be tried
      again at a later time.</p>

<p>Indicates that a deactivation is pending on the VC and the VC is no longer available for network
      communication until the deactivation has been completed and a successful activation has taken
      place.</p>

<p>Indicates that the miniport driver has rejected the call parameters at 
      <i>CallParameters</i> as invalid for the adapter.</p>

<p><i>ProtocolCmActivateVcComplete</i> must check the status returned in 
    <i>Status</i> to ensure that the virtual connection has been activated successfully. The call manager 
    <u>must not</u> attempt to communicate over the virtual connection if 
    <i>Status</i> is not NDIS_STATUS_SUCCESS.</p>

<p>Call managers must complete any processing required by their network media to ensure that the virtual
    connection is ready for data transmission before returning control to NDIS.</p>

<p>If the call manager specified either ROUND_UP_FLOW or ROUND_DOWN_FLOW in the 
    <i>CallParameters</i> 
    
     -&gt;
    
    <b>MediaParameters-&gt;Flags</b>, the call parameters returned in 
    <i>CallParameters</i> can have been changed by the miniport driver. Call managers should examine the call
    parameters that were returned to ensure proper operation. If the new call parameters are unsatisfactory,
    the call manager should either call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561649">NdisCmActivateVc</a> again with new call
    parameters or deactivate the VC with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561657">NdisCmDeactivateVc</a>.</p>

<p>To define a <i>ProtocolCmActivateVcComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmActivateVcComplete</i> function that is named "MyCmActivateVcComplete", use the <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>When other network components have completed their operations for activating a virtual connection,
    initiated when the call manager called 
    <b>NdisCmActivateVc</b>, NDIS notifies the call manager that the VC has been activated by calling its 
    <i>ProtocolCmActivateVcComplete</i> function. The status of the activation is found in 
    <i>Status</i> . Possible values for 
    <i>Status</i> include, but are not limited to:</p>

<p></p><dl>
<dt><a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS</dt>
<dd>
<p>Indicates that the VC completed successfully and the call manager can continue operations on this
      VC as required by its media.</p>
</dd>
<dt><a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES</dt>
<dd>
<p>Indicates that another component in the activation has failed to activate the virtual connection
      because of a lack of memory or an inability allocate another type of resource.</p>
</dd>
<dt><a id="NDIS_STATUS_NOT_ACCEPTED"></a><a id="ndis_status_not_accepted"></a>NDIS_STATUS_NOT_ACCEPTED</dt>
<dd>
<p>Indicates that an activation is currently pending on the virtual connection. Only one activation
      can be processed at a time for a virtual connection. The request to activate the VC should be tried
      again at a later time.</p>
</dd>
<dt><a id="NDIS_STATUS_CLOSING"></a><a id="ndis_status_closing"></a>NDIS_STATUS_CLOSING</dt>
<dd>
<p>Indicates that a deactivation is pending on the VC and the VC is no longer available for network
      communication until the deactivation has been completed and a successful activation has taken
      place.</p>
</dd>
<dt><a id="NDIS_STATUS_INVALID_DATA"></a><a id="ndis_status_invalid_data"></a>NDIS_STATUS_INVALID_DATA</dt>
<dd>
<p>Indicates that the miniport driver has rejected the call parameters at 
      <i>CallParameters</i> as invalid for the adapter.</p>
</dd>
</dl><p>Indicates that the VC completed successfully and the call manager can continue operations on this
      VC as required by its media.</p>

<p>Indicates that another component in the activation has failed to activate the virtual connection
      because of a lack of memory or an inability allocate another type of resource.</p>

<p>Indicates that an activation is currently pending on the virtual connection. Only one activation
      can be processed at a time for a virtual connection. The request to activate the VC should be tried
      again at a later time.</p>

<p>Indicates that a deactivation is pending on the VC and the VC is no longer available for network
      communication until the deactivation has been completed and a successful activation has taken
      place.</p>

<p>Indicates that the miniport driver has rejected the call parameters at 
      <i>CallParameters</i> as invalid for the adapter.</p>

<p><i>ProtocolCmActivateVcComplete</i> must check the status returned in 
    <i>Status</i> to ensure that the virtual connection has been activated successfully. The call manager 
    <u>must not</u> attempt to communicate over the virtual connection if 
    <i>Status</i> is not NDIS_STATUS_SUCCESS.</p>

<p>Call managers must complete any processing required by their network media to ensure that the virtual
    connection is ready for data transmission before returning control to NDIS.</p>

<p>If the call manager specified either ROUND_UP_FLOW or ROUND_DOWN_FLOW in the 
    <i>CallParameters</i> 
    
     -&gt;
    
    <b>MediaParameters-&gt;Flags</b>, the call parameters returned in 
    <i>CallParameters</i> can have been changed by the miniport driver. Call managers should examine the call
    parameters that were returned to ensure proper operation. If the new call parameters are unsatisfactory,
    the call manager should either call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561649">NdisCmActivateVc</a> again with new call
    parameters or deactivate the VC with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561657">NdisCmDeactivateVc</a>.</p>

<p>To define a <i>ProtocolCmActivateVcComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmActivateVcComplete</i> function that is named "MyCmActivateVcComplete", use the <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_ACTIVATE_VC_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/6da3e890-a7a7-44af-a593-6af261a90497">
   ProtocolCmActivateVcComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>
   ProtocolCmActivateVcComplete (NDIS 5.1)</i>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561649">NdisCmActivateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561657">NdisCmDeactivateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CM_ACTIVATE_VC_COMPLETE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
