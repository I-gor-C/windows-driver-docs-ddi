---
UID: NS:wwan._WWAN_DEVICE_SERVICE_COMMAND
title: "_WWAN_DEVICE_SERVICE_COMMAND"
author: windows-driver-content
description: The WWAN_DEVICE_SERVICE_COMMAND structure represents a device service command.
old-location: netvista\wwan_device_service_command.htm
old-project: netvista
ms.assetid: 475D7ECF-B8A8-445D-8ED7-029BD57C8C48
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_DEVICE_SERVICE_COMMAND, PWWAN_DEVICE_SERVICE_COMMAND, PWWAN_DEVICE_SERVICE_COMMAND structure pointer [Network Drivers Starting with Windows Vista], WWAN_DEVICE_SERVICE_COMMAND, WWAN_DEVICE_SERVICE_COMMAND structure [Network Drivers Starting with Windows Vista], _WWAN_DEVICE_SERVICE_COMMAND, netvista.wwan_device_service_command, wwan/PWWAN_DEVICE_SERVICE_COMMAND, wwan/WWAN_DEVICE_SERVICE_COMMAND"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
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
-	wwan.h
api_name:
-	WWAN_DEVICE_SERVICE_COMMAND
product: Windows
targetos: Windows
req.typenames: WWAN_DEVICE_SERVICE_COMMAND, *PWWAN_DEVICE_SERVICE_COMMAND
req.product: Windows 10 or later.
---

# _WWAN_DEVICE_SERVICE_COMMAND structure
The WWAN_DEVICE_SERVICE_COMMAND structure represents a device service command.

## Syntax
````
typedef struct _WWAN_DEVICE_SERVICE_COMMAND {
  GUID  DeviceServiceGuid;
  ULONG CommandID;
  ULONG uDataSize;
} WWAN_DEVICE_SERVICE_COMMAND, *PWWAN_DEVICE_SERVICE_COMMAND;
````

## Members


`DeviceServiceGuid`

The GUID of the device service that the command targets.

`CommandID`

The ID for the command.

`uDataSize`

The size, in bytes, of the device service command data that follows the structure instance in memory. This value should not exceed the value of the <b>uMaxCommandDataSize</b> member of the <a href="..\wwan\ns-wwan-_wwan_supported_device_services.md">WWAN_SUPPORTED_DEVICE_SERVICES</a> structure.

## Remarks
Device service command OIDs use this structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with  Windows 8. Supported starting with  Windows 8. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\wwan\ns-wwan-_wwan_supported_device_services.md">WWAN_SUPPORTED_DEVICE_SERVICES</a>