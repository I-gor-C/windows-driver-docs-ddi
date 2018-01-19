---
UID : NA:wudfusb
ms.assetid : 1287e4d2-981d-3a09-9dad-4006e24cb476
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# wudfusb.h header



wudfusb.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete.md) | IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed.md) | IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface. |
| [IWDFUsbInterface](nn-wudfusb-iwdfusbinterface.md) | The IWDFUsbInterface interface exposes a USB interface that a USB device exposes. |
| [IWDFUsbRequestCompletionParams](nn-wudfusb-iwdfusbrequestcompletionparams.md) | The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers. |
| [IWDFUsbTargetDevice](nn-wudfusb-iwdfusbtargetdevice.md) | The IWDFUsbTargetDevice interface exposes a USB device I/O target object. |
| [IWDFUsbTargetFactory](nn-wudfusb-iwdfusbtargetfactory.md) | The IWDFUsbTargetFactory interface is a factory interface that is used to create a USB target device object. |
| [IWDFUsbTargetPipe](nn-wudfusb-iwdfusbtargetpipe.md) | The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IWDFUsbTargetPipe2](nn-wudfusb-iwdfusbtargetpipe2.md) | The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target. |






## Enumerations
| Title | Description |
| ---- |:---- |
| [_WDF_USB_REQUEST_TYPE](ne-wudfusb-_wdf_usb_request_type.md) | The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object. |