---
UID: NC.ndis.PROTOCOL_CM_OPEN_AF
title: PROTOCOL_CM_OPEN_AF
author: windows-driver-content
description: The ProtocolCmOpenAf function is required.
old-location: netvista\protocolcmopenaf.htm
ms.assetid: 7422c205-bc41-4121-b430-ff9e6b49dc2e
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   ProtocolCmOpenAf (NDIS 5.1))
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   ProtocolCmOpenAf (NDIS 5.1))
   in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolCmOpenAf
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

# PROTOCOL_CM_OPEN_AF callback



## -description
<p>The 
  <i>ProtocolCmOpenAf</i> function is required. This function allocates per-open resources for a call manager
  to interact with a connection-oriented NDIS client that is opening the address family.</p>


## -prototype

````
PROTOCOL_CM_OPEN_AF ProtocolCmOpenAf;

NDIS_STATUS ProtocolCmOpenAf(
  _In_  NDIS_HANDLE        CallMgrBindingContext,
  _In_  PCO_ADDRESS_FAMILY AddressFamily,
  _In_  NDIS_HANDLE        NdisAfHandle,
  _Out_ PNDIS_HANDLE       CallMgrAfContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>CallMgrBindingContext</i> [in]

<dd>
<p>For a non-integrated call manager, <i>CallMgrBindingContext</i> specifies the handle to a call manager-allocated context area in which the call managers maintains
     its per-binding state information. The call manager supplied this handle when it called 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>.</p>
<p>For an integrated call manager (MCM), <i>CallMgrBindingContext</i> specifies the handle to a miniport-allocated context area in which the miniport maintains its per-adapter state information.  The miniport supplied this handle in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff553623">NdisMSetAttributesEx</a> call (for 5.x drivers) or its <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a> call (for 6.x drivers).</p>
</dd>

### -param <i>AddressFamily</i> [in]

<dd>
<p>Specifies the address family that a client is opening. This address family was registered by the
     call manager when it called 
     <a href="https://msdn.microsoft.com/8890bf31-f2c7-48b0-926d-8931893ede86">
     NdisCmRegisterAddressFamilyEx</a>.</p>
</dd>

### -param <i>NdisAfHandle</i> [in]

<dd>
<p>Specifies a handle, supplied by NDIS, that uniquely identifies this address family instance. This
     handle is opaque to the call manager and reserved for system use.</p>
</dd>

### -param <i>CallMgrAfContext</i> [out]

<dd>
<p>Specifies the handle to a call manager-supplied context area in which the call manager maintains
     state about this open of an address family it provides.</p>
</dd>
</dl>

## -returns
<p><i>ProtocolCmOpenAf</i> returns the status of its operation(s) as one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the call manager has successfully allocated and initialized any resources
       necessary to accept requests from the client to this address family.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>Indicates that the requested operation is being handled asynchronously. The call manager must
       call 
       <a href="https://msdn.microsoft.com/eed57341-0b1a-4697-b05d-680bc17da796">
       NdisCmOpenAddressFamilyComplete</a> when it has completed all its open-AF operations to indicate to
       NDIS (and the client) that the operation(s) has been completed.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>Indicates that the call manager could not complete its necessary operation(s) because of a lack
       of available system resources, such as memory.</p><dl>
<dt><b>NDIS_STATUS_<i>XXX</i></b></dt>
</dl><p>Indicates that the call manager could not set itself into a state where it can accept requests
       from the client to operate on this address family. This could be an error status propagated from
       another NDIS library function or any error status determined appropriate by the driver writer.</p>

<p> </p>

## -remarks
<p><i>ProtocolCmOpenAf</i> performs any required allocations of dynamic resources and structures that the
    call manager writer deems necessary to perform operations on behalf of the client that is opening an
    instance of this address family. Such resources include, but are not limited to, memory buffers, data
    structures, events, and other such similar resources. A call manager should also initialize any relevant
    per-open data before returning control to NDIS.</p>

<p>When a call manager has allocated its per-open state area, the address of the state area should be set
    in the 
    <i>CallMgrAfContext</i> handle before returning control to NDIS. To do this, dereference 
    <i>CallMgrAfContext</i> and store a pointer to the data area as the value of the handle. For example:</p>

<p>If 
    <i>ProtocolCmOpenAf</i> cannot allocate the per-open resources it needs to carry out subsequent requests
    on behalf of the client opening this address family, it should free all resources that it allocated for
    the open and return control to the NDIS with NDIS_STATUS_RESOURCES.</p>

<p>If 
    <i>ProtocolCmOpenAf</i> has completed its required operations and the CM is ready to accept requests from
    the client, 
    <i>ProtocolCmOpenAf</i> should return control as quickly as possible with a status of
    NDIS_STATUS_SUCCESS.</p>

<p>To define a <i>ProtocolCmOpenAf</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmOpenAf</i> function that is named "MyCmOpenAf", use the <b>PROTOCOL_CM_OPEN_AF</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_OPEN_AF</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_OPEN_AF</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>ProtocolCmOpenAf</i> performs any required allocations of dynamic resources and structures that the
    call manager writer deems necessary to perform operations on behalf of the client that is opening an
    instance of this address family. Such resources include, but are not limited to, memory buffers, data
    structures, events, and other such similar resources. A call manager should also initialize any relevant
    per-open data before returning control to NDIS.</p>

<p>When a call manager has allocated its per-open state area, the address of the state area should be set
    in the 
    <i>CallMgrAfContext</i> handle before returning control to NDIS. To do this, dereference 
    <i>CallMgrAfContext</i> and store a pointer to the data area as the value of the handle. For example:</p>

<p>If 
    <i>ProtocolCmOpenAf</i> cannot allocate the per-open resources it needs to carry out subsequent requests
    on behalf of the client opening this address family, it should free all resources that it allocated for
    the open and return control to the NDIS with NDIS_STATUS_RESOURCES.</p>

<p>If 
    <i>ProtocolCmOpenAf</i> has completed its required operations and the CM is ready to accept requests from
    the client, 
    <i>ProtocolCmOpenAf</i> should return control as quickly as possible with a status of
    NDIS_STATUS_SUCCESS.</p>

<p>To define a <i>ProtocolCmOpenAf</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>ProtocolCmOpenAf</i> function that is named "MyCmOpenAf", use the <b>PROTOCOL_CM_OPEN_AF</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>PROTOCOL_CM_OPEN_AF</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>PROTOCOL_CM_OPEN_AF</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff563209">ProtocolCmOpenAf (NDIS 5.1)</a>)
   in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <i>ProtocolCmOpenAf (NDIS 5.1)</i>)
   in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561639">NdisClOpenAddressFamilyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/eed57341-0b1a-4697-b05d-680bc17da796">
   NdisCmOpenAddressFamilyComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8890bf31-f2c7-48b0-926d-8931893ede86">
   NdisCmRegisterAddressFamilyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PROTOCOL_CM_OPEN_AF callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
