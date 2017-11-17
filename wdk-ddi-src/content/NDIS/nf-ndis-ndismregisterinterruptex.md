---
UID: NF.ndis.NdisMRegisterInterruptEx
title: NdisMRegisterInterruptEx
author: windows-driver-content
description: NDIS miniport drivers call the NdisMRegisterInterruptEx function to register an interrupt.
old-location: netvista\ndismregisterinterruptex.htm
ms.assetid: db0b3d51-5bbb-45fb-8c45-dda8c2212b5f
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMRegisterInterruptEx
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Init_DeRegisterInterrupt, Init_RegisterInterrupt, Irql_Interrupt_Function, NdisMDeregisterInterruptEx
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMRegisterInterruptEx
req.iface: 
---

# NdisMRegisterInterruptEx function



## -description
<p>NDIS miniport drivers call the 
  <b>NdisMRegisterInterruptEx</b> function to register an interrupt.</p>


## -syntax

````
NDIS_STATUS NdisMRegisterInterruptEx(
  _In_  NDIS_HANDLE                              MiniportAdapterHandle,
  _In_  NDIS_HANDLE                              MiniportInterruptContext,
  _In_  PNDIS_MINIPORT_INTERRUPT_CHARACTERISTICS MiniportInterruptCharacteristics,
  _Out_ PNDIS_HANDLE                             NdisInterruptHandle
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>MiniportInterruptContext</i> [in]

<dd>
<p>A pointer to a block of context information. The miniport driver allocates this memory to store
     information about the interrupt. NDIS passes the context information block in subsequent calls to other
     functions that are associated with the interrupt.</p>
</dd>

### -param <i>MiniportInterruptCharacteristics</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/f4176e2d-d8d2-4e75-bccb-0c452da4d703">
     NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a> structure that the miniport driver created. The driver
     initializes this structure with handler entry points and configuration parameters that define the
     interrupt characteristics.</p>
</dd>

### -param <i>NdisInterruptHandle</i> [out]

<dd>
<p>A pointer to an NDIS handle. NDIS writes the handle for the newly created interrupt object to the
     address that the 
     <i>NdisInterruptHandle</i> pointer specifies.</p>
</dd>
</dl>

## -returns
<p><b>NdisMRegisterInterruptEx</b> can return one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS initialized the interrupt object and supplied a valid interrupt handle at 
       <i>NdisInterruptHandle</i> . NDIS claimed hardware resources and set up the functions that it calls
       when an interrupt occurs.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><b>NdisMRegisterInterruptEx</b> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_<i>XXX</i> or NT_STATUS_<i>XXX</i></b></dt>
</dl><p>The attempt to initialize the interrupt object failed for reasons other than those in the
       preceding list.</p>

<p> </p>

## -remarks
<p>A miniport driver must call 
    <b>NdisMRegisterInterruptEx</b> from its 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function if
    it manages a NIC that generates interrupts.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> function before calling 
    <b>NdisMRegisterInterruptEx</b>.</p>

<p>The miniport driver must specify entry points for the following interrupt service functions:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/6016ab15-56c6-4430-8883-d4cdcdf6116f">
       MiniportDisableInterruptEx</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/61edeb80-a686-4b8c-ae19-4757616151ef">MiniportEnableInterruptEx</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</p>

<p>
<a href="https://msdn.microsoft.com/6016ab15-56c6-4430-8883-d4cdcdf6116f">
       MiniportDisableInterruptEx</a>
</p>

<p>
<a href="https://msdn.microsoft.com/61edeb80-a686-4b8c-ae19-4757616151ef">MiniportEnableInterruptEx</a>
</p>

<p>If the NIC supports message-signaled interrupts (MSI), the miniport driver should specify entry points
    for the following MSI service functions:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
       MiniportMessageInterruptDPC</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/68d2076d-c991-4219-b6c3-2399ff5c11a3">
       MiniportDisableMessageInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/b0e1bbef-8116-4455-aa5c-7f47386a3700">
       MiniportEnableMessageInterrupt</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
       MiniportMessageInterruptDPC</a>
</p>

<p>
<a href="https://msdn.microsoft.com/68d2076d-c991-4219-b6c3-2399ff5c11a3">
       MiniportDisableMessageInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/b0e1bbef-8116-4455-aa5c-7f47386a3700">
       MiniportEnableMessageInterrupt</a>
</p>

<p>If a driver specifies entry points for MSI, it must also specify entry points for the non-MSI
    interrupt service functions. Also, if 
    <b>NdisMRegisterInterruptEx</b> returns NDIS_STATUS_SUCCESS, the driver must examine the value of the 
    <b>InterruptType</b> member of the 
    <a href="https://msdn.microsoft.com/f4176e2d-d8d2-4e75-bccb-0c452da4d703">
    NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a> structure to determine the type of interrupts NDIS granted.
    If NDIS cannot grant MSI support, it will grant support for line based interrupts.</p>

<p>When interrupts are enabled on the NIC, a driver's 
    <i>MiniportInterrupt</i>(or 
    <i>MiniportMessageInterrupt</i>) function can be called at any time after the driver calls 
    <b>NdisMRegisterInterruptEx</b>, even before 
    <b>NdisMRegisterInterruptEx</b> returns. Therefore, a driver should not call 
    <b>NdisMRegisterInterruptEx</b> until it is ready to handle an interrupt.</p>

<p>Drivers call the 
    <a href="https://msdn.microsoft.com/bc0718b6-4c71-41a8-bab6-a52991b284d9">
    NdisMDeregisterInterruptEx</a> function to release resources that were previously allocated with 
    <b>NdisMRegisterInterruptEx</b>.</p>

<p>A miniport driver must call 
    <b>NdisMRegisterInterruptEx</b> from its 
    <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function if
    it manages a NIC that generates interrupts.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a> function before calling 
    <b>NdisMRegisterInterruptEx</b>.</p>

<p>The miniport driver must specify entry points for the following interrupt service functions:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/6016ab15-56c6-4430-8883-d4cdcdf6116f">
       MiniportDisableInterruptEx</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/61edeb80-a686-4b8c-ae19-4757616151ef">MiniportEnableInterruptEx</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/810503b9-75cd-4b38-ab1f-de240968ded6">MiniportInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/345715fb-878c-44d8-bf78-f3add10dd02b">MiniportInterruptDPC</a>
</p>

<p>
<a href="https://msdn.microsoft.com/6016ab15-56c6-4430-8883-d4cdcdf6116f">
       MiniportDisableInterruptEx</a>
</p>

<p>
<a href="https://msdn.microsoft.com/61edeb80-a686-4b8c-ae19-4757616151ef">MiniportEnableInterruptEx</a>
</p>

<p>If the NIC supports message-signaled interrupts (MSI), the miniport driver should specify entry points
    for the following MSI service functions:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
       MiniportMessageInterruptDPC</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/68d2076d-c991-4219-b6c3-2399ff5c11a3">
       MiniportDisableMessageInterrupt</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/b0e1bbef-8116-4455-aa5c-7f47386a3700">
       MiniportEnableMessageInterrupt</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">
       MiniportMessageInterruptDPC</a>
</p>

<p>
<a href="https://msdn.microsoft.com/68d2076d-c991-4219-b6c3-2399ff5c11a3">
       MiniportDisableMessageInterrupt</a>
</p>

<p>
<a href="https://msdn.microsoft.com/b0e1bbef-8116-4455-aa5c-7f47386a3700">
       MiniportEnableMessageInterrupt</a>
</p>

<p>If a driver specifies entry points for MSI, it must also specify entry points for the non-MSI
    interrupt service functions. Also, if 
    <b>NdisMRegisterInterruptEx</b> returns NDIS_STATUS_SUCCESS, the driver must examine the value of the 
    <b>InterruptType</b> member of the 
    <a href="https://msdn.microsoft.com/f4176e2d-d8d2-4e75-bccb-0c452da4d703">
    NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a> structure to determine the type of interrupts NDIS granted.
    If NDIS cannot grant MSI support, it will grant support for line based interrupts.</p>

<p>When interrupts are enabled on the NIC, a driver's 
    <i>MiniportInterrupt</i>(or 
    <i>MiniportMessageInterrupt</i>) function can be called at any time after the driver calls 
    <b>NdisMRegisterInterruptEx</b>, even before 
    <b>NdisMRegisterInterruptEx</b> returns. Therefore, a driver should not call 
    <b>NdisMRegisterInterruptEx</b> until it is ready to handle an interrupt.</p>

<p>Drivers call the 
    <a href="https://msdn.microsoft.com/bc0718b6-4c71-41a8-bab6-a52991b284d9">
    NdisMDeregisterInterruptEx</a> function to release resources that were previously allocated with 
    <b>NdisMRegisterInterruptEx</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975102">Init_DeRegisterInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547143">Init_RegisterInterrupt</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547955">Irql_Interrupt_Function</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff563575">NdisMDeregisterInterruptEx</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/6016ab15-56c6-4430-8883-d4cdcdf6116f">MiniportDisableInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/68d2076d-c991-4219-b6c3-2399ff5c11a3">
   MiniportDisableMessageInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/61edeb80-a686-4b8c-ae19-4757616151ef">MiniportEnableInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b0e1bbef-8116-4455-aa5c-7f47386a3700">
   MiniportEnableMessageInterrupt</a>
</dt>
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
<a href="https://msdn.microsoft.com/ec2e6f49-dc40-48e8-96dc-c9440a6662a3">MiniportMessageInterrupt</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c1eca20b-eda1-442c-8644-798fa864d5d7">MiniportMessageInterruptDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f4176e2d-d8d2-4e75-bccb-0c452da4d703">
   NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563575">NdisMDeregisterInterruptEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterInterruptEx function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
