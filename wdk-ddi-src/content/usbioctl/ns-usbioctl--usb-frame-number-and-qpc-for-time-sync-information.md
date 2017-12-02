---
UID: NS.usbioctl._USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
title: USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
author: windows-driver-content
description: Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC request.
old-location: buses\usb_frame_number_and_qpc_for_time_sync_information.htm
old-project: usbref
ms.assetid: F602B738-4D04-4A75-BE69-CFEC4F76904C
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION, USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION, *PUSB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
req.alt-loc: Usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION structure



## -description
<p>Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-frame-number-and-qpc-for-time-sync.md">IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC</a> request.</p>


## -syntax

````
typedef struct _USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION {
  HANDLE        TimeTrackingHandle;
  ULONG         InputFrameNumber;
  ULONG         InputMicroFrameNumber;
  LARGE_INTEGER QueryPerformanceCounterAtInputFrameOrMicroFrame;
  LARGE_INTEGER QueryPerformanceCounterFrequency;
  ULONG         PredictedAccuracyInMicroSeconds;
  ULONG         CurrentGenerationID;
  LARGE_INTEGER CurrentQueryPerformanceCounter;
  ULONG         CurrentHardwareFrameNumber;
  ULONG         CurrentHardwareMicroFrameNumber;
  ULONG         CurrentUSBFrameNumber;
} USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION, *PUSB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION;
````


## -struct-fields
<dl>

### -field TimeTrackingHandle

<dd>
<p>The time racking handle received in the previous <a href="..\usbioctl\ni-usbioctl-ioctl-usb-stop-tracking-for-time-sync.md">IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC</a> request.</p>
</dd>

### -field InputFrameNumber

<dd>
<p>A 32-bit USB bus frame number. </p>
</dd>

### -field InputMicroFrameNumber

<dd>
<p>A 3-bit value received from the hardware. </p>
</dd>

### -field QueryPerformanceCounterAtInputFrameOrMicroFrame

<dd>
<p>A value predicted by the USB driver stack that represents the system QPC value at the beginning of the frame and microframe represented by the <b>InputFrameNumber</b> and <b>InputMicroFrameNumber</b> input values.  

</p>
</dd>

### -field QueryPerformanceCounterFrequency

<dd>
<p>The current performance-counter frequency, in counts per second.</p>
</dd>

### -field PredictedAccuracyInMicroSeconds

<dd>
<p>A value that represents the accuracy of the predicted QPC value in micro seconds. 

</p>
</dd>

### -field CurrentGenerationID

<dd>
<p>An identifier for this request of time synchronization. </p>
</dd>

### -field CurrentQueryPerformanceCounter

<dd>
<p>Current QPC value captured that is synchronized with the bus frame numbers represented by <b>CurrentHardwareFrameNumber</b>, <b>CurrentHardwareMicroFrameNumber</b> and <b>CurrentUSBFrameNumber</b>. 



 
</p>
</dd>

### -field CurrentHardwareFrameNumber

<dd>
<p>A 1-bit value of the current hardware frame number that is directly read  from the MFINDEX register. 

</p>
</dd>

### -field CurrentHardwareMicroFrameNumber

<dd>
<p>A 3-bit value of the current hardware micro frame number that is  directly read from the MFINDEX register. 

</p>
</dd>

### -field CurrentUSBFrameNumber

<dd>
<p>A 32-bit USB frame number value returned by <a href="buses._urb_get_current_frame_number">_URB_GET_CURRENT_FRAME_NUMBER</a>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h</dt>
</dl>
</td>
</tr>
</table>