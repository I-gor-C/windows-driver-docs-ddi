---
UID: NS:wdm._PCI_PM_CAPABILITY
title: "_PCI_PM_CAPABILITY"
author: windows-driver-content
description: The PCI_PM_CAPABILITY structure reports the power management capabilities of the device.
old-location: pci\pci_pm_capability.htm
old-project: PCI
ms.assetid: 829d4df0-2dc2-4a1f-9606-3d5f25624252
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PCI_PM_CAPABILITY structure [Buses], PPCI_PM_CAPABILITY, PCI.pci_pm_capability, PPCI_PM_CAPABILITY structure pointer [Buses], *PPCI_PM_CAPABILITY, wdm/PCI_PM_CAPABILITY, wdm/PPCI_PM_CAPABILITY, _PCI_PM_CAPABILITY, PCI_PM_CAPABILITY, pci_struct_041a9702-7b1e-43dc-8b8c-0371bc0eac26.xml
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
-	wdm.h
apiname:
-	PCI_PM_CAPABILITY
product: Windows
targetos: Windows
req.typenames: "*PPCI_PM_CAPABILITY, PCI_PM_CAPABILITY"
req.product: Windows 10 or later.
---

# _PCI_PM_CAPABILITY structure
The PCI_PM_CAPABILITY structure reports the power management capabilities of the device.

## Syntax
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

## Members


`Data`

Holds the contents of an optional data register that the device uses to report state-dependent operating data, such as heat dissipation or how much power the device has consumed.

`Header`

Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff537454">PCI_CAPABILITIES_HEADER</a> that identifies the capability and provides a link to the next capability description.

`PMC`



`PMCSR`



`PMCSR_BSE`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537581">PCI_PMC</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537587">PCI_PMCSR_BSE</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537583">PCI_PMCSR</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537454">PCI_CAPABILITIES_HEADER</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_PM_CAPABILITY structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>