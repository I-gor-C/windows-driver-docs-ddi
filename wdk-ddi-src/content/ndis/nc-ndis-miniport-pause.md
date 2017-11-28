---
UID: NC.ndis.MINIPORT_PAUSE
title: MINIPORT_PAUSE
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportPause function to stop the flow of network data through a specified miniport adapter.
old-location: netvista\miniportpause.htm
old-project: netvista
ms.assetid: 047241a5-6f52-4a82-a334-8508f0de5e1a
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
req.alt-api: MiniportPause
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

# MINIPORT_PAUSE callback



## -description
<p>NDIS calls a miniport driver's 
   <i>MiniportPause</i> function to stop the flow of network data through a specified miniport adapter.</p>


## -prototype

````
MINIPORT_PAUSE MiniportPause;

NDIS_STATUS MiniportPause(
  _In_ NDIS_HANDLE                     MiniportAdapterContext,
  _In_ PNDIS_MINIPORT_PAUSE_PARAMETERS MiniportPauseParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for an miniport adapter.</p>
</dd>

### -param <i>MiniportPauseParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-miniport-pause-parameters.md">
     NDIS_MINIPORT_PAUSE_PARAMETERS</a> structure that defines the pause parameters for the miniport
     adapter.</p>
</dd>
</dl>

## -returns
<p><i>MiniportPause</i> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><i>MiniportPause</i> successfully stopped the flow of network data through the miniport adapter.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p><i>MiniportPause</i> did not complete the pause operation and the operation will be completed
       asynchronously. The miniport driver must call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff563628">NdisMPauseComplete</a> function when the
       operation is complete.</p>

<p> </p>

## -remarks
<p>A driver specifies the 
    <i>MiniportPause</i> entry point when it calls the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>NDIS pauses a miniport adapter to stop data flow that could interfere with PnP operations such as
    adding or removing a filter driver, or binding or unbinding a protocol driver.</p>

<p>NDIS calls a miniport driver's 
    <i>MiniportPause</i> function to initiate a pause request for the miniport adapter specified at 
    <i>MiniportAdapterContext</i>. The miniport adapter remains in the 
    <i>Pausing</i> state until the pause operation is complete.</p>

<p>For a miniport adapter in the 
    <i>Pausing</i> state, the miniport driver:</p>

<p>Waits for all calls to the 
      <a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
      NdisMIndicateReceiveNetBufferLists</a> function to return.</p>

<p>Waits for NDIS to return the ownership of all 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures from
      outstanding receive indications to the miniport driver's 
      <a href="..\ndis\nc-ndis-miniport-return-net-buffer-lists.md">
      MiniportReturnNetBufferLists</a> function.</p>

<p>Completes all outstanding send requests and calls the 
      <a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
      NdisMSendNetBufferListsComplete</a> function for all the outstanding send requests.</p>

<p>Rejects all new send requests made to its 
      <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
      MiniportSendNetBufferLists</a> function immediately by calling 
      <b>NdisMSendNetBufferListsComplete</b>. It should set the complete status in each NET_BUFFER_LIST to
      NDIS_STATUS_PAUSED.</p>

<p>Can provide status indications with the 
      <a href="..\ndis\nf-ndis-ndismindicatestatusex.md">
      NdisMIndicateStatusEx</a> function.</p>

<p>Should handle OID requests in the 
      <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function.</p>

<p>Should not stop the miniport adapter completely if stopping the miniport adapter prevents the driver
      from handling requests or providing status indications.</p>

<p>Should not free the resources the driver allocated during initialization.</p>

<p>NDIS does not initiate other PnP operations for the miniport adapter, such as halt, initialize, power
    change, pause, or a restart requests, while the miniport adapter is in the 
    <i>Pausing</i> state. NDIS can initiate these PnP operations after a miniport adapter is in the 
    <i>Paused</i> state.</p>

<p>After a miniport driver completes all outstanding send requests and NDIS returns all received network
    data structures (from outstanding receive indications), the driver must complete the pause operation. If
    the driver returns NDIS_STATUS_SUCCESS from 
    <i>MiniportPause</i>, the pause operation is complete. If the driver returns NDIS_STATUS_PENDING, the
    miniport adapter can remain in the 
    <i>Pausing</i> state and the pause operation is complete after the driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563628">NdisMPauseComplete</a> function. After the
    pause operation is complete, the miniport adapter is in the 
    <i>Paused</i> state.</p>

<p>For a miniport adapter in the 
    <i>Paused</i> state, the miniport driver:</p>

<p>Must reject all send requests made to 
      <i>MiniportSendNetBufferLists</i> immediately by calling 
      <b>NdisMSendNetBufferListsComplete</b>. It should set the Status member in each NET_BUFFER_LIST to
      NDIS_STATUS_PAUSED.</p>

<p>Can handle receive interrupts (see the 
      <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function) and
      interrupt DPCs (see the 
      <a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a> function),
      but should not indicate received network data.</p>

<p>Can provide status indications with the 
      <b>NdisMIndicateStatusEx</b> function.</p>

<p>Should handle OID requests in the 
      <i>MiniportOidRequest</i> function.</p>

<p>Should handle requests to change the device power state in the 
      <a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
      MiniportDevicePnPEventNotify</a> function.</p>

<p>Can handle calls to 
      <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> functions.</p>

<p>Can handle requests to reset the hardware in the 
      <a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a> function.</p>

<p>Miniport drivers cannot fail a pause request. Therefore, if a miniport driver requires any resources
    to handle a pause request, it should preallocate the resources during initialization.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function to initiate a
    restart request for a miniport adapter that is paused.</p>

<p>NDIS calls 
    <i>MiniportPause</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportPause</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportPause</i> function that is named "MyPause", use the <b>MINIPORT_PAUSE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_PAUSE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_PAUSE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A driver specifies the 
    <i>MiniportPause</i> entry point when it calls the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>NDIS pauses a miniport adapter to stop data flow that could interfere with PnP operations such as
    adding or removing a filter driver, or binding or unbinding a protocol driver.</p>

<p>NDIS calls a miniport driver's 
    <i>MiniportPause</i> function to initiate a pause request for the miniport adapter specified at 
    <i>MiniportAdapterContext</i>. The miniport adapter remains in the 
    <i>Pausing</i> state until the pause operation is complete.</p>

<p>For a miniport adapter in the 
    <i>Pausing</i> state, the miniport driver:</p>

<p>Waits for all calls to the 
      <a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
      NdisMIndicateReceiveNetBufferLists</a> function to return.</p>

<p>Waits for NDIS to return the ownership of all 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structures from
      outstanding receive indications to the miniport driver's 
      <a href="..\ndis\nc-ndis-miniport-return-net-buffer-lists.md">
      MiniportReturnNetBufferLists</a> function.</p>

<p>Completes all outstanding send requests and calls the 
      <a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
      NdisMSendNetBufferListsComplete</a> function for all the outstanding send requests.</p>

<p>Rejects all new send requests made to its 
      <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
      MiniportSendNetBufferLists</a> function immediately by calling 
      <b>NdisMSendNetBufferListsComplete</b>. It should set the complete status in each NET_BUFFER_LIST to
      NDIS_STATUS_PAUSED.</p>

<p>Can provide status indications with the 
      <a href="..\ndis\nf-ndis-ndismindicatestatusex.md">
      NdisMIndicateStatusEx</a> function.</p>

<p>Should handle OID requests in the 
      <a href="..\ndis\nc-ndis-miniport-oid-request.md">MiniportOidRequest</a> function.</p>

<p>Should not stop the miniport adapter completely if stopping the miniport adapter prevents the driver
      from handling requests or providing status indications.</p>

<p>Should not free the resources the driver allocated during initialization.</p>

<p>NDIS does not initiate other PnP operations for the miniport adapter, such as halt, initialize, power
    change, pause, or a restart requests, while the miniport adapter is in the 
    <i>Pausing</i> state. NDIS can initiate these PnP operations after a miniport adapter is in the 
    <i>Paused</i> state.</p>

<p>After a miniport driver completes all outstanding send requests and NDIS returns all received network
    data structures (from outstanding receive indications), the driver must complete the pause operation. If
    the driver returns NDIS_STATUS_SUCCESS from 
    <i>MiniportPause</i>, the pause operation is complete. If the driver returns NDIS_STATUS_PENDING, the
    miniport adapter can remain in the 
    <i>Pausing</i> state and the pause operation is complete after the driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563628">NdisMPauseComplete</a> function. After the
    pause operation is complete, the miniport adapter is in the 
    <i>Paused</i> state.</p>

<p>For a miniport adapter in the 
    <i>Paused</i> state, the miniport driver:</p>

<p>Must reject all send requests made to 
      <i>MiniportSendNetBufferLists</i> immediately by calling 
      <b>NdisMSendNetBufferListsComplete</b>. It should set the Status member in each NET_BUFFER_LIST to
      NDIS_STATUS_PAUSED.</p>

<p>Can handle receive interrupts (see the 
      <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function) and
      interrupt DPCs (see the 
      <a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a> function),
      but should not indicate received network data.</p>

<p>Can provide status indications with the 
      <b>NdisMIndicateStatusEx</b> function.</p>

<p>Should handle OID requests in the 
      <i>MiniportOidRequest</i> function.</p>

<p>Should handle requests to change the device power state in the 
      <a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
      MiniportDevicePnPEventNotify</a> function.</p>

<p>Can handle calls to 
      <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> functions.</p>

<p>Can handle requests to reset the hardware in the 
      <a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a> function.</p>

<p>Miniport drivers cannot fail a pause request. Therefore, if a miniport driver requires any resources
    to handle a pause request, it should preallocate the resources during initialization.</p>

<p>NDIS calls the 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function to initiate a
    restart request for a miniport adapter that is paused.</p>

<p>NDIS calls 
    <i>MiniportPause</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportPause</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportPause</i> function that is named "MyPause", use the <b>MINIPORT_PAUSE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_PAUSE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_PAUSE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-device-pnp-event-notify.md">
   MiniportDevicePnPEventNotify</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-reset.md">MiniportResetEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-return-net-buffer-lists.md">
   MiniportReturnNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-pause-parameters.md">
   NDIS_MINIPORT_PAUSE_PARAMETERS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
   NdisMIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563600">NdisMIndicateStatusEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563628">NdisMPauseComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
   NdisMSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_PAUSE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
