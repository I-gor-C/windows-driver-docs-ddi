---
UID: NS:miniport._PCI_EXPRESS_DEVICE_CONTROL_REGISTER
title: "_PCI_EXPRESS_DEVICE_CONTROL_REGISTER"
author: windows-driver-content
description: The PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure describes a PCI Express (PCIe) device control register of a PCIe capability structure.
old-location: pci\pci_express_device_control_register.htm
old-project: PCI
ms.assetid: 888f88db-2149-4da2-acdb-4bf88a5362dd
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PPCI_EXPRESS_DEVICE_CONTROL_REGISTER, PCI.pci_express_device_control_register, PCI_EXPRESS_DEVICE_CONTROL_REGISTER, PCI_EXPRESS_DEVICE_CONTROL_REGISTER union [Buses], PPCI_EXPRESS_DEVICE_CONTROL_REGISTER, PPCI_EXPRESS_DEVICE_CONTROL_REGISTER union pointer [Buses], _PCI_EXPRESS_DEVICE_CONTROL_REGISTER, ntddk/PCI_EXPRESS_DEVICE_CONTROL_REGISTER, ntddk/PPCI_EXPRESS_DEVICE_CONTROL_REGISTER, pci_struct_344c5f1d-566f-4755-ba52-57635c4fabfe.xml"
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
-	PCI_EXPRESS_DEVICE_CONTROL_REGISTER
product: Windows
targetos: Windows
req.typenames: PCI_EXPRESS_DEVICE_CONTROL_REGISTER, *PPCI_EXPRESS_DEVICE_CONTROL_REGISTER
---

# _PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure
The PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure describes a PCI Express (PCIe) device control register of a PCIe capability structure.

## Syntax
````
typedef union _PCI_EXPRESS_DEVICE_CONTROL_REGISTER {
  struct {
    USHORT CorrectableErrorEnable  :1;
    USHORT NonFatalErrorEnable  :1;
    USHORT FatalErrorEnable  :1;
    USHORT UnsupportedRequestErrorEnable  :1;
    USHORT EnableRelaxedOrder  :1;
    USHORT MaxPayloadSize  :3;
    USHORT ExtendedTagEnable  :1;
    USHORT PhantomFunctionsEnable  :1;
    USHORT AuxPowerEnable  :1;
    USHORT NoSnoopEnable  :1;
    USHORT MaxReadRequestSize  :3;
    USHORT BridgeConfigRetryEnable  :1;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_DEVICE_CONTROL_REGISTER, *PPCI_EXPRESS_DEVICE_CONTROL_REGISTER;
````

## Members


`DUMMYSTRUCTNAME`



`DUMMYSTRUCTNAME2`



`AsUSHORT`

A USHORT representation of the contents of the <b>PCI_EXPRESS_DEVICE_CONTROL_REGISTER</b> structure.

## Remarks
The PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_DEVICE_CONTROL_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | miniport.h (include Ntddk.h, Miniport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>