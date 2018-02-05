---
UID : NI:ntddstor.IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS
title : IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS
author : windows-driver-content
description : The IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS control code queries for and returns the physical element status from a device.
old-location : storage\ioctl_storage_get_physical_element_status.htm
old-project : storage
ms.assetid : ED46241E-1A71-447A-8D96-E81B4500E070
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : storage.ioctl_storage_get_physical_element_status, IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS control code [Storage Devices], IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS, ntddstor/IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : ioctl
req.header : ntddstor.h
req.include-header : WinIoctl.h
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
req.typenames : STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION
---

# IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS IOCTL
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS</b> 
   control code queries for and returns  the physical element status from a device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<text></text>

### Input Buffer Length
<text></text>

### Output Buffer
<text></text>

### Output Buffer Length
<text></text>

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].

## Remarks
To perform this operation, call the <a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a> 
   function with the following parameters.


<pre class="syntax">BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         // handle to device
                    (DWORD)        IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure</pre>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include WinIoctl.h) |

## See Also

<a href="https://msdn.microsoft.com/A0876712-4D9B-4A97-8E94-AA570A71C53D">PHYSICAL_ELEMENT_STATUS_REQUEST</a>

<a href="https://msdn.microsoft.com/1d35c087-6672-4fc6-baa1-a886dd9d3878">DeviceIoControl</a>

<a href="https://msdn.microsoft.com/5E2AB36E-5A5C-4253-9791-A5CC157F15E3">PHYSICAL_ELEMENT_STATUS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS control code%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>