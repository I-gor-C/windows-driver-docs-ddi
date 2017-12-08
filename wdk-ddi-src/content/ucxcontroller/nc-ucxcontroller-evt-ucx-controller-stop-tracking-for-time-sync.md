---
UID: NC.ucxcontroller.EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC
title: EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC
author: windows-driver-content
description: UCX invokes this callback function to the stop time tracking functionality in the controller.
old-location: buses\evt_ucx_controller_stop_tracking_for_time_sync.htm
old-project: usbref
ms.assetid: C65A250A-594B-4317-AEE6-C3E60D122A1D
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvUcxControllerStopTrackingForTimeSync
req.alt-loc: Ucxcontroller.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC callback



## -description
<p>UCX invokes this callback function to the stop  time tracking functionality in the controller. </p>


## -prototype

````
EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC EvUcxControllerStopTrackingForTimeSync;

void EvUcxControllerStopTrackingForTimeSync(
  _In_ UCXCONTROLLER UcxController,
  _In_ WDFREQUEST    WdfRequest,
  _In_ size_t        OutputBufferLength,
  _In_ size_t        InputBufferLength
)
{ ... }
````


## -parameters
<dl>

### -param UcxController [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>
</dd>

### -param WdfRequest [in]

<dd>
<p>A framework request object that contains the request to stop time tracking.</p>
</dd>

### -param OutputBufferLength [in]

<dd>
<p>The length, in bytes, of the request's output buffer, if an output buffer
        is available. This value is the size of the <a href="..\usbioctl\ns-usbioctl--usb-stop-tracking-for-time-sync-information.md">USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION</a> structure. </p>
</dd>

### -param InputBufferLength [in]

<dd>
<p>The length, in bytes, of the request's input buffer, if an input buffer
        is available. This value is the size of the <a href="..\usbioctl\ns-usbioctl--usb-stop-tracking-for-time-sync-information.md">USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION</a> structure.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl-usb-stop-tracking-for-time-sync.md">IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
