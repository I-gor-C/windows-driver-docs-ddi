---
UID: NS.usbioctl._USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
title: USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
author: windows-driver-content
description: Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC request.
old-location: buses\usb_frame_number_and_qpc_for_time_sync_information.htm
ms.assetid: F602B738-4D04-4A75-BE69-CFEC4F76904C
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
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
ms.keywords: USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION, USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION, *PUSB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION structure



## -description
<p>Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the <a href="https://msdn.microsoft.com/701A7ED2-F35F-4B6B-BC91-ADCF60E294D2">IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC</a> request.</p>


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

### -field <b>TimeTrackingHandle</b>

<dd>
<p>The time racking handle received in the previous <a href="https://msdn.microsoft.com/232AC14B-CE3C-44AC-9428-5594993CD749">IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC</a> request.</p>
</dd>

### -field <b>InputFrameNumber</b>

<dd>
<p>A 32-bit USB bus frame number. </p>
</dd>

### -field <b>InputMicroFrameNumber</b>

<dd>
<p>A 3-bit value received from the hardware. </p>
</dd>

### -field <b>QueryPerformanceCounterAtInputFrameOrMicroFrame</b>

<dd>
<p>A value predicted by the USB driver stack that represents the system QPC value at the beginning of the frame and microframe represented by the <b>InputFrameNumber</b> and <b>InputMicroFrameNumber</b> input values.  

</p>
</dd>

### -field <b>QueryPerformanceCounterFrequency</b>

<dd>
<p>The current performance-counter frequency, in counts per second.</p>
</dd>

### -field <b>PredictedAccuracyInMicroSeconds</b>

<dd>
<p>A value that represents the accuracy of the predicted QPC value in micro seconds. 

</p>
</dd>

### -field <b>CurrentGenerationID</b>

<dd>
<p>An identifier for this request of time synchronization. </p>
</dd>

### -field <b>CurrentQueryPerformanceCounter</b>

<dd>
<p>Current QPC value captured that is synchronized with the bus frame numbers represented by <b>CurrentHardwareFrameNumber</b>, <b>CurrentHardwareMicroFrameNumber</b> and <b>CurrentUSBFrameNumber</b>. 



 
</p>
</dd>

### -field <b>CurrentHardwareFrameNumber</b>

<dd>
<p>A 1-bit value of the current hardware frame number that is directly read  from the MFINDEX register. 

</p>
</dd>

### -field <b>CurrentHardwareMicroFrameNumber</b>

<dd>
<p>A 3-bit value of the current hardware micro frame number that is  directly read from the MFINDEX register. 

</p>
</dd>

### -field <b>CurrentUSBFrameNumber</b>

<dd>
<p>A 32-bit USB frame number value returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff540401">_URB_GET_CURRENT_FRAME_NUMBER</a>.</p>
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