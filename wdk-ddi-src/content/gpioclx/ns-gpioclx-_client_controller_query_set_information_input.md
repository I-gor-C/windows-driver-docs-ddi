---
UID: NS:gpioclx._CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
title: "_CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT"
author: windows-driver-content
description: The CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure contains a request for the hardware attributes of the general-purpose I/O (GPIO) controller.
old-location: gpio\client_controller_query_set_information_input.htm
old-project: GPIO
ms.assetid: C4AA60FF-03AD-444F-B897-654B787B5F86
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, gpioclx/CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, gpioclx/PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure [Parallel Ports], GPIO.client_controller_query_set_information_input, CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure pointer [Parallel Ports]
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Gpioclx.h
apiname:
-	CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
product: Windows
targetos: Windows
req.typenames: CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT
---

# _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure
The <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure contains a request for the hardware attributes of the general-purpose I/O (GPIO) controller.

## Syntax
````
typedef struct _CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT {
  CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE RequestType;
  USHORT                                   Size;
  ULONG                                    Flags;
  union {
    struct {
      BANK_ID BankId;
    } BankPowerInformation;
    struct {
      WDFCMRESLIST ResourcesTranslated;
      WDFCMRESLIST ResourcesRaw;
      USHORT       TotalBanks;
    } BankInterruptBinding;
    struct {
      PVOID  InputBuffer;
      SIZE_T InputBufferSize;
      SIZE_T OutputBufferSize;
      USHORT TotalBanks;
    } ControllerFunctionBankMapping;
  };
} CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT, *PCLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT;
````

## Members


`Flags`

A set of flag bits that supply additional information about the type of attribute request indicated by the <b>RequestType</b> member. No flags are currently defined for the <b>Flags</b> member.

`RequestType`

The type of attribute information that is being requested. This member is set to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh698240">CLIENT_CONTROLLER_QUERY_SET_REQUEST_TYPE</a> enumeration value.

`Size`

Specifies the size, in bytes, of the <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure.

## Remarks
The <i>InputBuffer</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a> function is a pointer to a <b>CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT</b> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 8. Supported starting with Windows 8. |
| **Header** | gpioclx.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439399">CLIENT_QueryControllerBasicInformation</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439358">CLIENT_CONTROLLER_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh698239">CLIENT_CONTROLLER_QUERY_SET_INFORMATION_OUTPUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh698241">CLIENT_QuerySetControllerInformation</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_CONTROLLER_QUERY_SET_INFORMATION_INPUT structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>