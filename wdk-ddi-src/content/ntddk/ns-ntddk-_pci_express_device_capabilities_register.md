---
UID : NS:ntddk._PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER
title : "_PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER"
author : windows-driver-content
description : The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure.
old-location : pci\pci_express_device_capabilities_register.htm
old-project : PCI
ms.assetid : 895b49e5-181b-4312-ab1c-7f67c102b32f
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : ntddk/PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER union [Buses], ntddk/PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, pci_struct_6643c57c-39dd-483b-9611-b0bf96cacbd8.xml, _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, *PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER union pointer [Buses], PCI.pci_express_device_capabilities_register
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER"
---

# _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure
The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure describes a PCI Express (PCIe) device capabilities register of a PCIe capability structure.

## Syntax
````
typedef union _PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER {
  struct {
    ULONG MaxPayloadSizeSupported  :3;
    ULONG PhantomFunctionsSupported  :2;
    ULONG ExtendedTagSupported  :1;
    ULONG L0sAcceptableLatency  :3;
    ULONG L1AcceptableLatency  :3;
    ULONG Undefined  :3;
    ULONG RoleBasedErrorReporting  :1;
    ULONG Rsvd1  :2;
    ULONG CapturedSlotPowerLimit  :8;
    ULONG CapturedSlotPowerLimitScale  :2;
    ULONG Rsvd2  :4;
  };
  ULONG  AsULONG;
} PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER, *PPCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER;
````

## Members


`AsULONG`

A ULONG representation of the contents of the PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure.

`DUMMYSTRUCTNAME`



## Remarks
The PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure is available in Windows Server 2008 and later versions of Windows.

A PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER structure is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537460">PCI_EXPRESS_CAPABILITY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER union%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>