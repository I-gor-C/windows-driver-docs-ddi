---
UID: NN.wudfusb.IWDFUsbInterface
title: IWDFUsbInterface
author: windows-driver-content
description: The IWDFUsbInterface interface exposes a USB interface that a USB device exposes.
old-location: wdf\iwdfusbinterface.htm
old-project: wdf
ms.assetid: 90770016-1267-437e-af70-99741231dc29
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _WDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbInterface
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFUsbInterface interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFUsbInterface</b> interface exposes a USB interface that a USB device exposes.

The <b>IWDFUsbInterface</b> interface exposes a USB interface that a USB device exposes.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbInterface</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFUsbInterface</b> also has these types of members:

The <b>IWDFUsbInterface</b> interface has these methods.

The <a href="wdf.iwdfusbinterface_getconfiguredsettingindex">GetConfiguredSettingIndex</a> method retrieves the current setting index for a USB interface.

The <a href="wdf.iwdfusbinterface_getinterfacedescriptor">GetInterfaceDescriptor</a> method retrieves a descriptor for a USB interface.

The <a href="wdf.iwdfusbinterface_getinterfacenumber">GetInterfaceNumber</a> method retrieves the index of a USB interface.

The <a href="wdf.iwdfusbinterface_getnumendpoints">GetNumEndPoints</a> method retrieves the number of endpoints (pipes) on a USB interface.

The <a href="wdf.iwdfusbinterface_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a USB interface.

The <a href="wdf.iwdfusbinterface_retrieveusbpipeobject">RetrieveUsbPipeObject</a> method retrieves a USB pipe object for the specified pipe index.

The <a href="wdf.iwdfusbinterface_selectsetting">SelectSetting</a> method selects the specified alternate setting on a USB interface.

 

## -members
The <b>IWDFUsbInterface</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_getconfiguredsettingindex">IWDFUsbInterface::GetConfiguredSettingIndex</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_getconfiguredsettingindex">GetConfiguredSettingIndex</a> method retrieves the current setting index for a USB interface.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_getinterfacedescriptor">IWDFUsbInterface::GetInterfaceDescriptor</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_getinterfacedescriptor">GetInterfaceDescriptor</a> method retrieves a descriptor for a USB interface.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_getinterfacenumber">IWDFUsbInterface::GetInterfaceNumber</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_getinterfacenumber">GetInterfaceNumber</a> method retrieves the index of a USB interface.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_getnumendpoints">IWDFUsbInterface::GetNumEndPoints</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_getnumendpoints">GetNumEndPoints</a> method retrieves the number of endpoints (pipes) on a USB interface.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_getwinusbhandle">IWDFUsbInterface::GetWinUsbHandle</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a USB interface.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_retrieveusbpipeobject">IWDFUsbInterface::RetrieveUsbPipeObject</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_retrieveusbpipeobject">RetrieveUsbPipeObject</a> method retrieves a USB pipe object for the specified pipe index.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbinterface_selectsetting">IWDFUsbInterface::SelectSetting</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbinterface_selectsetting">SelectSetting</a> method selects the specified alternate setting on a USB interface.
</td>
</tr>
</table>The <a href="wdf.iwdfusbinterface_getconfiguredsettingindex">GetConfiguredSettingIndex</a> method retrieves the current setting index for a USB interface.

The <a href="wdf.iwdfusbinterface_getinterfacedescriptor">GetInterfaceDescriptor</a> method retrieves a descriptor for a USB interface.

The <a href="wdf.iwdfusbinterface_getinterfacenumber">GetInterfaceNumber</a> method retrieves the index of a USB interface.

The <a href="wdf.iwdfusbinterface_getnumendpoints">GetNumEndPoints</a> method retrieves the number of endpoints (pipes) on a USB interface.

The <a href="wdf.iwdfusbinterface_getwinusbhandle">GetWinUsbHandle</a> method retrieves the WinUsb interface handle that is associated with a USB interface.

The <a href="wdf.iwdfusbinterface_retrieveusbpipeobject">RetrieveUsbPipeObject</a> method retrieves a USB pipe object for the specified pipe index.

The <a href="wdf.iwdfusbinterface_selectsetting">SelectSetting</a> method selects the specified alternate setting on a USB interface.

 

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
1.5
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h</dt>
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