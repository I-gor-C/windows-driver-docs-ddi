---
UID: NF:ucxusbdevice.UCX_USBDEVICE_EVENT_CALLBACKS_INIT
title: UCX_USBDEVICE_EVENT_CALLBACKS_INIT function
author: windows-driver-content
description: Initializes a UCX_USBDEVICE_EVENT_CALLBACKS structure with the function pointers to client driver's callback functions.
old-location: buses\_ucx_usbdevice_event_callbacks_init.htm
old-project: usbref
ms.assetid: 594583B0-6CCB-469F-82AB-604825D85E2E
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UCX_USBDEVICE_EVENT_CALLBACKS_INIT, UCX_USBDEVICE_EVENT_CALLBACKS_INIT function [Buses], buses._ucx_usbdevice_event_callbacks_init, ucxusbdevice/UCX_USBDEVICE_EVENT_CALLBACKS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucxusbdevice.h
api_name:
-	UCX_USBDEVICE_EVENT_CALLBACKS_INIT
product: Windows
targetos: Windows
req.typenames: UCX_USBDEVICE_CHARACTERISTIC_TYPE
req.product: Windows 10 or later.
---


# UCX_USBDEVICE_EVENT_CALLBACKS_INIT function
Initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188067">UCX_USBDEVICE_EVENT_CALLBACKS</a> structure with the function pointers to client driver's callback functions.

## Syntax

```
void UCX_USBDEVICE_EVENT_CALLBACKS_INIT(
  PUCX_USBDEVICE_EVENT_CALLBACKS         Callbacks,
  PFN_UCX_USBDEVICE_ENDPOINTS_CONFIGURE  EvtUsbDeviceEndpointsConfigure,
  PFN_UCX_USBDEVICE_ENABLE               EvtUsbDeviceEnable,
  PFN_UCX_USBDEVICE_DISABLE              EvtUsbDeviceDisable,
  PFN_UCX_USBDEVICE_RESET                EvtUsbDeviceReset,
  PFN_UCX_USBDEVICE_ADDRESS              EvtUsbDeviceAddress,
  PFN_UCX_USBDEVICE_UPDATE               EvtUsbDeviceUpdate,
  PFN_UCX_USBDEVICE_HUB_INFO             EvtUsbDeviceHubInfo,
  PFN_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD EvtUsbDeviceDefaultEndpointAdd,
  PFN_UCX_USBDEVICE_ENDPOINT_ADD         EvtUsbDeviceEndpointAdd
);
```

## Parameters

`Callbacks`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188067">UCX_USBDEVICE_EVENT_CALLBACKS</a> structure to initialize.

`EvtUsbDeviceEndpointsConfigure`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187842">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> event callback function.

`EvtUsbDeviceEnable`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187841">EVT_UCX_USBDEVICE_ENABLE</a> event callback function.

`EvtUsbDeviceDisable`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187840">EVT_UCX_USBDEVICE_DISABLE</a> event callback function.

`EvtUsbDeviceReset`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187845">EVT_UCX_USBDEVICE_RESET</a> event callback function.

`EvtUsbDeviceAddress`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187838">EVT_UCX_USBDEVICE_ADDRESS</a> event callback function.

`EvtUsbDeviceUpdate`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187846">EVT_UCX_USBDEVICE_UPDATE</a> event callback function.

`EvtUsbDeviceHubInfo`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187844">EVT_UCX_USBDEVICE_HUB_INFO</a> event callback function.

`EvtUsbDeviceDefaultEndpointAdd`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187839">EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</a> event callback function.

`EvtUsbDeviceEndpointAdd`

A pointer to client driver's implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187843">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> event callback function.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10  |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188067">UCX_USBDEVICE_EVENT_CALLBACKS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt188053">UcxUsbDeviceInitSetEventCallbacks</a>