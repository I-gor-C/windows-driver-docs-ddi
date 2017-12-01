---
UID: NC.ucxcontroller.EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC
title: EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC
author: windows-driver-content
description: UCX invokes this callback to retrieves the system query performance counter (QPC) value synchronized with the frame and microframe.
old-location: buses\evt_ucx_controller_get_frame_number_and_qpc_for_time_sync.htm
old-project: usbref
ms.assetid: A8D666BD-5C2A-416F-901E-5FF7CF38A084
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
req.alt-api: EvtUcxControllerGetFrameNumberAndQpcForTimeSync
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

# EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC callback



## -description
<p>UCX invokes this callback to retrieves the system query performance counter (QPC) value  synchronized with the  frame and microframe.</p>


## -prototype

````
EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC EvtUcxControllerGetFrameNumberAndQpcForTimeSync;

void EvtUcxControllerGetFrameNumberAndQpcForTimeSync(
  _In_ UCXCONTROLLER UcxController,
  _In_ WDFREQUEST    WdfRequest,
  _In_ size_t        OutputBufferLength,
  _In_ size_t        InputBufferLength
)
{ ... }
````


## -parameters
<dl>

### -param <i>UcxController</i> [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="buses._ucxcontrollercreate">UcxControllerCreate</a> method.</p>
</dd>

### -param <i>WdfRequest</i> [in]

<dd>
<p>A framework request object that contains the request to get the synchronized frame and microframe number.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the request's output buffer, if an output buffer
        is available. This value is the size of the <a href="buses.usb_frame_number_and_qpc_for_time_sync_information">USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION</a> structure. </p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>The length, in bytes, of the request's input buffer, if an input buffer
        is available. This value is the size of the <a href="buses.usb_frame_number_and_qpc_for_time_sync_information">USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION</a> structure.</p>
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
<a href="buses._ioctl_usb_get_frame_number_and_qpc_for_time_sync">IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
