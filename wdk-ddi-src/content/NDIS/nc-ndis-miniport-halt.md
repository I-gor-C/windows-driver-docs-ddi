---
UID: NC.ndis.MINIPORT_HALT
title: MINIPORT_HALT
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportHaltEx function to free resources when a miniport adapter is removed, and to stop the hardware.
old-location: netvista\miniporthaltex.htm
ms.assetid: b8d452b4-bef3-4991-87cf-fac15bedfde4
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
req.alt-api: MiniportHaltEx
req.alt-loc: Ndis.h
req.ddi-compliance: WlanAssociation, WlanConnectionRoaming, WlanDisassociation, WlanTimedAssociation, WlanTimedConnectionRoaming, WlanTimedConnectRequest, WlanTimedLinkQuality, WlanTimedScan
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

# MINIPORT_HALT callback



## -description
<p>NDIS calls a miniport driver's 
   <i>MiniportHaltEx</i> function to free resources when a miniport adapter is
   removed, and to stop the hardware. This function puts the miniport into the Halted state, where no other callback can occur (including <a href="https://msdn.microsoft.com/7c88ff02-e791-4642-ad40-78f2ef2cba7d">MiniportShutdownEx</a>). For more information about miniport driver states, see <a href="NULL">Miniport Adapter States and Operations</a>.</p>


## -prototype

````
MINIPORT_HALT MiniportHaltEx;

VOID MiniportHaltEx(
  _In_ NDIS_HANDLE      MiniportAdapterContext,
  _In_ NDIS_HALT_ACTION HaltAction
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>

### -param <i>HaltAction</i> [in]

<dd>
<p>The reason for halting the miniport adapter. It can be one of the following values:
     </p>
<p></p>
<dl>

### -param <a id="NdisHaltDeviceDisabled"></a><a id="ndishaltdevicedisabled"></a><a id="NDISHALTDEVICEDISABLED"></a><b>NdisHaltDeviceDisabled</b>

<dd>
<p>NDIS is halting the miniport adapter in response to a Plug and Play (PnP) remove message.</p>
</dd>

### -param <a id="NdisHaltDeviceInstanceDeInitialized"></a><a id="ndishaltdeviceinstancedeinitialized"></a><a id="NDISHALTDEVICEINSTANCEDEINITIALIZED"></a><b>NdisHaltDeviceInstanceDeInitialized</b>

<dd>
<p>NDIS is halting the miniport adapter in response to an intermediate driver calling the 
       <a href="https://msdn.microsoft.com/badfab43-ba58-4711-a181-af87dcfeba4d">
       NdisIMDeInitializeDeviceInstance</a> function.</p>
</dd>

### -param <a id="NdisHaltDevicePoweredDown"></a><a id="ndishaltdevicepowereddown"></a><a id="NDISHALTDEVICEPOWEREDDOWN"></a><b>NdisHaltDevicePoweredDown</b>

<dd>
<p>NDIS is halting the miniport adapter because the system is going to a sleeping state.</p>
</dd>

### -param <a id="NdisHaltDeviceSurpriseRemoved"></a><a id="ndishaltdevicesurpriseremoved"></a><a id="NDISHALTDEVICESURPRISEREMOVED"></a><b>NdisHaltDeviceSurpriseRemoved</b>

<dd>
<p>The miniport adapter has been surprise removed and the hardware is not present.</p>
</dd>

### -param <a id="NdisHaltDeviceFailed"></a><a id="ndishaltdevicefailed"></a><a id="NDISHALTDEVICEFAILED"></a><b>NdisHaltDeviceFailed</b>

<dd>
<p>The miniport adapter is being removed because of a hardware failure. Either the miniport driver
       called the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff563661">NdisMRemoveMiniport</a> function or a
       bus driver did not power up the NIC on resume.</p>
</dd>

### -param <a id="NdisHaltDeviceInitializationFailed"></a><a id="ndishaltdeviceinitializationfailed"></a><a id="NDISHALTDEVICEINITIALIZATIONFAILED"></a><b>NdisHaltDeviceInitializationFailed</b>

<dd>
<p>NDIS could not initialize the miniport adapter for an unknown reason after the 
       <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function completed successfully.</p>
</dd>

### -param <a id="NdisHaltDeviceStopped"></a><a id="ndishaltdevicestopped"></a><a id="NDISHALTDEVICESTOPPED"></a><b>NdisHaltDeviceStopped</b>

<dd>
<p>NDIS is halting the miniport adapter in response to a PnP stop device message.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver specifies the 
    <i>MiniportHaltEx</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>NDIS can call 
    <i>MiniportHaltEx</i> at any time after a driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function
    returns successfully. If the driver controls a physical NIC, 
    <i>MiniportHaltEx</i> should stop the NIC. If an NDIS intermediate driver calls the 
    <a href="https://msdn.microsoft.com/badfab43-ba58-4711-a181-af87dcfeba4d">
    NdisIMDeInitializeDeviceInstance</a> function, NDIS calls the 
    <i>MiniportHaltEx</i> function for the driver's virtual device.</p>

<p><i>MiniportHaltEx</i> must free all resources that were allocated in 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> for a device. 
    <i>MiniportHaltEx</i> also frees any other resources that the driver allocated in
    subsequent operations for that device. The driver must call the reciprocals of the 
    <b>Ndis<i>Xxx</i></b> functions with which it originally allocated the resources. As a general
    rule, a 
    <i>MiniportHaltEx</i> function should call the reciprocal 
    <b>Ndis<i>Xxx</i></b> functions in reverse order to the calls the driver made from 
    <i>MiniportInitializeEx</i>.</p>

<p>If a NIC generates interrupts, a miniport driver's 
    <i>MiniportHaltEx</i> function can be preempted by the driver's 
    <a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a> function until the 
    <i>MiniportHaltEx</i> call to the 
    <a href="https://msdn.microsoft.com/bc0718b6-4c71-41a8-bab6-a52991b284d9">
    NdisMDeregisterInterruptEx</a> function returns. Such a driver's 
    <i>MiniportHaltEx</i> function should disable interrupts, and call 
    <b>
    NdisMDeregisterInterruptEx</b> as soon as possible. Note that a driver can keep getting interrupts
    until 
    <b>
    NdisMDeregisterInterruptEx</b> returns. 
    <b>
    NdisMDeregisterInterruptEx</b> does not return until the driver finishes all the scheduled DPCs (see
    the 
    <a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a> function for
    more information).</p>

<p>If the driver has a 
    <a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a> function that is
    associated with a timer object that could be in the system timer queue, 
    <i>MiniportHaltEx</i> should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function. If 
    <b>NdisCancelTimerObject</b> fails, the timer could have already fired. In this case, the driver should
    wait for the timer function to complete before the driver returns from 
    <i>MiniportHaltEx</i>.</p>

<p>NDIS does not call 
    <i>MiniportHaltEx</i> if there are outstanding OID requests or send requests. NDIS
    submits no further requests for the affected device after NDIS calls 
    <i>MiniportHaltEx</i>.</p>

<p>If the driver must wait for any operation to complete, 
    <i>MiniportHaltEx</i> can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function.</p>

<p>NDIS calls
    <i>MiniportHaltEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportHaltEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportHaltEx</i> function that is named "MyHaltEx", use the <b>MINIPORT_HALT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_HALT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_HALT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A driver specifies the 
    <i>MiniportHaltEx</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>NDIS can call 
    <i>MiniportHaltEx</i> at any time after a driver's 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function
    returns successfully. If the driver controls a physical NIC, 
    <i>MiniportHaltEx</i> should stop the NIC. If an NDIS intermediate driver calls the 
    <a href="https://msdn.microsoft.com/badfab43-ba58-4711-a181-af87dcfeba4d">
    NdisIMDeInitializeDeviceInstance</a> function, NDIS calls the 
    <i>MiniportHaltEx</i> function for the driver's virtual device.</p>

<p><i>MiniportHaltEx</i> must free all resources that were allocated in 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> for a device. 
    <i>MiniportHaltEx</i> also frees any other resources that the driver allocated in
    subsequent operations for that device. The driver must call the reciprocals of the 
    <b>Ndis<i>Xxx</i></b> functions with which it originally allocated the resources. As a general
    rule, a 
    <i>MiniportHaltEx</i> function should call the reciprocal 
    <b>Ndis<i>Xxx</i></b> functions in reverse order to the calls the driver made from 
    <i>MiniportInitializeEx</i>.</p>

<p>If a NIC generates interrupts, a miniport driver's 
    <i>MiniportHaltEx</i> function can be preempted by the driver's 
    <a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a> function until the 
    <i>MiniportHaltEx</i> call to the 
    <a href="https://msdn.microsoft.com/bc0718b6-4c71-41a8-bab6-a52991b284d9">
    NdisMDeregisterInterruptEx</a> function returns. Such a driver's 
    <i>MiniportHaltEx</i> function should disable interrupts, and call 
    <b>
    NdisMDeregisterInterruptEx</b> as soon as possible. Note that a driver can keep getting interrupts
    until 
    <b>
    NdisMDeregisterInterruptEx</b> returns. 
    <b>
    NdisMDeregisterInterruptEx</b> does not return until the driver finishes all the scheduled DPCs (see
    the 
    <a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a> function for
    more information).</p>

<p>If the driver has a 
    <a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a> function that is
    associated with a timer object that could be in the system timer queue, 
    <i>MiniportHaltEx</i> should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a> function. If 
    <b>NdisCancelTimerObject</b> fails, the timer could have already fired. In this case, the driver should
    wait for the timer function to complete before the driver returns from 
    <i>MiniportHaltEx</i>.</p>

<p>NDIS does not call 
    <i>MiniportHaltEx</i> if there are outstanding OID requests or send requests. NDIS
    submits no further requests for the affected device after NDIS calls 
    <i>MiniportHaltEx</i>.</p>

<p>If the driver must wait for any operation to complete, 
    <i>MiniportHaltEx</i> can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function.</p>

<p>NDIS calls
    <i>MiniportHaltEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportHaltEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportHaltEx</i> function that is named "MyHaltEx", use the <b>MINIPORT_HALT</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_HALT</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_HALT</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/dn305122">WlanAssociation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305123">WlanConnectionRoaming</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305124">WlanDisassociation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305125">WlanTimedAssociation</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305126">WlanTimedConnectionRoaming</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305127">WlanTimedConnectRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305128">WlanTimedLinkQuality</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/dn305129">WlanTimedScan</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0f33ae87-164e-40dc-a915-28211a0d74b7">
   MiniportReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561624">NdisCancelTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/badfab43-ba58-4711-a181-af87dcfeba4d">
   NdisIMDeInitializeDeviceInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563575">NdisMDeregisterInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563661">NdisMRemoveMiniport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/76e59376-58a4-4e35-bac4-ec5938c88cd7">NetTimerCallback</a>
</dt>
<dt>
<a href="NULL">Adapter States of a Miniport Driver</a>
</dt>
<dt>
<a href="NULL">Halting a Miniport Adapter</a>
</dt>
<dt>
<a href="NULL">Miniport Adapter States and Operations</a>
</dt>
<dt>
<a href="NULL">Miniport Driver Reset and Halt Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_HALT callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
