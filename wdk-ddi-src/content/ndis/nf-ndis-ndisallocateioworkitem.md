---
UID: NF.ndis.NdisAllocateIoWorkItem
title: NdisAllocateIoWorkItem
author: windows-driver-content
description: NDIS drivers call the NdisAllocateIoWorkItem function to allocate a work item. For more information, see NDIS I/O Work Items.
old-location: netvista\ndisallocateioworkitem.htm
old-project: netvista
ms.assetid: 54977838-381e-4c86-a6ca-646202fdc619
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAllocateIoWorkItem
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
req.alt-api: NdisAllocateIoWorkItem
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Init_NdisAllocateIoWorkItem, Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisAllocateIoWorkItem function



## -description
<p>NDIS drivers call the 
  <b>NdisAllocateIoWorkItem</b> function to allocate a work item. For more information, see <a href="NULL">NDIS I/O Work Items</a>.</p>


## -syntax

````
NDIS_HANDLE NdisAllocateIoWorkItem(
  _In_ NDIS_HANDLE NdisObjectHandle
);
````


## -parameters
<dl>

### -param <i>NdisObjectHandle</i> [in]

<dd>
<p>The handle of an NDIS object that is associated with a device object or driver object.</p>
</dd>
</dl>

## -returns
<p>If 
     <b>NdisAllocateIoWorkItem</b> successfully allocates a work item, it returns a handle to the work item.
     If it fails, 
     <b>NdisAllocateIoWorkItem</b> returns <b>NULL</b>.</p>

## -remarks
<p>NDIS miniport drivers pass 
    <b>NdisAllocateIoWorkItem</b> either of two handles: the adapter handle that NDIS passed to the 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function or
    the miniport driver handle that NDIS returned when the miniport driver called 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a>.</p>

<p>NDIS filter drivers can pass 
    <b>NdisAllocateIoWorkItem</b> the filter driver handle that NDIS returned when the filter driver called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>.</p>

<p>NDIS miniport drivers and filter drivers can also pass 
    <b>NdisAllocateIoWorkItem</b> the NDIS device handle that NDIS returned when the driver called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a>. 
    <b>NdisAllocateIoWorkItem</b> gets the device object or driver object that is associated with the handle
    and passes the device object or driver object to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a> function.</p>

<p>NDIS drivers call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563775">NdisQueueIoWorkItem</a> function to queue
    work items. After a driver calls 
    <b>NdisQueueIoWorkItem</b>, NDIS calls the driver-specified callback function at IRQL = PASSIVE_LEVEL.
    This can improve system performance by allowing the current function to end immediately and the driver to
    do work later at a lower IRQL.</p>

<p>NDIS drivers must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a> function to free the
    resources associated with a work item that 
    <b>NdisAllocateIoWorkItem</b> allocated.</p>

<p>Drivers can call
    <b>NdisFreeIoWorkItem</b> in the callback routine that is passed to 
    <b>NdisQueueIoWorkItem</b>.</p>

<p>If a miniport driver used the handle that NDIS passed to 
    <i>MiniportInitializeEx</i> when it called 
    <b>NdisAllocateIoWorkItem</b>, the work item must be freed before or in the call to the drivers 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function.</p>

<p>If a miniport driver used the handle that 
    <b>NdisMRegisterMiniportDriver</b> returned when the driver called 
    <b>NdisAllocateIoWorkItem</b>, the driver must free the work item before the driver unloads.</p>

<p>In general, a driver must free the work item before the driver unloads.</p>

<p>NDIS miniport drivers pass 
    <b>NdisAllocateIoWorkItem</b> either of two handles: the adapter handle that NDIS passed to the 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function or
    the miniport driver handle that NDIS returned when the miniport driver called 
    <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
    NdisMRegisterMiniportDriver</a>.</p>

<p>NDIS filter drivers can pass 
    <b>NdisAllocateIoWorkItem</b> the filter driver handle that NDIS returned when the filter driver called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>.</p>

<p>NDIS miniport drivers and filter drivers can also pass 
    <b>NdisAllocateIoWorkItem</b> the NDIS device handle that NDIS returned when the driver called 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a>. 
    <b>NdisAllocateIoWorkItem</b> gets the device object or driver object that is associated with the handle
    and passes the device object or driver object to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a> function.</p>

<p>NDIS drivers call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563775">NdisQueueIoWorkItem</a> function to queue
    work items. After a driver calls 
    <b>NdisQueueIoWorkItem</b>, NDIS calls the driver-specified callback function at IRQL = PASSIVE_LEVEL.
    This can improve system performance by allowing the current function to end immediately and the driver to
    do work later at a lower IRQL.</p>

<p>NDIS drivers must call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a> function to free the
    resources associated with a work item that 
    <b>NdisAllocateIoWorkItem</b> allocated.</p>

<p>Drivers can call
    <b>NdisFreeIoWorkItem</b> in the callback routine that is passed to 
    <b>NdisQueueIoWorkItem</b>.</p>

<p>If a miniport driver used the handle that NDIS passed to 
    <i>MiniportInitializeEx</i> when it called 
    <b>NdisAllocateIoWorkItem</b>, the work item must be freed before or in the call to the drivers 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> function.</p>

<p>If a miniport driver used the handle that 
    <b>NdisMRegisterMiniportDriver</b> returned when the driver called 
    <b>NdisAllocateIoWorkItem</b>, the driver must free the work item before the driver unloads.</p>

<p>In general, a driver must free the work item before the driver unloads.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975103">Init_NdisAllocateIoWorkItem</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547982">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548276">IoAllocateWorkItem</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561855">NdisFreeIoWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563775">NdisQueueIoWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564518">NdisRegisterDeviceEx</a>
</dt>
<dt>
<a href="NULL">NDIS I/O Work Items</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateIoWorkItem function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
