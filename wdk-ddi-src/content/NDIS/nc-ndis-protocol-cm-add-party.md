---
UID: NC.ndis.PROTOCOL_CM_ADD_PARTY
title: PROTOCOL_CM_ADD_PARTY
author: windows-driver-content
description: The ProtocolCmAddParty function is a required function.
old-location: netvista\protocolcmaddparty.htm
ms.assetid: 06aa5ff6-974c-43dd-8395-bc1a1a8421d5
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   ProtocolCmAddParty (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolCmAddParty (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCmAddParty
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

# PROTOCOL_CM_ADD_PARTY callback



## -description
<p>The 
  <i>ProtocolCmAddParty</i> function is a required function. 
  <i>ProtocolCmAddParty</i> sets up the media-specific parameters to add a party to an existing multipoint
  call, stores state data for the new party, and causes the party to be added to the call.</p>


## -prototype

````
PROTOCOL_CM_ADD_PARTY ProtocolCmAddParty;

NDIS_STATUS ProtocolCmAddParty(
  _In_    NDIS_HANDLE         CallMgrVcContext,
  _Inout_ PCO_CALL_PARAMETERS CallParameters,
  _In_    NDIS_HANDLE         NdisPartyHandle,
  _Out_   PNDIS_HANDLE        CallMgrPartyContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>CallMgrVcContext</i> [in]

<dd>
<p>Specifies the handle to a call manager-allocated context area in which the call manager maintains
     its per-VC state. The call manager supplied this handle to NDIS from its 
     <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> function.</p>
</dd>

### -param <i>CallParameters</i> [in, out]

<dd>
<p>Pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> structure that contains
     the parameters, specified by a connection-oriented client, for the party that is being added to an
     existing call.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in]

<dd>
<p>Specifies a handle, supplied by NDIS, that uniquely identifies a multipoint party that is to be
     added to an existing virtual connection. This handle is opaque to the call manager and reserved for NDIS
     library use.</p>
</dd>

### -param <i>CallMgrPartyContext</i> [out]

<dd>
<p>Specifies, on return, a handle to a call manager-supplied context area in which the call manager
     maintains state about this party for the multipoint call.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolCmAddParty</i> returns the status of its operation(s) as one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the call manager successfully allocated the necessary resources to maintain state
       about the party and successfully added the party to the call.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>Indicates that the call manager will complete the request to add a party asynchronously. When
       the call manager has completed all operations for adding the party, it must call 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff561651">NdisCmAddPartyComplete</a> to signal
       NDIS that this operation has been completed.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>Indicates that the call manager was unable to allocate and/or initialize its resources for
       adding a party to the connection.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>Indicates that the call manager was unable to add the party to the multipoint call because the
       caller requested invalid or unavailable features in the call parameters at 
       <i>CallParameters</i> or else that the media type supported by this call manager does not support
       multipoint calls.</p>

<p> </p>

## -remarks
<p><i>ProtocolCmAddParty</i> performs any necessary allocations of dynamic resources and structures that the
    call manager requires to maintain state information about the party, specified by 
    <i>NdisPartyHandle</i>, to be added to a multipoint call. Such resources could include, but are not
    limited to, memory buffers, data structures, events, and other similar resources. Call managers should
    also initialize relevant per-party structures in this function.</p>

<p>In the per-party state area that the call manager allocates, the call manager 
    <u>must</u> store the handle specified by 
    <i>NdisPartyHandle</i> for reference in future calls. After the call manager has allocated and finish
    initializing its per-party state area, the address of the state buffer should be set as the 
    <i>CallMgrPartyContext</i> handle before returning control to NDIS. To do this, dereference the handle and
    store a pointer to the state buffer as the value of the handle. For example:</p>

<p>Call managers perform any necessary communication with their network hardware or other media-specific
    actors, as necessary, to add the party specified by the call parameters at 
    <i>CallParameters</i> to an existing multipoint call.</p>

<p>To define a <i>ProtocolCmAddParty</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmAddParty</i> function that is named "MyCmAddParty", use the <b>PROTOCOL_CM_ADD_PARTY</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_ADD_PARTY</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_ADD_PARTY</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>ProtocolCmAddParty</i> performs any necessary allocations of dynamic resources and structures that the
    call manager requires to maintain state information about the party, specified by 
    <i>NdisPartyHandle</i>, to be added to a multipoint call. Such resources could include, but are not
    limited to, memory buffers, data structures, events, and other similar resources. Call managers should
    also initialize relevant per-party structures in this function.</p>

<p>In the per-party state area that the call manager allocates, the call manager 
    <u>must</u> store the handle specified by 
    <i>NdisPartyHandle</i> for reference in future calls. After the call manager has allocated and finish
    initializing its per-party state area, the address of the state buffer should be set as the 
    <i>CallMgrPartyContext</i> handle before returning control to NDIS. To do this, dereference the handle and
    store a pointer to the state buffer as the value of the handle. For example:</p>

<p>Call managers perform any necessary communication with their network hardware or other media-specific
    actors, as necessary, to add the party specified by the call parameters at 
    <i>CallParameters</i> to an existing multipoint call.</p>

<p>To define a <i>ProtocolCmAddParty</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmAddParty</i> function that is named "MyCmAddParty", use the <b>PROTOCOL_CM_ADD_PARTY</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_ADD_PARTY</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_ADD_PARTY</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/272fb985-3377-449a-9cb2-12891d4a91ba">ProtocolCmAddParty (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCmAddParty (NDIS
   5.1)</i>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561625">NdisClAddParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ea3ebbe9-fd94-44b8-8801-639d099c5158">ProtocolClAddPartyComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CM_ADD_PARTY callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
