---
UID: NC.ndis.PROTOCOL_CL_MAKE_CALL_COMPLETE
title: PROTOCOL_CL_MAKE_CALL_COMPLETE
author: windows-driver-content
description: The ProtocolClMakeCallComplete function is used by connection-oriented NDIS clients that make outgoing calls.
old-location: netvista\protocolclmakecallcomplete.htm
ms.assetid: 6bb69f78-8dab-46a7-84fb-7bc17e894535
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   ProtocolClMakeCallComplete
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolClMakeCallComplete
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClMakeCallComplete
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

# PROTOCOL_CL_MAKE_CALL_COMPLETE callback



## -description
<p>The 
  <i>ProtocolClMakeCallComplete</i> function is used by connection-oriented NDIS clients that make outgoing
  calls. Such clients must have 
  <i>ProtocolClMakeCallComplete</i> functions to complete the asynchronous operations that they initiate with 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>. Otherwise, such a protocol
  driver's registered 
  <i>ProtocolClMakeCallComplete</i> function can simply return control.</p>


## -prototype

````
PROTOCOL_CL_MAKE_CALL_COMPLETE ProtocolClMakeCallComplete;

VOID ProtocolClMakeCallComplete(
  _In_     NDIS_STATUS         Status,
  _In_     NDIS_HANDLE         ProtocolVcContext,
  _In_opt_ NDIS_HANDLE         NdisPartyHandle,
  _In_     PCO_CALL_PARAMETERS CallParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client's original call to 
     <b>NdisClMakeCall</b>, which can be one of the following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The client's attempt to set up a virtual connection succeded. Consequently, the client can
       proceed to make transfers on the active VC using the 
       <i>NdisVcHandle</i> returned by 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>, which the client has
       stored in its per-VC context area at 
       <i>ProtocolVcContext</i> .</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>NDIS, the call manager, or an underlying driver could not allocate sufficient resources to set
       up the connection.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX"></a><a id="ndis_status_xxx"></a>NDIS_STATUS_<i>XXX</i>

<dd>
<p>The call manager or underlying miniport driver failed to establish an active connection and NDIS
       propagated this driver-determined failure status to the client.</p>
</dd>
</dl>
</dd>

### -param <i>ProtocolVcContext</i> [in]

<dd>
<p>Specifies the handle to the client's per-VC context area, which the client originally supplied to
     NDIS when it called 
     <b>NdisCoCreateVc</b> to set up the VC for its outgoing call.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in, optional]

<dd>
<p>If 
     <i>Status</i> is NDIS_STATUS_SUCCESS and the client created a multipoint VC by passing an explicit 
     <i>ProtocolPartyContext</i> handle to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>, this is a valid 
     <i>NdisPartyHandle</i> . Otherwise, this parameter is <b>NULL</b>.
     </p>
<p><i>ProtocolClMakeCallComplete</i> must save any valid input 
     <i>NdisPartyHandle</i>, usually in the client's per-party context area. The client must use this handle
     if (or when) it makes a subsequent call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> or 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a> that refers to this
     party.</p>
</dd>

### -param <i>CallParameters</i> [in]

<dd>
<p>Pointer to a buffered CO_CALL_PARAMETERS structure. The client allocated this buffer and
     initialized this structure with client-determined data before passing this pointer to 
     <b>NdisClMakeCall</b>. While processing the client's request, the call manager can modify this data to
     reflect the results of its negotiation with the network or with a signaling peer.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClMakeCallComplete</i> indicates that the call manager has completed processing the client's
    request to establish a virtual connection with 
    <b>NdisClMakeCall</b>.</p>

<p>If the client's attempt to establish an outgoing call is unsuccessful (input 
    <i>Status</i> is anything except NDIS_STATUS_SUCCESS), 
    <i>ProtocolClMakeCallComplete</i> should do the following:</p>

<p>Release or prepare for reuse the 
      <i>ProtocolPartyContext</i> area, if any, and the buffer at 
      <i>CallParameters</i> that the client allocated.</p>

<p>Tear down the client-created VC with a call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> and release or prepare for
      reuse the client-allocated 
      <i>ProtocolVcContext</i> area.</p>

<p>Otherwise, 
    <i>ProtocolClMakeCallComplete</i> should do the following:</p>

<p>Check the 
      <b>Flags</b> member of the structure at 
      <i>CallParameters</i> to see whether CALL_PARAMETERS_CHANGED is set, which indicates that the call
      manager modified the client-supplied call parameters.</p>

<p>If so, examine the data at 
      <i>CallParameters</i> to determine whether they are acceptable for this connection.</p>

<p>For example, the client might retain the buffered call parameters for the active VC, save the 
      <i>NdisPartyHandle</i> if this is a multipoint VC, and generally make the client ready for subsequent
      transfers and other operations on the active VC if it finds the given call parameters satisfactory.</p>

<p>If not, the signaling protocol determines whether the client can attempt to renegotiate for
      acceptable call parameters with the call manager.</p>

<p>For example, a particular call manager might allow its clients to call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> one or more
      times in these circumstances.</p>

<p>If the CM-modified call parameters are unacceptable and further renegotiation is impossible, 
      <i>ProtocolClMakeCallComplete</i> must tear down the call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>.</p>

<p>In this case, 
      <i>ProtocolClMakeCallComplete</i> should 
      <u>not</u> attempt to release any client-allocated resources on return from 
      <b>NdisClCloseCall</b> but can simply return control. Instead, the client should release the resources
      it allocated (or prepare them for reuse) within its 
      <i>ProtocolClCloseCallComplete</i> function.</p>

<p>To define a <i>ProtocolClMakeCallComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClMakeCallComplete</i> function that is named "MyClMakeCallComplete", use the <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A call to 
    <i>ProtocolClMakeCallComplete</i> indicates that the call manager has completed processing the client's
    request to establish a virtual connection with 
    <b>NdisClMakeCall</b>.</p>

<p>If the client's attempt to establish an outgoing call is unsuccessful (input 
    <i>Status</i> is anything except NDIS_STATUS_SUCCESS), 
    <i>ProtocolClMakeCallComplete</i> should do the following:</p>

<p>Release or prepare for reuse the 
      <i>ProtocolPartyContext</i> area, if any, and the buffer at 
      <i>CallParameters</i> that the client allocated.</p>

<p>Tear down the client-created VC with a call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> and release or prepare for
      reuse the client-allocated 
      <i>ProtocolVcContext</i> area.</p>

<p>Otherwise, 
    <i>ProtocolClMakeCallComplete</i> should do the following:</p>

<p>Check the 
      <b>Flags</b> member of the structure at 
      <i>CallParameters</i> to see whether CALL_PARAMETERS_CHANGED is set, which indicates that the call
      manager modified the client-supplied call parameters.</p>

<p>If so, examine the data at 
      <i>CallParameters</i> to determine whether they are acceptable for this connection.</p>

<p>For example, the client might retain the buffered call parameters for the active VC, save the 
      <i>NdisPartyHandle</i> if this is a multipoint VC, and generally make the client ready for subsequent
      transfers and other operations on the active VC if it finds the given call parameters satisfactory.</p>

<p>If not, the signaling protocol determines whether the client can attempt to renegotiate for
      acceptable call parameters with the call manager.</p>

<p>For example, a particular call manager might allow its clients to call 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561636">NdisClModifyCallQoS</a> one or more
      times in these circumstances.</p>

<p>If the CM-modified call parameters are unacceptable and further renegotiation is impossible, 
      <i>ProtocolClMakeCallComplete</i> must tear down the call with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>.</p>

<p>In this case, 
      <i>ProtocolClMakeCallComplete</i> should 
      <u>not</u> attempt to release any client-allocated resources on return from 
      <b>NdisClCloseCall</b> but can simply return control. Instead, the client should release the resources
      it allocated (or prepare them for reuse) within its 
      <i>ProtocolClCloseCallComplete</i> function.</p>

<p>To define a <i>ProtocolClMakeCallComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClMakeCallComplete</i> function that is named "MyClMakeCallComplete", use the <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_MAKE_CALL_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/97036de6-8b12-4ff1-aae8-f489c4fcde4a">ProtocolClMakeCallComplete
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolClMakeCallComplete
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561677">NdisCmMakeCallComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2405a405-177a-420a-9628-a340e0d0acb3">
   NdisFreeToNPagedLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563544">NdisMCmMakeCallComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a7ba1ab2-04c9-45b5-a184-e1ad1448561a">ProtocolClCloseCallComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ede0a18a-cd3b-4fbb-a16b-e7493940d633">ProtocolCmMakeCall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_MAKE_CALL_COMPLETE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
