---
UID: NN.wudfddi.IPnpCallbackHardware2~r1
title: IPnpCallbackHardware2
author: windows-driver-content
description: The IPnpCallbackHardware2 interface exposes callback methods related to hardware.
old-location: wdf\ipnpcallbackhardware2.htm
old-project: wdf
ms.assetid: C0DB967F-0A1A-4749-B902-EBA0D59A3E45
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IPnpCallbackHardware2
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IPnpCallbackHardware2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>  The <b>IPnpCallbackHardware2</b>  interface exposes callback methods related to hardware.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackHardware2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackHardware2</b> also has these types of members:</p>

<p>The <b>IPnpCallbackHardware2</b> interface has these methods.</p>

<p>
   The <a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a> method performs any operations that are needed to make a device accessible to the driver.
  </p>

<p>The <a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a> method performs operations that are needed when a device is no longer accessible.</p>

<p> </p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackHardware2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackHardware2</b> also has these types of members:</p>

<p>The <b>IPnpCallbackHardware2</b> interface has these methods.</p>

<p>
   The <a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a> method performs any operations that are needed to make a device accessible to the driver.
  </p>

<p>The <a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a> method performs operations that are needed when a device is no longer accessible.</p>

<p> </p>

## -members
<p>The <b>IPnpCallbackHardware2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a>
</td>
<td align="left" width="63%">
<p>
   The <a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a> method performs any operations that are needed to make a device accessible to the driver.
  </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a> method performs operations that are needed when a device is no longer accessible.</p>
</td>
</tr>
</table><p>
   The <a href="wdf.ipnpcallbackhardware2_onpreparehardware">OnPrepareHardware</a> method performs any operations that are needed to make a device accessible to the driver.
  </p>

<p>The <a href="wdf.ipnpcallbackhardware2_onreleasehardware">OnReleaseHardware</a> method performs operations that are needed when a device is no longer accessible.</p>

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
<p>1.11</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="com.iunknown">IUnknown</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IPnpCallbackHardware2 interface%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
