---
UID: NS.ntddk._PCI_EXPRESS_SLOT_STATUS_REGISTER
title: PCI_EXPRESS_SLOT_STATUS_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_SLOT_STATUS_REGISTER structure describes a PCI Express (PCIe) slot status register of a PCIe capability structure.
old-location: pci\pci_express_slot_status_register.htm
ms.assetid: 1012abf2-a73b-49d9-8017-b0b1a1c7fbcd
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
req.alt-api: PCI_EXPRESS_SLOT_STATUS_REGISTER
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
ms.keywords: PCI_EXPRESS_SLOT_STATUS_REGISTER, PCI_EXPRESS_SLOT_STATUS_REGISTER, *PPCI_EXPRESS_SLOT_STATUS_REGISTER
req.iface: 
---

# PCI_EXPRESS_SLOT_STATUS_REGISTER structure



## -description
<p>The PCI_EXPRESS_SLOT_STATUS_REGISTER structure describes a PCI Express (PCIe) slot status register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_SLOT_STATUS_REGISTER {
  struct {
    USHORT AttentionButtonPressed  :1;
    USHORT PowerFaultDetected  :1;
    USHORT MRLSensorChanged  :1;
    USHORT PresenceDetectChanged  :1;
    USHORT CommandCompleted  :1;
    USHORT MRLSensorState  :1;
    USHORT PresenceDetectState  :1;
    USHORT ElectromechanicalLockEngaged  :1;
    USHORT DataLinkStateChanged  :1;
    USHORT Rsvd  :7;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_SLOT_STATUS_REGISTER, *PPCI_EXPRESS_SLOT_STATUS_REGISTER;
````


## -struct-fields
<dl>

### -field <b>AttentionButtonPressed</b>

<dd>
<p>A single bit that indicates that the attention button for the slot is being pressed.</p>
</dd>

### -field <b>PowerFaultDetected</b>

<dd>
<p>A single bit that indicates that a power fault at the slot has been detected.</p>
</dd>

### -field <b>MRLSensorChanged</b>

<dd>
<p>A single bit that indicates that the state of the slot's manually operated retention latch (MRL) sensor has changed.</p>
</dd>

### -field <b>PresenceDetectChanged</b>

<dd>
<p>A single bit that indicates that the card presence detection state for the slot has changed.</p>
</dd>

### -field <b>CommandCompleted</b>

<dd>
<p>A single bit that indicates that a command has been completed by the slot's hot-plug controller.</p>
</dd>

### -field <b>MRLSensorState</b>

<dd>
<p>The slot's manually operated retention latch (MRL) sensor state. Possible values are:</p>
<p></p>
<dl>

### -field <a id="MRLClosed"></a><a id="mrlclosed"></a><a id="MRLCLOSED"></a><b>MRLClosed</b>

<dd>
<p>The MRL is closed.</p>
</dd>

### -field <a id="MRLOpen"></a><a id="mrlopen"></a><a id="MRLOPEN"></a><b>MRLOpen</b>

<dd>
<p>The MRL is open.</p>
</dd>
</dl>
</dd>

### -field <b>PresenceDetectState</b>

<dd>
<p>The slot's card presence detection state. Possible values are:</p>
<p></p>
<dl>

### -field <a id="SlotEmpty"></a><a id="slotempty"></a><a id="SLOTEMPTY"></a><b>SlotEmpty</b>

<dd>
<p>The slot is empty.</p>
</dd>

### -field <a id="CardPresent"></a><a id="cardpresent"></a><a id="CARDPRESENT"></a><b>CardPresent</b>

<dd>
<p>A card is present in the slot.</p>
</dd>
</dl>
</dd>

### -field <b>ElectromechanicalLockEngaged</b>

<dd>
<p>A single bit that indicates if the slot's electromechanical interlock is engaged.</p>
</dd>

### -field <b>DataLinkStateChanged</b>

<dd>
<p>A single bit that indicates that the data link layer active bit of the PCIe link status register of the PCIe capability structure has changed.</p>
</dd>

### -field <b>Rsvd</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the PCI_EXPRESS_SLOT_STATUS_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_SLOT_STATUS_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_SLOT_STATUS_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_SLOT_STATUS_REGISTER union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
