---
UID: NF.wudfddi.IWDFRemoteTarget.CloseForQueryRemove
title: IWDFRemoteTarget::CloseForQueryRemove
author: windows-driver-content
description: The CloseForQueryRemove method closes a remote I/O target because the operating system might allow the device to be removed.
old-location: wdf\iwdfremotetarget_closeforqueryremove.htm
old-project: wdf
ms.assetid: 9e23ae80-7c39-4cee-b1ab-80085f24d41f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFRemoteTarget, CloseForQueryRemove, IWDFRemoteTarget::CloseForQueryRemove
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFRemoteTarget.CloseForQueryRemove
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
req.iface: IWDFRemoteTarget
req.product: Windows 10 or later.
---

# IWDFRemoteTarget::CloseForQueryRemove method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CloseForQueryRemove</b> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.</p>


## -syntax

````
HRESULT CloseForQueryRemove();
````


## -parameters


## -returns
<p>The <b>CloseForQueryRemove</b> method always returns S_OK.</p>

<p>The <b>CloseForQueryRemove</b> method always returns S_OK.</p>

<p>The <b>CloseForQueryRemove</b> method always returns S_OK.</p>

## -remarks
<p>If your driver provides an <a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove</a> callback function, the callback function must call <b>CloseForQueryRemove</b> if it returns <b>TRUE</b> to indicate that the device can be removed. </p>

<p>The <b>CloseForQueryRemove</b> method completes or cancels all I/O requests that the driver has sent to the I/O target.</p>

<p>After a driver calls <b>CloseForQueryRemove</b>, the driver cannot send I/O requests to the I/O target until it calls <a href="wdf.iwdfremotetarget_reopen">IWDFRemoteTarget::Reopen</a>.</p>

<p>For more information about the <b>CloseForQueryRemove</b> method, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

<p>The following code example shows an <a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove</a> callback function that calls <b>CloseForQueryRemove</b>.</p>

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
<p>1.9</p>
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
<a href="..\wudfddi\nn-wudfddi-iwdfremotetarget.md">IWDFRemoteTarget</a>
</dt>
<dt>
<a href="wdf.iwdfremotetarget_close">IWDFRemoteTarget::Close</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFRemoteTarget::CloseForQueryRemove method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
