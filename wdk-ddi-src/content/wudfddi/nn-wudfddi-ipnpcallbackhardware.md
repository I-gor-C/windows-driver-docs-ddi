---
UID: NN.wudfddi.IPnpCallbackHardware
title: IPnpCallbackHardware
author: windows-driver-content
description: The IPnpCallbackHardware interface is a Plug and Play (PnP) and power management (PM) interface.
old-location: wdf\ipnpcallbackhardware.htm
old-project: wdf
ms.assetid: 2746e7ab-690c-4382-be9a-124a7d68cf72
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
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
req.alt-api: IPnpCallbackHardware
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IPnpCallbackHardware interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IPnpCallbackHardware</b> interface is a Plug and Play (PnP) and power management (PM) interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackHardware</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackHardware</b> also has these types of members:</p>

<p>The <b>IPnpCallbackHardware</b> interface has these methods.</p>

<p>The <a href="wdf.ipnpcallbackhardware_onpreparehardware">OnPrepareHardware</a> method notifies a driver to make the specified hardware accessible.</p>

<p>The <a href="wdf.ipnpcallbackhardware_onreleasehardware">OnReleaseHardware</a> method notifies a driver to perform operations that are necessary when the specified hardware is no longer accessible.</p>

<p> </p>

## -members
<p>The <b>IPnpCallbackHardware</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackhardware_onpreparehardware">IPnpCallbackHardware::OnPrepareHardware</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.ipnpcallbackhardware_onpreparehardware">OnPrepareHardware</a> method notifies a driver to make the specified hardware accessible.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackhardware_onreleasehardware">IPnpCallbackHardware::OnReleaseHardware</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.ipnpcallbackhardware_onreleasehardware">OnReleaseHardware</a> method notifies a driver to perform operations that are necessary when the specified hardware is no longer accessible.</p>
</td>
</tr>
</table><p>The <a href="wdf.ipnpcallbackhardware_onpreparehardware">OnPrepareHardware</a> method notifies a driver to make the specified hardware accessible.</p>

<p>The <a href="wdf.ipnpcallbackhardware_onreleasehardware">OnReleaseHardware</a> method notifies a driver to perform operations that are necessary when the specified hardware is no longer accessible.</p>

<p> </p>

## -remarks
<p>A driver registers the <b>IPnpCallbackHardware</b> interface when the driver calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. </p>

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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-ipnpcallbackhardware2.md">IPnpCallbackHardware2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardware interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
