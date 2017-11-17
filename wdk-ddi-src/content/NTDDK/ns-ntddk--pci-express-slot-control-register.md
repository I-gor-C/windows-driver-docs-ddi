---
UID: NS.ntddk._PCI_EXPRESS_SLOT_CONTROL_REGISTER
title: PCI_EXPRESS_SLOT_CONTROL_REGISTER
author: windows-driver-content
description: The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure.
old-location: pci\pci_express_slot_control_register.htm
ms.assetid: 4755f4c3-305e-41a5-afdf-eda8e8e81b74
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
req.alt-api: PCI_EXPRESS_SLOT_CONTROL_REGISTER
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
ms.keywords: PCI_EXPRESS_SLOT_CONTROL_REGISTER, PCI_EXPRESS_SLOT_CONTROL_REGISTER, *PPCI_EXPRESS_SLOT_CONTROL_REGISTER
req.iface: 
---

# PCI_EXPRESS_SLOT_CONTROL_REGISTER structure



## -description
<p>The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure.</p>


## -syntax

````
typedef union _PCI_EXPRESS_SLOT_CONTROL_REGISTER {
  struct {
    USHORT AttentionButtonEnable  :1;
    USHORT PowerFaultDetectEnable  :1;
    USHORT MRLSensorEnable;
    USHORT PresenceDetectEnable  :1;
    USHORT CommandCompletedEnable  :1;
    USHORT HotPlugInterruptEnable  :1;
    USHORT AttentionIndicatorControl  :2;
    USHORT PowerIndicatorControl  :2;
    USHORT PowerControllerControl  :1;
    USHORT ElectromechanicalLockControl  :1;
    USHORT DataLinkStateChangeEnable  :1;
    USHORT Rsvd  :3;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_SLOT_CONTROL_REGISTER, *PPCI_EXPRESS_SLOT_CONTROL_REGISTER;
````


## -struct-fields
<dl>

### -field <b>AttentionButtonEnable</b>

<dd>
<p>A single bit that indicates that the attention button for the slot is enabled to generate events.</p>
</dd>

### -field <b>PowerFaultDetectEnable</b>

<dd>
<p>A single bit that indicates that power fault detection for the slot is enabled to generate events.</p>
</dd>

### -field <b>MRLSensorEnable</b>

<dd>
<p>A single bit that indicates that the manually operated retention latch (MRL) sensor for the slot is enabled to generate events.</p>
</dd>

### -field <b>PresenceDetectEnable</b>

<dd>
<p>A single bit that indicates that card presence detection for the slot is enabled to generate events.</p>
</dd>

### -field <b>CommandCompletedEnable</b>

<dd>
<p>A single bit that indicates that notification is enabled for the slot when an issued command is completed by the hot-plug controller.</p>
</dd>

### -field <b>HotPlugInterruptEnable</b>

<dd>
<p>A single bit that indicates that interrupts for the slot are enabled for hot-plug events.</p>
</dd>

### -field <b>AttentionIndicatorControl</b>

<dd>
<p>The state of the slot's attention indicator. Possible values are:</p>
<p></p>
<dl>

### -field <a id="IndicatorOn"></a><a id="indicatoron"></a><a id="INDICATORON"></a><b>IndicatorOn</b>

<dd>
<p>The indicator is on.</p>
</dd>

### -field <a id="IndicatorBlink"></a><a id="indicatorblink"></a><a id="INDICATORBLINK"></a><b>IndicatorBlink</b>

<dd>
<p>The indicator is blinking.</p>
</dd>

### -field <a id="IndicatorOff"></a><a id="indicatoroff"></a><a id="INDICATOROFF"></a><b>IndicatorOff</b>

<dd>
<p>The indicator is off.</p>
</dd>
</dl>
</dd>

### -field <b>PowerIndicatorControl</b>

<dd>
<p>The state of the slot's power indicator. Possible values are:</p>
<p></p>
<dl>

### -field <a id="IndicatorOn"></a><a id="indicatoron"></a><a id="INDICATORON"></a><b>IndicatorOn</b>

<dd>
<p>The indicator is on.</p>
</dd>

### -field <a id="IndicatorBlink"></a><a id="indicatorblink"></a><a id="INDICATORBLINK"></a><b>IndicatorBlink</b>

<dd>
<p>The indicator is blinking.</p>
</dd>

### -field <a id="IndicatorOff"></a><a id="indicatoroff"></a><a id="INDICATOROFF"></a><b>IndicatorOff</b>

<dd>
<p>The indicator is off.</p>
</dd>
</dl>
</dd>

### -field <b>PowerControllerControl</b>

<dd>
<p>The state of the slot's power controller. Possible values are:</p>
<p></p>
<dl>

### -field <a id="PowerOn"></a><a id="poweron"></a><a id="POWERON"></a><b>PowerOn</b>

<dd>
<p>The power is on.</p>
</dd>

### -field <a id="PowerOff"></a><a id="poweroff"></a><a id="POWEROFF"></a><b>PowerOff</b>

<dd>
<p>The power is off.</p>
</dd>
</dl>
</dd>

### -field <b>ElectromechanicalLockControl</b>

<dd>
<p>This member always contains zero.</p>
</dd>

### -field <b>DataLinkStateChangeEnable</b>

<dd>
<p>A single bit that indicates that notification is enabled for the slot for changes to the data link layer active bit of the link status register of the PCIe capability structure.</p>
</dd>

### -field <b>Rsvd</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the PCI_EXPRESS_SLOT_CONTROL_REGISTER structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_SLOT_CONTROL_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_SLOT_CONTROL_REGISTER union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
