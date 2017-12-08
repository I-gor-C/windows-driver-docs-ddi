---
UID: NS.ntddk._PCI_EXPRESS_CAPABILITIES_REGISTER
title: PCI_EXPRESS_CAPABILITIES_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) capabilities register of a PCIe capability structure.
old-location: pci\pci_express_capabilities_register.htm
old-project: PCI
ms.assetid: aae9218e-e52b-4a72-9d96-d648ff6d2f5d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_EXPRESS_CAPABILITIES_REGISTER, PCI_EXPRESS_CAPABILITIES_REGISTER, *PPCI_EXPRESS_CAPABILITIES_REGISTER
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
req.alt-api: PCI_EXPRESS_CAPABILITIES_REGISTER
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

# PCI_EXPRESS_CAPABILITIES_REGISTER structure



## -description
<p>The PCI_EXPRESS_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) capabilities register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_CAPABILITIES_REGISTER {
  struct {
    USHORT CapabilityVersion  :4;
    USHORT DeviceType  :4;
    USHORT SlotImplemented  :1;
    USHORT InterruptMessageNumber  :5;
    USHORT Rsvd  :2;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_CAPABILITIES_REGISTER, *PPCI_EXPRESS_CAPABILITIES_REGISTER;
````


## -struct-fields
<dl>

### -field CapabilityVersion

<dd>
<p>The version number of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure that contains the PCI_EXPRESS_CAPABILITIES_REGISTER structure.</p>
</dd>

### -field DeviceType

<dd>
<p>The type of PCIe logical device. Possible values are:</p>
<p></p>
<dl>

### -field PciExpressEndpoint

<dd>
<p>A PCIe endpoint device.</p>
</dd>

### -field PciExpressLegacyEndpoint

<dd>
<p>A legacy PCIe endpoint device.</p>
</dd>

### -field PciExpressRootPort

<dd>
<p>A root port of a PCIe root complex.</p>
</dd>

### -field PciExpressUpstreamSwitchPort

<dd>
<p>An upstream port of a PCIe switch.</p>
</dd>

### -field PciExpressDownstreamSwitchPort

<dd>
<p>A downstream port of a PCIe switch.</p>
</dd>

### -field PciExpressToPciXBridge

<dd>
<p>A PCIe-to-PCI or PCI-X bridge.</p>
</dd>

### -field PciXToExpressBridge

<dd>
<p>A PCI- or PCI-X-to PCIe bridge.</p>
</dd>

### -field PciExpressRootComplexIntegratedEndpoint

<dd>
<p>A PCIe endpoint device that is integrated into the root complex.</p>
</dd>

### -field PciExpressRootComplexEventCollector

<dd>
<p>A PCIe root complex event collector.</p>
</dd>
</dl>
</dd>

### -field SlotImplemented

<dd>
<p>A single bit that indicates that the PCIe link associated with this port is connected to a physical PCIe slot. This member is valid only if the <b>DeviceType</b> member is set to <b>PciExpressRootPort</b> or <b>PciExpressDownstreamSwitchPort</b>.</p>
</dd>

### -field InterruptMessageNumber

<dd>
<p>The MSI or MSI-X vector that is used for interrupt messages that are generated in association with the status bits in either the slot status register or the root status register of the PCIe capability structure.</p>
</dd>

### -field Rsvd

<dd>
<p>Reserved.</p>
</dd>

### -field AsUSHORT

<dd>
<p>A USHORT representation of the contents of the PCI_EXPRESS_CAPABILITIES_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_CAPABILITIES_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_CAPABILITIES_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_CAPABILITIES_REGISTER union%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
