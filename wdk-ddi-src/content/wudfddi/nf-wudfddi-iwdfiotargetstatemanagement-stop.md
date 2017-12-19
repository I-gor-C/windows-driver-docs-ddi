---
UID: NF.wudfddi.IWDFIoTargetStateManagement.Stop
title: IWDFIoTargetStateManagement::Stop method
author: windows-driver-content
description: The Stop method stops sending queued requests to a local I/O target.
old-location: wdf\iwdfiotargetstatemanagement_stop.htm
old-project: wdf
ms.assetid: c0d5ea59-c1df-403b-9e74-b1ab60761640
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFIoTargetStateManagement, IWDFIoTargetStateManagement::Stop, Stop
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoTargetStateManagement.Stop
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFIoTargetStateManagement::Stop method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>Stop</b> method stops sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.



## -syntax

````
HRESULT Stop(
  [in] WDF_IO_TARGET_SENT_IO_ACTION Action
);
````


## -parameters

### -param Action [in]

A <a href="wdf.wdf_io_target_sent_io_action__umdf_">WDF_IO_TARGET_SENT_IO_ACTION</a>-typed value that identifies how to handle sent I/O when the I/O target object is stopped.


## -returns
<b>Stop</b> always returns S_OK.


## -remarks
If your driver can detect recoverable device errors, you might want your driver to call <b>Stop</b> to temporarily stop sending requests to the local I/O target, then later call <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a> to resume sending requests.

Additionally, if a driver calls <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="wdf.ipnpcallback_ond0exit">IPnpCallback::OnD0Exit</a> callback function must call <b>Stop</b> to stop the reader.

If a driver has called <b>Stop</b>, it can still send a request to the target by setting the WDF_REQUEST_OPTION_IGNORE_TARGET_STATE flag when it calls <a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>. If a driver sets this flag, the driver can send a request, such as a request to reset a USB pipe (see <a href="wdf.iwdfusbtargetpipe_reset">IWDFUsbTargetPipe::Reset</a>), to a device after the driver has called <b>Stop</b>.

Your driver must call <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a> and <b>Stop</b> synchronously. After the driver calls one of these functions, it must not call either function before the first call returns.

Your driver can call <b>Stop</b> multiple times without calling <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a>. For example, your driver might do the following:

Call <b>Stop</b> and specify an <i>Action</i> value of <b>WdfIoTargetLeaveSentIoPending</b>. 

Determine whether the target should resume processing I/O requests. 

If the target should resume, call <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a>. Otherwise, call <b>Stop</b> again with an <i>Action</i> value of <b>WdfIoTargetCancelSentIo</b>. 

For more information about <b>Stop</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State</a>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets</a>.

The following code example shows how an <a href="wdf.ipnpcallback_ond0exit">IPnpCallback::OnD0Exit</a> callback function can call <b>Stop</b>, if the driver uses a continuous reader for a USB pipe. (To see how to obtain the <a href="..\wudfddi\nn-wudfddi-iwdfiotargetstatemanagement.md">IWDFIoTargetStateManagement</a> interface, see the code example at <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a>.)


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfiotargetstatemanagement.md">IWDFIoTargetStateManagement</a>
</dt>
<dt>
<a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoTargetStateManagement::Stop method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

