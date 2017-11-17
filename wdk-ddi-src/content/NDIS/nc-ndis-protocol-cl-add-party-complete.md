---
UID: NC.ndis.PROTOCOL_CL_ADD_PARTY_COMPLETE
title: PROTOCOL_CL_ADD_PARTY_COMPLETE
author: windows-driver-content
description: The ProtocolClAddPartyComplete function is required for connection-oriented NDIS clients that set up multipoint connections.
old-location: netvista\protocolcladdpartycomplete.htm
ms.assetid: ea3ebbe9-fd94-44b8-8801-639d099c5158
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   ProtocolClAddPartyComplete
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolClAddPartyComplete
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClAddPartyComplete
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
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# PROTOCOL_CL_ADD_PARTY_COMPLETE callback



## -description
<p>The 
  <i>ProtocolClAddPartyComplete</i> function is required for connection-oriented NDIS clients that set up
  multipoint connections. Such clients must have 
  <i>ProtocolClAddPartyComplete</i> functions to complete the asynchronous operations that they initiate with 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>. Otherwise, such a protocol
  driver's registered 
  <i>ProtocolClAddPartyComplete</i> function can simply return control.</p>


## -prototype

````
PROTOCOL_CL_ADD_PARTY_COMPLETE ProtocolClAddPartyComplete;

VOID ProtocolClAddPartyComplete(
  _In_ NDIS_STATUS         Status,
  _In_ NDIS_HANDLE         ProtocolPartyContext,
  _In_ NDIS_HANDLE         NdisPartyHandle,
  _In_ PCO_CALL_PARAMETERS CallParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies final status of the client-initiated add-party operation, which can be one of the
     following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The given party was added on the client's active multipoint VC.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>NDIS could not allocate sufficient resources to track the new party.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>The client passed an invalid 
       <i>NdisVcHandle</i> to 
       <b>NdisClAddParty</b>.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX"></a><a id="ndis_status_xxx"></a>NDIS_STATUS_<i>XXX</i>

<dd>
<p>The call manager's 
       <a href="https://msdn.microsoft.com/06aa5ff6-974c-43dd-8395-bc1a1a8421d5">ProtocolCmAddParty</a> function
       returned a CM-determined value to indicate why it could not add the party to the VC.</p>
</dd>
</dl>
</dd>

### -param <i>ProtocolPartyContext</i> [in]

<dd>
<p>Specifies the client-supplied handle originally passed to 
     <b>NdisClAddParty</b>.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in]

<dd>
<p>If 
     <i>Status</i> is NDIS_STATUS_SUCCESS, this NDIS-supplied handle represents the association between the
     call manager and client regarding this party. Otherwise, the attempt to add a party failed and the
     client should consider this parameter an invalid handle.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to a structure of type 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>, originally set up by
     the client for its call to 
     <b>NdisClAddParty</b> but possibly modified subsequently by the call manager.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClAddPartyComplete</i> indicates completion of the asynchronous operation initiated when the
    client called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>. If the input 
    <i>Status</i> is set to anything other than NDIS_STATUS_SUCCESS, 
    <i>ProtocolClAddPartyComplete</i> can release or reuse the client-allocated buffers at 
    <i>ProtocolPartyContext</i> and at 
    <i>CallParameters</i> .</p>

<p>If the attempt to add a party succeeded, 
    <i>ProtocolClAddPartyComplete</i> should save the input 
    <i>NdisPartyHandle</i> for subsequent calls to NDIS library functions concerning this party in the
    client's 
    <i>ProtocolPartyContext</i> area. For example, the client must pass this handle in a subsequent call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> eventually unless the
    remote party that it represents closes its connection first.</p>

<p>The structure at 
    <i>CallParameters</i> originally was allocated and initialized by the client, which passed this pointer to
    
    <b>NdisClAddParty</b>. However, the call manager might have modified the client-supplied values to
    reflect the results of the CM's negotiation with the network or with a signaling peer while processing
    the client's add-party request. To determine whether the call manager made any modifications, 
    <i>ProtocolClAddPartyComplete</i> can check the 
    <b>Flags</b> member of this structure for whether CALL_PARAMETERS_CHANGED is set. If so, 
    <i>ProtocolClAddPartyComplete</i> must update the per-party state that the client maintains for this call
    at 
    <i>ProtocolPartyContext</i> unless it finds the CM's modifications unacceptable. The particular signaling
    protocol determines what the client can do in this case. Usually, a client calls 
    <b>NdisClDropParty</b> if it finds the CM-modified call parameters unacceptable.</p>

<p>Depending on the signaling protocol of the call manager, the traffic parameters at 
    <i>CallParameters</i> can be identical for all parties on any particular multipoint connection. That is,
    as the client of such a call manager adds parties on a multipoint connection that the client originally
    set up with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>, it can supply only the
    target address of each party and leave the traffic parameters as originally set up for the multipoint VC
    each time it calls 
    <b>NdisClAddParty</b>.</p>

<p>To define a <i>ProtocolClAddPartyComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClAddPartyComplete</i> function that is named "MyClAddPartyComplete", use the <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A call to 
    <i>ProtocolClAddPartyComplete</i> indicates completion of the asynchronous operation initiated when the
    client called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>. If the input 
    <i>Status</i> is set to anything other than NDIS_STATUS_SUCCESS, 
    <i>ProtocolClAddPartyComplete</i> can release or reuse the client-allocated buffers at 
    <i>ProtocolPartyContext</i> and at 
    <i>CallParameters</i> .</p>

<p>If the attempt to add a party succeeded, 
    <i>ProtocolClAddPartyComplete</i> should save the input 
    <i>NdisPartyHandle</i> for subsequent calls to NDIS library functions concerning this party in the
    client's 
    <i>ProtocolPartyContext</i> area. For example, the client must pass this handle in a subsequent call to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> eventually unless the
    remote party that it represents closes its connection first.</p>

<p>The structure at 
    <i>CallParameters</i> originally was allocated and initialized by the client, which passed this pointer to
    
    <b>NdisClAddParty</b>. However, the call manager might have modified the client-supplied values to
    reflect the results of the CM's negotiation with the network or with a signaling peer while processing
    the client's add-party request. To determine whether the call manager made any modifications, 
    <i>ProtocolClAddPartyComplete</i> can check the 
    <b>Flags</b> member of this structure for whether CALL_PARAMETERS_CHANGED is set. If so, 
    <i>ProtocolClAddPartyComplete</i> must update the per-party state that the client maintains for this call
    at 
    <i>ProtocolPartyContext</i> unless it finds the CM's modifications unacceptable. The particular signaling
    protocol determines what the client can do in this case. Usually, a client calls 
    <b>NdisClDropParty</b> if it finds the CM-modified call parameters unacceptable.</p>

<p>Depending on the signaling protocol of the call manager, the traffic parameters at 
    <i>CallParameters</i> can be identical for all parties on any particular multipoint connection. That is,
    as the client of such a call manager adds parties on a multipoint connection that the client originally
    set up with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>, it can supply only the
    target address of each party and leave the traffic parameters as originally set up for the multipoint VC
    each time it calls 
    <b>NdisClAddParty</b>.</p>

<p>To define a <i>ProtocolClAddPartyComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClAddPartyComplete</i> function that is named "MyClAddPartyComplete", use the <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_ADD_PARTY_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/e78b2cfa-2c60-4a70-8926-97b2ef75914c">ProtocolClAddPartyComplete
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolClAddPartyComplete
   (NDIS 5.1)</i>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561651">NdisCmAddPartyComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562798">NdisMCmAddPartyComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3815ca4b-f4bc-4de9-a28a-5d3ee20bcdd8">ProtocolClIncomingDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/06aa5ff6-974c-43dd-8395-bc1a1a8421d5">ProtocolCmAddParty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_ADD_PARTY_COMPLETE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
