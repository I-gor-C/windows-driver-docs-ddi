---
UID: NS:miniport._PCI_EXPRESS_SLOT_CONTROL_REGISTER
title: "_PCI_EXPRESS_SLOT_CONTROL_REGISTER"
author: windows-driver-content
description: The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure.
old-location: pci\pci_express_slot_control_register.htm
old-project: PCI
ms.assetid: 4755f4c3-305e-41a5-afdf-eda8e8e81b74
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PPCI_EXPRESS_SLOT_CONTROL_REGISTER, PCI.pci_express_slot_control_register, PCI_EXPRESS_SLOT_CONTROL_REGISTER, PCI_EXPRESS_SLOT_CONTROL_REGISTER union [Buses], PPCI_EXPRESS_SLOT_CONTROL_REGISTER, PPCI_EXPRESS_SLOT_CONTROL_REGISTER union pointer [Buses], _PCI_EXPRESS_SLOT_CONTROL_REGISTER, ntddk/PCI_EXPRESS_SLOT_CONTROL_REGISTER, ntddk/PPCI_EXPRESS_SLOT_CONTROL_REGISTER, pci_struct_d554e74d-130d-4d6d-8801-c65ea66653cb.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: miniport.h
req.include-header: Ntddk.h, Miniport.h
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
req.irql: Any level (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddk.h
api_name:
-	PCI_EXPRESS_SLOT_CONTROL_REGISTER
product:
- Windows
targetos: Windows
req.typenames: PCI_EXPRESS_SLOT_CONTROL_REGISTER, *PPCI_EXPRESS_SLOT_CONTROL_REGISTER
---

# _PCI_EXPRESS_SLOT_CONTROL_REGISTER structure
The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) slot control register of a PCIe capability structure.

## Syntax
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

## Members


`DUMMYSTRUCTNAME`



`AsUSHORT`

A USHORT representation of the contents of the PCI_EXPRESS_SLOT_CONTROL_REGISTER structure.

## Remarks
The PCI_EXPRESS_SLOT_CONTROL_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_SLOT_CONTROL_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | miniport.h (include Ntddk.h, Miniport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>