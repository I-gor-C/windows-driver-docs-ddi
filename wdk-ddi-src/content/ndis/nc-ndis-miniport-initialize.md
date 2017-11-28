---
UID: NC.ndis.MINIPORT_INITIALIZE
title: MINIPORT_INITIALIZE
author: windows-driver-content
description: NDIS calls a miniport driver's MiniportInitializeEx function to initialize a miniport adapter for network I/O operations.
old-location: netvista\miniportinitializeex.htm
old-project: netvista
ms.assetid: b146fa81-005b-4a6c-962d-4cb023ea790e
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
req.alt-api: MiniportInitializeEx
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

# MINIPORT_INITIALIZE callback



## -description
<p>NDIS calls a miniport driver's
   <i>MiniportInitializeEx</i> function to initialize a miniport adapter for network I/O operations.</p>


## -prototype

````
MINIPORT_INITIALIZE MiniportInitializeEx;

NDIS_STATUS MiniportInitializeEx(
  _In_ NDIS_HANDLE                    NdisMiniportHandle,
  _In_ NDIS_HANDLE                    MiniportDriverContext,
  _In_ PNDIS_MINIPORT_INIT_PARAMETERS MiniportInitParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>NdisMiniportHandle</i> [in]

<dd>
<p>An NDIS-supplied handle that identifies the miniport adapter that the miniport driver should
     initialize.</p>
</dd>

### -param <i>MiniportDriverContext</i> [in]

<dd>
<p>A handle to a driver-allocated context area where the driver maintains state and configuration
     information. The miniport driver passed this context area to the 
     <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
     NdisMRegisterMiniportDriver</a> function.</p>
</dd>

### -param <i>MiniportInitParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-miniport-init-parameters.md">
     NDIS_MINIPORT_INIT_PARAMETERS</a> structure that defines the initialization parameters for the
     miniport adapter.</p>
</dd>
</dl>

## -returns
<p><i>MiniportInitializeEx</i> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><i>MiniportInitializeEx</i> configured and set up the miniport adapter, and allocated all the resources
       that the driver must have to perform network I/O operations.</p><dl>
<dt><b>NDIS_STATUS_NOT_ACCEPTED</b></dt>
</dl><p><i>MiniportInitializeEx</i> could not get the miniport adapter to accept the configuration parameters
       that 
       <i>MiniportInitializeEx</i> obtained from the registry.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><i>MiniportInitializeEx</i> could not allocate resources to perform network I/O operations. 
       <i>MiniportInitializeEx</i> should call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff564663">NdisWriteErrorLogEntry</a> function
       to identify the resource conflict (for example, I/O port range, interrupt vector, device memory range,
       as appropriate). Supplying an error log record gives the user or system administrator information that
       can be used to reconfigure the computer to avoid such hardware resource conflicts.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p><i>MiniportInitializeEx</i> failed for reasons other than those in the preceding list. The driver
       should call 
       <b>NdisWriteErrorLogEntry</b> with parameters that specify the reason for the failure.</p>

<p> </p>

## -remarks
<p>NDIS calls 
    <i>MiniportInitializeEx</i> as part of a system PnP operation. Drivers specify the 
    <i>MiniportInitializeEx</i> entry point by calling the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function from the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. NDIS can call 
    <i>MiniportInitializeEx</i> after 
    <b>DriverEntry</b> returns. For more information, see 
    <a href="netvista.driverentry_of_ndis_miniport_drivers">DriverEntry of NDIS
    Miniport Drivers</a>.</p>

<p>For NDIS intermediate drivers, NDIS can call 
    <i>MiniportInitializeEx</i> in the context of the 
    <a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
    NdisIMInitializeDeviceInstanceEx</a> function or after it returns. Such a driver's 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function
    usually calls 
    <b>NdisIMInitializeDeviceInstanceEx</b>.</p>

<p>Drivers can register as a combined miniport driver and intermediate driver (see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>).
    Such a miniport-intermediate driver functions similarly to an intermediate driver layered over a physical
    miniport driver. For each virtual or physical device instance of a miniport-intermediate driver, if the 
    <b>IMMiniport</b> registry key is set to 
    <b>DWORD:0x0000001</b>, NDIS calls the 
    <i>MiniportInitializeEx</i> function that the driver registered for the virtual device. Otherwise, NDIS
    calls the driver's 
    <i>MiniportInitializeEx</i> function that the driver registered for the physical device.</p>

<p>Until 
    <i>MiniportInitializeEx</i> returns, NDIS submits no requests for the miniport adapter being initialized.
    The miniport adapter is in the 
    <i>initializing</i> state.</p>

<p>To obtain configuration information for the miniport adapter, a driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a> functions. The
    driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a> function to obtain
    bus-specific information.</p>

<p>Miniport drivers must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function and provide an 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">
    NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure which contains the following
    attributes:</p>

<p>A handle to a driver-allocated context area.</p>

<p>Appropriate attributes flags.</p>

<p>The time-out interval for calling its 
      <a href="..\ndis\nc-ndis-miniport-check-for-hang.md">
      MiniportCheckForHangEx</a> function.</p>

<p>The interface type.</p>

<p>The miniport driver passes
    <b>NdisMSetMiniportAttributes</b> a handle at the 
    <b>MiniportAdapterContext</b> member of NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES. The driver
    maintains state information for the specified miniport adapter in this context area. NDIS passes this
    handle as an input parameter to other 
    <i>MiniportXxx</i> functions.</p>

<p>Miniport drivers must set the attributes in the 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
    NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a> structure after they set the registration attributes in
    the NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure and before they set any additional
    attributes.</p>

<p><i>MiniportInitializeEx</i> can also allocate resources such as the following:</p>

<p>Non-paged pool memory</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> and 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure pools</p>

<p>Spin locks</p>

<p>Timers</p>

<p>IO ports</p>

<p>DMA</p>

<p>Shared memory</p>

<p>Interrupts</p>

<p>If the driver indicates receives with the 
    <a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
    NdisMIndicateReceiveNetBufferLists</a> function, the 
    <i>MiniportInitializeEx</i> function should call the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
    NdisAllocateNetBufferListPool</a> and 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferpool.md">
    NdisAllocateNetBufferPool</a> functions and save the handles returned by these NDIS functions.
    Typically, the network data that the driver subsequently indicates with 
    <b>NdisMIndicateReceiveNetBufferLists</b> references structures that were allocated with the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
    NdisAllocateNetBufferAndNetBufferList</a> function. A driver can also use structures that were
    allocated with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>, and 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlist.md">
    NdisAllocateNetBufferList</a> functions.</p>

<p>If driver functions, other than the 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function, share
    resources, 
    <i>MiniportInitializeEx</i> should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function to set
    up any spin locks necessary to synchronize access to such shared resources. Resources that other driver
    functions share with 
    <i>MiniportInterrupt</i>, such as NIC registers, are protected by the interrupt object that the driver
    set up with the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function. Driver functions access these resources by calling the 
    <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
    NdisMSynchronizeWithInterruptEx</a> function.</p>

<p><i>MiniportInitializeEx</i> can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a> function
    with a driver-supplied 
    <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> function and a pointer
    to driver-allocated memory for a timer object. Drivers can set up multiple 
    <i>NetTimerCallback</i> functions, each with its own timer object. A driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function to enable a
    periodic 
    <i>NetTimerCallback</i> function. A driver can also call the 
    <b>NdisSetTimerObject</b> function to enable a one-time 
    <i>NetTimerCallback</i> function.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function before it calls any 
    <b>NdisM<i>Xxx</i></b> function, such as the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a> functions, that claims
    hardware resources for the miniport adapter. 
    <i>MiniportInitializeEx</i> must call 
    <b>NdisMSetMiniportAttributes</b> before it tries to allocate resources for DMA operations.</p>

<p>If the device supports bus-master DMA, 
    <i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
    NdisMRegisterScatterGatherDma</a> function after it calls 
    <b>NdisMSetMiniportAttributes</b> and before it calls the 
    <a href="..\ndis\nf-ndis-ndismallocatesharedmemory.md">
    NdisMAllocateSharedMemory</a> function. If the device supports subordinate DMA, 
    <i>MiniportInitializeEx</i> must call 
    <b>NdisMSetMiniportAttributes</b> before it calls the 
    <a href="..\ndis\nf-ndis-ndismregisterdmachannel.md">
    NdisMRegisterDmaChannel</a> function.</p>

<p>After 
    <i>MiniportInitializeEx</i> calls the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function, NDIS can call the driver's 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function. NDIS
    calls 
    <i>MiniportInterrupt</i> if the NIC generates an interrupt or if any other device with which the NIC
    shares an interrupt generates an interrupt. Note that a miniport driver can get an interrupt as soon as
    it calls 
    <b>NdisMRegisterInterruptEx</b> and keeps getting interrupts until its call to the 
    <a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">
    NdisMDeregisterInterruptEx</a> function returns.</p>

<p><i>MiniportInitializeEx</i> should test the NIC to make sure that the hardware is configured correctly. If
    the driver must wait for state changes to occur in the hardware, 
    <i>MiniportInitializeEx</i> can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function.</p>

<p>After 
    <i>MiniportInitializeEx</i> returns successfully, the miniport adapter is in the 
    <i>Paused</i> state. NDIS can call the 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function to transition the
    miniport adapter to the 
    <i>Running</i> state.</p>

<p>If 
    <i>MiniportInitializeEx</i> returns NDIS_STATUS_SUCCESS, the driver should release all the resources for
    the miniport adapter in the 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function.</p>

<p>If 
    <i>MiniportInitializeEx</i> failed, 
    <i>MiniportInitializeEx</i> must release all resources that it allocated before it returns and the
    miniport adapter returns to the 
    <i>Halted</i> state.</p>

<p>NDIS calls 
    <i>MiniportInitializeEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportInitializeEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportInitializeEx</i> function that is named "MyInitializeEx", use the <b>MINIPORT_INITIALIZE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_INITIALIZE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_INITIALIZE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>NDIS calls 
    <i>MiniportInitializeEx</i> as part of a system PnP operation. Drivers specify the 
    <i>MiniportInitializeEx</i> entry point by calling the 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a> function from the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. NDIS can call 
    <i>MiniportInitializeEx</i> after 
    <b>DriverEntry</b> returns. For more information, see 
    <a href="netvista.driverentry_of_ndis_miniport_drivers">DriverEntry of NDIS
    Miniport Drivers</a>.</p>

<p>For NDIS intermediate drivers, NDIS can call 
    <i>MiniportInitializeEx</i> in the context of the 
    <a href="..\ndis\nf-ndis-ndisiminitializedeviceinstanceex.md">
    NdisIMInitializeDeviceInstanceEx</a> function or after it returns. Such a driver's 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> function
    usually calls 
    <b>NdisIMInitializeDeviceInstanceEx</b>.</p>

<p>Drivers can register as a combined miniport driver and intermediate driver (see 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>).
    Such a miniport-intermediate driver functions similarly to an intermediate driver layered over a physical
    miniport driver. For each virtual or physical device instance of a miniport-intermediate driver, if the 
    <b>IMMiniport</b> registry key is set to 
    <b>DWORD:0x0000001</b>, NDIS calls the 
    <i>MiniportInitializeEx</i> function that the driver registered for the virtual device. Otherwise, NDIS
    calls the driver's 
    <i>MiniportInitializeEx</i> function that the driver registered for the physical device.</p>

<p>Until 
    <i>MiniportInitializeEx</i> returns, NDIS submits no requests for the miniport adapter being initialized.
    The miniport adapter is in the 
    <i>initializing</i> state.</p>

<p>To obtain configuration information for the miniport adapter, a driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a> functions. The
    driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a> function to obtain
    bus-specific information.</p>

<p>Miniport drivers must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function and provide an 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">
    NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a> structure which contains the following
    attributes:</p>

<p>A handle to a driver-allocated context area.</p>

<p>Appropriate attributes flags.</p>

<p>The time-out interval for calling its 
      <a href="..\ndis\nc-ndis-miniport-check-for-hang.md">
      MiniportCheckForHangEx</a> function.</p>

<p>The interface type.</p>

<p>The miniport driver passes
    <b>NdisMSetMiniportAttributes</b> a handle at the 
    <b>MiniportAdapterContext</b> member of NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES. The driver
    maintains state information for the specified miniport adapter in this context area. NDIS passes this
    handle as an input parameter to other 
    <i>MiniportXxx</i> functions.</p>

<p>Miniport drivers must set the attributes in the 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
    NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a> structure after they set the registration attributes in
    the NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure and before they set any additional
    attributes.</p>

<p><i>MiniportInitializeEx</i> can also allocate resources such as the following:</p>

<p>Non-paged pool memory</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> and 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure pools</p>

<p>Spin locks</p>

<p>Timers</p>

<p>IO ports</p>

<p>DMA</p>

<p>Shared memory</p>

<p>Interrupts</p>

<p>If the driver indicates receives with the 
    <a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
    NdisMIndicateReceiveNetBufferLists</a> function, the 
    <i>MiniportInitializeEx</i> function should call the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
    NdisAllocateNetBufferListPool</a> and 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferpool.md">
    NdisAllocateNetBufferPool</a> functions and save the handles returned by these NDIS functions.
    Typically, the network data that the driver subsequently indicates with 
    <b>NdisMIndicateReceiveNetBufferLists</b> references structures that were allocated with the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
    NdisAllocateNetBufferAndNetBufferList</a> function. A driver can also use structures that were
    allocated with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>, and 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlist.md">
    NdisAllocateNetBufferList</a> functions.</p>

<p>If driver functions, other than the 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function, share
    resources, 
    <i>MiniportInitializeEx</i> should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a> function to set
    up any spin locks necessary to synchronize access to such shared resources. Resources that other driver
    functions share with 
    <i>MiniportInterrupt</i>, such as NIC registers, are protected by the interrupt object that the driver
    set up with the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function. Driver functions access these resources by calling the 
    <a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
    NdisMSynchronizeWithInterruptEx</a> function.</p>

<p><i>MiniportInitializeEx</i> can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a> function
    with a driver-supplied 
    <a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a> function and a pointer
    to driver-allocated memory for a timer object. Drivers can set up multiple 
    <i>NetTimerCallback</i> functions, each with its own timer object. A driver can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a> function to enable a
    periodic 
    <i>NetTimerCallback</i> function. A driver can also call the 
    <b>NdisSetTimerObject</b> function to enable a one-time 
    <i>NetTimerCallback</i> function.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function before it calls any 
    <b>NdisM<i>Xxx</i></b> function, such as the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a> functions, that claims
    hardware resources for the miniport adapter. 
    <i>MiniportInitializeEx</i> must call 
    <b>NdisMSetMiniportAttributes</b> before it tries to allocate resources for DMA operations.</p>

<p>If the device supports bus-master DMA, 
    <i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
    NdisMRegisterScatterGatherDma</a> function after it calls 
    <b>NdisMSetMiniportAttributes</b> and before it calls the 
    <a href="..\ndis\nf-ndis-ndismallocatesharedmemory.md">
    NdisMAllocateSharedMemory</a> function. If the device supports subordinate DMA, 
    <i>MiniportInitializeEx</i> must call 
    <b>NdisMSetMiniportAttributes</b> before it calls the 
    <a href="..\ndis\nf-ndis-ndismregisterdmachannel.md">
    NdisMRegisterDmaChannel</a> function.</p>

<p>After 
    <i>MiniportInitializeEx</i> calls the 
    <a href="..\ndis\nf-ndis-ndismregisterinterruptex.md">
    NdisMRegisterInterruptEx</a> function, NDIS can call the driver's 
    <a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a> function. NDIS
    calls 
    <i>MiniportInterrupt</i> if the NIC generates an interrupt or if any other device with which the NIC
    shares an interrupt generates an interrupt. Note that a miniport driver can get an interrupt as soon as
    it calls 
    <b>NdisMRegisterInterruptEx</b> and keeps getting interrupts until its call to the 
    <a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">
    NdisMDeregisterInterruptEx</a> function returns.</p>

<p><i>MiniportInitializeEx</i> should test the NIC to make sure that the hardware is configured correctly. If
    the driver must wait for state changes to occur in the hardware, 
    <i>MiniportInitializeEx</i> can use the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function or the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a> function.</p>

<p>After 
    <i>MiniportInitializeEx</i> returns successfully, the miniport adapter is in the 
    <i>Paused</i> state. NDIS can call the 
    <a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a> function to transition the
    miniport adapter to the 
    <i>Running</i> state.</p>

<p>If 
    <i>MiniportInitializeEx</i> returns NDIS_STATUS_SUCCESS, the driver should release all the resources for
    the miniport adapter in the 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function.</p>

<p>If 
    <i>MiniportInitializeEx</i> failed, 
    <i>MiniportInitializeEx</i> must release all resources that it allocated before it returns and the
    miniport adapter returns to the 
    <i>Halted</i> state.</p>

<p>NDIS calls 
    <i>MiniportInitializeEx</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportInitializeEx</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportInitializeEx</i> function that is named "MyInitializeEx", use the <b>MINIPORT_INITIALIZE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_INITIALIZE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_INITIALIZE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-check-for-hang.md">MiniportCheckForHangEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-restart.md">MiniportRestart</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-general-attributes.md">
   NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-registration-attributes.md">
   NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565972">NDIS_MINIPORT_INIT_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561609">NdisAllocateNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
   NdisAllocateNetBufferAndNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561613">NdisAllocateNetBufferPool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561617">NdisAllocateSpinLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561618">NdisAllocateTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562782">NdisMAllocateSharedMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563575">NdisMDeregisterInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismindicatereceivenetbufferlists.md">
   NdisMIndicateReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563649">NdisMRegisterInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975121">NdisMRegisterIoPortRange</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
   NdisMRegisterScatterGatherDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563677">NdisMSleep</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsynchronizewithinterruptex.md">
   NdisMSynchronizeWithInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975122">NdisOpenConfigurationEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564511">NdisReadConfiguration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564563">NdisSetTimerObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564663">NdisWriteErrorLogEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-ndis-timer-function.md">NetTimerCallback</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_INITIALIZE callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
