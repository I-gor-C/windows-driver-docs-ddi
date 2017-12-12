---
UID: NN.wudfddi.IPnpCallbackSelfManagedIo~r1
title: IPnpCallbackSelfManagedIo
author: windows-driver-content
description: The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface.
old-location: wdf\ipnpcallbackselfmanagedio.htm
old-project: wdf
ms.assetid: 34971df0-4abc-41a1-8d2f-6e36df1daf20
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
req.product: Windows 10 or later.
---

# IPnpCallbackSelfManagedIo interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IPnpCallbackSelfManagedIo</b> interface is a Plug and Play (PnP) and power management (PM) interface. 



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackSelfManagedIo</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackSelfManagedIo</b> also has these types of members:

The <b>IPnpCallbackSelfManagedIo</b> interface has these methods.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediocleanup">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioflush">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioinit">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediorestart">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediostop">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediosuspend">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.

 


## -members
The <b>IPnpCallbackSelfManagedIo</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediocleanup">IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediocleanup">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioflush">IPnpCallbackSelfManagedIo::OnSelfManagedIoFlush</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioflush">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioinit">IPnpCallbackSelfManagedIo::OnSelfManagedIoInit</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioinit">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediorestart">IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediorestart">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediostop">IPnpCallbackSelfManagedIo::OnSelfManagedIoStop</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediostop">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediosuspend">IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediosuspend">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.

</td>
</tr>
</table>The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediocleanup">OnSelfManagedIoCleanup</a> method releases memory for a device's self-managed I/O operations, after the device is removed.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioflush">OnSelfManagedIoFlush</a> method flushes the device for a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagedioinit">OnSelfManagedIoInit</a> method initializes a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediorestart">OnSelfManagedIoRestart</a> method restarts a device's self-managed I/O operations.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediostop">OnSelfManagedIoStop</a> method is not used in the current version of the UMDF.

The <a href="wdf.ipnpcallbackselfmanagedio_onselfmanagediosuspend">OnSelfManagedIoSuspend</a> method suspends a device's self-managed I/O operations.

 


## -remarks
A driver registers the <b>IPnpCallbackSelfManagedIo</b> interface when the driver calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. 


## -requirements
<table>
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
</table>