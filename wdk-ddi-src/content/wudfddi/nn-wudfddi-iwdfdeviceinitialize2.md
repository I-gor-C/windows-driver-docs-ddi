---
UID: NN.wudfddi.IWDFDeviceInitialize2
title: IWDFDeviceInitialize2
author: windows-driver-content
description: The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method.
old-location: wdf\iwdfdeviceinitialize2.htm
old-project: wdf
ms.assetid: 78d0c888-955f-481f-aa59-f2e5eea1aa81
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDeviceInitialize2
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFDeviceInitialize2</b> interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDeviceInitialize2</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfdeviceinitialize.md">IWDFDeviceInitialize</a>. <b>IWDFDeviceInitialize2</b> also has these types of members:</p>

<p>The <b>IWDFDeviceInitialize2</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfdeviceinitialize2_setiotypepreference">SetIoTypePreference</a> method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests.</p>

<p> </p>

## -members
<p>The <b>IWDFDeviceInitialize2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdeviceinitialize2_setiotypepreference">IWDFDeviceInitialize2::SetIoTypePreference</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdeviceinitialize2_setiotypepreference">SetIoTypePreference</a> method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfdeviceinitialize2_setiotypepreference">SetIoTypePreference</a> method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests.</p>

<p> </p>

## -remarks
<p>Drivers obtain the <b>IWDFDeviceInitialize2</b> interface by calling <b>IWDFDeviceInitialize::QueryInterface</b>.</p>

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