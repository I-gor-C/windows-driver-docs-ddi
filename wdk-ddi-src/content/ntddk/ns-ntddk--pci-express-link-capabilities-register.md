---
UID: NS.ntddk._PCI_EXPRESS_LINK_CAPABILITIES_REGISTER
title: PCI_EXPRESS_LINK_CAPABILITIES_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) link capabilities register of a PCIe capability structure.
old-location: pci\pci_express_link_capabilities_register.htm
old-project: PCI
ms.assetid: d49d1deb-cb98-4dc0-9ec5-7015b765c9e4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_EXPRESS_LINK_CAPABILITIES_REGISTER, PCI_EXPRESS_LINK_CAPABILITIES_REGISTER, *PPCI_EXPRESS_LINK_CAPABILITIES_REGISTER
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
req.alt-api: PCI_EXPRESS_LINK_CAPABILITIES_REGISTER
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

# PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure



## -description
<p>The PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) link capabilities register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_LINK_CAPABILITIES_REGISTER {
  struct {
    ULONG MaximumLinkSpeed  :4;
    ULONG MaximumLinkWidth  :6;
    ULONG ActiveStatePMSupport  :2;
    ULONG L0sExitLatency  :3;
    ULONG L1ExitLatency  :3;
    ULONG ClockPowerManagement  :1;
    ULONG SurpriseDownErrorReportingCapable  :1;
    ULONG DataLinkLayerActiveReportingCapable  :1;
    ULONG Rsvd  :3;
    ULONG PortNumber  :8;
  };
  ULONG  AsULONG;
} PCI_EXPRESS_LINK_CAPABILITIES_REGISTER, *PPCI_EXPRESS_LINK_CAPABILITIES_REGISTER;
````


## -struct-fields
<dl>

### -field MaximumLinkSpeed

<dd>
<p>The maximum link speed of the PCIe link. The only valid value is:</p>
<p></p>
<dl>

### -field 1

<dd>
<p>2.5 gigabits per second</p>
</dd>
</dl>
<p>All other values are reserved.</p>
</dd>

### -field MaximumLinkWidth

<dd>
<p>The maximum link width (number of lanes) implemented by the component. Possible values are:</p>
<p></p>
<dl>

### -field 1

<dd>
<p>x1 (1 lane)</p>
</dd>

### -field 2

<dd>
<p>x2 (2 lanes)</p>
</dd>

### -field 4

<dd>
<p>x4 (4 lanes)</p>
</dd>

### -field 8

<dd>
<p>x8 (8 lanes)</p>
</dd>

### -field 12

<dd>
<p>x12 (12 lanes)</p>
</dd>

### -field 16

<dd>
<p>x16 (16 lanes)</p>
</dd>

### -field 32

<dd>
<p>x32 (32 lanes)</p>
</dd>
</dl>
<p>All other values are reserved.</p>
</dd>

### -field ActiveStatePMSupport

<dd>
<p>The level of active state power management supported on the PCIe link. Possible values are:</p>
<p></p>
<dl>

### -field L0sEntrySupport

<dd>
<p>L0s is supported.</p>
</dd>

### -field L0sAndL1EntrySupport

<dd>
<p>L0s and L1 are supported.</p>
</dd>
</dl>
<p>All other values are reserved.</p>
</dd>

### -field L0sExitLatency

<dd>
<p>The L0s exit latency for the PCIe link. This value indicates the length of time this port requires to complete a transition from L0s to L0.</p>
<p></p>
<dl>

### -field L0s_Below64ns

<dd>
<p>Less than 64 nanoseconds</p>
</dd>

### -field L0s_64ns_128ns

<dd>
<p>64 nanoseconds to 128 nanoseconds</p>
</dd>

### -field L0s_128ns_256ns

<dd>
<p>128 nanoseconds to 256 nanoseconds</p>
</dd>

### -field L0s_256ns_512ns

<dd>
<p>256 nanoseconds to 512 nanoseconds</p>
</dd>

### -field L0s_512ns_1us

<dd>
<p>512 nanoseconds to 1 microsecond</p>
</dd>

### -field L0s_1us_2us

<dd>
<p>1 microsecond to 2 microseconds</p>
</dd>

### -field L0s_2us_4us

<dd>
<p>2 microseconds to 4 microseconds</p>
</dd>

### -field L0s_Above4us

<dd>
<p>More than 4 microseconds</p>
</dd>
</dl>
</dd>

### -field L1ExitLatency

<dd>
<p>The L1 exit latency for the PCIe link. This value indicates the length of time this port requires to complete a transition from L1 to L0.</p>
<p></p>
<dl>

### -field L1_Below1us

<dd>
<p>Less than 1 microsecond</p>
</dd>

### -field L1_1us_2us

<dd>
<p>1 microsecond to 2 microseconds</p>
</dd>

### -field L1_2us_4us

<dd>
<p>2 microseconds to 4 microseconds</p>
</dd>

### -field L1_4us_8us

<dd>
<p>4 microseconds to 8 microseconds</p>
</dd>

### -field L1_8us_16us

<dd>
<p>8 microseconds to 16 microseconds</p>
</dd>

### -field L1_16us_32us

<dd>
<p>16 microseconds to 32 microseconds</p>
</dd>

### -field L1_32us_64us

<dd>
<p>32 microseconds to 64 microseconds</p>
</dd>

### -field L1_Above64us

<dd>
<p>More than 64 microseconds</p>
</dd>
</dl>
<p>This value is ignored if the <b>ActiveStatePMSupport </b>member is not set to <b>L0sAndL1EntrySupport</b>.</p>
</dd>

### -field ClockPowerManagement

<dd>
<p>A single bit that indicates that the component supports clock power management.</p>
</dd>

### -field SurpriseDownErrorReportingCapable

<dd>
<p>A single bit that indicates that the component supports the optional capability of detecting and reporting a surprise-down error condition. This bit only applies to downstream ports.</p>
</dd>

### -field DataLinkLayerActiveReportingCapable

<dd>
<p>A single bit that indicates that the component supports the optional capability of reporting the data link active state of the data link control and management state machine. This bit only applies to downstream ports. Hot-plug capable downstream ports must support this capability.</p>
</dd>

### -field Rsvd

<dd>
<p>Reserved.</p>
</dd>

### -field PortNumber

<dd>
<p>The PCIe port number for the PCIe link.</p>
</dd>

### -field AsULONG

<dd>
<p>A ULONG representation of the contents of the PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_LINK_CAPABILITIES_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_LINK_CAPABILITIES_REGISTER union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
