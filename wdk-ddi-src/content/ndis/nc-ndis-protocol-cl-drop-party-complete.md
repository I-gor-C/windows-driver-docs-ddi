---
UID: NC.ndis.PROTOCOL_CL_DROP_PARTY_COMPLETE
title: PROTOCOL_CL_DROP_PARTY_COMPLETE
author: windows-driver-content
description: The ProtocolClDropPartyComplete function is used by connection-oriented NDIS clients that set up multipoint connections.
old-location: netvista\protocolcldroppartycomplete.htm
old-project: netvista
ms.assetid: c916f379-393c-41d7-ab30-2f3181c3ada6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       ProtocolClDropPartyComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       ProtocolClDropPartyComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClDropPartyComplete
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

# PROTOCOL_CL_DROP_PARTY_COMPLETE callback



## -description
<p>The 
  <i>ProtocolClDropPartyComplete</i> function is used by connection-oriented NDIS clients that set up
  multipoint connections. Such clients must have 
  <i>ProtocolClDropPartyComplete</i> functions to complete the asynchronous operations that they initiate with
  
  <a href="..\ndis\nf-ndis-ndiscldropparty.md">NdisClDropParty</a>. Otherwise, such a protocol
  driver's registered 
  <i>ProtocolClDropPartyComplete</i> function can simply return control.</p>


## -prototype

````
PROTOCOL_CL_DROP_PARTY_COMPLETE ProtocolClDropPartyComplete;

VOID ProtocolClDropPartyComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE ProtocolPartyContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client-initiated drop-party operation, which can be one of the
     following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The party has been dropped. The 
       <i>NdisPartyHandle</i> that represented this party, which the client stored in its 
       <i>ProtocolPartyContext</i> area, is now invalid.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>The given party was the last remaining on the client's multipoint VC. Therefore, the client
       should call 
       <a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a> to drop this
       party.</p>
</dd>
</dl>
</dd>

### -param <i>ProtocolPartyContext</i> [in]

<dd>
<p>Specifies the handle to the client's per-party context area, which the client originally supplied
     to NDIS either when it called 
     <a href="..\ndis\nf-ndis-ndiscladdparty.md">NdisClAddParty</a> or 
     <a href="..\ndis\nf-ndis-ndisclmakecall.md">NdisClMakeCall</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClDropPartyComplete</i> indicates that the call manager has completed processing of the request
    initiated by the client's previous call to 
    <a href="..\ndis\nf-ndis-ndiscldropparty.md">NdisClDropParty</a>. 
    <i>ProtocolClDropPartyComplete</i> can either release the client-allocated per-party context area or
    prepare it for reuse in a subsequent call to 
    <b>NdisClAddParty</b>.</p>

<p>If the client is in the process of tearing down a multipoint VC that it created, 
    <i>ProtocolClDropPartyComplete</i> can call 
    <b>NdisClDropParty</b> with any valid 
    <i>NdisPartyHandle</i> to one of the remaining parties on the client's active multipoint VC. If only one
    more party remains on its multipoint VC, the client should drop that party by passing its 
    <i>NdisPartyHandle</i> to 
    <a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a>.</p>

<p>To define a <i>ProtocolClDropPartyComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClDropPartyComplete</i> function that is named "MyClDropPartyComplete", use the <b>PROTOCOL_CL_DROP_PARTY_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_DROP_PARTY_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_DROP_PARTY_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/6294d8b9-c403-477f-87c8-7a8b36845343">
   ProtocolClDropPartyComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>
   ProtocolClDropPartyComplete (NDIS 5.1)</i>) in Windows XP.</p>
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
<a href="..\ndis\nf-ndis-ndiscladdparty.md">NdisClAddParty</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisclclosecall.md">NdisClCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscldropparty.md">NdisClDropParty</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisclmakecall.md">NdisClMakeCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmdroppartycomplete.md">NdisCmDropPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreememory.md">NdisFreeMemory</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreetonpagedlookasidelist.md">
   NdisFreeToNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmdroppartycomplete.md">NdisMCmDropPartyComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-drop-party.md">ProtocolCmDropParty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_DROP_PARTY_COMPLETE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
