---
UID: NN.wudfddi.IWDFIoTargetStateManagement
title: IWDFIoTargetStateManagement
author: windows-driver-content
description: The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object.
old-location: wdf\iwdfiotargetstatemanagement.htm
ms.assetid: 6870b6fa-1a90-4a7a-935a-4ce8eda940a1
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
req.umdf-ver: 1.5
req.alt-api: IWDFIoTargetStateManagement
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

# IWDFIoTargetStateManagement interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFIoTargetStateManagement</b> interface exposes methods that manage and monitor the state of an I/O target object.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoTargetStateManagement</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IWDFIoTargetStateManagement</b> also has these types of members:</p>

<p>The <b>IWDFIoTargetStateManagement</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/f915294f-457f-4913-b4b0-e94e1806a06d">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439492">Remove</a> method removes a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method starts sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method stops sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p> </p>

## -members
<p>The <b>IWDFIoTargetStateManagement</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559202">IWDFIoTargetStateManagement::GetState</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/f915294f-457f-4913-b4b0-e94e1806a06d">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559208">IWDFIoTargetStateManagement::Remove</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439492">Remove</a> method removes a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559213">IWDFIoTargetStateManagement::Start</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method starts sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559217">IWDFIoTargetStateManagement::Stop</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method stops sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/f915294f-457f-4913-b4b0-e94e1806a06d">GetState</a> method returns the current state of a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439492">Remove</a> method removes a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh973223">Start</a> method starts sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn927275">Stop</a> method stops sending queued requests to a <a href="wdf.general_i_o_targets_in_umdf">local  I/O target</a>.</p>

<p> </p>

## -remarks
<p>Drivers obtain the <b>IWDFIoTargetStateManagement</b> interface by calling <b>IWDFIoTarget::QueryInterface</b>, <b>IWDFUsbTargetPipe::QueryInterface</b>, or <b>IWDFUsbTargetPipe2::QueryInterface</b>.</p>

<p>Drivers obtain the <b>IWDFIoTargetStateManagement</b> interface by calling <b>IWDFIoTarget::QueryInterface</b>, <b>IWDFUsbTargetPipe::QueryInterface</b>, or <b>IWDFUsbTargetPipe2::QueryInterface</b>.</p>

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