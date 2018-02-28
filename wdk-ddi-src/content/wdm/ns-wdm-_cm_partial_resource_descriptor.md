---
UID: NS:wdm._CM_PARTIAL_RESOURCE_DESCRIPTOR
title: "_CM_PARTIAL_RESOURCE_DESCRIPTOR"
author: windows-driver-content
description: The CM_PARTIAL_RESOURCE_DESCRIPTOR structure specifies one or more system hardware resources, of a single type, assigned to a device.
old-location: kernel\cm_partial_resource_descriptor.htm
old-project: kernel
ms.assetid: 96bf7bab-b8f5-439c-8717-ea6956ed0213
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PCM_PARTIAL_RESOURCE_DESCRIPTOR, CM_PARTIAL_RESOURCE_DESCRIPTOR, CM_PARTIAL_RESOURCE_DESCRIPTOR structure [Kernel-Mode Driver Architecture], CM_RESOURCE_CONNECTION_CLASS_GPIO, CM_RESOURCE_CONNECTION_CLASS_SERIAL, CM_RESOURCE_CONNECTION_TYPE_GPIO_IO, CM_RESOURCE_CONNECTION_TYPE_SERIAL_I2C, CM_RESOURCE_CONNECTION_TYPE_SERIAL_SPI, CM_RESOURCE_CONNECTION_TYPE_SERIAL_UART, CmResourceShareDeviceExclusive, CmResourceShareDriverExclusive, CmResourceShareShared, PCM_PARTIAL_RESOURCE_DESCRIPTOR, PCM_PARTIAL_RESOURCE_DESCRIPTOR structure pointer [Kernel-Mode Driver Architecture], _CM_PARTIAL_RESOURCE_DESCRIPTOR, kernel.cm_partial_resource_descriptor, kstruct_a_2a821975-e3b8-4ce0-9dd5-8afe348001d8.xml, wdm/CM_PARTIAL_RESOURCE_DESCRIPTOR, wdm/PCM_PARTIAL_RESOURCE_DESCRIPTOR"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	CM_PARTIAL_RESOURCE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: CM_PARTIAL_RESOURCE_DESCRIPTOR, *PCM_PARTIAL_RESOURCE_DESCRIPTOR
req.product: Windows 10 or later.
---

# _CM_PARTIAL_RESOURCE_DESCRIPTOR structure
The <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure specifies one or more system hardware resources, of a single type, assigned to a device. This structure is used to create an array within a <a href="..\wudfwdm\ns-wudfwdm-_cm_partial_resource_list.md">CM_PARTIAL_RESOURCE_LIST</a> structure.

## Syntax
````
typedef struct _CM_PARTIAL_RESOURCE_DESCRIPTOR {
  UCHAR  Type;
  UCHAR  ShareDisposition;
  USHORT Flags;
  union {
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length;
    } Generic;
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length;
    } Port;
    struct {
#if defined(NT_PROCESSOR_GROUPS)
      USHORT    Level;
      USHORT    Group;
#else 
      ULONG     Level;
#endif 
      ULONG     Vector;
      KAFFINITY Affinity;
    } Interrupt;
    struct {
      union {
        struct {
#if defined(NT_PROCESSOR_GROUPS)
          USHORT    Group;
#else 
          USHORT    Reserved;
#endif 
          USHORT    MessageCount;
          ULONG     Vector;
          KAFFINITY Affinity;
        } Raw;
        struct {
#if defined(NT_PROCESSOR_GROUPS)
          USHORT    Level;
          USHORT    Group;
#else 
          ULONG     Level;
#endif 
          ULONG     Vector;
          KAFFINITY Affinity;
        } Translated;
      };
    } MessageInterrupt;
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length;
    } Memory;
    struct {
      ULONG Channel;
      ULONG Port;
      ULONG Reserved1;
    } Dma;
    struct {
      ULONG Channel;
      ULONG RequestLine;
      UCHAR TransferWidth;
      UCHAR Reserved1;
      UCHAR Reserved2;
      UCHAR Reserved3;
    } DmaV3;
    struct {
      ULONG Data[3];
    } DevicePrivate;
    struct {
      ULONG Start;
      ULONG Length;
      ULONG Reserved;
    } BusNumber;
    struct {
      ULONG DataSize;
      ULONG Reserved1;
      ULONG Reserved2;
    } DeviceSpecificData;
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length40;
    } Memory40;
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length48;
    } Memory48;
    struct {
      PHYSICAL_ADDRESS Start;
      ULONG            Length64;
    } Memory64;
    struct {
      UCHAR Class;
      UCHAR Type;
      UCHAR Reserved1;
      UCHAR Reserved2;
      ULONG IdLowPart;
      ULONG IdHighPart;
    } Connection;
  } u;
} CM_PARTIAL_RESOURCE_DESCRIPTOR, *PCM_PARTIAL_RESOURCE_DESCRIPTOR;
````

## Members


`Flags`

Contains flag bits that are specific to the resource type, as indicated in the following table. Flags can be bitwise-ORed together as appropriate.

<table>
<tr>
<th>Resource type</th>
<th colspan="2">Flag</th>
<th>Definition</th>
</tr>
<tr>
<td colspan="4">
<b>CmResourceTypePort</b>

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_MEMORY

</td>
<td>
The device is accessed in memory address space.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_IO

</td>
<td>
The device is accessed in I/O address space.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_10_BIT_DECODE

</td>
<td>
The device decodes 10 bits of the port address.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_12_BIT_DECODE

</td>
<td>
The device decodes 12 bits of the port address.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_16_BIT_DECODE

</td>
<td>
The device decodes 16 bits of the port address.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_POSITIVE_DECODE

</td>
<td>
The device uses "positive decode" instead of "subtractive decode". (In general, PCI devices use positive decode and ISA buses use subtractive decode.)

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_PASSIVE_DECODE

</td>
<td>
The device decodes the port but the driver does not use it.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_PORT_WINDOW_DECODE

</td>
<td>
<u>Reserved for system use.
          </u>

</td>
</tr>
<tr>
<td colspan="4">
<b>CmResourceTypeInterrupt</b>

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_LEVEL_SENSITIVE

</td>
<td>
The IRQ line is level-triggered. (These IRQs are usually sharable.)

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_LATCHED

</td>
<td>
The IRQ line is edge-triggered.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_MESSAGE

</td>
<td>
If this flag is set, the interrupt is a message-signaled interrupt. Otherwise, the interrupt is a line-based interrupt. This flag can be set starting with Windows Vista.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_POLICY_INCLUDED

</td>
<td>
Not used with the <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure. For more information about this flag, see <a href="..\wdm\ns-wdm-_io_resource_descriptor.md">IO_RESOURCE_DESCRIPTOR</a>.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_SECONDARY_INTERRUPT

</td>
<td>
The interrupt is a secondary interrupt. This flag can be set starting with Windows 8. For more information about secondary interrupts, see <a href="https://msdn.microsoft.com/0F56AD4C-E0BF-49F1-AB67-0107D08DEF9F">GPIO Interrupts</a>.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_INTERRUPT_WAKE_HINT

</td>
<td>
The interrupt is capable of waking the operating system from a low-power idle state or a system sleep state. This flag can be set starting with Windows 8. For more information about wake capabilities, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544239">Enabling Device Wake-Up</a>.

</td>
</tr>
<tr>
<td colspan="4">
<b>CmResourceTypeMemory</b>

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_READ_WRITE

</td>
<td>
The memory range is readable and writable.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_READ_ONLY

</td>
<td>
The memory range is read-only.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_WRITE_ONLY

</td>
<td>
The memory range is write-only.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_PREFETCHABLE

</td>
<td>
The memory range is prefetchable.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_COMBINEDWRITE

</td>
<td>
Combined-write caching is allowed.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_24

</td>
<td>
The device uses 24-bit addressing.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_MEMORY_CACHEABLE

</td>
<td>
The memory range is cacheable.

</td>
</tr>
<tr>
<td colspan="4">
<b>CmResourceTypeMemoryLarge</b>

</td>
</tr>
<tr>
<td></td>
<td>
CM_RESOURCE_MEMORY_LARGE_40

</td>
<td colspan="2">
The memory descriptor uses the <b>u.Memory40</b> member.

</td>
</tr>
<tr>
<td></td>
<td>
CM_RESOURCE_MEMORY_LARGE_48

</td>
<td colspan="2">
The memory descriptor uses the <b>u.Memory48</b> member.

</td>
</tr>
<tr>
<td></td>
<td>
CM_RESOURCE_MEMORY_LARGE_64

</td>
<td colspan="2">
The memory descriptor uses the <b>u.Memory64</b> member.

</td>
</tr>
<tr>
<td colspan="4">
<b>CmResourceTypeDma</b>

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_8

</td>
<td>
8-bit DMA channel

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_16

</td>
<td>
16-bit DMA channel

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_32

</td>
<td>
32-bit DMA channel

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_8_AND_16

</td>
<td>
8-bit and 16-bit DMA channel

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_BUS_MASTER

</td>
<td>
The device supports bus master DMA transfers.

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_TYPE_A

</td>
<td>
Type A DMA

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_TYPE_B

</td>
<td>
Type B DMA

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_TYPE_F

</td>
<td>
Type F DMA

</td>
</tr>
<tr>
<td></td>
<td colspan="2">
CM_RESOURCE_DMA_V3

</td>
<td>
Use the <b>DmaV3</b> member instead of the <b>Dma</b> member. The <b>DmaV3</b> member is available starting with Windows 8.

</td>
</tr>
</table>

`ShareDisposition`

Indicates whether the described resource can be shared. Valid constant values are listed in the following table.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="CmResourceShareDeviceExclusive"></a><a id="cmresourcesharedeviceexclusive"></a><a id="CMRESOURCESHAREDEVICEEXCLUSIVE"></a><dl>
<dt><b>CmResourceShareDeviceExclusive</b></dt>
</dl>
</td>
<td width="60%">
The device requires exclusive use of the resource.

</td>
</tr>
<tr>
<td width="40%"><a id="CmResourceShareDriverExclusive"></a><a id="cmresourcesharedriverexclusive"></a><a id="CMRESOURCESHAREDRIVEREXCLUSIVE"></a><dl>
<dt><b>CmResourceShareDriverExclusive</b></dt>
</dl>
</td>
<td width="60%">
The driver requires exclusive use of the resource. (Not supported for WDM drivers.)

</td>
</tr>
<tr>
<td width="40%"><a id="CmResourceShareShared"></a><a id="cmresourceshareshared"></a><a id="CMRESOURCESHARESHARED"></a><dl>
<dt><b>CmResourceShareShared</b></dt>
</dl>
</td>
<td width="60%">
The resource can be shared without restriction.

</td>
</tr>
</table>

`Type`

Identifies the resource type. The constant value specified for <b>Type</b> indicates which structure within the <b>u</b> union is valid, as indicated in the following table. (These flags are used within both <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> and <a href="..\wdm\ns-wdm-_io_resource_descriptor.md">IO_RESOURCE_DESCRIPTOR</a> structures, except where noted.)

<table>
<tr>
<th>Type value</th>
<th>u member substructure</th>
</tr>
<tr>
<td>
<b>CmResourceTypePort</b>

</td>
<td>
<b>u.Port</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeInterrupt</b>

</td>
<td><b>u.Interrupt</b> or <b>u.MessageInterrupt</b>.If the CM_RESOURCE_INTERRUPT_MESSAGE flag of <b>Flags</b> is set, use <b>u.MessageInterrupt</b>; otherwise, use <b>u.Interrupt</b>.

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeMemory</b>

</td>
<td>
<b>u.Memory</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeMemoryLarge</b>

</td>
<td>One of <b>u.Memory40</b>, <b>u.Memory48</b>, or <b>u.Memory64</b>.The CM_RESOURCE_MEMORY_LARGE_<i>XXX</i> flags set in the <b>Flags</b> member determines which structure is used.

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeDma</b>

</td>
<td>
<b>u.Dma</b>
          (if CM_RESOURCE_DMA_V3 is not set) or <b>u.DmaV3</b> (if CM_RESOURCE_DMA_V3 flag is set)

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeDevicePrivate</b>

</td>
<td>
<b>u.DevicePrivate</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeBusNumber</b>

</td>
<td>
<b>u.BusNumber</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeDeviceSpecific</b>

</td>
<td><b>u.DeviceSpecificData</b>(Not used within <b>IO_RESOURCE_DESCRIPTOR</b>.)

</td>
</tr>
<tr>
<td>
<b>CmResourceTypePcCardConfig</b>

</td>
<td>
<b>u.DevicePrivate</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeMfCardConfig</b>

</td>
<td>
<b>u.DevicePrivate</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeConnection</b>

</td>
<td>
<b>u.Connection</b>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeConfigData</b>

</td>
<td>
<i>Reserved for system use.</i>

</td>
</tr>
<tr>
<td>
<b>CmResourceTypeNonArbitrated</b>

</td>
<td>
<i>
           Not used.</i>

</td>
</tr>
</table>

`u`



## Remarks
A <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure can describe either a raw (bus-relative) resource or a translated (system physical) resource, depending on the routine or IRP with which it is being used. For more information, see <a href="https://msdn.microsoft.com/dfc1376d-7a1a-421c-82ae-e183cac77ec8">Raw and Translated Resources</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h) |

## See Also

<a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a>



<a href="..\ntddk\nf-ntddk-ioreportresourcefordetection.md">IoReportResourceForDetection</a>



<a href="..\wdm\ns-wdm-_io_resource_descriptor.md">IO_RESOURCE_DESCRIPTOR</a>



<a href="..\wdm\ns-wdm-_cm_keyboard_device_data.md">CM_KEYBOARD_DEVICE_DATA</a>



<a href="..\wdm\ns-wdm-_cm_serial_device_data.md">CM_SERIAL_DEVICE_DATA</a>



<a href="..\wudfwdm\ns-wudfwdm-_cm_resource_list.md">CM_RESOURCE_LIST</a>



<a href="..\wdm\nf-wdm-rtlcmencodememioresource.md">RtlCmEncodeMemIoResource</a>



<a href="..\wudfwdm\ns-wudfwdm-_cm_full_resource_descriptor.md">CM_FULL_RESOURCE_DESCRIPTOR</a>



<a href="..\wdm\ns-wdm-_cm_scsi_device_data.md">CM_SCSI_DEVICE_DATA</a>



<a href="..\wdm\ns-wdm-_cm_floppy_device_data.md">CM_FLOPPY_DEVICE_DATA</a>



<a href="..\wdm\nf-wdm-rtlcmdecodememioresource.md">RtlCmDecodeMemIoResource</a>



<a href="..\wudfwdm\ns-wudfwdm-_cm_partial_resource_list.md">CM_PARTIAL_RESOURCE_LIST</a>



<a href="..\wdm\ns-wdm-_dma_operations.md">DMA_OPERATIONS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551830">KAFFINITY</a>



<a href="..\wdm\nf-wdm-iogetdeviceproperty.md">IoGetDeviceProperty</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_PARTIAL_RESOURCE_DESCRIPTOR structure%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>