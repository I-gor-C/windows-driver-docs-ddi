---
UID: NF.wudfddi.IWDFIoTargetStateManagement.Start
title: IWDFIoTargetStateManagement::Start
author: windows-driver-content
description: The Start method starts sending queued requests to a local I/O target.
old-location: wdf\iwdfiotargetstatemanagement_start.htm
old-project: wdf
ms.assetid: e242b62a-7a4f-491b-b1a7-3388cf9c5a40
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFIoTargetStateManagement, Start, IWDFIoTargetStateManagement::Start
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoTargetStateManagement.Start
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFIoTargetStateManagement
req.product: Windows 10 or later.
---

# IWDFIoTargetStateManagement::Start method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Start</b> method starts sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>


## -syntax

````
HRESULT Start();
````


## -parameters


## -returns
<p><b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:</p><dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl><p>The device has been removed.</p>

<p> </p>

<p>This method might return one of the other error codes that Winerror.h defines.</p>

<p><b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:</p><dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl><p>The device has been removed.</p>

<p> </p>

<p>This method might return one of the other error codes that Winerror.h defines.</p>

<p><b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:</p><dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl><p>The device has been removed.</p>

<p> </p>

<p>This method might return one of the other error codes that Winerror.h defines.</p>

## -remarks
<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> to temporarily stop sending requests to the local I/O target, then later call <b>Start</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560395">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function must call <b>Start</b> to start the reader.</p>

<p>Your driver must call <b>Start</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>Start</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets in UMDF</a>. </p>

<p>The following code example first shows how a driver can obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559198">IWDFIoTargetStateManagement</a> interface for a USB pipe object. The code example then  shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function can call <b>Start</b>, if the driver uses a continuous reader for the USB pipe. </p>

<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> to temporarily stop sending requests to the local I/O target, then later call <b>Start</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560395">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function must call <b>Start</b> to start the reader.</p>

<p>Your driver must call <b>Start</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>Start</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets in UMDF</a>. </p>

<p>The following code example first shows how a driver can obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559198">IWDFIoTargetStateManagement</a> interface for a USB pipe object. The code example then  shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function can call <b>Start</b>, if the driver uses a continuous reader for the USB pipe. </p>

<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> to temporarily stop sending requests to the local I/O target, then later call <b>Start</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560395">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function must call <b>Start</b> to start the reader.</p>

<p>Your driver must call <b>Start</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>Start</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets in UMDF</a>. </p>

<p>The following code example first shows how a driver can obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559198">IWDFIoTargetStateManagement</a> interface for a USB pipe object. The code example then  shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function can call <b>Start</b>, if the driver uses a continuous reader for the USB pipe. </p>

<p>If your driver can detect recoverable device errors, you might want your driver to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> to temporarily stop sending requests to the local I/O target, then later call <b>Start</b> to resume sending requests.</p>

<p>Additionally, if a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff560395">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function must call <b>Start</b> to start the reader.</p>

<p>Your driver must call <b>Start</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.</p>

<p>For more information about <b>Start</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>. </p>

<p>For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets in UMDF</a>. </p>

<p>The following code example first shows how a driver can obtain the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559198">IWDFIoTargetStateManagement</a> interface for a USB pipe object. The code example then  shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556799">IPnpCallback::OnD0Entry</a> callback function can call <b>Start</b>, if the driver uses a continuous reader for the USB pipe. </p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559198">IWDFIoTargetStateManagement</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560289">IWDFRemoteTarget::Stop</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoTargetStateManagement::Start method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
