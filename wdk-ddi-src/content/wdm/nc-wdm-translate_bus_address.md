---
UID : NC:wdm.TRANSLATE_BUS_ADDRESS
title : TRANSLATE_BUS_ADDRESS
author : windows-driver-content
description : The TranslateBusAddress routine translates addresses on the parent bus to logical addresses.
old-location : kernel\translatebusaddress.htm
old-project : kernel
ms.assetid : DDED1237-74B7-4127-8E86-D0794A1FB49B
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.translatebusaddress, TranslateBusAddress routine [Kernel-Mode Driver Architecture], TranslateBusAddress, TRANSLATE_BUS_ADDRESS, TRANSLATE_BUS_ADDRESS, wdm/TranslateBusAddress, kernel.bustranslatebusaddress, drvr_interface_68887adb-724b-47ca-80e6-b8b934ae2414.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wdm.h
req.include-header : Ntddk.h
req.target-type : Desktop
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
req.typenames : "*PWDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME"
req.product : Windows 10 or later.
---


# TRANSLATE_BUS_ADDRESS function
The <i>TranslateBusAddress</i> routine translates addresses on the parent bus to logical addresses.

## Syntax

```
TRANSLATE_BUS_ADDRESS TranslateBusAddress;

_IRQL_requires_same_ BOOLEAN TranslateBusAddress(
  PVOID Context,
  PHYSICAL_ADDRESS BusAddress,
  ULONG Length,
  PULONG AddressSpace,
  PPHYSICAL_ADDRESS TranslatedAddress
)
{...}
```

## Parameters

`Context`

A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\wdm\ns-wdm-_bus_interface_standard.md">BUS_INTERFACE_STANDARD</a> structure for the interface.

`BusAddress`

The bus-relative address to be translated.

`Length`

The length, in bytes, of the input memory that <i>BusAddress</i> points to.

`AddressSpace`

On input, the address space in which the device's hardware address resides. A value of 0x0 signifies memory space, and a value of 0x1 signifies port I/O space. On output, <i>AddressSpace</i> indicates the address space in which the <i>TranslatedAddress</i> resides.

`TranslatedAddress`

The translated (logical) address that corresponds to the bus-relative address that the caller provides in <i>BusAddress</i>.


## Return Value

The 
      <i>TranslateBusAddress</i> routine returns <b>TRUE</b> if the translation operation succeeded and <b>FALSE</b> otherwise.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Ntddk.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\wdm\ns-wdm-_bus_interface_standard.md">BUS_INTERFACE_STANDARD</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20TRANSLATE_BUS_ADDRESS routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>