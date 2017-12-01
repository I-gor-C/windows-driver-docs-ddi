---
UID: NC.ndis.PROTOCOL_CM_MAKE_CALL
title: PROTOCOL_CM_MAKE_CALL
author: windows-driver-content
description: The ProtocolCmMakeCall function is a required function that sets up media specific parameters for a virtual connection (VC) and activates the virtual connection.Note  You must declare the function by using the PROTOCOL_CM_MAKE_CALL type.
old-location: netvista\protocolcmmakecall.htm
old-project: netvista
ms.assetid: ede0a18a-cd3b-4fbb-a16b-e7493940d633
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    ProtocolCmMakeCall (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    ProtocolCmMakeCall (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCmMakeCall
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

# PROTOCOL_CM_MAKE_CALL callback



## -description
<p>The 
  <i>ProtocolCmMakeCall</i> function is a required function that sets up media specific parameters for a
  virtual connection (VC) and activates the virtual connection.</p>


## -prototype

````
PROTOCOL_CM_MAKE_CALL ProtocolCmMakeCall;

NDIS_STATUS ProtocolCmMakeCall(
  _In_      NDIS_HANDLE         CallMgrVcContext,
  _Inout_   PCO_CALL_PARAMETERS CallParameters,
  _In_opt_  NDIS_HANDLE         NdisPartyHandle,
  _Out_opt_ PNDIS_HANDLE        CallMgrPartyContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>CallMgrVcContext</i> [in]

<dd>
<p>Specifies the handle to a call manager-allocated context area in which the call managers maintains
     its per-VC state. The call manager supplied this handle to NDIS from its 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function.</p>
</dd>

### -param <i>CallParameters</i> [in, out]

<dd>
<p>Pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> structure that contains
     the parameters, specified by a connection-oriented client, for this outgoing call.</p>
</dd>

### -param <i>NdisPartyHandle</i> [in, optional]

<dd>
<p>Specifies a handle, supplied by NDIS, that uniquely identifies the initial party on the multipoint
     virtual connection. This handle is opaque to the call manager and reserved for NDIS library use. This
     handle is <b>NULL</b> if the client is not setting up an outgoing multipoint call.</p>
</dd>

### -param <i>CallMgrPartyContext</i> [out, optional]

<dd>
<p>On return, specifies a handle to a call manager-supplied context area in which the call manager
     maintains state about the initial party on the multipoint call. If 
     <i>NdisPartyHandle</i> is <b>NULL</b>, this handle must be set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolCmMakeCall</i> returns the status of its operation(s) as one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the call manager successfully allocated the necessary resources to make the call
       and was able to activate the virtual connection with the miniport driver.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>Indicates that the call manager will complete the request to make a call asynchronously. When
       the call manager has completed all operations for making a call, it must call 
       <a href="..\ndis\nf-ndis-ndiscmmakecallcomplete.md">NdisCmMakeCallComplete</a> to signal
       NDIS that this call has been completed.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>Indicates that the call manager was unable to allocate and/or initialize its resources for
       activating the virtual connection as requested by the client.</p><dl>
<dt><b>NDIS_STATUS_NOT_SUPPORTED</b></dt>
</dl><p>Indicates that the call manager was unable to activate a virtual connection because the caller
       requested invalid or unavailable features in the call parameters specified at 
       <i>CallParameters</i> .</p>

<p> </p>

## -remarks
<p>If 
    <i>ProtocolCmMakeCall</i> is given an explicit 
    <i>NdisPartyHandle</i>, this VC was created by the client for a multipoint call. The call manager must
    allocate and initialize any necessary resources required to maintain state information and control a
    multipoint call. Such resources include, but are not limited to, memory buffers, data structures, events,
    and other similar resources. If the call manager cannot allocate or initialize the needed resources for
    its state area(s), it should return control to NDIS with NDIS_STATUS_RESOURCES.</p>

<p><i>ProtocolCmMakeCall</i> communicates with network control devices or other media-specific actors, as
    necessary, to make a connection between the local node and a remote node based on the call parameters
    specified at 
    <i>CallParameters</i> . Such actions could include, but are not limited to, communication with switching
    hardware, communications with a network control station, or other actions as appropriate to the network
    medium.</p>

<p>If a call manager is required to communication with networking hardware (such as a networking switch)
    it should use a virtual connection to the network control device that it established in its 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function.
    Call managers communicate with their network hardware through the miniport driver by calling 
    <a href="..\ndis\nf-ndis-ndiscosendnetbufferlists.md">NdisCoSendNetBufferLists</a>.
    Miniport drivers with integrated call-management support will not call 
    <b>NdisCoSendNetBufferLists</b>, but rather will transmit the data themselves.</p>

<p>After a call manager has done all necessary communication with its networking hardware as required by
    its medium, call managers must call 
    <a href="..\ndis\nf-ndis-ndiscmactivatevc.md">NdisCmActivateVc</a>.</p>

<p>If this call was a multipoint call, after the call manager has communicated with the networking
    hardware, verified call parameters, and allocated and initialized its per-party state data, the address
    of its state block should be set in the handle 
    <i>CallMgrPartyContext</i> before returning control to NDIS. The handle is set by dereferencing the handle
    and storing a pointer to the state block as the value of the handle. For example:</p>

<p>If 
    <i>ProtocolCmMakeCall</i> has completed the required operations for its network and the VC has been
    successfully activated through 
    <b>NdisCmActivateVc</b>, 
    <i>ProtocolCmMakeCall</i> should return control as quickly as possible with a status of
    STATUS_SUCCESS.</p>

<p>After 
    <i>ProtocolCmMakeCall</i> returns control to NDIS, the call manager should expect to take no further
    actions on this call to set it up. 
    <i>ProtocolCmMakeCall</i> is responsible for establishing the connection so that the client can make data
    transfers over the network on this VC. However, the call manager can be called subsequently to modify the
    call's quality of service, to add or drop parties if this is a multipoint VC, and eventually to terminate
    this call.</p>

<p>To define a <i>ProtocolCmMakeCall</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmMakeCall</i> function that is named "MyCmMakeCall", use the <b>PROTOCOL_CM_MAKE_CALL</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_MAKE_CALL</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_MAKE_CALL</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/c3f4b0d1-0ad6-46d9-87f7-0395b8c81421">ProtocolCmMakeCall (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCmMakeCall (NDIS
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
<a href="..\ndis\nf-ndis-ndisclmakecall.md">NdisClMakeCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmactivatevc.md">NdisCmActivateVc</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmmakecallcomplete.md">NdisCmMakeCallComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CM_MAKE_CALL callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
