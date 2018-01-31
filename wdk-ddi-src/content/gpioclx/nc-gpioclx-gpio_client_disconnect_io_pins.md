---
UID : NC:gpioclx.GPIO_CLIENT_DISCONNECT_IO_PINS
title : GPIO_CLIENT_DISCONNECT_IO_PINS
author : windows-driver-content
description : The CLIENT_DisconnectIoPins event callback function closes a logical connection to a set of general-purpose I/O (GPIO) pins that are configured for data read or write operations.
old-location : gpio\client_disconnectiopins.htm
old-project : GPIO
ms.assetid : FA6ACAE4-54D9-4EE6-AC63-3FFB973DD37F
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : GPIO.client_disconnectiopins, CLIENT_DisconnectIoPins callback function [Parallel Ports], CLIENT_DisconnectIoPins, GPIO_CLIENT_DISCONNECT_IO_PINS, GPIO_CLIENT_DISCONNECT_IO_PINS, gpioclx/CLIENT_DisconnectIoPins
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : gpioclx.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : Supported starting with Windows 8.
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
req.irql : Called at PASSIVE_LEVEL.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : GNSS_V2UPL_NI_INFO, *PGNSS_V2UPL_NI_INFO
---


# GPIO_CLIENT_DISCONNECT_IO_PINS function
The <i>CLIENT_DisconnectIoPins</i> event callback function closes a logical connection to a set of general-purpose I/O (GPIO) pins that are configured for data read or write operations.

## Syntax

```
GPIO_CLIENT_DISCONNECT_IO_PINS GpioClientDisconnectIoPins;

NTSTATUS GpioClientDisconnectIoPins(
  PVOID Context,
  PGPIO_DISCONNECT_IO_PINS_PARAMETERS DisconnectParameters
)
{...}
```

## Parameters

`Context`

A pointer to the GPIO controller driver's <a href="https://msdn.microsoft.com/4BE99C71-9BA6-44E3-A54F-DE8C3440A474">device context</a>.

`DisconnectParameters`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh698250">GPIO_DISCONNECT_IO_PINS_PARAMETERS</a> structure that describes the set of GPIO pins that are to be disconnected.


## Return Value

The <i>CLIENT_DisconnectIoPins</i> function returns STATUS_SUCCESS if the call is successful. Otherwise, it returns an appropriate error code.

## Remarks

This callback function is implemented by the GPIO controller driver. The GPIO framework extension (GpioClx) calls this function to close a connection that was previously opened by a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439347">CLIENT_ConnectIoPins</a> callback function.

To register your driver's <i>CLIENT_DisconnectIoPins</i> callback function, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a> method. This method accepts, as an input parameter, a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a> structure that contains a <i>CLIENT_DisconnectIoPins</i> function pointer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | gpioclx.h |
| **Library** |  |
| **IRQL** | Called at PASSIVE_LEVEL. |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh698250">GPIO_DISCONNECT_IO_PINS_PARAMETERS</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439347">CLIENT_ConnectIoPins</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439490">GPIO_CLX_RegisterClient</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439479">GPIO_CLIENT_REGISTRATION_PACKET</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [GPIO\parports]:%20CLIENT_DisconnectIoPins callback function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>