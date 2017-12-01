---
UID: NC.ndis.PROTOCOL_CM_CLOSE_CALL
title: PROTOCOL_CM_CLOSE_CALL
author: windows-driver-content
description: The ProtocolCmCloseCall function is a required function that terminates an existing call and releases any resources that the call manager allocated for the call.Note  You must declare the function by using the PROTOCOL_CM_CLOSE_CALL type.
old-location: netvista\protocolcmclosecall.htm
old-project: netvista
ms.assetid: b5307e1b-3905-4e43-a0b0-0068ba18ef0d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    ProtocolCmCloseCall (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    ProtocolCmCloseCall (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCmCloseCall
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

# PROTOCOL_CM_CLOSE_CALL callback



## -description
<p>The 
  <i>ProtocolCmCloseCall</i> function is a required function that terminates an existing call and releases any
  resources that the call manager allocated for the call.</p>


## -prototype

````
PROTOCOL_CM_CLOSE_CALL ProtocolCmCloseCall;

NDIS_STATUS ProtocolCmCloseCall(
  _In_     NDIS_HANDLE CallMgrVcContext,
  _In_opt_ NDIS_HANDLE CallMgrPartyContext,
  _In_opt_ PVOID       CloseData,
  _In_opt_ UINT        Size
)
{ ... }
````


## -parameters
<dl>

### -param <i>CallMgrVcContext</i> [in]

<dd>
<p>Specifies the handle to a call manager-allocated context area in which the call manager maintains
     its per-VC state. This handle was provided to NDIS from the call managers 
     <a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a> function.</p>
</dd>

### -param <i>CallMgrPartyContext</i> [in, optional]

<dd>
<p>Specifies the handle, if any, to a call manager-allocated context area in which the call manager
     maintain information about a party on a multipoint VC. This handle is <b>NULL</b> if the call being closed is
     not a multipoint call.</p>
</dd>

### -param <i>CloseData</i> [in, optional]

<dd>
<p>Pointer to a buffer containing connection-oriented client-specified data that should be sent
     across the connection before the call is terminated. This parameter is <b>NULL</b> if the underlying network
     medium does not support transfers of data when closing a connection.</p>
</dd>

### -param <i>Size</i> [in, optional]

<dd>
<p>Specifies the length, in bytes, of the buffer at 
     <i>CloseData</i>, zero if 
     <i>CloseData</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolCmCloseCall</i> returns the status of its operation(s) as one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the call manager successfully terminated the call.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>Indicates that the call manager will complete the request to terminate the call asynchronously.
       When the call manager has completed all operations required to terminate the connection, it must then
       call 
       <a href="..\ndis\nf-ndis-ndiscmclosecallcomplete.md">NdisCmCloseCallComplete</a> to
       signal NDIS that the call has been closed.</p><dl>
<dt><b>NDIS_STATUS_INVALID_DATA</b></dt>
</dl><p>Indicates that 
       <i>CloseData</i> was specified, but the underlying network medium does not support sending data
       concurrent with terminating a call.</p><dl>
<dt><b>NDIS_STATUS_<i>XXX</i></b></dt>
</dl><p>Indicates that the call manager could not terminate the call. The actual error returned can be a
       status propagated from another NDIS library routine.</p>

<p> </p>

## -remarks
<p><i>ProtocolCmCloseCall</i> communicated with network control devices or other media-specific actors, as
    necessitated by its media, to terminate a connection between the local node and a remote node. If the
    call manager is required to communicate with network control devices (such as a networking switch) it
    should use a virtual connection to the network control device that it established in its 
    <i>ProtocolBindAdapterEx</i> function. Stand-alone call managers communicate to such network devices by
    calling 
    <a href="..\ndis\nf-ndis-ndiscosendnetbufferlists.md">NdisCoSendNetBufferLists</a>.
    Miniport drivers with integrated call-management support never call 
    <b>NdisCoSendNetBufferLists</b>. Instead, they transmit the data directly across the network.</p>

<p>If 
    <i>CloseData</i> is non-<b>NULL</b> and sending data at connection termination is supported by the media that
    this call manager handles, the call manager should transmit the data specified at 
    <i>CloseData</i> to the remote node before completing the call termination. If sending data concurrent
    with a connection being terminated is not supported, call managers should return
    NDIS_STATUS_INVALID_DATA.</p>

<p>If 
    <i>ProtocolCmCloseCall</i> is passed an explicit 
    <i>CallMgrPartyContext</i>, then the call being terminated is a multipoint VC, and the call manager must
    perform any necessary network communication with its networking hardware, as appropriate to its media
    type, to terminate the call as a multipoint call. The call manager must also free the memory that it
    allocated earlier, in 
    <a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a>, for its
    per-party state that is pointed to by 
    <i>CallMgrPartyContext</i> . Failure to properly release, deallocate, or otherwise deactivate those
    resources causes a memory leak.</p>

<p>After the call has been terminated with the network, any close data has been sent, and any resources
    at 
    <i>CallMgrPartyContext</i> have been freed, the call manager must call 
    <a href="..\ndis\nf-ndis-ndiscmdeactivatevc.md">NdisCmDeactivateVc</a>. This notifies NDIS
    and the underlying miniport driver, if any, to expect no further transfers on the given VC.</p>

<p>To define a <i>ProtocolCmCloseCall</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmCloseCall</i> function that is named "MyCmCloseCall", use the <b>PROTOCOL_CM_CLOSE_CALL</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_CLOSE_CALL</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_CLOSE_CALL</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/07eeeab8-456c-4d7c-97d1-f772b89937ed">ProtocolCmCloseCall (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCmCloseCall (NDIS
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
<a href="..\ndis\nf-ndis-ndiscmdeactivatevc.md">NdisCmDeactivateVc</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscosendnetbufferlists.md">NdisCoSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-make-call.md">ProtocolCmMakeCall</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CM_CLOSE_CALL callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
