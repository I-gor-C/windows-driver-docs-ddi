---
UID: NC.ndis.MINIPORT_RESET
title: MINIPORT_RESET
author: windows-driver-content
description: NDIS calls an NDIS miniport driver's MiniportResetEx function to initiate a reset of a network interface card (NIC). For more information, see Miniport Adapter Check-for-Hang and Reset Operations and Miniport Driver Hardware Reset.
old-location: netvista\miniportresetex.htm
old-project: netvista
ms.assetid: 15f82163-a1b5-4cef-a53e-8a97adb2cd92
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: MiniportResetEx
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

# MINIPORT_RESET callback



## -description
<p>NDIS calls an NDIS miniport driver's 
   <i>MiniportResetEx</i> function to initiate a reset of a network interface card (NIC). For more information, see <a href="netvista.miniport_adapter_check_for_hang_and_reset_operations">Miniport Adapter Check-for-Hang and Reset Operations</a> and <a href="https://msdn.microsoft.com/92a469de-396a-4f13-b73d-dc30dd08be7f">Miniport Driver Hardware Reset</a>.</p>


## -prototype

````
MINIPORT_RESET MiniportResetEx;

NDIS_STATUS MiniportResetEx(
  _In_  NDIS_HANDLE MiniportAdapterContext,
  _Out_ PBOOLEAN    AddressingReset
)
{ ... }
````


## -parameters
<dl>

### -param MiniportAdapterContext [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>

### -param AddressingReset [out]

<dd>
<p>A pointer to a Boolean variable. The miniport driver sets this variable to <b>TRUE</b> if NDIS should call the 
     <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function to
     restore addressing and other configuration settings to the current values. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff546572">Hardware Reset</a>.</p>
</dd>
</dl>

## -returns
<p><i>MiniportResetEx</i> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a> successfully reset the miniport adapter to an operational state.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>The driver will complete the reset operation asynchronously by calling the 
       <a href="..\ndis\nf-ndis-ndismresetcomplete.md">NdisMResetComplete</a> function when the
       operation is done.</p><dl>
<dt><b>NDIS_STATUS_RESET_IN_PROGRESS</b></dt>
</dl><p>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a> determined that the miniport adapter was currently being reset, so this call is
       superfluous.</p><dl>
<dt><b>NDIS_STATUS_SOFT_ERRORS</b></dt>
</dl><p><i>MiniportResetEx</i> successfully reset the miniport adapter but a recoverable error occurred during
       the operation. 
       <i>MiniportResetEx</i> should have called the 
       <a href="..\ndis\nf-ndis-ndiswriteerrorlogentry.md">NdisWriteErrorLogEntry</a> function
       with more information about the error.</p><dl>
<dt><b>NDIS_STATUS_HARD_ERRORS</b></dt>
</dl><p><i>MiniportResetEx</i> tried to reset the miniport adapter but an unrecoverable error occurred during
       the operation. 
       <i>MiniportResetEx</i> should have called 
       <b>NdisWriteErrorLogEntry</b> with more information about the error.</p>

<p> </p>

## -remarks
<p>A driver specifies the 
    <i>MiniportResetEx</i> entry point when it calls the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function.</p>

<p><i>MiniportResetEx</i> is not required for intermediate drivers.</p>

<p><i>MiniportResetEx</i> can reset the parameters of the miniport adapter. If a reset causes a change in the
    miniport adapter's station address, the miniport driver automatically restores the prior value of the
    station address after the reset is complete. Any multicast or functional addressing masks, reset by the
    hardware, do not have to be reset in this function.</p>

<p>If a reset operation changes other information, such as multicast or functional addressing
    information, 
    <i>MiniportResetEx</i> must set the variable at 
    <i>AddressingReset</i> to <b>TRUE</b> before it returns. This causes NDIS to call the 
    <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function to
    restore the information. NDIS also restores the Wake on the LAN (WoL) pattern list by calling 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569773">OID_PNP_ADD_WAKE_UP_PATTERN</a>. The
    driver should free the WoL pattern list from its adapter context because the hardware list is already
    reset.</p>

<p>NDIS will not abort any pending OID requests or send requests. If the driver can safely complete
    pending OID or send requests after a reset, the driver can hold pending OID or send requests until after
    the reset operation is complete. Otherwise, the driver should complete the pending OID or send requests
    by calling the 
    <a href="..\ndis\nf-ndis-ndismoidrequestcomplete.md">NdisMOidRequestComplete</a> or 
    <a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
    NdisMSendNetBufferListsComplete</a> functions respectively before 
    <i>MiniportResetEx</i> returns.</p>

<p>A miniport driver should not call the 
    <a href="..\ndis\nf-ndis-ndismindicatestatusex.md">NdisMIndicateStatusEx</a> function to
    signal the start and finish of each reset operation. NDIS notifies bound protocol drivers when a reset
    begins and ends.</p>

<p>If 
    <i>MiniportResetEx</i> must wait for state changes in the miniport adapter during reset operations, it can
    call the 
    <a href="..\ndis\nf-ndis-ndisstallexecution.md">NdisStallExecution</a> function. However, a
    
    <i>MiniportResetEx</i> function must not call 
    <b>NdisStallExecution</b> with a time interval larger than 50 microseconds. If the driver must wait longer
    than 50 microseconds (or if would poll), it should set a timer instead and return
    NDIS_STATUS_PENDING.</p>

<p>If 
    <i>MiniportResetEx</i> returns NDIS_STATUS_PENDING, the driver must complete the reset by calling the 
    <a href="..\ndis\nf-ndis-ndismresetcomplete.md">NdisMResetComplete</a> function.</p>

<p>If a miniport adapter is in the 
    <b>MediaConnectStateConnected</b> state and its state changes because of a reset, including a change to
    the 
    <b>MediaConnectStateUnknown</b> state, the miniport driver must report the state change with an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff567391">NDIS_STATUS_LINK_STATE</a> status
    indication. The miniport driver must also indicate a 
    <b>MediaConnectStateConnected</b> status indication when the link is reestablished after the reset.</p>

<p><i>MiniportResetEx</i> can be preempted by an interrupt.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-miniport-check-for-hang.md">MiniportCheckForHangEx</a> function
    periodically to determine whether it should call 
    <i>MiniportResetEx</i>. The default time-out for calling 
    <i>MiniportCheckForHangEx</i> is 2 seconds. If this default is too short, a miniport driver can set a larger <b>CheckForHangTimeInSeconds</b> value when calling the
    
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function during initialization. For more information, see <a href="netvista.miniport_adapter_check_for_hang_and_reset_operations">Miniport Adapter Check-for-Hang and Reset Operations</a>.</p>

<p>NDIS cannot determine whether a NIC has stopped responding for receive operations. To handle this kind
    of failure, the 
    <i>MiniportCheckForHangEx</i> function can monitor receive operations and, if necessary, return <b>TRUE</b> to
    force a reset. A miniport can also request a reset by calling <a href="..\ndis\nf-ndis-ndismresetminiport.md">NdisMResetMiniport</a>.</p>

<p>NDIS calls 
    <i>MiniportResetEx</i> at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>To define a <i>MiniportResetEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportResetEx</i> function that is named "MyResetEx", use the <b>MINIPORT_RESET</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_RESET</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_RESET</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-check-for-hang.md">MiniportCheckForHangEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567391">NDIS_STATUS_LINK_STATE</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismindicatestatusex.md">NdisMIndicateStatusEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismoidrequestcomplete.md">NdisMOidRequestComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismresetcomplete.md">NdisMResetComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismresetminiport.md">NdisMResetMiniport</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
   NdisMSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisstallexecution.md">NdisStallExecution</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiswriteerrorlogentry.md">NdisWriteErrorLogEntry</a>
</dt>
<dt>
<a href="netvista.miniport_adapter_check_for_hang_and_reset_operations">Miniport Adapter Check-for-Hang and Reset Operations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/92a469de-396a-4f13-b73d-dc30dd08be7f">Miniport Driver Hardware Reset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_RESET callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
