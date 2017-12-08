---
UID: NF.wdfiotarget.WdfIoTargetPurge
title: WdfIoTargetPurge function
author: windows-driver-content
description: The WdfIoTargetPurge method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued.
old-location: wdf\wdfiotargetpurge.htm
old-project: wdf
ms.assetid: C79492C5-3872-4ED9-9AD7-ABE5C5732D41
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfIoTargetPurge
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfIoTargetPurge
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
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

# WdfIoTargetPurge function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfIoTargetPurge</b> method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued. The method also attempts to cancel I/O requests that have left the I/O target's queue and entered lower drivers.


## -syntax

````
VOID WdfIoTargetPurge(
  _In_ WDFIOTARGET                   IoTarget,
  _In_ WDF_IO_TARGET_PURGE_IO_ACTION Action
);
````


## -parameters

### -param IoTarget [in]

A handle to a local or remote I/O target object that was obtained from a previous call to <a href="wdf.wdfdevicegetiotarget">WdfDeviceGetIoTarget</a> or <a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>, or from a method supplied by a specialized I/O target, such as <a href="wdf.wdfusbtargetpipegetiotarget">WdfUsbTargetPipeGetIoTarget</a>.

### -param Action [in]

A <a href="wdf.wdf_io_target_purge_io_action">WDF_IO_TARGET_PURGE_IO_ACTION</a>-typed value that indicates whether the framework should wait to return from  <b>WdfIoTargetPurge</b> until all delivered requests are completed or canceled. 

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
If the driver has previously called <a href="wdf.wdfusbtargetpipeconfigcontinuousreader">WdfUsbTargetPipeConfigContinuousReader</a>, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL. 
If the driver has not called <b>WdfUsbTargetPipeConfigContinuousReader</b> and if the <i>Action</i> parameter of <b>WdfIoTargetPurge</b> is <b>WdfIoTargetPurgeIo</b>, <b>WdfIoTargetPurge</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL.

To make <b>WdfIoTargetPurge</b> a synchronous call, the driver can set the <b>WdfIoTargetPurgeIoAndWait</b> value of the <i>Action</i> parameter. In this case, <b>WdfIoTargetPurge</b> waits to return until all delivered requests are completed or canceled.

After a driver has called <b>WdfIoTargetPurge</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure. For example, a driver might send a request, such as a request to reset a USB pipe (see <a href="wdf.wdfusbtargetpiperesetsynchronously">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetPurge</b>.

When a driver calls <b>WdfIoTargetPurge</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="wdf.wdf_request_send_options">WDF_REQUEST_SEND_OPTIONS</a> structure.

After a driver has purged an I/O queue, it can restart the queue by calling <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>.

Your driver must call <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>, <a href="wdf.wdfiotargetstop">WdfIoTargetStop</a> and <b>WdfIoTargetPurge</b> synchronously. After the driver calls one of these functions, it must not call any of the others until the previous call returns.


Your driver can call <b>WdfIoTargetPurge</b> multiple times without calling <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>. For example, your driver might do the following:
<ol>
<li>Call <b>WdfIoTargetPurge</b> and specify an <i>Action</i> value of <b>WdfIoTargetPurgeIo</b>.</li>
<li>Determine whether the target should resume processing I/O requests.</li>
<li>If the target should resume, call <a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetPurge</b> again with an <i>Action</i> value of <b>WdfIoTargetPurgeIoAndWait</b>. 
</li>
</ol>


For more information about I/O target states, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_d0_exit.md">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetPurge</b>, if the driver uses a continuous reader for a USB pipe.

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
1.11
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_io_target_purge_io_action">WDF_IO_TARGET_PURGE_IO_ACTION</a>
</dt>
<dt>
<a href="wdf.wdfiotargetgetstate">WdfIoTargetGetState</a>
</dt>
<dt>
<a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="wdf.wdfiotargetstart">WdfIoTargetStart</a>
</dt>
<dt>
<a href="wdf.wdfiotargetstop">WdfIoTargetStop</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetPurge method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
