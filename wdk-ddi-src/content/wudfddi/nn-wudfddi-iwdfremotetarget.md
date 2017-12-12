---
UID: NN.wudfddi.IWDFRemoteTarget
title: IWDFRemoteTarget
author: windows-driver-content
description: To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2::CreateRemoteTarget.
old-location: wdf\iwdfremotetarget.htm
old-project: wdf
ms.assetid: 60164136-4d4b-4e42-8504-ddd907edf0e9
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFRemoteTarget
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
req.product: Windows 10 or later.
---

# IWDFRemoteTarget interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

To obtain the <b>IWDFRemoteTarget</b> interface, drivers call <a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a>.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFRemoteTarget</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfiotarget2.md">IWDFIoTarget2</a>. <b>IWDFRemoteTarget</b> also has these types of members:

The <b>IWDFRemoteTarget</b> interface has these methods.

The <a href="wdf.iwdfremotetarget_close">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The <a href="wdf.iwdfremotetarget_closeforqueryremove">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.

The <a href="wdf.iwdfremotetarget_getstate">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The <a href="wdf.iwdfremotetarget_openfilebyname">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.

The <a href="wdf.iwdfremotetarget_openremoteinterface">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.

The <a href="wdf.iwdfremotetarget_reopen">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.

The <a href="wdf.iwdfremotetarget_start">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.

The <a href="wdf.iwdfremotetarget_stop">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

 


## -members
The <b>IWDFRemoteTarget</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_close">IWDFRemoteTarget::Close</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_close">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_closeforqueryremove">IWDFRemoteTarget::CloseForQueryRemove</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_closeforqueryremove">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_getstate">IWDFRemoteTarget::GetState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_getstate">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_openfilebyname">IWDFRemoteTarget::OpenFileByName</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_openfilebyname">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_openremoteinterface">IWDFRemoteTarget::OpenRemoteInterface</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_openremoteinterface">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_reopen">IWDFRemoteTarget::Reopen</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_reopen">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_start">IWDFRemoteTarget::Start</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_start">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfremotetarget_stop">IWDFRemoteTarget::Stop</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfremotetarget_stop">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

</td>
</tr>
</table>The <a href="wdf.iwdfremotetarget_close">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The <a href="wdf.iwdfremotetarget_closeforqueryremove">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.

The <a href="wdf.iwdfremotetarget_getstate">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The <a href="wdf.iwdfremotetarget_openfilebyname">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.

The <a href="wdf.iwdfremotetarget_openremoteinterface">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.

The <a href="wdf.iwdfremotetarget_reopen">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.

The <a href="wdf.iwdfremotetarget_start">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.

The <a href="wdf.iwdfremotetarget_stop">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

 


## -remarks


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
1.9

</td>
</tr>
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