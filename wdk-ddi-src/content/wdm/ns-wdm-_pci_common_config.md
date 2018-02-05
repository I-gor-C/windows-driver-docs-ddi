---
UID : NS:wdm._PCI_COMMON_CONFIG
title : "_PCI_COMMON_CONFIG"
author : windows-driver-content
description : The PCI_COMMON_CONFIG structure is obsolete.
old-location : kernel\pci_common_config.htm
old-project : kernel
ms.assetid : 239d0c0a-e78e-40d5-b359-36910bdd9358
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.pci_common_config, wdm/PCI_COMMON_CONFIG, PCI_COMMON_CONFIG structure [Kernel-Mode Driver Architecture], PCI_COMMON_CONFIG, kstruct_c_42f21057-e812-4a4d-96c5-f1177a03982b.xml, wdm/PPCI_COMMON_CONFIG, PPCI_COMMON_CONFIG structure pointer [Kernel-Mode Driver Architecture], PPCI_COMMON_CONFIG, *PPCI_COMMON_CONFIG, _PCI_COMMON_CONFIG
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
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
req.irql : PASSIVE_LEVEL (see Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PCI_COMMON_CONFIG, *PPCI_COMMON_CONFIG
req.product : Windows 10 or later.
---

# _PCI_COMMON_CONFIG structure
The <b>PCI_COMMON_CONFIG</b> structure is <u>obsolete</u>. It defines standard PCI configuration information returned by the obsolete <a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a> routine for the input <i>BusDataType</i> PCIConfiguration, assuming the caller-allocated <i>Buffer</i> is of sufficient <i>Length</i>.

## Syntax
````
typedef struct _PCI_COMMON_CONFIG {
  USHORT VendorID;
  USHORT DeviceID;
  USHORT Command;
  USHORT Status;
  UCHAR  RevisionID;
  UCHAR  ProgIf;
  UCHAR  SubClass;
  UCHAR  BaseClass;
  UCHAR  CacheLineSize;
  UCHAR  LatencyTimer;
  UCHAR  HeaderType;
  UCHAR  BIST;
  union {
    struct {
      ULONG BaseAddresses[PCI_TYPE0_ADDRESSES];
      ULONG Reserved1[2];
      ULONG ROMBaseAddress;
      ULONG Reserved2[2];
      UCHAR InterruptLine;
      UCHAR InterruptPin;
      UCHAR MinimumGrant;
      UCHAR MaximumLatency;
    } type0;
  } u;
  UCHAR  DeviceSpecific[192];
} PCI_COMMON_CONFIG, *PPCI_COMMON_CONFIG;
````

## Members


`DeviceSpecific`

Contains any device-specific initialization information that is available.

`PCI_COMMON_HEADER`



## Remarks
Certain members of this structure have read-only values, so attempts to reset them are ignored. These members include the following: <b>VendorID</b>, <b>DeviceID</b>, <b>RevisionID</b>, <b>ProgIf</b>, <b>SubClass</b>, <b>BaseClass</b>, <b>HeaderType</b>, <b>InterruptPin</b>, <b>MinimumGrant</b>, and <b>MaximumLatency.</b>

Other members are provisionally read-only: that is, the system initializes them to their correct values, so drivers can safely treat them as read-only. However, they can be reset if a bus-master driver finds it necessary. These members include the following: <b>CacheLineSize</b> and <b>LatencyTimer</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546580">HalAssignSlotResources</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546633">HalSetBusDataByOffset</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546628">HalSetBusData</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCI_COMMON_CONFIG structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>