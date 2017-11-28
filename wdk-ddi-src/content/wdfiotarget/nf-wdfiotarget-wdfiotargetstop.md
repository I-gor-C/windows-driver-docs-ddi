---
UID: NF.wdfiotarget.WdfIoTargetStop
title: WdfIoTargetStop
author: windows-driver-content
description: The WdfIoTargetStop method stops sending queued requests to a local or remote I/O target.
old-location: wdf\wdfiotargetstop.htm
old-project: wdf
ms.assetid: 3dd5aa58-e5a6-4ee3-9b88-d9cbb7eb558c
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoTargetStop function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoTargetStop</b> method stops sending queued requests to a local or remote I/O target.</p>


## -syntax

````
VOID WdfIoTargetStop(
  _In_ WDFIOTARGET                  IoTarget,
  _In_ WDF_IO_TARGET_SENT_IO_ACTION Action
);
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to a local or remote I/O target object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>, or from a method that a specialized I/O target supplies.</p>
</dd>

### -param <i>Action</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552388">WDF_IO_TARGET_SENT_IO_ACTION</a>-typed value that specifies how the framework should handle I/O requests that the driver has sent to the I/O target, if the target has not completed the requests.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If your driver can detect recoverable device errors, you might want your driver to call <b>WdfIoTargetStop</b> to temporarily stop sending requests, then later call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> to resume sending requests.</p>

<p>While stopped, an I/O target continues to accept new requests but does not deliver the queued requests to the appropriate driver.</p>

<p>For more information about possible states for I/O targets, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>.</p>

<p>If a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function must call <b>WdfIoTargetStop</b> to stop the reader.</p>

<p>If a driver has called <b>WdfIoTargetStop</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure. If a driver sets this flag, the driver can send a request, such as a request to reset a USB pipe (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551156">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetStop</b>.</p>

<p>When a driver calls <b>WdfIoTargetStop</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>

<p>Your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> and <b>WdfIoTargetStop</b> synchronously. After the driver calls one of these functions, it must not call either function before the first call returns.</p>

<p>Your driver can call <b>WdfIoTargetStop</b> multiple times from a single thread without calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. For example, your driver might do the following:</p>

<p>Call <b>WdfIoTargetStop</b> and specify an <i>Action</i> value of <b>WdfIoTargetLeaveSentIoPending</b>. </p>

<p>Determine whether the target should resume processing I/O requests. </p>

<p>If the target should resume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetStop</b> again with an <i>Action</i> value of <b>WdfIoTargetCancelSentIo</b>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> for the pipe, <b>WdfIoTargetStop</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>If the driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> and if the <i>Action</i> parameter of <b>WdfIoTargetStop</b> is <b>WdfIoTargetLeaveSentIoPending</b>, <b>WdfIoTargetStop</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetStop</b> is called at IRQL = PASSIVE_LEVEL. </p>

<p>The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetStop</b>, if the driver uses a continuous reader for a USB pipe. </p>

<p>If your driver can detect recoverable device errors, you might want your driver to call <b>WdfIoTargetStop</b> to temporarily stop sending requests, then later call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> to resume sending requests.</p>

<p>While stopped, an I/O target continues to accept new requests but does not deliver the queued requests to the appropriate driver.</p>

<p>For more information about possible states for I/O targets, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>.</p>

<p>If a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function must call <b>WdfIoTargetStop</b> to stop the reader.</p>

<p>If a driver has called <b>WdfIoTargetStop</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure. If a driver sets this flag, the driver can send a request, such as a request to reset a USB pipe (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551156">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetStop</b>.</p>

<p>When a driver calls <b>WdfIoTargetStop</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>

<p>Your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a> and <b>WdfIoTargetStop</b> synchronously. After the driver calls one of these functions, it must not call either function before the first call returns.</p>

<p>Your driver can call <b>WdfIoTargetStop</b> multiple times from a single thread without calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. For example, your driver might do the following:</p>

<p>Call <b>WdfIoTargetStop</b> and specify an <i>Action</i> value of <b>WdfIoTargetLeaveSentIoPending</b>. </p>

<p>Determine whether the target should resume processing I/O requests. </p>

<p>If the target should resume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetStop</b> again with an <i>Action</i> value of <b>WdfIoTargetCancelSentIo</b>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>If the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> for the pipe, <b>WdfIoTargetStop</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>If the driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a> and if the <i>Action</i> parameter of <b>WdfIoTargetStop</b> is <b>WdfIoTargetLeaveSentIoPending</b>, <b>WdfIoTargetStop</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetStop</b> is called at IRQL = PASSIVE_LEVEL. </p>

<p>The following code example shows how an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetStop</b>, if the driver uses a continuous reader for a USB pipe. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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
<dt>Wdfiotarget.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975077">FailD0EntryIoTargetState</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551156">WdfUsbTargetPipeResetSynchronously</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetStop method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
