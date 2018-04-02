---
UID: NS:miniport._PCI_EXPRESS_ROOT_STATUS_REGISTER
title: "_PCI_EXPRESS_ROOT_STATUS_REGISTER"
author: windows-driver-content
description: The PCI_EXPRESS_ROOT_STATUS_REGISTER structure describes a PCI Express (PCIe) root status register of a PCIe capability structure.
old-location: pci\pci_express_root_status_register.htm
old-project: PCI
ms.assetid: e7f6a8b9-22f1-4c5b-a0b7-b87ceb2c0b1b
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PPCI_EXPRESS_ROOT_STATUS_REGISTER, PCI.pci_express_root_status_register, PCI_EXPRESS_ROOT_STATUS_REGISTER, PCI_EXPRESS_ROOT_STATUS_REGISTER union [Buses], PPCI_EXPRESS_ROOT_STATUS_REGISTER, PPCI_EXPRESS_ROOT_STATUS_REGISTER union pointer [Buses], _PCI_EXPRESS_ROOT_STATUS_REGISTER, ntddk/PCI_EXPRESS_ROOT_STATUS_REGISTER, ntddk/PPCI_EXPRESS_ROOT_STATUS_REGISTER, pci_struct_ff3a211f-421b-41f3-9250-d658636bfe49.xml"
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
-	PCI_EXPRESS_ROOT_STATUS_REGISTER
product:
- Windows
targetos: Windows
req.typenames: PCI_EXPRESS_ROOT_STATUS_REGISTER, *PPCI_EXPRESS_ROOT_STATUS_REGISTER
---

# _PCI_EXPRESS_ROOT_STATUS_REGISTER structure
The PCI_EXPRESS_ROOT_STATUS_REGISTER structure describes a PCI Express (PCIe) root status register of a PCIe capability structure.

## Syntax
````
typedef union _PCI_EXPRESS_ROOT_STATUS_REGISTER {
  struct {
    ULONG PMERequestorId  :16;
    ULONG PMEStatus  :1;
    ULONG PMEPending  :1;
    ULONG Rsvd  :14;
  };
  ULONG  AsULONG;
} PCI_EXPRESS_ROOT_STATUS_REGISTER, *PPCI_EXPRESS_ROOT_STATUS_REGISTER;
````

## Members


`DUMMYSTRUCTNAME`



`AsULONG`

A ULONG representation of the contents of the PCI_EXPRESS_ROOT_STATUS_REGISTER structure.

## Remarks
The PCI_EXPRESS_ROOT_STATUS_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_ROOT_STATUS_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | miniport.h (include Ntddk.h, Miniport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537471">PCI_EXPRESS_PME_REQUESTOR_ID</a>