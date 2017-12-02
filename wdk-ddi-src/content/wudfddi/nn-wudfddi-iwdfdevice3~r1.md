---
UID: NN.wudfddi.IWDFDevice3~r1
title: IWDFDevice3
author: windows-driver-content
description: To obtain the IWDFDevice3 interface, drivers call IWDFDevice::QueryInterface.
old-location: wdf\iwdfdevice3.htm
old-project: wdf
ms.assetid: C4AEC0DA-EB93-481D-A94C-7BB7BF15EFBC
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: IWDFDevice3
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

# IWDFDevice3 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>To obtain the <b>IWDFDevice3</b> interface, drivers call <b>IWDFDevice::QueryInterface</b>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDevice3</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a>. <b>IWDFDevice3</b> also has these types of members:</p>

<p>The <b>IWDFDevice3</b> interface has these methods.</p>

<p>The 
  <a href="wdf.iwdfdevice3_assigns0idlesettingsex">AssignS0IdleSettingsEx</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>

<p>The <a href="wdf.iwdfdevice3_createinterrupt">CreateInterrupt</a> method creates a framework interrupt object.
</p>

<p>The <a href="wdf.iwdfdevice3_createworkitem">CreateWorkItem</a> method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue.</p>

<p>A driver calls <a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">GetHardwareRegisterMappedAddress</a> to get the user-mode mapped address of the memory resource it earlier mapped using <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a>.</p>

<p>The <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method maps the given physical address range to system address space and returns a pseudo base address. </p>

<p>The <a href="wdf.iwdfdevice3_readfromhardware">ReadFromHardware</a> method is used internally by the framework. Do not use.</p>

<p>The <a href="wdf.iwdfdevice3_unmapiospace">UnmapIoSpace</a> method unmaps a specified range of physical addresses previously mapped by <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method.</p>

<p>The <a href="wdf.iwdfdevice3_writetohardware">WriteToHardware</a> method is used internally by the framework. Do not use.</p>

<p> </p>

## -members
<p>The <b>IWDFDevice3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_assigns0idlesettingsex">AssignS0IdleSettingsEx</a>
</td>
<td align="left" width="63%">
<p>The 
  <a href="wdf.iwdfdevice3_assigns0idlesettingsex">AssignS0IdleSettingsEx</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_createinterrupt">CreateInterrupt</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_createinterrupt">CreateInterrupt</a> method creates a framework interrupt object.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_createworkitem">CreateWorkItem</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_createworkitem">CreateWorkItem</a> method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">GetHardwareRegisterMappedAddress</a>
</td>
<td align="left" width="63%">
<p>A driver calls <a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">GetHardwareRegisterMappedAddress</a> to get the user-mode mapped address of the memory resource it earlier mapped using <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method maps the given physical address range to system address space and returns a pseudo base address. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_readfromhardware">ReadFromHardware</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_readfromhardware">ReadFromHardware</a> method is used internally by the framework. Do not use.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_unmapiospace">UnmapIoSpace</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_unmapiospace">UnmapIoSpace</a> method unmaps a specified range of physical addresses previously mapped by <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice3_writetohardware">WriteToHardware</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice3_writetohardware">WriteToHardware</a> method is used internally by the framework. Do not use.</p>
</td>
</tr>
</table><p>The 
  <a href="wdf.iwdfdevice3_assigns0idlesettingsex">AssignS0IdleSettingsEx</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>

<p>The <a href="wdf.iwdfdevice3_createinterrupt">CreateInterrupt</a> method creates a framework interrupt object.
</p>

<p>The <a href="wdf.iwdfdevice3_createworkitem">CreateWorkItem</a> method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue.</p>

<p>A driver calls <a href="wdf.iwdfdevice3_gethardwareregistermappedaddress">GetHardwareRegisterMappedAddress</a> to get the user-mode mapped address of the memory resource it earlier mapped using <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a>.</p>

<p>The <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method maps the given physical address range to system address space and returns a pseudo base address. </p>

<p>The <a href="wdf.iwdfdevice3_readfromhardware">ReadFromHardware</a> method is used internally by the framework. Do not use.</p>

<p>The <a href="wdf.iwdfdevice3_unmapiospace">UnmapIoSpace</a> method unmaps a specified range of physical addresses previously mapped by <a href="wdf.iwdfdevice3_mapiospace">MapIoSpace</a> method.</p>

<p>The <a href="wdf.iwdfdevice3_writetohardware">WriteToHardware</a> method is used internally by the framework. Do not use.</p>

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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfdevice2.md">IWDFDevice2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice3 interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
