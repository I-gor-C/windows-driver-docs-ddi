---
UID: NS:miniport._PCI_EXPRESS_ROOT_CONTROL_REGISTER
title: "_PCI_EXPRESS_ROOT_CONTROL_REGISTER"
author: windows-driver-content
description: The PCI_EXPRESS_ROOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) root control register of a PCIe capability structure.
old-location: pci\pci_express_root_control_register.htm
old-project: PCI
ms.assetid: 0f2c321c-f03b-4655-bbd1-25fcc6c52cfa
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PPCI_EXPRESS_ROOT_CONTROL_REGISTER, PCI.pci_express_root_control_register, PCI_EXPRESS_ROOT_CONTROL_REGISTER, PCI_EXPRESS_ROOT_CONTROL_REGISTER union [Buses], PPCI_EXPRESS_ROOT_CONTROL_REGISTER, PPCI_EXPRESS_ROOT_CONTROL_REGISTER union pointer [Buses], _PCI_EXPRESS_ROOT_CONTROL_REGISTER, ntddk/PCI_EXPRESS_ROOT_CONTROL_REGISTER, ntddk/PPCI_EXPRESS_ROOT_CONTROL_REGISTER, pci_struct_ef335e30-c046-4066-8411-27bf96cbcd08.xml"
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
-	PCI_EXPRESS_ROOT_CONTROL_REGISTER
product: Windows
targetos: Windows
req.typenames: PCI_EXPRESS_ROOT_CONTROL_REGISTER, *PPCI_EXPRESS_ROOT_CONTROL_REGISTER
---

# _PCI_EXPRESS_ROOT_CONTROL_REGISTER structure
The PCI_EXPRESS_ROOT_CONTROL_REGISTER structure describes a PCI Express (PCIe) root control register of a PCIe capability structure.

## Syntax
````
typedef union _PCI_EXPRESS_ROOT_CONTROL_REGISTER {
  struct {
    USHORT CorrectableSerrEnable  :1;
    USHORT NonFatalSerrEnable  :1;
    USHORT FatalSerrEnable  :1;
    USHORT PMEInterruptEnable  :1;
    USHORT CRSSoftwareVisibilityEnable  :1;
    USHORT Rsvd  :11;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_ROOT_CONTROL_REGISTER, *PPCI_EXPRESS_ROOT_CONTROL_REGISTER;
````

## Members


`DUMMYSTRUCTNAME`



`AsUSHORT`

A USHORT representation of the contents of the PCI_EXPRESS_ROOT_CONTROL_REGISTER structure.

## Remarks
The PCI_EXPRESS_ROOT_CONTROL_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_ROOT_CONTROL_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | miniport.h (include Ntddk.h, Miniport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>