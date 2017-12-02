---
UID: NE.wudfddi_types._WDF_IO_TARGET_SENT_IO_ACTION
title: WDF_IO_TARGET_SENT_IO_ACTION
author: windows-driver-content
description: The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls IWDFIoTargetStateManagement::Stop or IWDFRemoteTarget::Stop to stop an I/O target.
old-location: wdf\wdf_io_target_sent_io_action__umdf_.htm
old-project: wdf
ms.assetid: 9cdcf964-9f2d-437f-8693-de5bb4bb9895
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WRITE_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.0
req.alt-api: WDF_IO_TARGET_SENT_IO_ACTION
req.alt-loc: Wudfddi_types.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_IO_TARGET_SENT_IO_ACTION enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration identifies the actions that the framework can take when a driver calls <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> or  <a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a> to stop an I/O target.</p>


## -syntax

````
typedef enum _WDF_IO_TARGET_SENT_IO_ACTION { 
  WdfIoTargetSentIoUndefined          = 0,
  WdfIoTargetCancelSentIo             = 1,
  WdfIoTargetWaitForSentIoToComplete  = 2,
  WdfIoTargetLeaveSentIoPending       = 3,
  WdfIoTargetSentIoMaximum            = ( WdfIoTargetLeaveSentIoPending + 1 )
} WDF_IO_TARGET_SENT_IO_ACTION;
````


## -enum-fields
<dl>

### -field WdfIoTargetSentIoUndefined

<dd>
<p>Reservied for system use.</p>
</dd>

### -field WdfIoTargetCancelSentIo

<dd>
<p>Before the framework stops the I/O target, it will attempt to cancel I/O requests that are in the I/O target's queue. The framework cancels all of the target queue's I/O requests before <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> or <a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a> returns.</p>
</dd>

### -field WdfIoTargetWaitForSentIoToComplete

<dd>
<p>Before the framework stops the I/O target, it will wait for I/O requests that are in the I/O target's queue to be completed. The framework completes all of the target queue's I/O requests, and calls each request's <a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a> callback function, before <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> or <a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a> returns.</p>
</dd>

### -field WdfIoTargetLeaveSentIoPending

<dd>
<p>The framework will leave I/O requests in the I/O target's queue. The requests remain in the target's queue until the driver calls <a href="wdf.iwdfiotargetstatemanagement_start">IWDFIoTargetStateManagement::Start</a> or <a href="wdf.iwdfremotetarget_start">IWDFRemoteTarget::Start</a> or the device is removed.</p>
</dd>

### -field WdfIoTargetSentIoMaximum

<dd>
<p>Valid enumeration values were exceeded.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_TARGET_SENT_IO_ACTION</b> enumeration is used as an input parameter to the <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> and  <a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a> methods.</p>

<p>If your driver specifies the <b>WdfIoTargetWaitForSentIoToComplete</b> flag, the driver must not call <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> or <a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a> from a request handler, an <a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a> callback function, or an <a href="wdf.iusbtargetpipecontinuousreadercallbackreadersfailed_onreaderfailure">IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure</a> callback function.</p>

<p>For the KMDF version of this enumeration, see <a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-target-sent-io-action.md">WDF_IO_TARGET_SENT_IO_ACTION</a>.</p>

## -requirements
<table>
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
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-io-target-sent-io-action.md">WDF_IO_TARGET_SENT_IO_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_IO_TARGET_SENT_IO_ACTION enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
