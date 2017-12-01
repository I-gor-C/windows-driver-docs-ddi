---
UID: NS.strmini._PORT_CONFIGURATION_INFORMATION~r1
title: PORT_CONFIGURATION_INFORMATION
author: windows-driver-content
description: PORT_CONFIGURATION_INFORMATION describes the hardware settings of a streaming minidriver's device. The class driver fills in most members with information provided by the operating system.
old-location: stream\port_configuration_information.htm
old-project: stream
ms.assetid: fa990867-4e2f-4940-b6fc-310ec7fc2b68
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PORT_CONFIGURATION_INFORMATION, PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PORT_CONFIGURATION_INFORMATION
req.alt-loc: strmini.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PORT_CONFIGURATION_INFORMATION structure



## -description
<p>PORT_CONFIGURATION_INFORMATION describes the hardware settings of a streaming minidriver's device. The class driver fills in most members with information provided by the operating system.</p>


## -syntax

````
typedef struct _PORT_CONFIGURATION_INFORMATION {
  ULONG           SizeOfThisPacket;
  PVOID           HwDeviceExtension;
  PDEVICE_OBJECT  ClassDeviceObject;
  PDEVICE_OBJECT  PhysicalDeviceObject;
  ULONG           SystemIoBusNumber;
  INTERFACE_TYPE  AdapterInterfaceType;
  ULONG           BusInterruptLevel;
  ULONG           BusInterruptVector;
  KINTERRUPT_MODE InterruptMode;
  ULONG           DmaChannel;
  ULONG           NumberOfAccessRanges;
  PACCESS_RANGE   AccessRanges;
  ULONG           StreamDescriptorSize;
  PIRP            Irp;
  PKINTERRUPT     InterruptObject;
  PADAPTER_OBJECT DmaAdapterObject;
  PDEVICE_OBJECT  RealPhysicalDeviceObject;
  ULONG           Reserved[1];
} PORT_CONFIGURATION_INFORMATION, *PPORT_CONFIGURATION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>SizeOfThisPacket</b>

<dd>
<p>The size of this structure, in bytes. The class driver fills in this member.</p>
</dd>

### -field <b>HwDeviceExtension</b>

<dd>
<p>Pointer to the minidriver's device extension. The minidriver may use this buffer to record private information global to the minidriver. The minidriver sets the size of this buffer in the <a href="..\strmini\ns-strmini--hw-initialization-data.md">HW_INITIALIZATION_DATA</a> structure it passes when it registers itself via <a href="stream.streamclassregisterminidriver">StreamClassRegisterMinidriver</a>. The class driver also passes pointers to this buffer in the <b>HwDeviceExtension</b> member of the <a href="..\strmini\ns-strmini--hw-stream-object~r1.md">HW_STREAM_OBJECT</a>, <a href="..\strmini\ns-strmini--hw-stream-request-block.md">HW_STREAM_REQUEST_BLOCK</a>, and <a href="..\strmini\ns-strmini--hw-time-context.md">HW_TIME_CONTEXT</a> structures it passes to the minidriver.</p>
</dd>

### -field <b>ClassDeviceObject</b>

<dd>
<p>Points to the class-driver-provided functional device object (FDO) for the driver's device.</p>
</dd>

### -field <b>PhysicalDeviceObject</b>

<dd>
<p>Points to the device object for the driver at the top of the driver stack when the class driver attaches to the driver stack. Drivers use this member when calling <a href="..\wdm\nf-wdm-iocalldriver.md">IoCallDriver</a> to communicate with the driver stack. The <b>RealPhysicalDeviceObject</b> member points to the actual PDO for the driver's device.</p>
</dd>

### -field <b>SystemIoBusNumber</b>

<dd>
<p>The class driver fills in this member with the system bus ID number of the device. Bus 0 is the primary system bus. </p>
</dd>

### -field <b>AdapterInterfaceType</b>

<dd>
<dl>
<dd>
<p>Specifies the type of system bus the device is connected to. Possible values include <b>Isa</b>, <b>Eisa</b>, <b>MicroChannel</b>, <b>PCIBus</b>, and <b>PCMCIABus</b>. </p>
</dd>
</dl>
</dd>

### -field <b>BusInterruptLevel</b>

<dd>
<p>The class driver fills in this member with the IRQL for interrupts on this bus.</p>
</dd>

### -field <b>BusInterruptVector</b>

<dd>
<p>The class driver fills in this member with the interrupt vector used by the device.</p>
</dd>

### -field <b>InterruptMode</b>

<dd>
<p>The class driver fills in this member with the interrupt mode, either Latched or LevelSensitive.</p>
</dd>

### -field <b>DmaChannel</b>

<dd>
<p>If the device connects to the ISA bus, the class driver fills in this member with the DMA channel of the device.</p>
</dd>

### -field <b>NumberOfAccessRanges</b>

<dd>
<p>The number of entries in the <b>AccessRanges</b> array.</p>
</dd>

### -field <b>AccessRanges</b>

<dd>
<p>The number of entries in the <b>AccessRanges</b> array.</p>
</dd>

### -field <b>StreamDescriptorSize</b>

<dd>
<p>The minidriver fills in this member with the size of its <a href="..\strmini\ns-strmini--hw-stream-descriptor.md">HW_STREAM_DESCRIPTOR</a> structure.</p>
</dd>

### -field <b>Irp</b>

<dd>
<p>Pointer to the PnP device start IRP that triggered this SRB_INITIALIZE_DEVICE request.</p>
</dd>

### -field <b>InterruptObject</b>

<dd>
<p>If the device uses interrupts, the class driver fills in this member with a pointer to the associated Interrupt object. </p>
</dd>

### -field <b>DmaAdapterObject</b>

<dd>
<p>If the device uses DMA, the class driver fills in this member with a pointer to the associated DmaAdapter object.</p>
</dd>

### -field <b>RealPhysicalDeviceObject</b>

<dd>
<p>Pointer to the PDO for the driver's device.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>
</dl>

## -remarks
<p>Most of the members of PORT_CONFIGURATION_INFORMATION provide information to the minidriver about its use of hardware resources, such as its interrupt vector and the IRQL for its interrupts.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>