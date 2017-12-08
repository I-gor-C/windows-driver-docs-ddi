---
UID: NF.wudfddi.IRemoteTargetCallbackRemoval.OnRemoteTargetQueryRemove
title: IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove
author: windows-driver-content
description: A UMDF-based driver's OnRemoteTargetQueryRemove event callback function determines whether a remote I/O target's device can be stopped and removed.
old-location: wdf\iremotetargetcallbackremoval_onremotetargetqueryremove.htm
old-project: wdf
ms.assetid: 10a9510a-a11c-46fa-adb8-b122f6c571f4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IRemoteTargetCallbackRemoval, OnRemoteTargetQueryRemove, IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove
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
req.alt-api: IRemoteTargetCallbackRemoval.OnRemoteTargetQueryRemove
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IRemoteTargetCallbackRemoval
req.product: Windows 10 or later.
---

# IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A UMDF-based driver's <b>OnRemoteTargetQueryRemove</b> event callback function determines whether a remote I/O target's device can be stopped and removed.</p>


## -syntax

````
BOOL OnRemoteTargetQueryRemove(
  [in] IWDFRemoteTarget *pWdfRemoteTarget
);
````


## -parameters
<dl>

### -param pWdfRemoteTarget [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfremotetarget.md">IWDFRemoteTarget</a> interface of a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>. The driver obtains this pointer when it calls <a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a>.</p>
</dd>
</dl>

## -returns
<p>If the driver determines that the device can be stopped and removed, the <b>OnRemoteTargetQueryRemove</b> event callback function must return <b>TRUE</b>. Otherwise, the callback function must return <b>FALSE</b>.</p>

## -remarks
<p>If your driver provides an <b>OnRemoteTargetQueryRemove</b> event callback function, the callback function should determine if the operating system should allow removal of the device. If the driver determines that the device can be removed, it should do the following:</p>

<p>Do any driver-specific actions needed to stop I/O to the remote target.</p>

<p>Call <a href="wdf.iwdfremotetarget_closeforqueryremove">IWDFRemoteTarget::CloseForQueryRemove</a>.</p>

<p>Return <b>TRUE</b> to indicate that the removal can occur. </p>

<p>If the driver determines that the device should not be removed, the callback function must return <b>FALSE</b>. Typically, drivers should avoid returning <b>FALSE</b>, because a <b>FALSE</b> return value can cause Windows to restart.</p>

<p>If the driver does not provide this callback function, the framework calls <a href="wdf.iwdfremotetarget_closeforqueryremove">IWDFRemoteTarget::CloseForQueryRemove</a> for the driver. In other words, the framework always allows the device to be removed unless the driver provides an <b>OnRemoteTargetQueryRemove</b> event callback function.</p>

<p>For more information about the <b>OnRemoteTargetQueryRemove</b> event callback function, see <a href="wdf.controlling_a_general_i_o_target_s_state_in_umdf">Controlling a General I/O Target's State in UMDF</a>.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iremotetargetcallbackremoval.md">IRemoteTargetCallbackRemoval</a>
</dt>
<dt>
<a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecanceled">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a>
</dt>
<dt>
<a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecomplete">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
