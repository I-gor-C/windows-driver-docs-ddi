---
UID: NF.wudfusb.IWDFUsbInterface.SelectSetting
title: IWDFUsbInterface::SelectSetting
author: windows-driver-content
description: The SelectSetting method selects the specified alternate setting on a USB interface.
old-location: wdf\iwdfusbinterface_selectsetting.htm
old-project: wdf
ms.assetid: c47b025b-1be9-4fdc-965a-a9a82a394177
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFUsbInterface, SelectSetting, IWDFUsbInterface::SelectSetting
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbInterface.SelectSetting
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
req.iface: IWDFUsbInterface
req.product: Windows 10 or later.
---

# IWDFUsbInterface::SelectSetting method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>SelectSetting</b> method selects the specified alternate setting on a USB interface.</p>


## -syntax

````
HRESULT SelectSetting(
  [in] UCHAR SettingNumber
);
````


## -parameters
<dl>

### -param <i>SettingNumber</i> [in]

<dd>
<p>The setting to select on the USB interface.</p>
</dd>
</dl>

## -returns
<p><b>SelectSetting</b> returns one of the following values: </p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdfusbinterface_selectsetting">SelectSetting</a> successfully selected the setting that the <i>SettingNumber</i> parameter specified. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdfusbinterface_selectsetting">SelectSetting</a> encountered an allocation failure.</p><dl>
<dt><b>An error code that is defined in Winerror.h</b></dt>
</dl><p>This value corresponds to the error code that the WinUsb API returned.</p>

<p> </p>

## -remarks
<p>The framework automatically selects configuration zero, its interface zero, and the alternate setting zero. To change the alternate setting, the driver can call <b>SelectSetting</b>.</p>

<p>For more info <a href="buses.usb_configuration_descriptors">USB Configuration Descriptors</a>
</p>

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
<dt>Wudfusb.h (include Wudfusb.h)</dt>
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
<a href="..\wudfusb\nn-wudfusb-iwdfusbinterface.md">IWDFUsbInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbInterface::SelectSetting method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
