---
UID: NC:ucxendpoint.EVT_UCX_ENDPOINT_SET_CHARACTERISTIC
title: EVT_UCX_ENDPOINT_SET_CHARACTERISTIC
author: windows-driver-content
description: UCX invokes this callback function to set the priority on an endpoint.
old-location: buses\evt_ucx_endpoint_set_characteristic.htm
old-project: usbref
ms.assetid: 4FA3F175-52E4-472D-A9B3-B3B4B37E1701
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: EVT_UCX_ENDPOINT_SET_CHARACTERISTIC, EvtUcxEndpointSetCharacteristic, EvtUcxEndpointSetCharacteristic callback function [Buses], buses.evt_ucx_endpoint_set_characteristic, ucxendpoint/EvtUcxEndpointSetCharacteristic
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxendpoint.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
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
req.irql: "<=DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	Ucxendpoint.h
api_name:
-	EvtUcxEndpointSetCharacteristic
product: Windows
targetos: Windows
req.typenames: UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS
req.product: Windows 10 or later.
---


# EVT_UCX_ENDPOINT_SET_CHARACTERISTIC callback function
UCX invokes this callback function to set the priority on an endpoint.

## Syntax

```
EVT_UCX_ENDPOINT_SET_CHARACTERISTIC EvtUcxEndpointSetCharacteristic;

void EvtUcxEndpointSetCharacteristic(
  UCXENDPOINT UcxEndpoint,
  PUCX_ENDPOINT_CHARACTERISTIC UcxEndpointCharacteristic
)
{...}
```

## Parameters

`UcxEndpoint`



`UcxEndpointCharacteristic`

A pointer to a <a href="..\ucxendpoint\ns-ucxendpoint-_ucx_endpoint_characteristic.md">UCX_ENDPOINT_CHARACTERISTIC</a> structure that contains endpoint characteristics.


## Return Value

This callback function does not return a value.

## Remarks

The UCX client driver registers this callback function with the USB host controller extension (UCX) by calling the <a href="..\ucxendpoint\nf-ucxendpoint-ucxendpointcreate.md">UcxEndpointCreate</a>
 method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | ucxendpoint.h (include Ucxclass.h) |
| **IRQL** | "<=DISPATCH_LEVEL" |

## See Also

<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/usbcon/usb-client-drivers-for-ma-usb">USB client drivers for Media-Agnostic (MA-USB)</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_ENDPOINT_SET_CHARACTERISTIC callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>