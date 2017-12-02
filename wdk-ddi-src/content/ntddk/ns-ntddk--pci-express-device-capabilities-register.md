---
UID: NS.ntddk._PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
title: PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure.
old-location: pci\pci_express_device_capabilities_register.htm
old-project: PCI
ms.assetid: 895b49e5-181b-4312-ab1c-7f67c102b32f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, *PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
req.alt-loc: ntddk.h
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

# PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure



## -description
<p>The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER {
  struct {
    ULONG MaxPayloadSizeSupported  :3;
    ULONG PhantomFunctionsSupported  :2;
    ULONG ExtendedTagSupported  :1;
    ULONG L0sAcceptableLatency  :3;
    ULONG L1AcceptableLatency  :3;
    ULONG Undefined  :3;
    ULONG RoleBasedErrorReporting  :1;
    ULONG Rsvd1  :2;
    ULONG CapturedSlotPowerLimit  :8;
    ULONG CapturedSlotPowerLimitScale  :2;
    ULONG Rsvd2  :4;
  };
  ULONG  AsULONG;
} PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, *PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER;
````


## -struct-fields
<dl>

### -field MaxPayloadSizeSupported

<dd>
<p>The maximum payload size that is supported by the device. Possible values are:</p>
<p></p>
<dl>

### -field MaxPayload128Bytes

<dd>
<p>128 byte maximum payload size</p>
</dd>

### -field MaxPayload256Bytes

<dd>
<p>256 byte maximum payload size</p>
</dd>

### -field MaxPayload512Bytes

<dd>
<p>512 byte maximum payload size</p>
</dd>

### -field MaxPayload1024Bytes

<dd>
<p>1024 byte maximum payload size</p>
</dd>

### -field MaxPayload2048Bytes

<dd>
<p>2048 byte maximum payload size</p>
</dd>

### -field MaxPayload4096Bytes

<dd>
<p>4096 byte maximum payload size</p>
</dd>
</dl>
</dd>

### -field PhantomFunctionsSupported

<dd>
<p>A value that indicates the support of unused function numbers (phantom functions) to extend the number of outstanding transactions that are allowed for the device. Possible values are:</p>
<p></p>
<dl>

### -field 0

<dd>
<p>No function number bits are used for phantom functions. The device can implement functions for all eight function numbers.</p>
</dd>

### -field 1

<dd>
<p>The most significant bit in the function number is used for phantom functions. The device can implement functions for function numbers 0 to 3.</p>
</dd>

### -field 2

<dd>
<p>The two most significant bits in the function number are used for phantom functions. The device can implement functions for function numbers 0 and 1.</p>
</dd>

### -field 3

<dd>
<p>All three bits in the function number are used for phantom functions. The device implements only a single function for function number 0.</p>
</dd>
</dl>
</dd>

### -field ExtendedTagSupported

<dd>
<p>A single bit that specifies the maximum supported size of the Tag field in a PCIe transaction descriptor when the device is a requester. If this bit is clear, a 5-bit Tag field is supported. If this bit is set, an 8-bit Tag field is supported.</p>
</dd>

### -field L0sAcceptableLatency

<dd>
<p>The maximum acceptable total latency that the device can withstand due to a transition from the L0s state to the L0 state. Possible values are:</p>
<p></p>
<dl>

### -field L0s_Below64ns

<dd>
<p>64 nanoseconds</p>
</dd>

### -field L0s_64ns_128ns

<dd>
<p>128 nanoseconds</p>
</dd>

### -field L0s_128ns_256ns

<dd>
<p>256 nanoseconds</p>
</dd>

### -field L0s_256ns_512ns

<dd>
<p>512 nanoseconds</p>
</dd>

### -field L0s_512ns_1us

<dd>
<p>1 microsecond</p>
</dd>

### -field L0s_1us_2us

<dd>
<p>2 microseconds</p>
</dd>

### -field L0s_2us_4us

<dd>
<p>4 microseconds</p>
</dd>

### -field L0s_Above4us

<dd>
<p>No limit</p>
</dd>
</dl>
</dd>

### -field L1AcceptableLatency

<dd>
<p>The maximum acceptable total latency that the device can withstand due to a transition from the L1 state to the L0 state. Possible values are:</p>
<p></p>
<dl>

### -field L1_Below1us

<dd>
<p>1 microsecond</p>
</dd>

### -field L1_1us_2us

<dd>
<p>2 microseconds</p>
</dd>

### -field L1_2us_4us

<dd>
<p>4 microseconds</p>
</dd>

### -field L1_4us_8us

<dd>
<p>8 microseconds</p>
</dd>

### -field L1_8us_16us

<dd>
<p>16 microseconds</p>
</dd>

### -field L1_16us_32us

<dd>
<p>32 microseconds</p>
</dd>

### -field L1_32us_64us

<dd>
<p>64 microseconds</p>
</dd>

### -field L1_Above64us

<dd>
<p>No limit</p>
</dd>
</dl>
</dd>

### -field Undefined

<dd>
<p>Reserved.</p>
</dd>

### -field RoleBasedErrorReporting

<dd>
<p>A single bit that indicates that the device implements role-based error reporting.</p>
</dd>

### -field Rsvd1

<dd>
<p>Reserved.</p>
</dd>

### -field CapturedSlotPowerLimit

<dd>
<p>The maximum amount of power that can be supplied by the slot. This value is used in combination with the value of the <b>CapturedSlotPowerLimitScale</b> member to compute the power in watts.</p>
</dd>

### -field CapturedSlotPowerLimitScale

<dd>
<p>The scale used for the value contained in the <b>CapturedSlotPowerLimit</b> member to compute the maximum power, in watts, that can be supplied by the slot. Possible values are:</p>
<p></p>
<dl>

### -field 0

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 1.0.</p>
</dd>

### -field 1

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.1.</p>
</dd>

### -field 2

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.01.</p>
</dd>

### -field 3

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.001.</p>
</dd>
</dl>
</dd>

### -field Rsvd2

<dd>
<p>Reserved.</p>
</dd>

### -field AsULONG

<dd>
<p>A ULONG representation of the contents of the PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
