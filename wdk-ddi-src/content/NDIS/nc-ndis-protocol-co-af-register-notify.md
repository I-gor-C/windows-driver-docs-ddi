---
UID: NC.ndis.PROTOCOL_CO_AF_REGISTER_NOTIFY
title: PROTOCOL_CO_AF_REGISTER_NOTIFY
author: windows-driver-content
description: The ProtocolCoAfRegisterNotify function is used by connection-oriented NDIS clients.
old-location: netvista\protocolcoafregisternotify.htm
ms.assetid: 272d99da-ef08-4ebd-90e7-74e99410b3f5
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   ProtocolCoAfRegisterNotify
   (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolCoAfRegisterNotify
   (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCoAfRegisterNotify
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
req.irql: PASSIVE_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# PROTOCOL_CO_AF_REGISTER_NOTIFY callback



## -description
<p>The 
  <i>ProtocolCoAfRegisterNotify</i> function is used by connection-oriented NDIS clients. All
  connection-oriented NDIS clients must have fully functional 
  <i>ProtocolCoAfRegisterNotify</i> functions. Stand-alone connection-oriented call managers have registered 
  <i>ProtocolCoAfRegisterNotify</i> functions that simply return control.</p>


## -prototype

````
PROTOCOL_CO_AF_REGISTER_NOTIFY ProtocolCoAfRegisterNotify;

VOID ProtocolCoAfRegisterNotify(
  _In_ NDIS_HANDLE        ProtocolBindingContext,
  _In_ PCO_ADDRESS_FAMILY AddressFamily
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolBindingContext</i> [in]

<dd>
<p>Specifies the handle to the client-allocated context area in which the client protocol maintains
     per-binding run-time state. The client's 
     <a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a> function
     supplied this handle when it called 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>.</p>
</dd>

### -param <i>AddressFamily</i> [in]

<dd>
<p>Pointer to a buffer describing the signaling-protocol support provided by a call manager that just
     registered these services with NDIS by calling 
     <a href="https://msdn.microsoft.com/8890bf31-f2c7-48b0-926d-8931893ede86">
     NdisCmRegisterAddressFamilyEx</a> or 
     <a href="https://msdn.microsoft.com/f58a9c08-d2cf-48d1-98d1-68aecd3b7bd0">
     NdisMCmRegisterAddressFamilyEx</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A call to 
    <i>ProtocolCoAfRegisterNotify</i> advertises a particular call manager's or MCM driver's call-management
    services on an underlying connection-oriented NIC to which the client is bound.</p>

<p><i>ProtocolCoAfRegisterNotify</i> examines the data at 
    <i>AddressFamily</i> to determine whether the client can use the services of this particular call manager.
    Whether the client can make modifications in the (M)CM-supplied data at 
    <i>AddressFamily</i> depends on the particular signaling-protocol support of the call manager.</p>

<p>If the client finds the offered call-management services unacceptable, 
    <i>ProtocolCoAfRegisterNotify</i> returns control, and NDIS might call 
    <i>ProtocolCoAfRegisterNotify</i> again with the same 
    <i>ProtocolBindingContext</i> handle and an AF specification supplied by this or another call manager also
    bound to the same underlying miniport driver. Otherwise, 
    <i>ProtocolAfRegisterNotify</i> allocates a per-AF context area for the client and calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a> with
    the 
    <i>AddressFamily</i> pointer. If this call succeeds, the client has registered its 
    <i>ProtocolClXxx</i> functions with NDIS for subsequent connection-oriented operations using this call manager's
    services.</p>

<p>For example, 
    <i>ProtocolCoAfRegisterNotify</i> or 
    <i>ProtocolClOpenAfCompleteEx</i> might call 
    <a href="https://msdn.microsoft.com/d240f2cc-18a6-4c2d-889f-e25a9486d5fe">
    NdisInitializeNPagedLookasideList</a> one or more times in preparation for dynamic allocations and
    releases of per-SAP, per-VC, and/or per-party context areas that the client will need subsequently.</p>

<p>If it accepts incoming calls, a client's 
    <i>ProtocolCoAfRegisterNotify</i> or 
    <a href="https://msdn.microsoft.com/03ddbbfd-8fe8-44b6-8d3e-12a7bf6f8f6b">
    ProtocolClOpenAfCompleteEx</a> function usually registers one or more SAPs with the call manager. After
    opening that call manager's AF, the client might proceed to allocate a per-SAP state area and call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a> one or more times with
    the 
    <i>NdisAfHandle</i> it obtained from 
    <b>NdisClOpenAddressFamilyEx</b>. If it makes outgoing calls, the client might proceed to allocated a
    per-VC state area and create a VC with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> in anticipation of an
    incoming request from one of its own clients to make an outgoing call to a remote node.</p>

<p>To define a <i>ProtocolCoAfRegisterNotify</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoAfRegisterNotify</i> function that is named "MyCoAfRegisterNotify", use the <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A call to 
    <i>ProtocolCoAfRegisterNotify</i> advertises a particular call manager's or MCM driver's call-management
    services on an underlying connection-oriented NIC to which the client is bound.</p>

<p><i>ProtocolCoAfRegisterNotify</i> examines the data at 
    <i>AddressFamily</i> to determine whether the client can use the services of this particular call manager.
    Whether the client can make modifications in the (M)CM-supplied data at 
    <i>AddressFamily</i> depends on the particular signaling-protocol support of the call manager.</p>

<p>If the client finds the offered call-management services unacceptable, 
    <i>ProtocolCoAfRegisterNotify</i> returns control, and NDIS might call 
    <i>ProtocolCoAfRegisterNotify</i> again with the same 
    <i>ProtocolBindingContext</i> handle and an AF specification supplied by this or another call manager also
    bound to the same underlying miniport driver. Otherwise, 
    <i>ProtocolAfRegisterNotify</i> allocates a per-AF context area for the client and calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a> with
    the 
    <i>AddressFamily</i> pointer. If this call succeeds, the client has registered its 
    <i>ProtocolClXxx</i> functions with NDIS for subsequent connection-oriented operations using this call manager's
    services.</p>

<p>For example, 
    <i>ProtocolCoAfRegisterNotify</i> or 
    <i>ProtocolClOpenAfCompleteEx</i> might call 
    <a href="https://msdn.microsoft.com/d240f2cc-18a6-4c2d-889f-e25a9486d5fe">
    NdisInitializeNPagedLookasideList</a> one or more times in preparation for dynamic allocations and
    releases of per-SAP, per-VC, and/or per-party context areas that the client will need subsequently.</p>

<p>If it accepts incoming calls, a client's 
    <i>ProtocolCoAfRegisterNotify</i> or 
    <a href="https://msdn.microsoft.com/03ddbbfd-8fe8-44b6-8d3e-12a7bf6f8f6b">
    ProtocolClOpenAfCompleteEx</a> function usually registers one or more SAPs with the call manager. After
    opening that call manager's AF, the client might proceed to allocate a per-SAP state area and call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a> one or more times with
    the 
    <i>NdisAfHandle</i> it obtained from 
    <b>NdisClOpenAddressFamilyEx</b>. If it makes outgoing calls, the client might proceed to allocated a
    per-VC state area and create a VC with 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> in anticipation of an
    incoming request from one of its own clients to make an outgoing call to a remote node.</p>

<p>To define a <i>ProtocolCoAfRegisterNotify</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCoAfRegisterNotify</i> function that is named "MyCoAfRegisterNotify", use the <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CO_AF_REGISTER_NOTIFY</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/456c8179-b91b-4385-a22b-d0dd0b310f29">ProtocolCoAfRegisterNotify
   (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCoAfRegisterNotify
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545368">CO_ADDRESS_FAMILY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561648">NdisClRegisterSap</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8890bf31-f2c7-48b0-926d-8931893ede86">
   NdisCmRegisterAddressFamilyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d240f2cc-18a6-4c2d-889f-e25a9486d5fe">
   NdisInitializeNPagedLookasideList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f58a9c08-d2cf-48d1-98d1-68aecd3b7bd0">
   NdisMCmRegisterAddressFamilyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1958722e-012e-4110-a82c-751744bcf9b5">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/03ddbbfd-8fe8-44b6-8d3e-12a7bf6f8f6b">ProtocolClOpenAfCompleteEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CO_AF_REGISTER_NOTIFY callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
