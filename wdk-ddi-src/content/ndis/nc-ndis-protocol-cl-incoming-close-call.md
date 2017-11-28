---
UID: NC.ndis.PROTOCOL_CL_INCOMING_CLOSE_CALL
title: PROTOCOL_CL_INCOMING_CLOSE_CALL
author: windows-driver-content
description: The ProtocolClIncomingCloseCall function is used by all connection-oriented NDIS clients.
old-location: netvista\protocolclincomingclosecall.htm
old-project: netvista
ms.assetid: 01c7d887-eb54-47c3-98f0-bc567b60fb4b
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
   
   ProtocolClIncomingCloseCall (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   
   ProtocolClIncomingCloseCall (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClIncomingCloseCall
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

# PROTOCOL_CL_INCOMING_CLOSE_CALL callback



## -description
<p>The 
  <i>ProtocolClIncomingCloseCall</i> function is used by all connection-oriented NDIS clients. All such
  clients must have fully functional 
  <i>ProtocolClIncomingCloseCall</i> functions.</p>


## -prototype

````
PROTOCOL_CL_INCOMING_CLOSE_CALL ProtocolClIncomingCloseCall;

VOID ProtocolClIncomingCloseCall(
  _In_ NDIS_STATUS CloseStatus,
  _In_ NDIS_HANDLE ProtocolVcContext,
  _In_ PVOID       CloseData,
  _In_ UINT        Size
)
{ ... }
````


## -parameters
<dl>

### -param <i>CloseStatus</i> [in]

<dd>
<p>Specifies the status that indicates the cause of the connection teardown, which is usually
     NDIS_STATUS_SUCCESS to indicate that the remote party to the call requested that the connection be
     closed. Any other value indicates that problems on the network caused the call manager to terminate the
     connection.</p>
</dd>

### -param <i>ProtocolVcContext</i> [in]

<dd>
<p>Specifies the handle to the client's per-VC context area for the VC on which the connection is
     being closed. Whatever the value of 
     <i>CloseStatus</i>, the client can neither send nor receive data on the VC designated by the 
     <i>NdisVcHandle</i> that it stored in this context area.</p>
</dd>

### -param <i>CloseData</i> [in]

<dd>
<p>Pointer to a buffer containing a protocol-specific close message, possibly one supplied by the
     remote client that the call manager received over the network, or this parameter can be <b>NULL</b>. 
     </p>
<p>When 
     <i>CloseStatus</i> is NDIS_STATUS_SUCCESS, this parameter is <b>NULL</b> if the underlying network medium does
     not support transfers of data when closing a connection. However, any particular call manager might
     define a structure to pass additional diagnostic information to its clients on call teardowns caused by
     problems on the network.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer at 
     <i>CloseData</i>, zero if 
     <i>CloseData</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClIncomingCloseCall</i> indicates that the one of the following has occurred:</p>

<p>The call manager has received a request over the network to close an established connection,
      identified by the 
      <i>NdisVcHandle</i> that the client stored in its per-VC context area at 
      <i>ProtocolVcContext</i> .</p>

<p>The call manager has detected that network problems will prevent further data transfers on the
      established connection.</p>

<p>In either case, 
    <i>ProtocolClIncomingCloseCall</i> should carry out any protocol-determined operations, such as notifying
    the client's own client(s) that the connection is being broken. For example, if the call to be closed is
    a multipoint VC created by the client, 
    <i>ProtocolClIncomingCloseCall</i> must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> one or more times until
    only a single party remains on its multipoint VC.</p>

<p>Whether the given VC is a single-point or multipoint connection, 
    <i>ProtocolClIncomingCloseCall</i> must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a> to acknowledge that the
    client will neither attempt to send nor expect to receive data on this particular VC. If the call manager
    created this VC, 
    <i>ProtocolClIncomingCloseCall</i> should return control after it calls 
    <b>NdisClCloseCall</b>. It is the responsibility of the call manager to destroy or reuse any VC that it
    created.</p>

<p>If the client originally created this VC for an outgoing call, 
    <i>ProtocolClIncomingCloseCall</i> can do one of the following after it calls 
    <b>NdisClDropParty</b> as many times as necessary, if any, and 
    <b>NdisClCloseCall</b>:</p>

<p>If 
      <i>CloseStatus</i> is NDIS_STATUS_SUCCESS, tear down the VC with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> and either release the
      client's per-VC context area or prepare it for reuse in a subsequent call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>.</p>

<p>If 
      <i>CloseStatus</i> is NDIS_STATUS_SUCCESS, retain the VC that the client created and prepare its per-VC
      context area for reuse in a subsequent call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>.</p>

<p>Otherwise, tear down the VC with 
      <b>NdisCoDeleteVc</b> and release its per-VC context area if the call manager indicated that the network
      has become inoperative.</p>

<p>To define a <i>ProtocolClIncomingCloseCall</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClIncomingCloseCall</i> function that is named "MyClIncomingCloseCall", use the <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A call to 
    <i>ProtocolClIncomingCloseCall</i> indicates that the one of the following has occurred:</p>

<p>The call manager has received a request over the network to close an established connection,
      identified by the 
      <i>NdisVcHandle</i> that the client stored in its per-VC context area at 
      <i>ProtocolVcContext</i> .</p>

<p>The call manager has detected that network problems will prevent further data transfers on the
      established connection.</p>

<p>In either case, 
    <i>ProtocolClIncomingCloseCall</i> should carry out any protocol-determined operations, such as notifying
    the client's own client(s) that the connection is being broken. For example, if the call to be closed is
    a multipoint VC created by the client, 
    <i>ProtocolClIncomingCloseCall</i> must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a> one or more times until
    only a single party remains on its multipoint VC.</p>

<p>Whether the given VC is a single-point or multipoint connection, 
    <i>ProtocolClIncomingCloseCall</i> must call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a> to acknowledge that the
    client will neither attempt to send nor expect to receive data on this particular VC. If the call manager
    created this VC, 
    <i>ProtocolClIncomingCloseCall</i> should return control after it calls 
    <b>NdisClCloseCall</b>. It is the responsibility of the call manager to destroy or reuse any VC that it
    created.</p>

<p>If the client originally created this VC for an outgoing call, 
    <i>ProtocolClIncomingCloseCall</i> can do one of the following after it calls 
    <b>NdisClDropParty</b> as many times as necessary, if any, and 
    <b>NdisClCloseCall</b>:</p>

<p>If 
      <i>CloseStatus</i> is NDIS_STATUS_SUCCESS, tear down the VC with 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a> and either release the
      client's per-VC context area or prepare it for reuse in a subsequent call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>.</p>

<p>If 
      <i>CloseStatus</i> is NDIS_STATUS_SUCCESS, retain the VC that the client created and prepare its per-VC
      context area for reuse in a subsequent call to 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>.</p>

<p>Otherwise, tear down the VC with 
      <b>NdisCoDeleteVc</b> and release its per-VC context area if the call manager indicated that the network
      has become inoperative.</p>

<p>To define a <i>ProtocolClIncomingCloseCall</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClIncomingCloseCall</i> function that is named "MyClIncomingCloseCall", use the <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_INCOMING_CLOSE_CALL</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/485db86b-f494-48ee-920a-cd9606ead9d4">
   ProtocolClIncomingCloseCall (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>
   ProtocolClIncomingCloseCall (NDIS 5.1)</i>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561629">NdisClDropParty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561635">NdisClMakeCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmdispatchincomingclosecall.md">
   NdisCmDispatchIncomingCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreetonpagedlookasidelist.md">
   NdisFreeToNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmdispatchincomingclosecall.md">
   NdisMCmDispatchIncomingCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cl-drop-party-complete.md">ProtocolClDropPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-delete-vc.md">ProtocolCoDeleteVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_INCOMING_CLOSE_CALL callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
