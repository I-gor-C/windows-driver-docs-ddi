---
UID: NC:usbbusif.PUSB_BUSIFFN_GETUSBDI_VERSION
title: PUSB_BUSIFFN_GETUSBDI_VERSION
author: windows-driver-content
description: The GetUSBDIVersion routine returns the USB interface version number and the version number of the USB specification that defines the interface, along with information about host controller capabilities.
old-location: buses\getusbdiversion.htm
old-project: usbref
ms.assetid: 05a22049-5165-41a3-aa6f-134c5d1b6c15
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: GetUSBDIVersion, GetUSBDIVersion callback function [Buses], PUSB_BUSIFFN_GETUSBDI_VERSION, USB_BUSIFFN_GETUSBDI_VERSION, buses.getusbdiversion, usbbusif/GetUSBDIVersion, usbinterKR_48f5b2a5-9cd8-46c2-abf9-313469817541.xml
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	usbbusif.h
api_name:
-	GetUSBDIVersion
product:
- Windows
targetos: Windows
req.typenames: USBD_VERSION_INFORMATION, *PUSBD_VERSION_INFORMATION
req.product: Windows 10 or later.
---


# PUSB_BUSIFFN_GETUSBDI_VERSION callback function
The <b>GetUSBDIVersion</b> routine returns the USB interface version number and the version number of the USB specification that defines the interface, along with information about host controller capabilities. 
<div class="alert"><b>Note</b>  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406233">USBD_IsInterfaceVersionSupported</a> replaces the <b>GetUSBDIVersion</b>  routine. To determine the capabilities of the host controller and the underlying USB driver stack, call <a href="https://msdn.microsoft.com/library/windows/hardware/hh406230">USBD_QueryUsbCapability</a>.</div><div> </div>

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

The function returns the highest USBDI Interface Version supported by the port driver. This function replaces the <a href="https://msdn.microsoft.com/library/windows/hardware/ff539063">USBD_GetUSBDIVersion</a> library function provided by usbd.sys. 

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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539063">USBD_GetUSBDIVersion</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539149">USBD_VERSION_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539210">USB_BUS_INTERFACE_USBDI_V0</a>