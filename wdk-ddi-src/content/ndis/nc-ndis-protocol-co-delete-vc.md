---
UID: NC.ndis.PROTOCOL_CO_DELETE_VC
title: PROTOCOL_CO_DELETE_VC
author: windows-driver-content
description: The ProtocolCoDeleteVc function is required.
old-location: netvista\protocolcodeletevc.htm
old-project: netvista
ms.assetid: d761270f-bf77-441e-834c-9ac7fb3d350f
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
   ProtocolCoDeleteVc (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolCoDeleteVc (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCoDeleteVc
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

# PROTOCOL_CO_DELETE_VC callback



## -description
<p>The 
  <i>ProtocolCoDeleteVc</i> function is required. This function tears down the client's or call manager's
  state for an established virtual connection that is being closed by the original creator of that VC.</p>


## -prototype

````
PROTOCOL_CO_DELETE_VC ProtocolCoDeleteVc;

NDIS_STATUS ProtocolCoDeleteVc(
  _In_ NDIS_HANDLE ProtocolVcContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolVcContext</i> [in]

<dd>
<p>Specifies the handle to the client's or call manager's per-VC context area. The protocol
     originally supplied this handle from its 
     <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolCoDeleteVc</i> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The protocol has released or prepared for reuse all the resources that it originally allocated
       for the VC.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p>The VC is still active and the protocol has outstanding operations pending on the VC so it could
       not be destroyed.</p><dl>
<dt><b>NDIS_STATUS_<i>XXX</i></b></dt>
</dl><p>The protocol failed the VC deletion for a driver-determined reason.</p>

<p> </p>

## -remarks
<p><i>ProtocolCoDeleteVc</i> is the reciprocal of the driver's 
    <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function. In
    general, it releases any dynamic resources and structures that the call manager or client previously
    allocated to perform operations on the active VC.</p>

<p>When 
    <i>ProtocolCoDeleteVc</i> returns control with NDIS_STATUS_SUCCESS, the 
    <i>NdisVcHandle</i> that its 
    <i>ProtocolCoCreateVc</i> function stored in the area at 
    <i>ProtocolVcContext</i> becomes invalid.</p>

<p><i>ProtocolCoDeleteVc</i> can return any driver-determined NDIS_STATUS_<i>XXX</i> to fail the deletion of the VC, but it 
    <u>cannot</u> return NDIS_STATUS_PENDING. Calls to 
    <i>ProtocolCoDeleteVc</i> are inherently synchronous in nature.</p>

<p>To define a <i>ProtocolCoDeleteVc</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoDeleteVc</i> function that is named "MyCoDeleteVc", use the <b>PROTOCOL_CO_DELETE_VC</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_DELETE_VC</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_DELETE_VC</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>ProtocolCoDeleteVc</i> is the reciprocal of the driver's 
    <a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a> function. In
    general, it releases any dynamic resources and structures that the call manager or client previously
    allocated to perform operations on the active VC.</p>

<p>When 
    <i>ProtocolCoDeleteVc</i> returns control with NDIS_STATUS_SUCCESS, the 
    <i>NdisVcHandle</i> that its 
    <i>ProtocolCoCreateVc</i> function stored in the area at 
    <i>ProtocolVcContext</i> becomes invalid.</p>

<p><i>ProtocolCoDeleteVc</i> can return any driver-determined NDIS_STATUS_<i>XXX</i> to fail the deletion of the VC, but it 
    <u>cannot</u> return NDIS_STATUS_PENDING. Calls to 
    <i>ProtocolCoDeleteVc</i> are inherently synchronous in nature.</p>

<p>To define a <i>ProtocolCoDeleteVc</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoDeleteVc</i> function that is named "MyCoDeleteVc", use the <b>PROTOCOL_CO_DELETE_VC</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_DELETE_VC</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_DELETE_VC</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/8dd2520c-d25a-42d5-ae21-7895943cacac">ProtocolCoDeleteVc (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCoDeleteVc (NDIS
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561627">NdisClCloseCall</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiscmdispatchincomingclosecall.md">
   NdisCmDispatchIncomingCloseCall</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561698">NdisCoDeleteVc</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-co-create-vc.md">ProtocolCoCreateVc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CO_DELETE_VC callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
