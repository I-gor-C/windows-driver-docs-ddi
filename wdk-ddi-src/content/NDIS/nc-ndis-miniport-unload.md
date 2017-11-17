---
UID: NC.ndis.MINIPORT_UNLOAD
title: MINIPORT_UNLOAD
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportDriverUnload function to request the driver to release resources before the system completes a driver unload operation.
old-location: netvista\miniportdriverunload.htm
ms.assetid: 25c803cf-f8a6-4e41-a731-c3ae7f1db211
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportDriverUnload
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

# MINIPORT_UNLOAD callback



## -description
<p>NDIS calls a miniport driver's 
   <i>MiniportDriverUnload</i> function to request the driver to release resources before the system completes
   a driver unload operation.</p>


## -prototype

````
MINIPORT_UNLOAD MiniportDriverUnload;

VOID MiniportDriverUnload(
  _In_ PDRIVER_OBJECT DriverObject
)
{ ... }
````


## -parameters
<dl>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a> structure that is the driver's
     driver object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver specifies the 
    <i>MiniportDriverUnload</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>The driver object that is associated with an NDIS miniport driver specifies an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564886">Unload</a> routine. The operating system calls the 
    <b>Unload</b> routine when all the devices the miniport driver services have been removed. NDIS provides
    the 
    <b>Unload</b> routine for NDIS drivers. NDIS calls a miniport driver's 
    <i>MiniportDriverUnload</i> function from the 
    <b>Unload</b> routine.</p>

<p>The functionality of the 
    <b>Unload</b> routine is driver-specific. As a general rule, 
    <i>MiniportDriverUnload</i> should undo the operations that were performed in the driver's 
    <b>DriverEntry</b> routine.</p>

<p>A miniport driver calls the 
    <a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
    NdisMDeregisterMiniportDriver</a> function from 
    <i>MiniportDriverUnload</i>.</p>

<p>In addition to 
    <b>NdisMDeregisterMiniportDriver</b>, an intermediate driver also calls the 
    <a href="https://msdn.microsoft.com/792f8f89-ff2c-45d1-bb15-9fcdafd14231">
    NdisDeregisterProtocolDriver</a> function to deregister the protocol interface of the driver. 
    <i>MiniportDriverUnload</i> should also perform any necessary cleanup operations, such as deallocating any
    protocol driver interface resources.</p>

<p>If a miniport driver manages more than one device instance, such as a load-balancing driver, NDIS will
    not call 
    <i>MiniportDriverUnload</i> until after NDIS calls the 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function one time for
    each device instance.</p>

<p>NDIS calls 
    <i>MiniportDriverUnload</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportDriverUnload</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportDriverUnload</i> function that is named "MyDriverUnload", use the <b>MINIPORT_UNLOAD</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_UNLOAD</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_UNLOAD</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A driver specifies the 
    <i>MiniportDriverUnload</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>The driver object that is associated with an NDIS miniport driver specifies an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564886">Unload</a> routine. The operating system calls the 
    <b>Unload</b> routine when all the devices the miniport driver services have been removed. NDIS provides
    the 
    <b>Unload</b> routine for NDIS drivers. NDIS calls a miniport driver's 
    <i>MiniportDriverUnload</i> function from the 
    <b>Unload</b> routine.</p>

<p>The functionality of the 
    <b>Unload</b> routine is driver-specific. As a general rule, 
    <i>MiniportDriverUnload</i> should undo the operations that were performed in the driver's 
    <b>DriverEntry</b> routine.</p>

<p>A miniport driver calls the 
    <a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
    NdisMDeregisterMiniportDriver</a> function from 
    <i>MiniportDriverUnload</i>.</p>

<p>In addition to 
    <b>NdisMDeregisterMiniportDriver</b>, an intermediate driver also calls the 
    <a href="https://msdn.microsoft.com/792f8f89-ff2c-45d1-bb15-9fcdafd14231">
    NdisDeregisterProtocolDriver</a> function to deregister the protocol interface of the driver. 
    <i>MiniportDriverUnload</i> should also perform any necessary cleanup operations, such as deallocating any
    protocol driver interface resources.</p>

<p>If a miniport driver manages more than one device instance, such as a load-balancing driver, NDIS will
    not call 
    <i>MiniportDriverUnload</i> until after NDIS calls the 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function one time for
    each device instance.</p>

<p>NDIS calls 
    <i>MiniportDriverUnload</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportDriverUnload</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportDriverUnload</i> function that is named "MyDriverUnload", use the <b>MINIPORT_UNLOAD</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_UNLOAD</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_UNLOAD</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544174">DRIVER_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561743">NdisDeregisterProtocolDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c428e30d-ce86-4ca0-bc65-45d84a7c910e">
   NdisMDeregisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564886">Unload</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_UNLOAD callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
