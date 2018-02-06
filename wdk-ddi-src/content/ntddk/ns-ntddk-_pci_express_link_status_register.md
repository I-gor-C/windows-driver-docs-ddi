---
UID: NS:ntddk._PCI_EXPRESS_LINK_STATUS_REGISTER
title: "_PCI_EXPRESS_LINK_STATUS_REGISTER"
author: windows-driver-content
description: The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure.
old-location: pci\pci_express_link_status_register.htm
old-project: PCI
ms.assetid: c3431e89-4a47-44e6-98d8-eae444ea1915
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PPCI_EXPRESS_LINK_STATUS_REGISTER, PCI_EXPRESS_LINK_STATUS_REGISTER, ntddk/PPCI_EXPRESS_LINK_STATUS_REGISTER, PPCI_EXPRESS_LINK_STATUS_REGISTER union pointer [Buses], ntddk/PCI_EXPRESS_LINK_STATUS_REGISTER, pci_struct_41d11df3-521f-4709-a30e-be70ad36db8f.xml, PCI_EXPRESS_LINK_STATUS_REGISTER union [Buses], PCI.pci_express_link_status_register, _PCI_EXPRESS_LINK_STATUS_REGISTER, *PPCI_EXPRESS_LINK_STATUS_REGISTER
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddk.h
apiname:
-	PCI_EXPRESS_LINK_STATUS_REGISTER
product: Windows
targetos: Windows
req.typenames: "*PPCI_EXPRESS_LINK_STATUS_REGISTER, PCI_EXPRESS_LINK_STATUS_REGISTER"
---

# _PCI_EXPRESS_LINK_STATUS_REGISTER structure
The PCI_EXPRESS_LINK_STATUS_REGISTER structure describes a PCI Express (PCIe) link status register of a PCIe capability structure.

## Syntax
````
typedef union _PCI_EXPRESS_LINK_STATUS_REGISTER {
  struct {
    USHORT LinkSpeed  :4;
    USHORT LinkWidth  :6;
    USHORT Undefined  :1;
    USHORT LinkTraining  :1;
    USHORT SlotClockConfig  :1;
    USHORT DataLinkLayerActive  :1;
    USHORT Rsvd  :2;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_LINK_STATUS_REGISTER, *PPCI_EXPRESS_LINK_STATUS_REGISTER;
````

## Members


`AsUSHORT`

A USHORT representation of the contents of the PCI_EXPRESS_LINK_STATUS_REGISTER structure.

`DUMMYSTRUCTNAME`



## Remarks
The PCI_EXPRESS_LINK_STATUS_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_LINK_STATUS_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_LINK_STATUS_REGISTER union%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>