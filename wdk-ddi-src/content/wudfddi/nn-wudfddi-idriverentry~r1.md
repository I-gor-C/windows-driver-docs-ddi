---
UID: NN.wudfddi.IDriverEntry~r1
title: IDriverEntry
author: windows-driver-content
description: The IDriverEntry interface exposes the user-mode driver's main entry and exit points.
old-location: wdf\idriverentry.htm
old-project: wdf
ms.assetid: eae6f032-2f31-43e1-9ac0-38ccc4840580
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
req.alt-api: IDriverEntry
req.alt-loc: Wudfddi.h
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

# IDriverEntry interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IDriverEntry</b> interface exposes the user-mode driver's main entry and exit points.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDriverEntry</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDriverEntry</b> also has these types of members:

The <b>IDriverEntry</b> interface has these methods.

The <a href="wdf.idriverentry_ondeinitialize">OnDeinitialize</a> method performs any operations that are necessary before a system unloads a driver.

The <a href="wdf.idriverentry_ondeviceadd">OnDeviceAdd</a> method adds a new device to a system.

The <a href="wdf.idriverentry_oninitialize">OnInitialize</a> method performs any operations that are necessary to initialize a driver.

 

## -members
The <b>IDriverEntry</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.idriverentry_ondeinitialize">IDriverEntry::OnDeinitialize</a>
</td>
<td align="left" width="63%">
The <a href="wdf.idriverentry_ondeinitialize">OnDeinitialize</a> method performs any operations that are necessary before a system unloads a driver.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.idriverentry_ondeviceadd">IDriverEntry::OnDeviceAdd</a>
</td>
<td align="left" width="63%">
The <a href="wdf.idriverentry_ondeviceadd">OnDeviceAdd</a> method adds a new device to a system.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.idriverentry_oninitialize">IDriverEntry::OnInitialize</a>
</td>
<td align="left" width="63%">
The <a href="wdf.idriverentry_oninitialize">OnInitialize</a> method performs any operations that are necessary to initialize a driver.
</td>
</tr>
</table>The <a href="wdf.idriverentry_ondeinitialize">OnDeinitialize</a> method performs any operations that are necessary before a system unloads a driver.

The <a href="wdf.idriverentry_ondeviceadd">OnDeviceAdd</a> method adds a new device to a system.

The <a href="wdf.idriverentry_oninitialize">OnInitialize</a> method performs any operations that are necessary to initialize a driver.

 

## -remarks


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