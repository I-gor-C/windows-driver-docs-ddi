---
UID: NS:gpioclx._CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT
title: "_CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT"
author: windows-driver-content
description: The CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure contains a set of general-purpose I/O (GPIO) controller attributes that were requested by the GPIO framework extension (GpioClx).
old-location: gpio\client_controller_query_set_information_output.htm
old-project: GPIO
ms.assetid: D145BAD6-EFE2-4B04-AF6E-F00486C78E8A
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure [Parallel Ports], GPIO.client_controller_query_set_information_output, PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure pointer [Parallel Ports], _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, gpioclx/CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, gpioclx/PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gpioclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Gpioclx.h
api_name:
-	CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT
product: Windows
targetos: Windows
req.typenames: CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT
---

# _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT structure
The <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure contains a set of general-purpose I/O (GPIO) controller attributes that were requested by the GPIO framework extension (GpioClx).

## Syntax
````
typedef struct _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT {
  USHORT Version;
  USHORT Size;
  union {
    CLIENT_QUERY_BANK_POWER_INFORMATION_OUTPUT BankPowerInformation;
    struct {
      ULONG ResourceMapping[ANYSIZE_ARRAY];
    } BankInterruptBinding;
    struct {
      BOOLEAN Mapping[ANYSIZE_ARRAY];
    } ControllerFunctionBankMapping;
  };
} CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT;
````

## Members


`Version`

Specifies the version number of this structure.

`Size`

Specifies the size, in bytes, of this structure.

## Remarks
The optional <i>OutputBuffer</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> function is a pointer to a caller-allocated <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</b> structure. The function writes the requested attribute information to this structure, if <i>OutputBuffer</i> is non-NULL.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | gpioclx.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh698242">CLIENT_QUERY_BANK_POWER_INFORMATION_OUTPUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh698238">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</a>