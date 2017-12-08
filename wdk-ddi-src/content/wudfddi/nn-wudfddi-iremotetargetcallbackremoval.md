---
UID: NN.wudfddi.IRemoteTargetCallbackRemoval
title: IRemoteTargetCallbackRemoval
author: windows-driver-content
description: The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target.
old-location: wdf\iremotetargetcallbackremoval.htm
old-project: wdf
ms.assetid: 72271173-8851-4980-9b52-f9e14f1fe071
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, *PPOWER_ACTION, POWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRemoteTargetCallbackRemoval
req.alt-loc: wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# IRemoteTargetCallbackRemoval interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IRemoteTargetCallbackRemoval</b> interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IRemoteTargetCallbackRemoval</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IRemoteTargetCallbackRemoval</b> also has these types of members:

The <b>IRemoteTargetCallbackRemoval</b> interface has these methods.

A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">OnRemoteTargetQueryRemove</a> event callback function determines whether a remote I/O target's device can be stopped and removed.

A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecanceled">OnRemoteTargetRemoveCanceled</a> event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device.

A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecomplete">OnRemoteTargetRemoveComplete</a> event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device.

 

## -members
The <b>IRemoteTargetCallbackRemoval</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove</a>
</td>
<td align="left" width="63%">
A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">OnRemoteTargetQueryRemove</a> event callback function determines whether a remote I/O target's device can be stopped and removed.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecanceled">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled</a>
</td>
<td align="left" width="63%">
A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecanceled">OnRemoteTargetRemoveCanceled</a> event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecomplete">IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveComplete</a>
</td>
<td align="left" width="63%">
A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecomplete">OnRemoteTargetRemoveComplete</a> event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device.
</td>
</tr>
</table>A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetqueryremove">OnRemoteTargetQueryRemove</a> event callback function determines whether a remote I/O target's device can be stopped and removed.

A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecanceled">OnRemoteTargetRemoveCanceled</a> event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device.

A UMDF-based driver's <a href="wdf.iremotetargetcallbackremoval_onremotetargetremovecomplete">OnRemoteTargetRemoveComplete</a> event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device.

 

## -remarks
If your driver supports an <b>IRemoteTargetCallbackRemoval</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a> must return the interface. 

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
</table>