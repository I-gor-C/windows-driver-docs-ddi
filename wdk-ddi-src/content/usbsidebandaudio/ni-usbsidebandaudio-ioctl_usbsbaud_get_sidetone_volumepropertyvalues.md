---
UID : NI:usbsidebandaudio.IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES
title : IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES
author : windows-driver-content
description : TBD
old-location : audio\ioctl_usbsbaud_get_sidetone_volumepropertyvalues.htm
old-project : audio
ms.assetid : 6FF44B7C-2252-45A0-A280-95D844448CF9
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : audio.ioctl_usbsbaud_get_sidetone_volumepropertyvalues, IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES control code [Audio Devices], IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES, usbsidebandaudio/IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : usbsidebandaudio.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PUSBSCAN_TIMEOUT, USBSCAN_TIMEOUT"
req.product : Windows 10 or later.
---

# IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES IOCTL
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
| **Windows Driver kit version** |  |
| **Header** | usbsidebandaudio.h |
| **IRQL** |  |

## See Also

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md">WdfIoTargetSendInternalIoctlSynchronously</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md">WdfIoTargetSendIoctlSynchronously</a>

<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md">WdfIoTargetSendInternalIoctlOthersSynchronously</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IOCTL_USBSBAUD_GET_SIDETONE_VOLUMEPROPERTYVALUES control code%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>