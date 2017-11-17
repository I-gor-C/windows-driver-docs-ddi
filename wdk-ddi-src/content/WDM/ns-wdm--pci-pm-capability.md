---
UID: NS.wdm._PCI_PM_CAPABILITY
title: PCI_PM_CAPABILITY
author: windows-driver-content
description: The PCI_PM_CAPABILITY structure reports the power management capabilities of the device.
old-location: pci\pci_pm_capability.htm
ms.assetid: 829d4df0-2dc2-4a1f-9606-3d5f25624252
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: PCI
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_PM_CAPABILITY
req.alt-loc: wdm.h
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
ms.keywords: PCI_PM_CAPABILITY, PCI_PM_CAPABILITY, *PPCI_PM_CAPABILITY
req.iface: 
req.product: Windows 10 or later.
---

# PCI_PM_CAPABILITY structure



## -description
<p>The PCI_PM_CAPABILITY structure reports the power management capabilities of the device.</p>


## -syntax

````
typedef struct _PCI_PM_CAPABILITY {
  PCI_CAPABILITIES_HEADER Header;
  union {
    PCI_PMC Capabilities;
    USHORT  AsUSHORT;
  } PMC;
  union {
    PCI_PMCSR ControlStatus;
    USHORT    AsUSHORT;
  } PMCSR;
  union {
    PCI_PMCSR_BSE BridgeSupport;
    UCHAR         AsUCHAR;
  } PMCSR_BSE;
  UCHAR                   Data;
} PCI_PM_CAPABILITY, *PPCI_PM_CAPABILITY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537454">PCI_CAPABILITIES_HEADER</a> that identifies the capability and provides a link to the next capability description. </p>
</dd>

### -field <b>PMC</b>

<dd>
<dl>

### -field <b>Capabilities</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537581">PCI_PMC</a> that specifies the power management capabilities of the device. This information was retrieved from the power management capabilities register (offset 2 in the power management register block). For more information about the contents of the power management capabilities register, see the <i>PCI Power Management Specification</i>. </p>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>Contains the same data as the <b>Capabilities </b>member. </p>
</dd>
</dl>
</dd>

### -field <b>PMCSR</b>

<dd>
<dl>

### -field <b>ControlStatus</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537583">PCI_PMCSR</a> that reports the contents of the power management control status register. This register is used to monitor power management event signals and manage the device's power state. For more information about the contents of the power management control status register, see the <i>PCI Power Management Specification</i>. </p>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>Contains the same data as the <b>Capabilities </b>member. </p>
</dd>
</dl>
</dd>

### -field <b>PMCSR_BSE</b>

<dd>
<dl>

### -field <b>BridgeSupport</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537587">PCI_PMCSR_BSE</a> that reports the contents of the power management control status register for PCI bridge support extensions. </p>
</dd>

### -field <b>AsUCHAR</b>

<dd>
<p>Contains the same data as the <b>BridgeSupport</b> member.</p>
</dd>
</dl>
</dd>

### -field <b>Data</b>

<dd>
<p>Holds the contents of an optional data register that the device uses to report state-dependent operating data, such as heat dissipation or how much power the device has consumed.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537454">PCI_CAPABILITIES_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537581">PCI_PMC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537583">PCI_PMCSR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537587">PCI_PMCSR_BSE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_PM_CAPABILITY structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
