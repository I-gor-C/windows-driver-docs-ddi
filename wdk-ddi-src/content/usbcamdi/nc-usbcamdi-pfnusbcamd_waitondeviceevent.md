---
UID : NC:usbcamdi.PFNUSBCAMD_WaitOnDeviceEvent
title : PFNUSBCAMD_WaitOnDeviceEvent
author : windows-driver-content
description : The USBCAMD_WaitOnDeviceEvent service is used to perform a read from the interrupt pipe if the camera has an interrupt pipe for external event notifications.
old-location : stream\usbcamd_waitondeviceevent.htm
old-project : stream
ms.assetid : b9767479-3ad9-4b47-82d1-70b54329e7b8
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _USB_BUS_INTERFACE_USBDI_V3, USB_BUS_INTERFACE_USBDI_V3, *PUSB_BUS_INTERFACE_USBDI_V3
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : usbcamdi.h
req.include-header : Usbcamdi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : USBCAMD_WaitOnDeviceEvent
req.alt-loc : usbcamdi.h
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
req.typenames : USB_BUS_INTERFACE_USBDI_V3, *PUSB_BUS_INTERFACE_USBDI_V3
req.product : Windows 10 or later.
---


# PFNUSBCAMD_WaitOnDeviceEvent callback function
The <b>USBCAMD_WaitOnDeviceEvent</b> service is used to perform a read from the interrupt pipe if the camera has an interrupt pipe for external event notifications.

## Syntax

```
PFNUSBCAMD_WaitOnDeviceEvent PfnusbcamdWaitondeviceevent;

NTSTATUS PfnusbcamdWaitondeviceevent(
  PVOID DeviceContext,
  ULONG PipeIndex,
  PVOID Buffer,
  ULONG BufferLength,
  PCOMMAND_COMPLETE_FUNCTION EventComplete,
  PVOID EventContext,
  BOOLEAN LoopBack
)
{...}
```

## Parameters

`DeviceContext`

A pointer to device-specific context.

`PipeIndex`

Specifies the index of the interrupt pipe.

`Buffer`

A pointer to the read buffer.

`BufferLength`

Length of the read buffer, in bytes.

`EventComplete`

Pointer to a camera minidriver defined <a href="..\usbcamdi\nc-usbcamdi-pcommand_complete_function.md">CommandCompleteFunction</a>, which is called when the interrupt read is completed This value can be <b>NULL</b>.

`EventContext`

Pointer to a block of memory, that is passed as an argument to the camera minidriver defined <a href="..\usbcamdi\nc-usbcamdi-pcommand_complete_function.md">CommandCompleteFunction</a>.

`LoopBack`

Specifies if USBCAMD is to resubmit another read request to the interrupt pipe every time an interrupt read is completed. Set to <b>TRUE</b>


## Return Value

<b>USBCAMD_WaitOnDeviceEvent</b> returns STATUS_SUCCESS if the call was successful. Other possible error codes include:
<dl>
<dt><b>STATUS_FILE_CLOSED</b></dt>
</dl>The device has been removed.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>USBCAMD may return STATUS_INVALID_PARAMETER for a number of reasons, including:

The value passed in the <i>PipeIndex</i> argument is invalid.

The type of the pipe specified by the <i>PipeIndex</i> argument represents an invalid type of pipe.

A bulk read/write request already exists.

The <i>Buffer</i> argument is <b>NULL</b>.

The length specified in the BufferLength argument is smaller than the maximum packet size.
<dl>
<dt><b>STATUS_PENDING</b></dt>
</dl>The event work item is deferred.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There are insufficient resources to allocate a work item to read from the pipe.

## Remarks

The typical usage scenario for this function is a camera with a snapshot button and an interrupt pipe associated with the button. When a user presses the snapshot button, the read request on the interrupt pipe is satisfied and the camera minidriver is called back. If the camera minidriver sets USBCAMD_CamControlFlag_EnableDeviceEvents in the <i>CamControlFlag</i> argument during the <a href="..\usbcamdi\nf-usbcamdi-usbcamd_initializenewinterface.md">USBCAMD_InitializeNewInterface</a> call, the STI monitor also is notified of the snapshot event.

<b>USBCAMD_WaitOnDeviceEvent</b> is not available in USBCAMD version 1.0.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usbcamdi.h (include Usbcamdi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\usbcamdi\nc-usbcamdi-pcommand_complete_function.md">CommandCompleteFunction</a>
</dt>
<dt>
<a href="..\usbcamdi\nf-usbcamdi-usbcamd_initializenewinterface.md">USBCAMD_InitializeNewInterface</a>
</dt>
<dt>
<a href="..\usbcamdi\ns-usbcamdi-usbcamd_interface.md">USBCAMD_INTERFACE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_WaitOnDeviceEvent routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>