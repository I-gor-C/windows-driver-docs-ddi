---
UID: NN.wudfddi.IWDFRemoteTarget
title: IWDFRemoteTarget
author: windows-driver-content
description: To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2::CreateRemoteTarget.
old-location: wdf\iwdfremotetarget.htm
ms.assetid: 60164136-4d4b-4e42-8504-ddd907edf0e9
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
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
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFRemoteTarget interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>To obtain the <b>IWDFRemoteTarget</b> interface, drivers call <a href="https://msdn.microsoft.com/library/windows/hardware/ff556928">IWDFDevice2::CreateRemoteTarget</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFRemoteTarget</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559175">IWDFIoTarget2</a>. <b>IWDFRemoteTarget</b> also has these types of members:</p>

<p>The <b>IWDFRemoteTarget</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451151">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/9e23ae80-7c39-4cee-b1ab-80085f24d41f">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.</p>

<p>The <a href="https://msdn.microsoft.com/3918d764-c5bb-42b6-8b06-a2d544511a96">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/7f0cef78-3edc-434b-af70-39694776e8a7">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.</p>

<p>The <a href="https://msdn.microsoft.com/5d278cde-3ebe-4fee-86fd-1ec4e79bd837">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.</p>

<p>The <a href="https://msdn.microsoft.com/904904e7-ca59-4dcb-92db-8c7f6a9cbff7">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560280">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p> </p>

## -members
<p>The <b>IWDFRemoteTarget</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560253">IWDFRemoteTarget::Close</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451151">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560259">IWDFRemoteTarget::CloseForQueryRemove</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/9e23ae80-7c39-4cee-b1ab-80085f24d41f">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560265">IWDFRemoteTarget::GetState</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/3918d764-c5bb-42b6-8b06-a2d544511a96">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560273">IWDFRemoteTarget::OpenFileByName</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/7f0cef78-3edc-434b-af70-39694776e8a7">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560276">IWDFRemoteTarget::OpenRemoteInterface</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/5d278cde-3ebe-4fee-86fd-1ec4e79bd837">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560278">IWDFRemoteTarget::Reopen</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/904904e7-ca59-4dcb-92db-8c7f6a9cbff7">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560280">IWDFRemoteTarget::Start</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560280">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560289">IWDFRemoteTarget::Stop</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh451151">Close</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/9e23ae80-7c39-4cee-b1ab-80085f24d41f">CloseForQueryRemove</a> method closes a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> because the operating system might allow the device to be removed.</p>

<p>The <a href="https://msdn.microsoft.com/3918d764-c5bb-42b6-8b06-a2d544511a96">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/7f0cef78-3edc-434b-af70-39694776e8a7">OpenFileByName</a> method opens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is a file.</p>

<p>The <a href="https://msdn.microsoft.com/5d278cde-3ebe-4fee-86fd-1ec4e79bd837">OpenRemoteInterface</a> method opens a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> so that the driver can send I/O requests to it.</p>

<p>The <a href="https://msdn.microsoft.com/904904e7-ca59-4dcb-92db-8c7f6a9cbff7">Reopen</a> method reopens a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> after it has been temporarily closed.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560280">IWDFRemoteTarget::Start</a> method restarts a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a> that is stopped.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method temporarily stops a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p> </p>

## -remarks


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
<dt>Wudfddi.h</dt>
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