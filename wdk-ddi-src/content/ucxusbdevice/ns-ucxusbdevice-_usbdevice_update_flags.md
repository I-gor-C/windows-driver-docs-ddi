---
UID: NS:ucxusbdevice._USBDEVICE_UPDATE_FLAGS
title: "_USBDEVICE_UPDATE_FLAGS"
author: windows-driver-content
description: Contains request flags set by UCX that is passed in the USBDEVICE_UPDATE structure when UCX invokes the client driver's EVT_UCX_USBDEVICE_UPDATE callback function.
old-location: buses\_usbdevice_update_flags.htm
old-project: usbref
ms.assetid: 36F009C8-046B-437A-83D6-AE8D5BF51AF3
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: P_USBDEVICE_UPDATE_FLAGS, P_USBDEVICE_UPDATE_FLAGS structure pointer [Buses], USBDEVICE_UPDATE_FLAGS, USBDEVICE_UPDATE_FLAGS structure [Buses], _USBDEVICE_UPDATE_FLAGS, buses._usbdevice_update_flags, ucxusbdevice/P_USBDEVICE_UPDATE_FLAGS, ucxusbdevice/_USBDEVICE_UPDATE_FLAGS
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
-	USBDEVICE_UPDATE_FLAGS
product: Windows
targetos: Windows
req.typenames: USBDEVICE_UPDATE_FLAGS
req.product: Windows 10 or later.
---

# _USBDEVICE_UPDATE_FLAGS structure
Contains request flags set by UCX that is  passed in the <a href="..\ucxusbdevice\ns-ucxusbdevice-_usbdevice_update.md">USBDEVICE_UPDATE</a> structure when UCX invokes the client driver's <a href="..\ucxusbdevice\nc-ucxusbdevice-evt_ucx_usbdevice_update.md">EVT_UCX_USBDEVICE_UPDATE</a> callback function.

## Syntax
````
typedef struct _USBDEVICE_UPDATE_FLAGS {
  ULONG UpdateDeviceDescriptor  :1;
  ULONG UpdateBosDescriptor  :1;
  ULONG UpdateMaxExitLatency  :1;
  ULONG UpdateIsHub  :1;
  ULONG UpdateAllowIoOnInvalidPipeHandles  :1;
  ULONG Update20HardwareLpmParameters  :1;
  ULONG UpdateRootPortResumeTime  :1;
  ULONG Reserved  :26;
} USBDEVICE_UPDATE_FLAGS, *P_USBDEVICE_UPDATE_FLAGS;
````

## Members


`UpdateDeviceDescriptor`

If set, indicates a request to update the USB device descriptor.

`UpdateBosDescriptor`

If set, indicates a request to update the USB BOS descriptor.

`UpdateMaxExitLatency`

If set, indicates a request to update the maximum exit latency.

`UpdateIsHub`

If set, indicates a request to determine of the device is a hub.

`UpdateAllowIoOnInvalidPipeHandles`

If set, indicates the USB device or hub has been updated to allow I/O with invalid pipe handles.

`Update20HardwareLpmParameters`

If set, indicates a request to update the 2.0 LPM state.

`UpdateRootPortResumeTime`

If set, indicates a request to  update the root port resume time.

`Reserved`

Do not use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |

## See Also

<a href="..\ucxusbdevice\ns-ucxusbdevice-_usbdevice_update_failure_flags.md">USBDEVICE_UPDATE_FAILURE_FLAGS</a>



<a href="..\ucxusbdevice\ns-ucxusbdevice-_usbdevice_update_20_hardware_lpm_parameters.md">USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS</a>



<a href="..\ucxusbdevice\ns-ucxusbdevice-_usbdevice_update.md">USBDEVICE_UPDATE</a>