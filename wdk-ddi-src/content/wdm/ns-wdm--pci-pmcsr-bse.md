---
UID: NS.wdm._PCI_PMCSR_BSE
title: PCI_PMCSR_BSE
author: windows-driver-content
description: The PCI_PMCSR_BSE structure is used to report the contents of the power management control status register for PCI bridge support extensions.
old-location: pci\pci_pmcsr_bse.htm
old-project: PCI
ms.assetid: f65116f6-0a61-4609-993b-d7b2eabf12b5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PCI_PMCSR_BSE, PCI_PMCSR_BSE, *PPCI_PMCSR_BSE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_PMCSR_BSE
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
req.iface: 
req.product: Windows 10 or later.
---

# PCI_PMCSR_BSE structure



## -description
<p>The PCI_PMCSR_BSE structure is used to report the contents of the power management control status register for PCI bridge support extensions. </p>


## -syntax

````
typedef struct _PCI_PMCSR_BSE {
  UCHAR Rsvd1;
  UCHAR D3HotSupportsStopClock;
  UCHAR BusPowerClockControlEnabled;
} PCI_PMCSR_BSE, *PPCI_PMCSR_BSE;
````


## -struct-fields
<dl>

### -field <b>Rsvd1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>D3HotSupportsStopClock</b>

<dd>
<p>Indicates how the power state of a secondary bus is affected when the primary bus transitions to a D3 power state. For a detailed explanation of the values in this member and how they affect the relationship between the primary and secondary buses, see the <i>PCI Power Management Specification</i>. </p>
</dd>

### -field <b>BusPowerClockControlEnabled</b>

<dd>
<p>Indicates, when 1, that the bus's power clock control mechanism is enabled. A value of 0 indicates that the bus power clock control mechanism is disabled.  For a detailed explanation of the meaning of this member, see the <i>PCI Power Management Specification</i>. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537588">PCI_PM_CAPABILITY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_PMCSR_BSE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
