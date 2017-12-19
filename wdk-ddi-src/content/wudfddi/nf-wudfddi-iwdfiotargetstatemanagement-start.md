---
UID: NF.wudfddi.IWDFIoTargetStateManagement.Start
title: IWDFIoTargetStateManagement::Start method
author: windows-driver-content
description: The Start method starts sending queued requests to a local I/O target.
old-location: wdf\iwdfiotargetstatemanagement_start.htm
old-project: wdf
ms.assetid: e242b62a-7a4f-491b-b1a7-3388cf9c5a40
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFIoTargetStateManagement, IWDFIoTargetStateManagement::Start, Start
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFIoTargetStateManagement::Start method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>Start</b> method starts sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.



## -syntax

````
HRESULT Start();
````


## -parameters


## -returns
<b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:
<dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl>The device has been removed.

 

This method might return one of the other error codes that Winerror.h defines.

<b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:
<dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl>The device has been removed.

 

This method might return one of the other error codes that Winerror.h defines.

<b>Start</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the error codes:
<dl>
<dt><b>HRESULT_FROM_NT (STATUS_INVALID_DEVICE_STATE)</b></dt>
</dl>The device has been removed.

 

This method might return one of the other error codes that Winerror.h defines.


## -remarks
If your driver can detect recoverable device errors, you might want your driver to call <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> to temporarily stop sending requests to the local I/O target, then later call <b>Start</b> to resume sending requests.

Additionally, if a driver calls <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a> to configure a continuous reader for a USB pipe, the driver's <a href="wdf.ipnpcallback_ond0entry">IPnpCallback::OnD0Entry</a> callback function must call <b>Start</b> to start the reader.

Your driver must call <b>Start</b> and <a href="wdf.iwdfiotargetstatemanagement_stop">IWDFIoTargetStateManagement::Stop</a> synchronously. After the driver calls one of these functions, it must not call the other function before the first one returns.

For more information about <b>Start</b>, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets_in_umdf">Using I/O Targets in UMDF</a>. 

The following code example first shows how a driver can obtain the <a href="..\wudfddi\nn-wudfddi-iwdfiotargetstatemanagement.md">IWDFIoTargetStateManagement</a> interface for a USB pipe object. The code example then  shows how an <a href="wdf.ipnpcallback_ond0entry">IPnpCallback::OnD0Entry</a> callback function can call <b>Start</b>, if the driver uses a continuous reader for the USB pipe. 


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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoTargetStateManagement::Start method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

