---
UID: NF.wdfiotarget.WdfIoTargetPurge
title: WdfIoTargetPurge
author: windows-driver-content
description: The WdfIoTargetPurge method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued.
old-location: wdf\wdfiotargetpurge.htm
ms.assetid: C79492C5-3872-4ED9-9AD7-ABE5C5732D41
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
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
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: See Remarks section.
ms.keywords: WdfIoTargetPurge
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoTargetPurge function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfIoTargetPurge</b> method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued. The method also attempts to cancel I/O requests that have left the I/O target's queue and entered lower drivers.</p>


## -syntax

````
VOID WdfIoTargetPurge(
  _In_ WDFIOTARGET                   IoTarget,
  _In_ WDF_IO_TARGET_PURGE_IO_ACTION Action
);
````


## -parameters
<dl>

### -param <i>IoTarget</i> [in]

<dd>
<p>A handle to a local or remote I/O target object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff546017">WdfDeviceGetIoTarget</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>, or from a method supplied by a specialized I/O target, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff551146">WdfUsbTargetPipeGetIoTarget</a>.</p>
</dd>

### -param <i>Action</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406485">WDF_IO_TARGET_PURGE_IO_ACTION</a>-typed value that indicates whether the framework should wait to return from  <b>WdfIoTargetPurge</b> until all delivered requests are completed or canceled. </p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If the driver has previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a>, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL. 
If the driver has not called <b>WdfUsbTargetPipeConfigContinuousReader</b> and if the <i>Action</i> parameter of <b>WdfIoTargetPurge</b> is <b>WdfIoTargetPurgeIo</b>, <b>WdfIoTargetPurge</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>To make <b>WdfIoTargetPurge</b> a synchronous call, the driver can set the <b>WdfIoTargetPurgeIoAndWait</b> value of the <i>Action</i> parameter. In this case, <b>WdfIoTargetPurge</b> waits to return until all delivered requests are completed or canceled.</p>

<p>After a driver has called <b>WdfIoTargetPurge</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure. For example, a driver might send a request, such as a request to reset a USB pipe (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551156">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetPurge</b>.</p>

<p>When a driver calls <b>WdfIoTargetPurge</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>

<p>After a driver has purged an I/O queue, it can restart the queue by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>.</p>

<p>Your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> and <b>WdfIoTargetPurge</b> synchronously. After the driver calls one of these functions, it must not call any of the others until the previous call returns.</p>

<p>
Your driver can call <b>WdfIoTargetPurge</b> multiple times without calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. For example, your driver might do the following:
<ol>
<li>Call <b>WdfIoTargetPurge</b> and specify an <i>Action</i> value of <b>WdfIoTargetPurgeIo</b>.</li>
<li>Determine whether the target should resume processing I/O requests.</li>
<li>If the target should resume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetPurge</b> again with an <i>Action</i> value of <b>WdfIoTargetPurgeIoAndWait</b>. 
</li>
</ol>
</p>

<p>For more information about I/O target states, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/bc3af732-f9ab-43a4-bc6f-7fa0b4c05a66">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetPurge</b>, if the driver uses a continuous reader for a USB pipe.</p>

<p>If the driver has previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a>, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL. 
If the driver has not called <b>WdfUsbTargetPipeConfigContinuousReader</b> and if the <i>Action</i> parameter of <b>WdfIoTargetPurge</b> is <b>WdfIoTargetPurgeIo</b>, <b>WdfIoTargetPurge</b> can be called at IRQL &lt;= DISPATCH_LEVEL. Otherwise, <b>WdfIoTargetPurge</b> must be called at IRQL = PASSIVE_LEVEL.</p>

<p>To make <b>WdfIoTargetPurge</b> a synchronous call, the driver can set the <b>WdfIoTargetPurgeIoAndWait</b> value of the <i>Action</i> parameter. In this case, <b>WdfIoTargetPurge</b> waits to return until all delivered requests are completed or canceled.</p>

<p>After a driver has called <b>WdfIoTargetPurge</b>, it can still send a request to the target by setting the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure. For example, a driver might send a request, such as a request to reset a USB pipe (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551156">WdfUsbTargetPipeResetSynchronously</a>), to a device after the driver has called <b>WdfIoTargetPurge</b>.</p>

<p>When a driver calls <b>WdfIoTargetPurge</b>, the framework does not attempt to cancel or wait for I/O requests that were previously sent to the target using either the <b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b> flag or the <b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b> flag in the request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>

<p>After a driver has purged an I/O queue, it can restart the queue by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>.</p>

<p>Your driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a> and <b>WdfIoTargetPurge</b> synchronously. After the driver calls one of these functions, it must not call any of the others until the previous call returns.</p>

<p>
Your driver can call <b>WdfIoTargetPurge</b> multiple times without calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. For example, your driver might do the following:
<ol>
<li>Call <b>WdfIoTargetPurge</b> and specify an <i>Action</i> value of <b>WdfIoTargetPurgeIo</b>.</li>
<li>Determine whether the target should resume processing I/O requests.</li>
<li>If the target should resume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>. Otherwise, call <b>WdfIoTargetPurge</b> again with an <i>Action</i> value of <b>WdfIoTargetPurgeIoAndWait</b>. 
</li>
</ol>
</p>

<p>For more information about I/O target states, see <a href="wdf.controlling_a_general_i_o_target_s_state">Controlling a General I/O Target's State</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/bc3af732-f9ab-43a4-bc6f-7fa0b4c05a66">EvtDeviceD0Exit</a> callback function can call <b>WdfIoTargetPurge</b>, if the driver uses a continuous reader for a USB pipe.</p>

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
<p>1.11</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406485">WDF_IO_TARGET_PURGE_IO_ACTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548631">WdfIoTargetGetState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548591">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548677">WdfIoTargetStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetPurge method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
