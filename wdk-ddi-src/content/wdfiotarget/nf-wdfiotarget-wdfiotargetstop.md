---
UID: NF.wdfiotarget.WdfIoTargetStop
title: WdfIoTargetStop function
author: windows-driver-content
description: The WdfIoTargetStop method stops sending queued requests to a local or remote I/O target.
old-location: wdf\wdfiotargetstop.htm
old-project: wdf
ms.assetid: 3dd5aa58-e5a6-4ee3-9b88-d9cbb7eb558c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfIoTargetStop
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetStop
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, FailD0EntryIoTargetState, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# WdfIoTargetStop function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfIoTargetStop</b> method stops sending queued requests to a local or remote I/O target.


## -syntax

````
VOID WdfIoTargetStop(
  _In_ WDFIOTARGET                  IoTarget,
  _In_ WDF_IO_TARGET_SENT_IO_ACTION Action
);
````


## -parameters

### -param IoTarget [in]

A handle to a local or remote I/O target object that was obtained from a previous call to <a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a> or <a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>, or from a method that a specialized I/O target supplies.

### -param Action [in]

A <a href="wdf.wdf_io_target_sent_io_action">WDF_IO_TARGET_SENT_IO_ACTION</a>-typed value that specifies how the framework should handle I/O requests that the driver has sent to the I/O target, if the target has not completed the requests.

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
If your driver can detect recoverable device errors, you might want your driver to call <b>WdfIoTargetStop</b> to temporarily stop sending requests, then later call <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a> to resume sending requests.

While stopped, an I/O target continues to accept new requests but does not deliver the queued requests to the appropriate driver.

For more information about possible states for I/O targets, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>.

If a driver calls <a href="wdf.wdfusbtargetpipeconfigcontinuousreader">WdfUsbTargetPipeConfigContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_d0_exit.md">EvtDeviceD0Exit</a> callback function must call <b>WdfIoTargetStop</b> to stop the reader.

If a driver has called <b>WdfIoTargetStop</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure. If a driver sets this flag, the driver can send a request, such as a request to reset a USB pipe (see <a href="wdf.wdfusbtargetpiperesetsynchronously">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetStop</b>.

When a driver calls <b>WdfIoTargetStop</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure.

Your driver must call <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a> and <b>WdfIoTargetStop</b> synchronously. After the driver calls one of these functions, it must not call either function before the first call returns.

Your driver can call <b>WdfIoTargetStop</b> multiple times from a single thread without calling <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>. For example, your driver might do the following:

Call <b>WdfIoTargetStop</b> and specify an <i>Action</i> value of <b>WdfIoTargetLeaveSentIoPending</b>. 

Determine whether the target should resume processing I/O requests. 

If the target should resume, call <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetStop</b> again with an <i>Action</i> value of <b>WdfIoTargetCancelSentIo</b>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

If the driver has called <a href="wdf.wdfusbtargetpipeconfigcontinuousreader">WdfUsbTargetPipeConfigContinuousReader</a> for the pipe, <b>WdfIoTargetStop</b> must be called at IRQL = PASSIVE_LEVEL.

If the driver has not called <a href="wdf.wdfusbtargetpipeconfigcontinuousreader">WdfUsbTargetPipeConfigContinuousReader</a> and if the <i>Action</i> parameter of <b>WdfIoTargetStop</b> is <b>WdfIoTargetLeaveSentIoPending</b>, <b>WdfIoTargetStop</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetStop</b> is called at IRQL = PASSIVE_LEVEL. 

The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_d0_exit.md">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetStop</b>, if the driver uses a continuous reader for a USB pipe. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
See Remarks section.
</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_faild0entryiotargetstate">FailD0EntryIoTargetState</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_d0_exit.md">EvtDeviceD0Exit</a>
</dt>
<dt>
<a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
<dt>
<a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>
</dt>
<dt>
<a href="wdf.wdfusbtargetpipeconfigcontinuousreader">WdfUsbTargetPipeConfigContinuousReader</a>
</dt>
<dt>
<a href="wdf.wdfusbtargetpiperesetsynchronously">WdfUsbTargetPipeResetSynchronously</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetStop method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
