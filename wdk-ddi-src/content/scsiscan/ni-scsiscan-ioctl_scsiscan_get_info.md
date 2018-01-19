---
UID : NI:scsiscan.IOCTL_SCSISCAN_GET_INFO
title : IOCTL_SCSISCAN_GET_INFO
author : windows-driver-content
description : The IOCTL_SCSISCAN_GET_INFO I/O control code returns device information.
old-location : image\ioctl_scsiscan_get_info.htm
old-project : image
ms.assetid : 48045e29-5982-44e6-b9a7-3b000e5cf338
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : _ZONE_DESCRIPTIOR, ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : scsiscan.h
req.include-header : Scsiscan.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IOCTL_SCSISCAN_GET_INFO
req.alt-loc : scsiscan.h
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
req.typenames : ZONE_DESCRIPTIOR, *PZONE_DESCRIPTIOR
req.product : Windows 10 or later.
---

# IOCTL_SCSISCAN_GET_INFO IOCTL
The <b>IOCTL_SCSISCAN_GET_INFO</b> I/O control code returns device information.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
Set to NULL.

### Input Buffer Length
Set to 0.

### Output Buffer
Pointer to a <a href="..\scsiscan\ns-scsiscan-_scsiscan_info.md">SCSISCAN_INFO</a> structure.

### Output Buffer Length
Size of output buffer.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
I/O Status block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

    ## Remarks
        When the DeviceloControl function is called with the <b>IOCTL_SCSISCAN_GET_INFO</b> I/O control code, the caller must specify the address of a SCSISCAN_INFO structure as the function's lpOutbuffer parameter. The kernel-mode driver fills in the structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Header** | scsiscan.h (include Scsiscan.h) |
| **IRQL** |  |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md">WdfIoTargetSendInternalIoctlOthersSynchronously</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md">WdfIoTargetSendInternalIoctlSynchronously</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md">WdfIoTargetSendIoctlSynchronously</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IOCTL_SCSISCAN_GET_INFO control code%20 RELEASE:%20(1/17/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>