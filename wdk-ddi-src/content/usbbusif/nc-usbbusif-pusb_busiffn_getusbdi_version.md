---
UID: NC:usbbusif.PUSB_BUSIFFN_GETUSBDI_VERSION
title: PUSB_BUSIFFN_GETUSBDI_VERSION
author: windows-driver-content
description: The GetUSBDIVersion routine returns the USB interface version number and the version number of the USB specification that defines the interface, along with information about host controller capabilities.
old-location: buses\getusbdiversion.htm
old-project: UsbRef
ms.assetid: 05a22049-5165-41a3-aa6f-134c5d1b6c15
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: buses.getusbdiversion, GetUSBDIVersion, PUSB_BUSIFFN_GETUSBDI_VERSION, GetUSBDIVersion callback function [Buses], GetUSBDIVersion, USB_BUSIFFN_GETUSBDI_VERSION, USB_BUSIFFN_GETUSBDI_VERSION, usbbusif/GetUSBDIVersion, usbinterKR_48f5b2a5-9cd8-46c2-abf9-313469817541.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbbusif.h
req.include-header: Usbbusif.h
req.target-type: Desktop
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
req.irql: "< = DISPATCH_LEVEL"
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	usbbusif.h
apiname:
-	GetUSBDIVersion
product: Windows
targetos: Windows
req.typenames: "*PUSBD_VERSION_INFORMATION, USBD_VERSION_INFORMATION"
req.product: Windows 10 or later.
---


# PUSB_BUSIFFN_GETUSBDI_VERSION callback function
The <b>GetUSBDIVersion</b> routine returns the USB interface version number and the version number of the USB specification that defines the interface, along with information about host controller capabilities. 
<div class="alert"><b>Note</b>  <a href="..\usbdlib\nf-usbdlib-usbd_isinterfaceversionsupported.md">USBD_IsInterfaceVersionSupported</a> replaces the <b>GetUSBDIVersion</b>  routine. To determine the capabilities of the host controller and the underlying USB driver stack, call <a href="https://msdn.microsoft.com/library/windows/hardware/hh406230">USBD_QueryUsbCapability</a>.</div><div> </div>

## Syntax

```
PUSB_BUSIFFN_GETUSBDI_VERSION PusbBusiffnGetusbdiVersion;

void PusbBusiffnGetusbdiVersion(
  PVOID ,
  PUSBD_VERSION_INFORMATION ,
  PULONG 
)
{...}
```

## Parameters

`Arg1`



`Arg1`



`Arg1`




## Return Value

This callback function does not return a value.

## Remarks

The function returns the highest USBDI Interface Version supported by the port driver. This function replaces the <a href="..\usbdlib\nf-usbdlib-usbd_getusbdiversion.md">USBD_GetUSBDIVersion</a> library function provided by usbd.sys. 

The function definition that is provided on this reference page is an example function whose parameters are just placeholder names. The actual prototype of the function is declared in usbbusif.h as follows:

<pre class="syntax" xml:space="preserve"><code>typedef VOID
  (USB_BUSIFFN *PUSB_BUSIFFN_GETUSBDI_VERSION) (
    IN PVOID,
    IN OUT PUSBD_VERSION_INFORMATION,
    IN OUT PULONG 
  );</code></pre>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | usbbusif.h (include Usbbusif.h) |
| **IRQL** | "< = DISPATCH_LEVEL" |

## See Also

<a href="..\usbdlib\nf-usbdlib-usbd_getusbdiversion.md">USBD_GetUSBDIVersion</a>



<a href="..\usbbusif\ns-usbbusif-_usb_bus_interface_usbdi_v0.md">USB_BUS_INTERFACE_USBDI_V0</a>



<a href="..\usb\ns-usb-_usbd_version_information.md">USBD_VERSION_INFORMATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [UsbRef\buses]:%20USB_BUSIFFN_GETUSBDI_VERSION callback function%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>