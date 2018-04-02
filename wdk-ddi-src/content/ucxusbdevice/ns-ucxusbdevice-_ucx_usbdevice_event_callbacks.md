---
UID: NS:ucxusbdevice._UCX_USBDEVICE_EVENT_CALLBACKS
title: "_UCX_USBDEVICE_EVENT_CALLBACKS"
author: windows-driver-content
description: This structure provides a list of UCX USB device event callback functions.
old-location: buses\_ucx_usbdevice_event_callbacks.htm
old-project: usbref
ms.assetid: 7A320D48-E71C-40FE-A2EF-201CFCE55145
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCX_USBDEVICE_EVENT_CALLBACKS, P_UCX_USBDEVICE_EVENT_CALLBACKS, P_UCX_USBDEVICE_EVENT_CALLBACKS structure pointer [Buses], UCX_USBDEVICE_EVENT_CALLBACKS, UCX_USBDEVICE_EVENT_CALLBACKS structure [Buses], _UCX_USBDEVICE_EVENT_CALLBACKS, buses._ucx_usbdevice_event_callbacks, ucxusbdevice/P_UCX_USBDEVICE_EVENT_CALLBACKS, ucxusbdevice/_UCX_USBDEVICE_EVENT_CALLBACKS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ucxusbdevice.h
api_name:
-	UCX_USBDEVICE_EVENT_CALLBACKS
product:
- Windows
targetos: Windows
req.typenames: UCX_USBDEVICE_EVENT_CALLBACKS, *PUCX_USBDEVICE_EVENT_CALLBACKS
req.product: Windows 10 or later.
---

# _UCX_USBDEVICE_EVENT_CALLBACKS structure
This structure provides a list of UCX USB device event callback functions.

## Syntax
```
typedef struct _UCX_USBDEVICE_EVENT_CALLBACKS {
  ULONG                                  Size;
  PFN_UCX_USBDEVICE_ENDPOINTS_CONFIGURE  EvtUsbDeviceEndpointsConfigure;
  PFN_UCX_USBDEVICE_ENABLE               EvtUsbDeviceEnable;
  PFN_UCX_USBDEVICE_DISABLE              EvtUsbDeviceDisable;
  PFN_UCX_USBDEVICE_RESET                EvtUsbDeviceReset;
  PFN_UCX_USBDEVICE_ADDRESS              EvtUsbDeviceAddress;
  PFN_UCX_USBDEVICE_UPDATE               EvtUsbDeviceUpdate;
  PFN_UCX_USBDEVICE_HUB_INFO             EvtUsbDeviceHubInfo;
  PFN_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD EvtUsbDeviceDefaultEndpointAdd;
  PFN_UCX_USBDEVICE_ENDPOINT_ADD         EvtUsbDeviceEndpointAdd;
  PFN_UCX_USBDEVICE_SUSPEND              EvtUsbDeviceSuspend;
  PFN_UCX_USBDEVICE_RESUME               EvtUsbDeviceResume;
  PFN_UCX_USBDEVICE_GET_CHARACTERISTIC   EvtUsbDeviceGetCharacteristic;
} *PUCX_USBDEVICE_EVENT_CALLBACKS, UCX_USBDEVICE_EVENT_CALLBACKS;
```

## Members


`Size`

The size in bytes of this structure.

`EvtUsbDeviceEndpointsConfigure`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187842">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> callback function.

`EvtUsbDeviceEnable`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187841">EVT_UCX_USBDEVICE_ENABLE</a> callback function.

`EvtUsbDeviceDisable`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187840">EVT_UCX_USBDEVICE_DISABLE</a> callback function.

`EvtUsbDeviceReset`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187845">EVT_UCX_USBDEVICE_RESET</a> callback function.

`EvtUsbDeviceAddress`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187838">EVT_UCX_USBDEVICE_ADDRESS</a> callback function.

`EvtUsbDeviceUpdate`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187846">EVT_UCX_USBDEVICE_UPDATE</a> callback function.

`EvtUsbDeviceHubInfo`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187844">EVT_UCX_USBDEVICE_HUB_INFO</a> callback function.

`EvtUsbDeviceDefaultEndpointAdd`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187839">EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</a> callback function.

`EvtUsbDeviceEndpointAdd`

A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/mt187843">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> callback function.

`EvtUsbDeviceSuspend`

A pointer to an <a href="https://msdn.microsoft.com/809F946C-DDD4-4C4D-9F0F-F2B4A4657D12">EVT_UCX_USBDEVICE_SUSPEND</a> callback function.

`EvtUsbDeviceResume`

A pointer to an <a href="https://msdn.microsoft.com/876D9754-B3AA-42C5-8BDD-60CFD4F78951">EVT_UCX_USBDEVICE_RESUME</a> callback function.

`EvtUsbDeviceGetCharacteristic`

A pointer to an <a href="https://msdn.microsoft.com/EE8568F6-3D88-477E-9F0D-044D014EBCF3">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a> callback function.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188068">UCX_USBDEVICE_EVENT_CALLBACKS_INIT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt188053">UcxUsbDeviceInitSetEventCallbacks</a>