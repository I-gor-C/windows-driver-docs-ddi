---
UID: NS:wdm._IO_RESOURCE_DESCRIPTOR
title: "_IO_RESOURCE_DESCRIPTOR"
author: windows-driver-content
description: The IO_RESOURCE_DESCRIPTOR structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of IO_RESOURCE_DESCRIPTOR structures is contained within each IO_RESOURCE_LIST structure.
old-location: kernel\io_resource_descriptor.htm
old-project: kernel
ms.assetid: 03e3a656-c691-4aff-bcc8-4e0bc8390fd7
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: CM_RESOURCE_INTERRUPT_LATCHED, IO_RESOURCE_ALTERNATIVE, IO_RESOURCE_DESCRIPTOR, CM_RESOURCE_INTERRUPT_LEVEL_SENSITIVE, CM_RESOURCE_CONNECTION_CLASS_SERIAL, CM_RESOURCE_CONNECTION_TYPE_GPIO_IO, CM_RESOURCE_CONNECTION_TYPE_SERIAL_UART, CM_RESOURCE_CONNECTION_TYPE_SERIAL_SPI, IO_RESOURCE_DESCRIPTOR structure [Kernel-Mode Driver Architecture], PIO_RESOURCE_DESCRIPTOR structure pointer [Kernel-Mode Driver Architecture], wdm/PIO_RESOURCE_DESCRIPTOR, CM_RESOURCE_INTERRUPT_WAKE_HINT, kstruct_b_6b096887-dd89-43b8-abb8-4f3582392573.xml, IO_RESOURCE_PREFERRED, CM_RESOURCE_CONNECTION_CLASS_GPIO, 0, _IO_RESOURCE_DESCRIPTOR, wdm/IO_RESOURCE_DESCRIPTOR, PIO_RESOURCE_DESCRIPTOR, IO_RESOURCE_DEFAULT, CM_RESOURCE_CONNECTION_TYPE_SERIAL_I2C, kernel.io_resource_descriptor, *PIO_RESOURCE_DESCRIPTOR, CM_RESOURCE_INTERRUPT_POLICY_INCLUDED, CM_RESOURCE_INTERRUPT_SECONDARY_INTERRUPT, CM_RESOURCE_INTERRUPT_MESSAGE
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Wdm.h
apiname:
-	IO_RESOURCE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: IO_RESOURCE_DESCRIPTOR, *PIO_RESOURCE_DESCRIPTOR
req.product: Windows 10 or later.
---

# _IO_RESOURCE_DESCRIPTOR structure
The <b>IO_RESOURCE_DESCRIPTOR</b> structure describes a range of raw hardware resources, of one type, that can be used by a device. An array of <b>IO_RESOURCE_DESCRIPTOR</b> structures is contained within each <a href="..\wdm\ns-wdm-_io_resource_list.md">IO_RESOURCE_LIST</a> structure.

## Syntax
````
typedef struct _IO_RESOURCE_DESCRIPTOR {
  UCHAR  Option;
  UCHAR  Type;
  UCHAR  ShareDisposition;
  UCHAR  Spare1;
  USHORT Flags;
  USHORT Spare2;
  union {
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } port;
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory;
    struct {
      ULONG             MinimumVector;
      ULONG             MaximumVector;
#if defined(NT_PROCESSOR_GROUPS)
      IRQ_DEVICE_POLICY AffinityPolicy;
      USHORT            Group;
#else 
      IRQ_DEVICE_POLICY AffinityPolicy;
#endif 
      IRQ_PRIORITY      PriorityPolicy;
      KAFFINITY         TargetedProcessors;
    } Interrupt;
    struct {
      ULONG MinimumChannel;
      ULONG MaximumChannel;
    } Dma;
    struct {
      ULONG RequestLine;
      ULONG Reserved;
      ULONG Channel;
      ULONG TransferWidth;
    } DmaV3;
    struct {
      ULONG            Length;
      ULONG            Alignment;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Generic;
    struct {
      ULONG Data[3];
    } DevicePrivate;
    struct {
      ULONG Length;
      ULONG MinBusNumber;
      ULONG MaxBusNumber;
      ULONG Reserved;
    } BusNumber;
    struct {
      ULONG Priority;
      ULONG Reserved1;
      ULONG Reserved2;
    } ConfigData;
    struct {
      ULONG            Length40;
      ULONG            Alignment40;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory40;
    struct {
      ULONG            Length48;
      ULONG            Alignment48;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
    } Memory48;
    struct {
      ULONG            Length64;
      ULONG            Alignment64;
      PHYSICAL_ADDRESS MinimumAddress;
      PHYSICAL_ADDRESS MaximumAddress;
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
} IO_RESOURCE_DESCRIPTOR, *PIO_RESOURCE_DESCRIPTOR;
````

## Members


`Flags`

Contains bit flags that are specific to the resource type. The following table shows the flags that are valid if <b>Type</b> = <b>CmResourceTypeInterrupt.</b>

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_LEVEL_SENSITIVE"></a><a id="cm_resource_interrupt_level_sensitive"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_LEVEL_SENSITIVE</b></dt>
</dl>
</td>
<td width="60%">
The IRQ line is level-triggered. (These IRQs are usually sharable.)

</td>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_LATCHED"></a><a id="cm_resource_interrupt_latched"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_LATCHED</b></dt>
</dl>
</td>
<td width="60%">
The IRQ line is edge-triggered.

</td>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_MESSAGE"></a><a id="cm_resource_interrupt_message"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_MESSAGE</b></dt>
</dl>
</td>
<td width="60%">
If this flag is set, the interrupt is a message-signaled interrupt. Otherwise, the interrupt is a line-based interrupt. This flag can be set starting with Windows Vista.

</td>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_POLICY_INCLUDED"></a><a id="cm_resource_interrupt_policy_included"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_POLICY_INCLUDED</b></dt>
</dl>
</td>
<td width="60%">
If this flag is set, the u.Interrupt member includes data that describes the device's interrupt policy. This flag can be set starting with Windows Vista.

</td>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_SECONDARY_INTERRUPT"></a><a id="cm_resource_interrupt_secondary_interrupt"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_SECONDARY_INTERRUPT</b></dt>
</dl>
</td>
<td width="60%">
The interrupt is a secondary interrupt. This flag can be set starting with Windows 8. For more information about secondary interrupts, see <a href="https://msdn.microsoft.com/0F56AD4C-E0BF-49F1-AB67-0107D08DEF9F">GPIO Interrupts</a>.

</td>
</tr>
<tr>
<td width="40%"><a id="CM_RESOURCE_INTERRUPT_WAKE_HINT"></a><a id="cm_resource_interrupt_wake_hint"></a><dl>
<dt><b>CM_RESOURCE_INTERRUPT_WAKE_HINT</b></dt>
</dl>
</td>
<td width="60%">
The interrupt is capable of waking the operating system from a low-power idle state or a system sleep state. This flag can be set starting with Windows 8. For more information about wake capabilities, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544239">Enabling Device Wake-Up</a>.

</td>
</tr>
</table>
 

For a list of valid flags for other resource types, see the description of the <b>Flags</b> member of the <a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.

`Option`

Specifies whether this resource description is required, preferred, or alternative. One of the following values must be used:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0"></a><dl>
<dt><b>0</b></dt>
</dl>
</td>
<td width="60%">
The specified resource range is required, unless alternative ranges are also specified.

</td>
</tr>
<tr>
<td width="40%"><a id="IO_RESOURCE_PREFERRED"></a><a id="io_resource_preferred"></a><dl>
<dt><b>IO_RESOURCE_PREFERRED</b></dt>
</dl>
</td>
<td width="60%">
The specified resource range is preferred to any alternative ranges.

</td>
</tr>
<tr>
<td width="40%"><a id="IO_RESOURCE_ALTERNATIVE"></a><a id="io_resource_alternative"></a><dl>
<dt><b>IO_RESOURCE_ALTERNATIVE</b></dt>
</dl>
</td>
<td width="60%">
The specified resource range is an alternative to the range preceding it. For example, if one <b>IO_RESOURCE_DESCRIPTOR</b> structure specifies IRQ 5, with IO_RESOURCE_PREFERRED set, and the next structure specifies IRQ 3, with IO_RESOURCE_ALTERNATIVE set, the PnP manager assigns IRQ 3 to the device only if IRQ 5 is unavailable. (Multiple alternatives can be specified for each resource. Both IO_RESOURCE_ALTERNATIVE and IO_RESOURCE_PREFERRED can be set, indicating a preferred alternative.)

</td>
</tr>
<tr>
<td width="40%"><a id="IO_RESOURCE_DEFAULT"></a><a id="io_resource_default"></a><dl>
<dt><b>IO_RESOURCE_DEFAULT</b></dt>
</dl>
</td>
<td width="60%">
Not used.

</td>
</tr>
</table>

`ShareDisposition`

Indicates whether the described resource can be shared. For a list of valid values, see the <b>ShareDisposition</b> member of the <a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.

`Spare1`



`Spare2`



`Type`

Identifies the resource type. For a list of valid values, see the <b>Type</b> member of the <a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.

`u`

#### port

Specifies a range of I/O port addresses, using the following members.

Drivers for Windows Vista and later versions of the Windows operating system must use <a href="..\wdm\nf-wdm-rtliodecodememioresource.md">RtlIoDecodeMemIoResource</a> and <a href="..\wdm\nf-wdm-rtlioencodememioresource.md">RtlIoEncodeMemIoResource</a> to read and update this member, rather than updating it directly.



##### Length

The length, in bytes, of the range of assignable I/O port addresses.



##### Alignment

The alignment, in bytes, that the assigned starting address must adhere to. The assigned starting address must be an integer multiple of <i>Alignment</i>. 



##### MinimumAddress

The minimum bus-relative I/O port address that can be assigned to the device.



##### MaximumAddress

The maximum bus-relative I/O port address that can be assigned to the device.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wdm\ns-wdm-_cm_partial_resource_descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>



<a href="..\wdm\ns-wdm-_io_resource_list.md">IO_RESOURCE_LIST</a>



<a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a>



<a href="..\wdm\ns-wdm-_io_resource_requirements_list.md">IO_RESOURCE_REQUIREMENTS_LIST</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IO_RESOURCE_DESCRIPTOR structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>