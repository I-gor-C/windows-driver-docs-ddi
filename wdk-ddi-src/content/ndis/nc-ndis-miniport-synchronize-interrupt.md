---
UID: NC.ndis.MINIPORT_SYNCHRONIZE_INTERRUPT
title: MINIPORT_SYNCHRONIZE_INTERRUPT
author: windows-driver-content
description: A miniport driver must provide a MiniportSynchronizeInterrupt handler if any driver function that runs at less than DIRQL shares resources with the MiniportInterrupt function.
old-location: netvista\miniportsynchronizeinterrupt.htm
old-project: netvista
ms.assetid: aac1ff91-76aa-46a0-8e8a-85b9f8c3323c
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
req.alt-api: MiniportSynchronizeInterrupt
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
req.irql: See Remarks section
req.iface: 
---

# MINIPORT_SYNCHRONIZE_INTERRUPT callback



## -description
<p>A miniport driver must provide a 
   <i>MiniportSynchronizeInterrupt</i> handler if any driver function that runs at less than DIRQL shares
   resources with the 
   <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function.</p>


## -prototype

````
MINIPORT_SYNCHRONIZE_INTERRUPT MiniportSynchronizeInterrupt;

BOOLEAN MiniportSynchronizeInterrupt(
  _In_ NDIS_HANDLE SynchronizeContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>SynchronizeContext</i> [in]

<dd>
<p>A handle to a context area that is supplied when the miniport driver's 
     <i>MiniportXxx</i> or internal function called the 
     <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
     NdisMSynchronizeWithInterruptEx</a> function.</p>
</dd>
</dl>

## -returns
<p><i>MiniportSynchronizeInterrupt</i> returns a Boolean value with a driver-determined meaning. NDIS
     returns the same value when NDIS returns from 
     <b>NdisMSynchronizeWithInterruptEx</b>.</p>

## -remarks
<p>If any miniport driver function that runs at less than DIRQL shares resources, such as NIC registers,
    with the driver's 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function, that
    driver cannot access those resources directly. If such a lower priority function attempts to access the
    shared resources directly, it might be preempted by 
    <i>MiniportInterrupt</i>. 
    <i>MiniportInterrupt</i> could override the state changes of the lower priority driver function.</p>

<p>To synchronize access to shared resources with 
    <i>MiniportInterrupt</i>, lower priority driver functions must call the 
    <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
    NdisMSynchronizeWithInterruptEx</a> function. The driver's 
    <i>MiniportSynchronizeInterrupt</i> function accesses the shared resources at DIRQL. Calling 
    <b>NdisMSynchronizeWithInterruptEx</b> prevents race conditions and deadlocks in such a miniport
    driver.</p>

<p>Any lower priority driver functions that share resources among themselves (but not with any function
    that runs at DIRQL) should use a spin lock to protect those shared resources.</p>

<p><i>MiniportSynchronizeInterrupt</i> runs at the DIRQL assigned when the driver's 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    calls the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function. Like any driver function that runs at DIRQL, 
    <i>MiniportSynchronizeInterrupt</i> should return control back to the caller as quickly as possible, and
    it can call only those 
    <b>Ndis<i>Xxx</i></b> functions that are safe to call at any IRQL.</p>

<p>To define a <i>MiniportSynchronizeInterrupt</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportSynchronizeInterrupt</i> function that is named "MySynchronizeInterrupt", use the <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>If any miniport driver function that runs at less than DIRQL shares resources, such as NIC registers,
    with the driver's 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function, that
    driver cannot access those resources directly. If such a lower priority function attempts to access the
    shared resources directly, it might be preempted by 
    <i>MiniportInterrupt</i>. 
    <i>MiniportInterrupt</i> could override the state changes of the lower priority driver function.</p>

<p>To synchronize access to shared resources with 
    <i>MiniportInterrupt</i>, lower priority driver functions must call the 
    <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
    NdisMSynchronizeWithInterruptEx</a> function. The driver's 
    <i>MiniportSynchronizeInterrupt</i> function accesses the shared resources at DIRQL. Calling 
    <b>NdisMSynchronizeWithInterruptEx</b> prevents race conditions and deadlocks in such a miniport
    driver.</p>

<p>Any lower priority driver functions that share resources among themselves (but not with any function
    that runs at DIRQL) should use a spin lock to protect those shared resources.</p>

<p><i>MiniportSynchronizeInterrupt</i> runs at the DIRQL assigned when the driver's 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function
    calls the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function. Like any driver function that runs at DIRQL, 
    <i>MiniportSynchronizeInterrupt</i> should return control back to the caller as quickly as possible, and
    it can call only those 
    <b>Ndis<i>Xxx</i></b> functions that are safe to call at any IRQL.</p>

<p>To define a <i>MiniportSynchronizeInterrupt</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportSynchronizeInterrupt</i> function that is named "MySynchronizeInterrupt", use the <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_SYNCHRONIZE_INTERRUPT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<p>See Remarks section</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInetrrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563649">NdisMRegisterInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
   NdisMSynchronizeWithInterruptEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_SYNCHRONIZE_INTERRUPT callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
