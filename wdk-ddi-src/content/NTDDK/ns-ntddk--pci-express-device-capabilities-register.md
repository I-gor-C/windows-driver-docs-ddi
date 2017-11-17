---
UID: NS.ntddk._PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
title: PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure.
old-location: pci\pci_express_device_capabilities_register.htm
ms.assetid: 895b49e5-181b-4312-ab1c-7f67c102b32f
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: PCI
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
ms.keywords: PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, *PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
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

### -field <b>MaxPayloadSizeSupported</b>

<dd>
<p>The maximum payload size that is supported by the device. Possible values are:</p>
<p></p>
<dl>

### -field <a id="MaxPayload128Bytes"></a><a id="maxpayload128bytes"></a><a id="MAXPAYLOAD128BYTES"></a><b>MaxPayload128Bytes</b>

<dd>
<p>128 byte maximum payload size</p>
</dd>

### -field <a id="MaxPayload256Bytes"></a><a id="maxpayload256bytes"></a><a id="MAXPAYLOAD256BYTES"></a><b>MaxPayload256Bytes</b>

<dd>
<p>256 byte maximum payload size</p>
</dd>

### -field <a id="MaxPayload512Bytes"></a><a id="maxpayload512bytes"></a><a id="MAXPAYLOAD512BYTES"></a><b>MaxPayload512Bytes</b>

<dd>
<p>512 byte maximum payload size</p>
</dd>

### -field <a id="MaxPayload1024Bytes"></a><a id="maxpayload1024bytes"></a><a id="MAXPAYLOAD1024BYTES"></a><b>MaxPayload1024Bytes</b>

<dd>
<p>1024 byte maximum payload size</p>
</dd>

### -field <a id="MaxPayload2048Bytes"></a><a id="maxpayload2048bytes"></a><a id="MAXPAYLOAD2048BYTES"></a><b>MaxPayload2048Bytes</b>

<dd>
<p>2048 byte maximum payload size</p>
</dd>

### -field <a id="MaxPayload4096Bytes"></a><a id="maxpayload4096bytes"></a><a id="MAXPAYLOAD4096BYTES"></a><b>MaxPayload4096Bytes</b>

<dd>
<p>4096 byte maximum payload size</p>
</dd>
</dl>
</dd>

### -field <b>PhantomFunctionsSupported</b>

<dd>
<p>A value that indicates the support of unused function numbers (phantom functions) to extend the number of outstanding transactions that are allowed for the device. Possible values are:</p>
<p></p>
<dl>

### -field <a id="0"></a><b>0</b>

<dd>
<p>No function number bits are used for phantom functions. The device can implement functions for all eight function numbers.</p>
</dd>

### -field <a id="1"></a><b>1</b>

<dd>
<p>The most significant bit in the function number is used for phantom functions. The device can implement functions for function numbers 0 to 3.</p>
</dd>

### -field <a id="2"></a><b>2</b>

<dd>
<p>The two most significant bits in the function number are used for phantom functions. The device can implement functions for function numbers 0 and 1.</p>
</dd>

### -field <a id="3"></a><b>3</b>

<dd>
<p>All three bits in the function number are used for phantom functions. The device implements only a single function for function number 0.</p>
</dd>
</dl>
</dd>

### -field <b>ExtendedTagSupported</b>

<dd>
<p>A single bit that specifies the maximum supported size of the Tag field in a PCIe transaction descriptor when the device is a requester. If this bit is clear, a 5-bit Tag field is supported. If this bit is set, an 8-bit Tag field is supported.</p>
</dd>

### -field <b>L0sAcceptableLatency</b>

<dd>
<p>The maximum acceptable total latency that the device can withstand due to a transition from the L0s state to the L0 state. Possible values are:</p>
<p></p>
<dl>

### -field <a id="L0s_Below64ns"></a><a id="l0s_below64ns"></a><a id="L0S_BELOW64NS"></a><b>L0s_Below64ns</b>

<dd>
<p>64 nanoseconds</p>
</dd>

### -field <a id="L0s_64ns_128ns"></a><a id="l0s_64ns_128ns"></a><a id="L0S_64NS_128NS"></a><b>L0s_64ns_128ns</b>

<dd>
<p>128 nanoseconds</p>
</dd>

### -field <a id="L0s_128ns_256ns"></a><a id="l0s_128ns_256ns"></a><a id="L0S_128NS_256NS"></a><b>L0s_128ns_256ns</b>

<dd>
<p>256 nanoseconds</p>
</dd>

### -field <a id="L0s_256ns_512ns"></a><a id="l0s_256ns_512ns"></a><a id="L0S_256NS_512NS"></a><b>L0s_256ns_512ns</b>

<dd>
<p>512 nanoseconds</p>
</dd>

### -field <a id="L0s_512ns_1us"></a><a id="l0s_512ns_1us"></a><a id="L0S_512NS_1US"></a><b>L0s_512ns_1us</b>

<dd>
<p>1 microsecond</p>
</dd>

### -field <a id="L0s_1us_2us"></a><a id="l0s_1us_2us"></a><a id="L0S_1US_2US"></a><b>L0s_1us_2us</b>

<dd>
<p>2 microseconds</p>
</dd>

### -field <a id="L0s_2us_4us"></a><a id="l0s_2us_4us"></a><a id="L0S_2US_4US"></a><b>L0s_2us_4us</b>

<dd>
<p>4 microseconds</p>
</dd>

### -field <a id="L0s_Above4us"></a><a id="l0s_above4us"></a><a id="L0S_ABOVE4US"></a><b>L0s_Above4us</b>

<dd>
<p>No limit</p>
</dd>
</dl>
</dd>

### -field <b>L1AcceptableLatency</b>

<dd>
<p>The maximum acceptable total latency that the device can withstand due to a transition from the L1 state to the L0 state. Possible values are:</p>
<p></p>
<dl>

### -field <a id="L1_Below1us"></a><a id="l1_below1us"></a><a id="L1_BELOW1US"></a><b>L1_Below1us</b>

<dd>
<p>1 microsecond</p>
</dd>

### -field <a id="L1_1us_2us"></a><a id="l1_1us_2us"></a><a id="L1_1US_2US"></a><b>L1_1us_2us</b>

<dd>
<p>2 microseconds</p>
</dd>

### -field <a id="L1_2us_4us"></a><a id="l1_2us_4us"></a><a id="L1_2US_4US"></a><b>L1_2us_4us</b>

<dd>
<p>4 microseconds</p>
</dd>

### -field <a id="L1_4us_8us"></a><a id="l1_4us_8us"></a><a id="L1_4US_8US"></a><b>L1_4us_8us</b>

<dd>
<p>8 microseconds</p>
</dd>

### -field <a id="L1_8us_16us"></a><a id="l1_8us_16us"></a><a id="L1_8US_16US"></a><b>L1_8us_16us</b>

<dd>
<p>16 microseconds</p>
</dd>

### -field <a id="L1_16us_32us"></a><a id="l1_16us_32us"></a><a id="L1_16US_32US"></a><b>L1_16us_32us</b>

<dd>
<p>32 microseconds</p>
</dd>

### -field <a id="L1_32us_64us"></a><a id="l1_32us_64us"></a><a id="L1_32US_64US"></a><b>L1_32us_64us</b>

<dd>
<p>64 microseconds</p>
</dd>

### -field <a id="L1_Above64us"></a><a id="l1_above64us"></a><a id="L1_ABOVE64US"></a><b>L1_Above64us</b>

<dd>
<p>No limit</p>
</dd>
</dl>
</dd>

### -field <b>Undefined</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>RoleBasedErrorReporting</b>

<dd>
<p>A single bit that indicates that the device implements role-based error reporting.</p>
</dd>

### -field <b>Rsvd1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>CapturedSlotPowerLimit</b>

<dd>
<p>The maximum amount of power that can be supplied by the slot. This value is used in combination with the value of the <b>CapturedSlotPowerLimitScale</b> member to compute the power in watts.</p>
</dd>

### -field <b>CapturedSlotPowerLimitScale</b>

<dd>
<p>The scale used for the value contained in the <b>CapturedSlotPowerLimit</b> member to compute the maximum power, in watts, that can be supplied by the slot. Possible values are:</p>
<p></p>
<dl>

### -field <a id="0"></a><b>0</b>

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 1.0.</p>
</dd>

### -field <a id="1"></a><b>1</b>

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.1.</p>
</dd>

### -field <a id="2"></a><b>2</b>

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.01.</p>
</dd>

### -field <a id="3"></a><b>3</b>

<dd>
<p>Multiply the value in the <b>CapturedSlotPowerLimit</b> member by 0.001.</p>
</dd>
</dl>
</dd>

### -field <b>Rsvd2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>AsULONG</b>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
