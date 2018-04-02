---
UID: NE:usbioctl._USB_CONNECTION_STATUS
title: "_USB_CONNECTION_STATUS"
author: windows-driver-content
description: The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port.
old-location: buses\usb_connection_status.htm
old-project: usbref
ms.assetid: 9006f74f-4033-4f07-816c-380d6d8b3a2d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSB_CONNECTION_STATUS, DeviceCausedOvercurrent, DeviceConnected, DeviceEnumerating, DeviceFailedEnumeration, DeviceGeneralFailure, DeviceHubNestedTooDeeply, DeviceInLegacyHub, DeviceNotEnoughBandwidth, DeviceNotEnoughPower, DeviceReset, NoDeviceConnected, PUSB_CONNECTION_STATUS, PUSB_CONNECTION_STATUS enumeration pointer [Buses], USB_CONNECTION_STATUS, USB_CONNECTION_STATUS enumeration [Buses], _USB_CONNECTION_STATUS, buses.usb_connection_status, usbioctl/DeviceCausedOvercurrent, usbioctl/DeviceConnected, usbioctl/DeviceEnumerating, usbioctl/DeviceFailedEnumeration, usbioctl/DeviceGeneralFailure, usbioctl/DeviceHubNestedTooDeeply, usbioctl/DeviceInLegacyHub, usbioctl/DeviceNotEnoughBandwidth, usbioctl/DeviceNotEnoughPower, usbioctl/DeviceReset, usbioctl/NoDeviceConnected, usbioctl/PUSB_CONNECTION_STATUS, usbioctl/USB_CONNECTION_STATUS, usbstrct_3f747b8b-9fe5-48f1-bfc4-3701ab8be8e9.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbioctl.h
req.include-header: Usbioctl.h
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
-	usbioctl.h
api_name:
-	USB_CONNECTION_STATUS
product:
- Windows
targetos: Windows
req.typenames: USB_CONNECTION_STATUS, *PUSB_CONNECTION_STATUS, USB_CONNECTION_STATUS, *PUSB_CONNECTION_STATUS, USB_CONNECTION_STATUS, *PUSB_CONNECTION_STATUS
req.product: Windows 10 or later.
---

# _USB_CONNECTION_STATUS Enumeration
The <b>USB_CONNECTION_STATUS</b> enumerator indicates the status of the connection to a device on a USB hub port.

## Syntax
```
typedef enum _USB_CONNECTION_STATUS {
  NoDeviceConnected         ,
  DeviceConnected           ,
  DeviceFailedEnumeration   ,
  DeviceGeneralFailure      ,
  DeviceCausedOvercurrent   ,
  DeviceNotEnoughPower      ,
  DeviceNotEnoughBandwidth  ,
  DeviceHubNestedTooDeeply  ,
  DeviceInLegacyHub         ,
  DeviceEnumerating         ,
  DeviceReset
} USB_CONNECTION_STATUS, *PUSB_CONNECTION_STATUS;
```

## Constants

<table>
            
                <tr>
                    <td>NoDeviceConnected</td>
                    <td>Indicates that there is no device connected to the port.</td>
                </tr>
            
                <tr>
                    <td>DeviceConnected</td>
                    <td>Indicates that a device was successfully connected to the port.</td>
                </tr>
            
                <tr>
                    <td>DeviceFailedEnumeration</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but the enumeration of the device failed.</td>
                </tr>
            
                <tr>
                    <td>DeviceGeneralFailure</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but the connection failed for unspecified reasons.</td>
                </tr>
            
                <tr>
                    <td>DeviceCausedOvercurrent</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but the attempt failed because of an overcurrent condition.</td>
                </tr>
            
                <tr>
                    <td>DeviceNotEnoughPower</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but there was not enough power to drive the device, and the connection failed.</td>
                </tr>
            
                <tr>
                    <td>DeviceNotEnoughBandwidth</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but there was not enough bandwidth available for the device to function properly, and the connection failed.</td>
                </tr>
            
                <tr>
                    <td>DeviceHubNestedTooDeeply</td>
                    <td>Indicates that an attempt was made to connect a device to the port, but the nesting of USB hubs was too deep, so the connection failed.</td>
                </tr>
            
                <tr>
                    <td>DeviceInLegacyHub</td>
                    <td>Indicates that an attempt was made to connect a device to the port of an unsupported legacy hub, and the connection failed.</td>
                </tr>
            
                <tr>
                    <td>DeviceEnumerating</td>
                    <td>Indicates that a device connected to the port is currently being enumerated.  

<b>Note</b>  This constant is supported in Windows Vista and later operating systems.</td>
                </tr>
            
                <tr>
                    <td>DeviceReset</td>
                    <td>Indicates that device connected to the port is currently being reset.  

<b>Note</b>  This constant is supported in Windows Vista and later operating systems.</td>
                </tr>
</table>

## Remarks

The USB bus driver reports connection status in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540094">USB_NODE_CONNECTION_INFORMATION_EX</a> structure in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537321">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a> request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537321">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539322">USB Constants and Enumerations</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540094">USB_NODE_CONNECTION_INFORMATION_EX</a>