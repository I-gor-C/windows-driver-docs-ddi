---
UID : NF:ucxusbdevice.UCX_USBDEVICE_EVENT_CALLBACKS_INIT
title : UCX_USBDEVICE_EVENT_CALLBACKS_INIT function
author : windows-driver-content
description : Initializes a UCX_USBDEVICE_EVENT_CALLBACKS structure with the function pointers to client driver's callback functions.
old-location : buses\_ucx_usbdevice_event_callbacks_init.htm
old-project : usbref
ms.assetid : 594583B0-6CCB-469F-82AB-604825D85E2E
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses._ucx_usbdevice_event_callbacks_init, UCX_USBDEVICE_EVENT_CALLBACKS_INIT function [Buses], UCX_USBDEVICE_EVENT_CALLBACKS_INIT, ucxusbdevice/UCX_USBDEVICE_EVENT_CALLBACKS_INIT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ucxusbdevice.h
req.include-header : Ucxclass.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UCX_USBDEVICE_CHARACTERISTIC_TYPE
req.product : Windows 10 or later.
---


# UCX_USBDEVICE_EVENT_CALLBACKS_INIT function
Initializes a <a href="..\ucxusbdevice\ns-ucxusbdevice-_ucx_usbdevice_event_callbacks.md">UCX_USBDEVICE_EVENT_CALLBACKS</a> structure with the function pointers to client driver's callback functions.

## Syntax

````
__inline
void UCX_USBDEVICE_EVENT_CALLBACKS_INIT(
  _Out_ PUCX_USBDEVICE_EVENT_CALLBACKS          Callbacks,
  _In_  PEVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE  EvtUsbDeviceEndpointsConfigure,
  _In_  PEVT_UCX_USBDEVICE_ENABLE               EvtUsbDeviceEnable,
  _In_  PEVT_UCX_USBDEVICE_DISABLE              EvtUsbDeviceDisable,
  _In_  PEVT_UCX_USBDEVICE_RESET                EvtUsbDeviceReset,
  _In_  PEVT_UCX_USBDEVICE_ADDRESS              EvtUsbDeviceAddress,
  _In_  PEVT_UCX_USBDEVICE_UPDATE               EvtUsbDeviceUpdate,
  _In_  PEVT_UCX_USBDEVICE_HUB_INFO             EvtUsbDeviceHubInfo,
  _In_  PEVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD EvtUsbDeviceDefaultEndpointAdd,
  _In_  PEVT_UCX_USBDEVICE_ENDPOINT_ADD         EvtUsbDeviceEndpointAdd
);
````

## Parameters

`Callbacks`

A pointer to a <a href="..\ucxusbdevice\ns-ucxusbdevice-_ucx_usbdevice_event_callbacks.md">UCX_USBDEVICE_EVENT_CALLBACKS</a> structure to initialize.

`EvtUsbDeviceEndpointsConfigure`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_endpoints_configure.md">EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE</a> event callback function.

`EvtUsbDeviceEnable`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_enable.md">EVT_UCX_USBDEVICE_ENABLE</a> event callback function.

`EvtUsbDeviceDisable`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_disable.md">EVT_UCX_USBDEVICE_DISABLE</a> event callback function.

`EvtUsbDeviceReset`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_reset.md">EVT_UCX_USBDEVICE_RESET</a> event callback function.

`EvtUsbDeviceAddress`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_address.md">EVT_UCX_USBDEVICE_ADDRESS</a> event callback function.

`EvtUsbDeviceUpdate`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_update.md">EVT_UCX_USBDEVICE_UPDATE</a> event callback function.

`EvtUsbDeviceHubInfo`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_hub_info.md">EVT_UCX_USBDEVICE_HUB_INFO</a> event callback function.

`EvtUsbDeviceDefaultEndpointAdd`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_default_endpoint_add.md">EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD</a> event callback function.

`EvtUsbDeviceEndpointAdd`

A pointer to client driver's implementation of the <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_endpoint_add.md">EVT_UCX_USBDEVICE_ENDPOINT_ADD</a> event callback function.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdeviceinitseteventcallbacks.md">UcxUsbDeviceInitSetEventCallbacks</a>

<a href="..\ucxusbdevice\nf-ucxusbdevice-ucxusbdevicecreate.md">UcxUsbDeviceCreate</a>

<a href="..\ucxusbdevice\ns-ucxusbdevice-_ucx_usbdevice_event_callbacks.md">UCX_USBDEVICE_EVENT_CALLBACKS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_USBDEVICE_EVENT_CALLBACKS_INIT function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>