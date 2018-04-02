---
UID: NI:usbsidebandaudio.IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE
title: IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE
author: windows-driver-content
description: TBD
old-location: audio\ioctl_usbsbaud_get_stream_status_update.htm
old-project: audio
ms.assetid: F50F7AEC-EEF5-4055-9877-8FE221177D12
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE, IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE control code [Audio Devices], audio.ioctl_usbsbaud_get_stream_status_update, usbsidebandaudio/IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: usbsidebandaudio.h
req.include-header: 
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
-	USBSidebandAudio.h
api_name:
-	IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE
product:
- Windows
targetos: Windows
req.typenames: USBSCAN_TIMEOUT, *PUSBSCAN_TIMEOUT
req.product: Windows 10 or later.
---

# IOCTL_USBSBAUD_GET_STREAM_STATUS_UPDATE IOCTL
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

TBD

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
TBD

### Input Buffer Length
None

### Output Buffer
TBD

### Output Buffer Length
TBD

### Input / Output Buffer
TBD

### Input / Output Buffer Length
TBD

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

## Remarks
TBD

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbsidebandaudio.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>