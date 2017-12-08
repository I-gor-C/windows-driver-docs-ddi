---
UID: NC.ndis.PROTOCOL_CL_INCOMING_CALL
title: PROTOCOL_CL_INCOMING_CALL
author: windows-driver-content
description: The ProtocolClIncomingCall function is used by connection-oriented clients that accept incoming calls.
old-location: netvista\protocolclincomingcall.htm
old-project: netvista
ms.assetid: 8a5922ac-b22b-444e-9ea0-3bb56e71ef33
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    ProtocolClIncomingCall (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    ProtocolClIncomingCall (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClIncomingCall
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
---

# PROTOCOL_CL_INCOMING_CALL callback



## -description
The 
  <i>ProtocolClIncomingCall</i> function is used by connection-oriented clients that accept incoming calls.
  Such clients must have 
  <i>ProtocolClIncomingCall</i> functions. Otherwise, such a protocol driver's registered 
  <i>ProtocolClIncomingCall</i> function can simply return NDIS_STATUS_NOT_SUPPORTED.


## -prototype

````
PROTOCOL_CL_INCOMING_CALL ProtocolClIncomingCall;

NDIS_STATUS ProtocolClIncomingCall(
  _In_    NDIS_HANDLE         ProtocolSapContext,
  _In_    NDIS_HANDLE         ProtocolVcContext,
  _Inout_ PCO_CALL_PARAMETERS CallParameters
)
{ ... }
````


## -parameters

### -param ProtocolSapContext [in]

Specifies the handle that the client originally supplied when it registered the SAP, which the
     call manager matched to this incoming call offer.

### -param ProtocolVcContext [in]

Specifies the handle to the client's per-VC context area, previously returned to NDIS by its 
     <a href="..\ndis\nc-ndis-protocol_co_create_vc.md">ProtocolCoCreateVc</a> function.

### -param CallParameters [in, out]

Pointer to a buffer, formatted as a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a> structure, that contains
     the call parameters for this offered call.

## -returns
<i>ProtocolClIncomingCall</i> can return one of the following status codes:
<dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl>The client accepted the incoming call offer.
<dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl>The client is handling this request asynchronously, and it will call the 
       <a href="netvista.ndisclincomingcallcomplete">
       NdisClIncomingCallComplete</a> function when the close operation is complete.
<dl>
<dt><b>NDIS_STATUS_<i>XXX</i></b></dt>
</dl>The client rejected the incoming call offer for some driver-determined reason.

 

## -remarks
A call to 
    <i>ProtocolClIncomingCall</i> indicates that the call manager has received a request over the network from
    a signaling peer to establish a connection with this client. That is, the request to set up such a
    connection was directed to a SAP previously registered with the call manager by this client.

Depending on the signaling protocol supported by the call manager, 
    <i>ProtocolClIncomingCall</i> can modify the traffic parameters as part of the process of negotiating
    acceptance of an incoming call offer and/or, if the call manager supports QoS, the quality of service
    specification at 
    <i>CallParameters</i> . The client should copy any information it will need subsequently from this
    buffered structure if it accepts the offered call.

Assuming the call manager finds the client's modifications, if any, acceptable, NDIS next calls the
    client's 
    <i>ProtocolClIncomingCallConnected</i> function when it becomes possible for transfers to occur on the
    active VC representing the connection to the client on the remote node that originally initiated the call
    offer. If the client returns modified call parameters that are unacceptable, the call manager can tear
    down the VC it created for this offer, thereby causing calls to the client's 
    <a href="..\ndis\nc-ndis-protocol_cl_incoming_close_call.md">
    ProtocolClIncomingCloseCall</a> and then 
    <a href="..\ndis\nc-ndis-protocol_co_delete_vc.md">ProtocolCoDeleteVc</a> functions
    instead.

To define a <i>ProtocolClIncomingCall</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.

For example, to define a <i>ProtocolClIncomingCall</i> function that is named "MyClIncomingCall", use the <b>PROTOCOL_CL_INCOMING_CALL</b> type as shown in this code example:

Then, implement your function as follows:

The <b>PROTOCOL_CL_INCOMING_CALL</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_INCOMING_CALL</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. 

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/79115b66-8eb9-4a1e-944f-1bb81a08a3ad">ProtocolClIncomingCall (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolClIncomingCall (NDIS
   5.1)</i>) in Windows XP.
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
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545384">CO_CALL_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndisclincomingcallcomplete">NdisClIncomingCallComplete</a>
</dt>
<dt>
<a href="netvista.ndisclregistersap">NdisClRegisterSap</a>
</dt>
<dt>
<a href="netvista.ndiscmdispatchincomingcall">NdisCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="netvista.ndismcmdispatchincomingcall">NdisMCmDispatchIncomingCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_call_connected.md">ProtocolClCallConnected</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_cl_incoming_close_call.md">ProtocolClIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_co_create_vc.md">ProtocolCoCreateVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_co_delete_vc.md">ProtocolCoDeleteVc</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_INCOMING_CALL callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>