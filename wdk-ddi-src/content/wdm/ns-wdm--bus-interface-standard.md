---
UID: NS.wdm._BUS_INTERFACE_STANDARD
title: BUS_INTERFACE_STANDARD
author: windows-driver-content
description: The BUS_INTERFACE_STANDARD interface structure enables device drivers to make direct calls to parent bus driver routines. This structure defines the GUID_BUS_INTERFACE_STANDARD interface.
old-location: kernel\bus_interface_standard.htm
old-project: kernel
ms.assetid: cebe5b45-2a7a-4e33-aacb-5cc3ee112808
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BUS_INTERFACE_STANDARD, BUS_INTERFACE_STANDARD, *PBUS_INTERFACE_STANDARD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BUS_INTERFACE_STANDARD
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# BUS_INTERFACE_STANDARD structure



## -description
<p>The <b>BUS_INTERFACE_STANDARD</b> interface structure enables device drivers to make direct calls to parent bus driver routines. This structure defines the <a href="kernel.guid_bus_interface_standard">GUID_BUS_INTERFACE_STANDARD</a> interface.</p>


## -syntax

````
typedef struct _BUS_INTERFACE_STANDARD {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PTRANSLATE_BUS_ADDRESS TranslateBusAddress;
  PGET_DMA_ADAPTER       GetDmaAdapter;
  PGET_SET_DEVICE_DATA   SetBusData;
  PGET_SET_DEVICE_DATA   GetBusData;
} BUS_INTERFACE_STANDARD, *PBUS_INTERFACE_STANDARD;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field Version

<dd>
<p>The driver-defined interface version.</p>
</dd>

### -field Context

<dd>
<p>A pointer to interface-specific context information.</p>
</dd>

### -field InterfaceReference

<dd>
<p>A pointer to an <a href="kernel.interfacereference">InterfaceReference</a> routine that increments the interface's reference count.</p>
</dd>

### -field InterfaceDereference

<dd>
<p>A pointer to an <a href="kernel.interfacedereference">InterfaceDereference</a> routine that decrements the interface's reference count.</p>
</dd>

### -field TranslateBusAddress

<dd>
<p>A pointer to a <a href="..\wdm\nc-wdm-translate-bus-address.md">TranslateBusAddress</a> routine that translates addresses on the parent bus to logical addresses.</p>
</dd>

### -field GetDmaAdapter

<dd>
<p>A pointer to a <a href="kernel.getdmaadapter">GetDmaAdapter</a> routine that returns a DMA adapter structure (<a href="..\wdm\ns-wdm--dma-adapter.md">DMA_ADAPTER</a>) for the target device.</p>
</dd>

### -field SetBusData

<dd>
<p>A pointer to a <a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a> routine that writes data to the device's configuration space.</p>
</dd>

### -field GetBusData

<dd>
<p>A pointer to a <a href="..\wdm\nc-wdm-get-set-device-data.md">GetBusData</a> routine that reads data from the device's configuration space.</p>
</dd>
</dl>

## -remarks
<p>The <b>BUS_INTERFACE_STANDARD</b> structure is an extension of the <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure.</p>

<p>Some operations on a device are reserved for the device's parent bus driver. These operations might include accessing the device-specific configuration space of a bus or programming a DMA controller.</p>

<p>To read from or write to a device's configuration space, a device driver must rely on the agency of the bus driver in either of two ways:</p>

<p>By sending the I/O request packets (IRPs) <a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff551769">IRP_MN_WRITE_CONFIG</a> to the bus driver.</p>

<p>By obtaining an interface from the bus driver. The device driver can then access its device's configuration space by making direct calls to the bus driver routines provided by the <b>BUS_INTERFACE_STANDARD</b> interface structure. Its member routines, <a href="..\wdm\nc-wdm-get-set-device-data.md">GetBusData</a> and <a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a>, can be used to read from and write to a device's configuration space, respectively.

</p>

<p>For more information about the ways to access configuration space, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540450">Accessing Device Configuration Space</a>.</p>

<p>Some types of devices, such as a bus-mastering storage device, have on-board DMA controllers. However, the device drivers for these devices cannot program these DMA controllers directly. Instead they must rely on routines provided by the parent bus driver. For a device driver to program the DMA controller for its device, it must first request an adapter object from the parent bus driver. The adapter object contains the routines supplied by the bus driver that can be used to program the device's DMA controller. Device drivers must rely on the <b>BUS_INTERFACE_STANDARD</b>, either directly or indirectly, to obtain the adapter object.</p>

<p>If the driver is executing at IRQL = PASSIVE_LEVEL, it should obtain a device's DMA adapter object by calling <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>. <b>IoGetDmaAdapter</b> detects whether the bus driver supports the <b>BUS_INTERFACE_STANDARD</b> interface.   If it does, <b>IoGetDmaAdapter</b> calls the routine pointed to by the <a href="kernel.getdmaadapter">GetDmaAdapter</a> member of this interface to obtain the adapter object. Otherwise, <b>IoGetDmaAdapter</b> calls an equivalent legacy routine.</p>

<p>However, if a driver must obtain an adapter object while running at IRQL &gt;= DISPATCH_LEVEL, it cannot do so with <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>. In this case, the driver must query for the <b>BUS_INTERFACE_STANDARD</b> interface while still at IRQL = PASSIVE_LEVEL by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-description.md">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--dma-adapter.md">DMA_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/gg604850">GetBusData</a>
</dt>
<dt>
<a href="kernel.getdmaadapter">GetDmaAdapter</a>
</dt>
<dt>
<a href="kernel.guid_bus_interface_standard">GUID_BUS_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
<dt>
<a href="kernel.interfacedereference">InterfaceDereference</a>
</dt>
<dt>
<a href="kernel.interfacereference">InterfaceReference</a>
</dt>
<dt>
<a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/d57c30b8-83bd-41c9-906d-b8c95f8ca54e">IRP_MN_WRITE_CONFIG </a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-get-set-device-data.md">SetBusData</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-translate-bus-address.md">TranslateBusAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BUS_INTERFACE_STANDARD structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
