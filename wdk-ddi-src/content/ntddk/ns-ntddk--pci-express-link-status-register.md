---
UID: NS.ntddk._PCI_EXPRESS_LINK_STATUS_REGISTER
title: PCI_EXPRESS_LINK_STATUS_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure.
old-location: pci\pci_express_link_status_register.htm
old-project: PCI
ms.assetid: c3431e89-4a47-44e6-98d8-eae444ea1915
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_EXPRESS_LINK_STATUS_REGISTER, PCI_EXPRESS_LINK_STATUS_REGISTER, *PPCI_EXPRESS_LINK_STATUS_REGISTER
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
req.alt-api: PCI_EXPRESS_LINK_STATUS_REGISTER
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

# PCI_EXPRESS_LINK_STATUS_REGISTER structure



## -description
<p>The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_LINK_STATUS_REGISTER {
  struct {
    USHORT LinkSpeed  :4;
    USHORT LinkWidth  :6;
    USHORT Undefined  :1;
    USHORT LinkTraining  :1;
    USHORT SlotClockConfig  :1;
    USHORT DataLinkLayerActive  :1;
    USHORT Rsvd  :2;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_LINK_STATUS_REGISTER, *PPCI_EXPRESS_LINK_STATUS_REGISTER;
````


## -struct-fields
<dl>

### -field LinkSpeed

<dd>
<p>The negotiated link speed of the PCIe link.  Possible values are:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td><b>1</b></td>
<td>2.5 gigabits per second.</td>
</tr>
<tr>
<td><b>2</b></td>
<td>5.0 gigabits per second.</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved.</td>
</tr>
</table>
<p> </p>
</dd>

### -field LinkWidth

<dd>
<p>The negotiated link width (number of lanes) of the PCIe link. Possible values are:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td><b>1</b></td>
<td>x1 (1 lane)</td>
</tr>
<tr>
<td><b>2</b></td>
<td>x2 (2 lanes)</td>
</tr>
<tr>
<td><b>4</b></td>
<td>x4 (4 lanes)</td>
</tr>
<tr>
<td><b>8</b></td>
<td>x8 (8 lanes)</td>
</tr>
<tr>
<td><b>12</b></td>
<td>x12 (12 lanes)</td>
</tr>
<tr>
<td><b>16</b></td>
<td>x16 (16 lanes)</td>
</tr>
<tr>
<td><b>32</b></td>
<td>x32 (32 lanes)</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved.</td>
</tr>
</table>
<p> </p>
</dd>

### -field Undefined

<dd>
<p>Reserved. Device drivers and other system software should ignore any value read from this bit.</p>
</dd>

### -field LinkTraining

<dd>
<p>A single bit that indicates that the link is in the configuration or recovery state, or that a 1 was written to the retrain link bit of the PCIe link control register and the training has not yet begun. This member is not applicable to endpoint devices and upstream ports of switches.</p>
</dd>

### -field SlotClockConfig

<dd>
<p>A single bit that indicates that the component uses the same physical reference clock that the hardware platform provides on the PCIe slot connector. If this bit is clear, the component uses an independent clock irrespective of the presence of a reference clock on the PCIe slot connector.</p>
</dd>

### -field DataLinkLayerActive

<dd>
<p>A single bit that indicates that the data link control and management state machine is in the data link active state.</p>
</dd>

### -field Rsvd

<dd>
<p>Reserved.</p>
</dd>

### -field AsUSHORT

<dd>
<p>A USHORT representation of the contents of the PCI_EXPRESS_LINK_STATUS_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_LINK_STATUS_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_LINK_STATUS_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_LINK_STATUS_REGISTER union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
