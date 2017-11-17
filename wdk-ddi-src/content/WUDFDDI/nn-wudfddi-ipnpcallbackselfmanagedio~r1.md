---
UID: NN.wudfddi.IPnpCallbackSelfManagedIo~r1
title: IPnpCallbackSelfManagedIo
author: windows-driver-content
description: The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface.
old-location: wdf\ipnpcallbackselfmanagedio.htm
ms.assetid: 34971df0-4abc-41a1-8d2f-6e36df1daf20
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPnpCallbackSelfManagedIo
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
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IPnpCallbackSelfManagedIo interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IPnpCallbackSelfManagedIo</b> interface is a Plug and Play (PnP) and power management (PM) interface. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackSelfManagedIo</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackSelfManagedIo</b> also has these types of members:</p>

<p>The <b>IPnpCallbackSelfManagedIo</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/0890c352-8722-4108-9b76-60c81179b46b">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.</p>

<p>The <a href="https://msdn.microsoft.com/dee0e30b-ad03-43e4-8a0c-07d3782d7857">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/41b12fef-dbc7-4b91-a2d3-9fb1aafff237">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/dccc4be0-0724-44b6-8476-276b46acee6a">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/490c95f5-ea93-4521-8fa5-4ca1f83ff19d">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.</p>

<p>The <a href="https://msdn.microsoft.com/7ec30c51-5e07-496b-96af-8eafb564d98d">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.</p>

<p> </p>

## -members
<p>The <b>IPnpCallbackSelfManagedIo</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556780">IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/0890c352-8722-4108-9b76-60c81179b46b">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556783">IPnpCallbackSelfManagedIo::OnSelfManagedIoFlush</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/dee0e30b-ad03-43e4-8a0c-07d3782d7857">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556784">IPnpCallbackSelfManagedIo::OnSelfManagedIoInit</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/41b12fef-dbc7-4b91-a2d3-9fb1aafff237">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556785">IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/dccc4be0-0724-44b6-8476-276b46acee6a">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556787">IPnpCallbackSelfManagedIo::OnSelfManagedIoStop</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/490c95f5-ea93-4521-8fa5-4ca1f83ff19d">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556790">IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/7ec30c51-5e07-496b-96af-8eafb564d98d">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/0890c352-8722-4108-9b76-60c81179b46b">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.</p>

<p>The <a href="https://msdn.microsoft.com/dee0e30b-ad03-43e4-8a0c-07d3782d7857">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/41b12fef-dbc7-4b91-a2d3-9fb1aafff237">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/dccc4be0-0724-44b6-8476-276b46acee6a">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.</p>

<p>The <a href="https://msdn.microsoft.com/490c95f5-ea93-4521-8fa5-4ca1f83ff19d">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.</p>

<p>The <a href="https://msdn.microsoft.com/7ec30c51-5e07-496b-96af-8eafb564d98d">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.</p>

<p> </p>

## -remarks
<p>A driver registers the <b>IPnpCallbackSelfManagedIo</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object. </p>

<p>A driver registers the <b>IPnpCallbackSelfManagedIo</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create a device object. </p>

## -requirements
<table>
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