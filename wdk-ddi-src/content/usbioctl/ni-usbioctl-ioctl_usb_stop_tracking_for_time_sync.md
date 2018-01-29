---
UID : NI:usbioctl.IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC
title : IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC
author : windows-driver-content
description : This request unegisters the caller with USB driver stack for time sync services.
old-location : buses\_ioctl_usb_stop_tracking_for_time_sync.htm
old-project : usbref
ms.assetid : 232AC14B-CE3C-44AC-9428-5594993CD749
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses._ioctl_usb_stop_tracking_for_time_sync, IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC control code [Buses], IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC, usbioctl/ IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbioctl.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : USB_HUB_TYPE
req.product : Windows 10 or later.
---

# IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC IOCTL
This request unegisters the caller with USB driver stack for time sync services.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to a <a href="..\usbioctl\ns-usbioctl-_usb_stop_tracking_for_time_sync_information.md">USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION</a> structure that contains the time tracking handle previously received through the <a href="..\usbioctl\ni-usbioctl-ioctl_usb_start_tracking_for_time_sync.md">IOCTL_USB_START_TRACKING_FOR_TIME_SYNC</a> request.

### Input Buffer Length
The size of the <a href="..\usbioctl\ns-usbioctl-_usb_stop_tracking_for_time_sync_information.md">USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION</a> structure.

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> indicates an the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | usbioctl.h |
| **IRQL** | <= DISPATCH_LEVEL |

## See Also

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md">WdfIoTargetSendInternalIoctlSynchronously</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md">WdfIoTargetSendIoctlSynchronously</a>

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md">WdfIoTargetSendInternalIoctlOthersSynchronously</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20 IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC control code%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>