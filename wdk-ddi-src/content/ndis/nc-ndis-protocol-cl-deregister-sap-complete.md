---
UID: NC.ndis.PROTOCOL_CL_DEREGISTER_SAP_COMPLETE
title: PROTOCOL_CL_DEREGISTER_SAP_COMPLETE
author: windows-driver-content
description: The ProtocolClDeregisterSapComplete function is used by connection-oriented NDIS clients.
old-location: netvista\protocolclderegistersapcomplete.htm
old-project: netvista
ms.assetid: 93f8f74a-8ad4-42ea-83cf-ddfcd7f55ce6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see       ProtocolClDeregisterSapComplete (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see       ProtocolClDeregisterSapComplete (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolClDeregisterSapComplete
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

# PROTOCOL_CL_DEREGISTER_SAP_COMPLETE callback



## -description
<p>The 
  <i>ProtocolClDeregisterSapComplete</i> function is used by connection-oriented NDIS clients.
  Connection-oriented NDIS clients that accept incoming calls must have 
  <i>ProtocolClDeregisterSapComplete</i> functions to complete the asynchronous operations that they initiate
  with 
  <a href="..\ndis\nf-ndis-ndisclderegistersap.md">NdisClDeregisterSap</a>. Otherwise, such a
  protocol driver's registered 
  <i>ProtocolClDeregisterSapComplete</i> function can simply return control.</p>


## -prototype

````
PROTOCOL_CL_DEREGISTER_SAP_COMPLETE ProtocolClDeregisterSapComplete;

VOID ProtocolClDeregisterSapComplete(
  _In_ NDIS_STATUS Status,
  _In_ NDIS_HANDLE ProtocolSapContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>Specifies the final status of the client's request to deregister its SAP, which can be one of the
     following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The SAP was closed. The 
       <i>NdisSapHandle</i> that represented the client's previously registered SAP, which the client stored
       in its 
       <i>ProtocolSapContext</i> area, is now invalid.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>NDIS had marked the state of the AF as "closing," so the associated SAP represented by the 
       <i>NdisSapHandle</i> was already released when the client's call to 
       <a href="..\ndis\nf-ndis-ndisclderegistersap.md">
       NdisClDeregisterSap</a> occurred.</p>
</dd>

### -param <a id="NDIS_STATUS_XXX"></a><a id="ndis_status_xxx"></a>NDIS_STATUS_<i>XXX</i>

<dd>
<p>The call manager failed the request to close the SAP for some CM-determined reason, and NDIS
       propagated the status returned by its 
       <a href="..\ndis\nc-ndis-protocol-cm-deregister-sap.md">
       ProtocolCmDeregisterSap</a> function to the client.</p>
</dd>
</dl>
</dd>

### -param <i>ProtocolSapContext</i> [in]

<dd>
<p>Specifies the client-supplied handle to its per-SAP context area, originally passed to NDIS with 
     <b>NdisClRegisterSap</b>. After the call manager has successfully deregistered this SAP, the client can
     release its context area or prepare this context area for reuse.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolClDeregisterSapComplete</i> indicates that the client's preceding call to 
    <a href="..\ndis\nf-ndis-ndisclderegistersap.md">NdisClDeregisterSap</a> has been processed
    by the call manager.</p>

<p>Unless the call manager failed the deregistration for some CM-determined reason, the client should
    consider the 
    <i>NdisSapHandle</i> invalid when 
    <i>ProtocolClDeregisterSapComplete</i> is called. Consequently, 
    <i>ProtocolClDeregisterSapComplete</i> can release the per-SAP context area that the client allocated or
    prepare it for reuse in a subsequent call to 
    <a href="..\ndis\nf-ndis-ndisclregistersap.md">NdisClRegisterSap</a>.</p>

<p>To define a <i>ProtocolClDeregisterSapComplete</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolClDeregisterSapComplete</i> function that is named "MyClDeregisterSapComplete", use the <b>PROTOCOL_CL_DEREGISTER_SAP_COMPLETE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CL_DEREGISTER_SAP_COMPLETE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CL_DEREGISTER_SAP_COMPLETE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/14b9154a-041e-4a49-9a89-c04ef6696bf7">
   ProtocolClDeregisterSapComplete (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>
   ProtocolClDeregisterSapComplete (NDIS 5.1)</i>) in Windows XP.</p>
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
<a href="..\ndis\nf-ndis-ndisclderegistersap.md">NdisClDeregisterSap</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisclregistersap.md">NdisClRegisterSap</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmderegistersapcomplete.md">NdisCmDeregisterSapComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreememory.md">NdisFreeMemory</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreetonpagedlookasidelist.md">
   NdisFreeToNPagedLookasideList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcmderegistersapcomplete.md">NdisMCmDeregisterSapComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-cm-deregister-sap.md">ProtocolCmDeregisterSap</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CL_DEREGISTER_SAP_COMPLETE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
