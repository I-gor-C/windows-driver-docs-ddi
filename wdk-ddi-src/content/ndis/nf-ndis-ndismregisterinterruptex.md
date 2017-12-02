---
UID: NF.ndis.NdisMRegisterInterruptEx
title: NdisMRegisterInterruptEx
author: windows-driver-content
description: NDIS miniport drivers call the NdisMRegisterInterruptEx function to register an interrupt.
old-location: netvista\ndismregisterinterruptex.htm
old-project: netvista
ms.assetid: db0b3d51-5bbb-45fb-8c45-dda8c2212b5f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisMRegisterInterruptEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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

### -param MiniportAdapterHandle [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param MiniportInterruptContext [in]

<dd>
<p>A pointer to a block of context information. The miniport driver allocates this memory to store
     information about the interrupt. NDIS passes the context information block in subsequent calls to other
     functions that are associated with the interrupt.</p>
</dd>

### -param MiniportInterruptCharacteristics [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-miniport-interrupt-characteristics.md">
     NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a> structure that the miniport driver created. The driver
     initializes this structure with handler entry points and configuration parameters that define the
     interrupt characteristics.</p>
</dd>

### -param NdisInterruptHandle [out]

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
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function if
    it manages a NIC that generates interrupts.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function before calling 
    <b>NdisMRegisterInterruptEx</b>.</p>

<p>The miniport driver must specify entry points for the following interrupt service functions:</p>

<p>
<a href="..\ndis\nc-ndis-miniport-isr.md">MiniportInterrupt</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-disable-interrupt.md">
       MiniportDisableInterruptEx</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-enable-interrupt.md">MiniportEnableInterruptEx</a>
</p>

<p>If the NIC supports message-signaled interrupts (MSI), the miniport driver should specify entry points
    for the following MSI service functions:</p>

<p>
<a href="..\ndis\nc-ndis-miniport-message-interrupt.md">MiniportMessageInterrupt</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-message-interrupt-dpc.md">
       MiniportMessageInterruptDPC</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-disable-message-interrupt.md">
       MiniportDisableMessageInterrupt</a>
</p>

<p>
<a href="..\ndis\nc-ndis-miniport-enable-message-interrupt.md">
       MiniportEnableMessageInterrupt</a>
</p>

<p>If a driver specifies entry points for MSI, it must also specify entry points for the non-MSI
    interrupt service functions. Also, if 
    <b>NdisMRegisterInterruptEx</b> returns NDIS_STATUS_SUCCESS, the driver must examine the value of the 
    <b>InterruptType</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-miniport-interrupt-characteristics.md">
    NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a> structure to determine the type of interrupts NDIS granted.
    If NDIS cannot grant MSI support, it will grant support for line based interrupts.</p>

<p>When interrupts are enabled on the NIC, a driver's 
    <i>MiniportInterrupt</i>(or 
    <i>MiniportMessageInterrupt</i>) function can be called at any time after the driver calls 
    <b>NdisMRegisterInterruptEx</b>, even before 
    <b>NdisMRegisterInterruptEx</b> returns. Therefore, a driver should not call 
    <b>NdisMRegisterInterruptEx</b> until it is ready to handle an interrupt.</p>

<p>Drivers call the 
    <a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">
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
<a href="devtest.ndis_init_deregisterinterrupt">Init_DeRegisterInterrupt</a>, <a href="devtest.ndis_init_registerinterrupt">Init_RegisterInterrupt</a>, <a href="devtest.ndis_irql_interrupt_function">Irql_Interrupt_Function</a>, <a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">NdisMDeregisterInterruptEx</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-disable-interrupt.md">MiniportDisableInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-disable-message-interrupt.md">
   MiniportDisableMessageInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-enable-interrupt.md">MiniportEnableInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-enable-message-interrupt.md">
   MiniportEnableMessageInterrupt</a>
</dt>
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
<a href="..\ndis\nc-ndis-miniport-message-interrupt.md">MiniportMessageInterrupt</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-message-interrupt-dpc.md">MiniportMessageInterruptDPC</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-interrupt-characteristics.md">
   NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismderegisterinterruptex.md">NdisMDeregisterInterruptEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterInterruptEx function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
