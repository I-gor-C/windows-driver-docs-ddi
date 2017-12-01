---
UID: NC.ndis.MINIPORT_MESSAGE_INTERRUPT_DPC
title: MINIPORT_MESSAGE_INTERRUPT_DPC
author: windows-driver-content
description: A miniport driver must provide a MiniportMessageInterruptDPC handler if the driver calls the NdisMRegisterInterruptEx function to register an interrupt.
old-location: netvista\miniportmessageinterruptdpc.htm
old-project: netvista
ms.assetid: c1eca20b-eda1-442c-8644-798fa864d5d7
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: MiniportMessageInterruptDPC
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
req.irql: DISPATCH_LEVEL
req.iface: 
---

# MINIPORT_MESSAGE_INTERRUPT_DPC callback



## -description
<p>A miniport driver must provide a
   <i>MiniportMessageInterruptDPC</i> handler if the driver calls the 
   <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">NdisMRegisterInterruptEx</a> function
   to register an interrupt.</p>


## -prototype

````
MINIPORT_MESSAGE_INTERRUPT_DPC MiniportMessageInterruptDPC;

VOID MiniportMessageInterruptDPC(
  _In_ NDIS_HANDLE MiniportInterruptContext,
  _In_ ULONG       MessageId,
  _In_ PVOID       MiniportDpcContext,
  _In_ PVOID       ReceiveThrottleParameters,
  _In_ PVOID       NdisReserved2
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportInterruptContext</i> [in]

<dd>
<p>A handle to a block of interrupt context information. The miniport driver supplied this handle in
     the 
     <i>MiniportInterruptContext</i> parameter that the miniport driver passed to the 
     <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
     NdisMRegisterInterruptEx</a> function.</p>
</dd>

### -param <i>MessageId</i> [in]

<dd>
<p>A message-signaled interrupt (MSI) message identifier. 
     <i>MessageId</i> is an index to an 
     <a href="..\wdm\ns-wdm--io-interrupt-message-info-entry.md">
     IO_INTERRUPT_MESSAGE_INFO_ENTRY</a> structure inside a 
     <a href="..\wdm\ns-wdm--io-interrupt-message-info.md">
     IO_INTERRUPT_MESSAGE_INFO</a> structure. NDIS passes a pointer to the associated
     <b>IO_INTERRUPT_MESSAGE_INFO</b> structure in the 
     <b>MessageInfoTable</b> member when the driver successfully registers for MSI with the 
     <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">NdisMRegisterInterruptEx</a> function.</p>
</dd>

### -param <i>MiniportDpcContext</i> [in]

<dd>
<p>A pointer to a context area that the miniport driver supplied when it called the 
     <a href="..\ndis\nf-ndis-ndismqueuedpcex.md">NdisMQueueDpcEx</a> or 
     <a href="..\ndis\nf-ndis-ndismqueuedpc.md">NdisMQueueDpc</a> function. If NDIS called 
     <i>MiniportMessageInterruptDPC</i> because the miniport driver returned a bitmask in the 
     <i>TargetProcessors</i> parameter of the 
     <a href="..\ndis\nc-ndis-miniport-message-interrupt.md">
     MiniportMessageInterrupt</a> function, then 
     <i>MiniportDpcContext</i> is <b>NULL</b>.</p>
</dd>

### -param <i>ReceiveThrottleParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-receive-throttle-parameters.md">
     NDIS_RECEIVE_THROTTLE_PARAMETERS</a> structure specifies the maximum number of 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structures that a miniport
     driver should indicate in a DPC.</p>
<div class="alert"><b>Note</b>  In NDIS 6.1 and earlier, this parameter is named <i>NdisReserved1</i>, its datatype is <b>PULONG</b>, and it is reserved for NDIS.</div>
<div> </div>
</dd>

### -param <i>NdisReserved2</i> [in]

<dd>
<p>Reserved for NDIS.</p>
<div class="alert"><b>Note</b>  In NDIS 6.1 and earlier, this parameter's datatype is <b>PULONG</b>.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Miniport drivers that register a message-signaled interrupt with the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">NdisMRegisterInterruptEx</a> function
    must provide a 
    <i>MiniportMessageInterruptDPC</i> function.</p>

<p>NDIS calls 
    <i>MiniportMessageInterruptDPC</i> to complete the deferred processing of an interrupt. The miniport
    driver can call the 
    <a href="..\ndis\nf-ndis-ndismqueuedpcex.md">NdisMQueueDpcEx</a> or 
    <a href="..\ndis\nf-ndis-ndismqueuedpc.md">NdisMQueueDpc</a> function to request additional
    deferred procedure calls (DPCs) for other processors.</p>

<p>Miniport drivers determine the source of each interrupt and take appropriate action. For example, if
    an interrupt indicates the completion of a transmit operation, the miniport driver completes a pending
    send request. If the cause of the interrupt is a change in link state, the miniport driver indicates the
    new link status to NDIS. If there are outstanding receive packets, the miniport driver indicates the
    packets to NDIS.</p>

<p>A miniport driver that supports <a href="netvista.ndis_receive_side_scaling2">receive side scaling (RSS)</a>, and has the feature enabled, examines its
    receive queues in 
    <i>MiniportMessageInterruptDPC</i>. The NIC could have already queued received packets on separate queues
    based on hash values, if the NIC provides such capabilities. Otherwise, the miniport driver can sort the
    packets into separate queues in 
    <i>MiniportMessageInterruptDPC</i>.</p>

<p><i>MiniportMessageInterruptDPC</i> calls the 
    <a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
    NdisMIndicateReceiveNetBufferLists</a> function to indicate the packets on the current processor. 
    <i>MiniportMessageInterruptDPC</i> can determine processing that is required for other CPUs and request
    NDIS to schedule DPCs on CPUs where a DPC is not outstanding.</p>

<p>If the current DPC is running on the same CPU as the 
    <a href="..\ndis\nc-ndis-miniport-message-interrupt.md">
    MiniportMessageInterrupt</a> function, the miniport driver should indicate all of the packets that
    could not be mapped to a CPU. If this DPC is the last scheduled DPC and it will not request additional
    DPCs, 
    <i>MiniportMessageInterruptDPC</i> should reenable the interrupts on the NIC, for the specified message,
    before it returns.</p>

<p>Before NDIS calls 
    <i>MiniportMessageInterruptDPC</i>, interrupts for the specified message on the NIC, have typically been
    disabled in the 
    <a href="..\ndis\nc-ndis-miniport-message-interrupt.md">
    MiniportMessageInterrupt</a> function. Before it returns control, 
    <i>MiniportMessageInterruptDPC</i> can reenable interrupts. If the miniport driver queued additional DPCs
    while interrupts were disabled, the driver should enable the interrupts after the last DPC executes.</p>

<p>Miniport drivers should limit the number of the receive buffers that they indicate while they are
    processing an 
    <i>interrupt DPC batch</i> to complete within the required time limit. An interrupt DPC batch is the
    collection of all the DPCs that run after the ISR and before the interrupts are reenabled.</p>

<p>A miniport driver can call 
    <a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">NdisMDeregisterInterruptEx</a> from
    its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> or 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function to release
    resources that it allocated with 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">NdisMRegisterInterruptEx</a>. After 
    <b>NdisMDeregisterInterruptEx</b> returns, NDIS does not call a miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-message-interrupt.md">MiniportMessageInterrupt</a> or 
    <i>MiniportMessageInterruptDPC</i> function.</p>

<p>NDIS calls 
    <i>MiniportMessageInterruptDPC</i> at IRQL = DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportMessageInterruptDPC</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportMessageInterruptDPC</i> function that is named "MyMessageInterruptDPC", use the <b>MINIPORT_MESSAGE_INTERRUPT_DPC</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_MESSAGE_INTERRUPT_DPC</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_MESSAGE_INTERRUPT_DPC</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--io-interrupt-message-info.md">IO_INTERRUPT_MESSAGE_INFO</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--io-interrupt-message-info-entry.md">
   IO_INTERRUPT_MESSAGE_INFO_ENTRY</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-message-interrupt.md">MiniportMessageInterrupt</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-interrupt-characteristics.md">
   NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-receive-throttle-parameters.md">
     NDIS_RECEIVE_THROTTLE_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">NdisMDeregisterInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismqueuedpc.md">NdisMQueueDpc</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismqueuedpcex.md">NdisMQueueDpcEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
   NdisMIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">NdisMRegisterInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.ndis_receive_side_scaling2">Receive Side Scaling (RSS)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_MESSAGE_INTERRUPT_DPC callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
