---
UID: NC.usbcamdi.PFNUSBCAMD_WaitOnDeviceEvent
title: PFNUSBCAMD_WaitOnDeviceEvent
author: windows-driver-content
description: The USBCAMD_WaitOnDeviceEvent service is used to perform a read from the interrupt pipe if the camera has an interrupt pipe for external event notifications.
old-location: stream\usbcamd_waitondeviceevent.htm
old-project: stream
ms.assetid: b9767479-3ad9-4b47-82d1-70b54329e7b8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: USBC_FUNCTION_DESCRIPTOR, USBC_FUNCTION_DESCRIPTOR, *PUSBC_FUNCTION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_WaitOnDeviceEvent
req.alt-loc: usbcamdi.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PFNUSBCAMD_WaitOnDeviceEvent callback



## -description
<p>The <b>USBCAMD_WaitOnDeviceEvent</b> service is used to perform a read from the interrupt pipe if the camera has an interrupt pipe for external event notifications.</p>


## -prototype

````
PFNUSBCAMD_WaitOnDeviceEvent USBCAMD_WaitOnDeviceEvent;

NTSTATUS APIENTRY USBCAMD_WaitOnDeviceEvent(
  _In_ PVOID                      DeviceContext,
  _In_ ULONG                      PipeIndex,
  _In_ PVOID                      Buffer,
  _In_ ULONG                      BufferLength,
  _In_ PCOMMAND_COMPLETE_FUNCTION EventComplete,
  _In_ PVOID                      EventContext,
  _In_ BOOLEAN                    LoopBack
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceContext</i> [in]

<dd>
<p>A pointer to device-specific context.</p>
</dd>

### -param <i>PipeIndex</i> [in]

<dd>
<p>Specifies the index of the interrupt pipe.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the read buffer.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>Length of the read buffer, in bytes.</p>
</dd>

### -param <i>EventComplete</i> [in]

<dd>
<p>Pointer to a camera minidriver defined <a href="stream.commandcompletefunction">CommandCompleteFunction</a>, which is called when the interrupt read is completed This value can be <b>NULL</b>.</p>
</dd>

### -param <i>EventContext</i> [in]

<dd>
<p>Pointer to a block of memory, that is passed as an argument to the camera minidriver defined <a href="stream.commandcompletefunction">CommandCompleteFunction</a>.</p>
</dd>

### -param <i>LoopBack</i> [in]

<dd>
<p>Specifies if USBCAMD is to resubmit another read request to the interrupt pipe every time an interrupt read is completed. Set to <b>TRUE</b></p>
</dd>
</dl>

## -returns
<p><b>USBCAMD_WaitOnDeviceEvent</b> returns STATUS_SUCCESS if the call was successful. Other possible error codes include:</p><dl>
<dt><b>STATUS_FILE_CLOSED</b></dt>
</dl><p>The device has been removed.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>USBCAMD may return STATUS_INVALID_PARAMETER for a number of reasons, including:</p>

<p>The value passed in the <i>PipeIndex</i> argument is invalid.</p>

<p>The type of the pipe specified by the <i>PipeIndex</i> argument represents an invalid type of pipe.</p>

<p>A bulk read/write request already exists.</p>

<p>The <i>Buffer</i> argument is <b>NULL</b>.</p>

<p>The length specified in the BufferLength argument is smaller than the maximum packet size.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The event work item is deferred.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There are insufficient resources to allocate a work item to read from the pipe.</p>

<p> </p>

## -remarks
<p>The typical usage scenario for this function is a camera with a snapshot button and an interrupt pipe associated with the button. When a user presses the snapshot button, the read request on the interrupt pipe is satisfied and the camera minidriver is called back. If the camera minidriver sets USBCAMD_CamControlFlag_EnableDeviceEvents in the <i>CamControlFlag</i> argument during the <a href="..\usbcamdi\nf-usbcamdi-usbcamd-initializenewinterface.md">USBCAMD_InitializeNewInterface</a> call, the STI monitor also is notified of the snapshot event.</p>

<p><b>USBCAMD_WaitOnDeviceEvent</b> is not available in USBCAMD version 1.0.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.commandcompletefunction">CommandCompleteFunction</a>
</dt>
<dt>
<a href="..\usbcamdi\nf-usbcamdi-usbcamd-initializenewinterface.md">USBCAMD_InitializeNewInterface</a>
</dt>
<dt>
<a href="stream.usbcamd_interface">USBCAMD_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_WaitOnDeviceEvent routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
