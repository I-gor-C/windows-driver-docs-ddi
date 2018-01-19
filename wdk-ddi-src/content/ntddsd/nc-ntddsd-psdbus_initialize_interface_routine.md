---
UID : NC:ntddsd.PSDBUS_INITIALIZE_INTERFACE_ROUTINE
title : PSDBUS_INITIALIZE_INTERFACE_ROUTINE
author : windows-driver-content
description : The PSDBUS_INITIALIZE_INTERFACE_ROUTINE prototype declares the routine that a Secure Digital (SD) device driver uses to initialize an interface instance that it creates with the SdBusOpenInterface routine.
old-location : sd\psdbus_initialize_interface_routine.htm
old-project : SD
ms.assetid : 90d36eb1-d122-4266-9c33-206c9c9b44e8
ms.author : windowsdriverdev
ms.date : 12/18/2017
ms.keywords : _STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST, STORAGE_DIAGNOSTIC_MP_REQUEST
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ntddsd.h
req.include-header : Ntddsd.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : InitializeInterface
req.alt-loc : ntddsd.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSTORAGE_DIAGNOSTIC_MP_REQUEST, STORAGE_DIAGNOSTIC_MP_REQUEST"
---


# PSDBUS_INITIALIZE_INTERFACE_ROUTINE callback function
The PSDBUS_INITIALIZE_INTERFACE_ROUTINE prototype declares the routine that a Secure Digital (SD) device driver uses to initialize an interface instance that it creates with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537906">SdBusOpenInterface</a> routine.

## Syntax

```
PSDBUS_INITIALIZE_INTERFACE_ROUTINE PsdbusInitializeInterfaceRoutine;

NTSTATUS PsdbusInitializeInterfaceRoutine(
  PVOID Context,
  PSDBUS_INTERFACE_PARAMETERS InterfaceParameters
)
{...}
```

## Parameters

`Context`

Contains the interface context that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537906">SdBusOpenInterface</a> routine returns in the <b>Context</b> member of the <a href="https://msdn.microsoft.com/92b8762d-8af3-493c-aa1d-bc245b0cbd83">SDBUS_INTERFACE_STANDARD</a> structure.

`InterfaceParameters`

Pointer to a structure of type <a href="https://msdn.microsoft.com/d407131e-5dda-4d50-b09a-0f937774eefb">SDBUS_INTERFACE_PARAMETERS</a> that contains the information that the bus driver should use to initialize the interface instance.


## Return Value

Returns STATUS_SUCCESS if the operation succeeds, or the appropriate error status if the operation fails.

## Remarks

An SD card driver typically calls its initialization routine immediately after the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537906">SdBusOpenInterface</a> routine returns with a value of STATUS_SUCCESS. 

An SD card driver must call its initialization routine before attempting to send requests to the bus driver.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddsd.h (include Ntddsd.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/92b8762d-8af3-493c-aa1d-bc245b0cbd83">SDBUS_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537906">SdBusOpenInterface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SD\buses]:%20PSDBUS_INITIALIZE_INTERFACE_ROUTINE callback function%20 RELEASE:%20(12/18/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>