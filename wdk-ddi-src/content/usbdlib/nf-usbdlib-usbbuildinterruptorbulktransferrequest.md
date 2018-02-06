---
UID: NF:usbdlib.UsbBuildInterruptOrBulkTransferRequest
title: UsbBuildInterruptOrBulkTransferRequest macro
author: windows-driver-content
description: The UsbBuildInterruptOrBulkTransferRequest macro formats an URB to send or receive data on a bulk pipe, or to receive data from an interrupt pipe.
old-location: buses\usbbuildinterruptorbulktransferrequest.htm
old-project: usbref
ms.assetid: 2500fa22-b3f9-419d-9e37-5060b83403fb
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: buses.usbbuildinterruptorbulktransferrequest, UsbBuildInterruptOrBulkTransferRequest routine [Buses], usbfunc_ecc1d157-942d-4d0e-9c07-9fef00cd5faf.xml, UsbBuildInterruptOrBulkTransferRequest, usbdlib/UsbBuildInterruptOrBulkTransferRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: usbdlib.h
req.include-header: Usbdlib.h
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
req.lib: usbdlib.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	usbdlib.h
apiname:
-	UsbBuildInterruptOrBulkTransferRequest
product: Windows
targetos: Windows
req.typenames: USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2
req.product: Windows 10 or later.
---


# UsbBuildInterruptOrBulkTransferRequest function
The <b>UsbBuildInterruptOrBulkTransferRequest</b> macro formats an <a href="..\usb\ns-usb-_urb.md">URB</a> to send or receive data on a bulk pipe, or to receive data from an interrupt pipe.

## Syntax

````
void UsbBuildInterruptOrBulkTransferRequest(
  _Inout_  PURB             Urb,
  _In_     USHORT           Length,
  _In_     USBD_PIPE_HANDLE PipeHandle,
  _In_opt_ PVOID            TransferBuffer,
  _In_opt_ PMDL             TransferBufferMDL,
  _In_     ULONG            TransferBufferLength,
  _In_     ULONG            TransferFlags,
  _In_     PURB             Link
);
````

## Parameters

`urb`

TBD

`length`

TBD

`pipeHandle`

TBD

`transferBuffer`

TBD

`transferBufferMDL`

TBD

`transferBufferLength`

TBD

`transferFlags`

TBD

`link`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | usbdlib.h (include Usbdlib.h) |
| **Library** | usbdlib.h |

## See Also

<a href="..\usbspec\ns-usbspec-_usb_device_descriptor.md">USB_DEVICE_DESCRIPTOR</a>

<a href="..\usb\ns-usb-_urb.md">URB</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540134">USB device driver programming reference</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UsbBuildInterruptOrBulkTransferRequest routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>