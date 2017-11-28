---
UID: NC.ndis.SET_OPTIONS
title: SET_OPTIONS
author: windows-driver-content
description: NDIS calls a protocol driver's ProtocolSetOptions function to allow the protocol driver to register optional services.Note  You must declare the function by using the SET_OPTIONS type.
old-location: netvista\protocolsetoptions.htm
old-project: netvista
ms.assetid: 342e23ad-d38b-4100-949a-220b8fbdcf6e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolSetOptions
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
req.iface: 
---

# SET_OPTIONS callback



## -description
<p>NDIS calls a protocol driver's 
  <i>ProtocolSetOptions</i> function to allow the protocol driver to register optional services.</p>


## -prototype

````
SET_OPTIONS ProtocolSetOptions;

NDIS_STATUS ProtocolSetOptions(
  _In_ NDIS_HANDLE NdisDriverHandle,
  _In_ NDIS_HANDLE DriverContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisDriverHandle</i> [in]

<dd>
<p>A handle that identifies a protocol driver. NDIS returns this handle to the protocol driver when
     it returns from the 
     <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
     NdisRegisterProtocolDriver</a> function.</p>
</dd>

### -param <i>DriverContext</i> [in]

<dd>
<p>The handle that the driver passed to 
     <b>NdisRegisterProtocolDriver</b> that identifies the driver context area.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolSetOptions</i> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><i>ProtocolSetOptions</i> successfully registered the protocol driver's optional services and
       resources.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><i>ProtocolSetOptions</i> could not allocate the resources that the protocol driver requires.</p><dl>
<dt><b>NDIS_STATUS_XXX or NTSTATUS_XXX</b></dt>
</dl><p>The protocol driver's attempt to register options failed. Usually, such an error status is
       propagated from an 
       <b>Ndis<i>Xxx</i></b> function or a kernel-mode support routine.</p>

<p> </p>

## -remarks
<p><i>ProtocolSetOptions</i> is an optional function. NDIS calls 
    <i>ProtocolSetOptions</i> within the context of the protocol driver's call to the 
    <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
    NdisRegisterProtocolDriver</a> function.</p>

<p><i>ProtocolSetOptions</i> registers optional services and can allocate other driver resources. To register
    optional 
    <i>ProtocolXxx</i> functions, the protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function.
    The protocol driver passes the handle from the 
    <i>NdisDriverHandle</i> parameter at the 
    <i>NdisHandle</i> parameter of 
    <b>NdisSetOptionalHandlers</b> and passes a characteristics structure at the 
    <i>OptionalHandlers</i> parameter.</p>

<p>The optional services are defined in the following structures:</p><dl>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
</dl><p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>NDIS can call the protocol driver's other 
    <i>ProtocolXxx</i> functions at any time after 
    <i>ProtocolSetOptions</i> returns. The driver should be prepared to be called back at the 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function.
    The protocol bindings are in the 
    <i>Unbound</i> state before the NDIS calls 
    <i>ProtocolBindAdapterEx</i>.</p>

<p>If an attempt to allocate resources or services fails, 
    <i>ProtocolSetOptions</i> should undo all the allocations that succeeded before it returns control with a
    status other than NDIS_STATUS_SUCCESS.</p>

<p>NDIS calls 
    <i>ProtocolSetOptions</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>ProtocolSetOptions</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolSetOptions</i> function that is named "MySetOptions", use the <b>SET_OPTIONS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>SET_OPTIONS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>SET_OPTIONS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>ProtocolSetOptions</i> is an optional function. NDIS calls 
    <i>ProtocolSetOptions</i> within the context of the protocol driver's call to the 
    <a href="..\ndis\nf-ndis-ndisregisterprotocoldriver.md">
    NdisRegisterProtocolDriver</a> function.</p>

<p><i>ProtocolSetOptions</i> registers optional services and can allocate other driver resources. To register
    optional 
    <i>ProtocolXxx</i> functions, the protocol driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function.
    The protocol driver passes the handle from the 
    <i>NdisDriverHandle</i> parameter at the 
    <i>NdisHandle</i> parameter of 
    <b>NdisSetOptionalHandlers</b> and passes a characteristics structure at the 
    <i>OptionalHandlers</i> parameter.</p>

<p>The optional services are defined in the following structures:</p><dl>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>
</dd>
</dl><p>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
       NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
       NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</p>

<p>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
       NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</p>

<p>NDIS can call the protocol driver's other 
    <i>ProtocolXxx</i> functions at any time after 
    <i>ProtocolSetOptions</i> returns. The driver should be prepared to be called back at the 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function.
    The protocol bindings are in the 
    <i>Unbound</i> state before the NDIS calls 
    <i>ProtocolBindAdapterEx</i>.</p>

<p>If an attempt to allocate resources or services fails, 
    <i>ProtocolSetOptions</i> should undo all the allocations that succeeded before it returns control with a
    status other than NDIS_STATUS_SUCCESS.</p>

<p>NDIS calls 
    <i>ProtocolSetOptions</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>ProtocolSetOptions</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolSetOptions</i> function that is named "MySetOptions", use the <b>SET_OPTIONS</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>SET_OPTIONS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>SET_OPTIONS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-co-call-manager-optional-handlers.md">
   NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-co-client-optional-handlers.md">
   NDIS_CO_CLIENT_OPTIONAL_HANDLERS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-protocol-co-characteristics.md">
   NDIS_PROTOCOL_CO_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564520">NdisRegisterProtocolDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20SET_OPTIONS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
