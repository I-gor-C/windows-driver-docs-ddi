---
UID: NF.wdfusb.WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING
title: WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING
author: windows-driver-content
description: The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING function initializes a WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure so that a driver can select a USB interface by specifying a handle to an interface object and an alternate setting for the interface.
old-location: wdf\wdf_usb_interface_select_setting_params_init_setting.htm
old-project: wdf
ms.assetid: 2b58eb8f-c468-4bc6-ad50-0bc9f2dee561
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING
req.alt-loc: wdfusb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</b> function initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure so that a driver can select a USB interface by specifying a handle to an interface object and an alternate setting for the interface.</p>


## -syntax

````
VOID WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING(
  _Out_ PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS Params,
  _In_  UCHAR                                    SettingIndex
);
````


## -parameters
<dl>

### -param <i>Params</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure.</p>
</dd>

### -param <i>SettingIndex</i> [in]

<dd>
<p>An index value that identifies an alternate setting for the interface. (The interface is identified by an interface object handle that the driver passes to <a href="..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md">WdfUsbInterfaceSelectSetting</a>.) </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</b> function zeros the <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure and sets its <b>Size</b> member to the size of the structure. It also sets the <b>Type</b> member to <b>WdfUsbInterfaceSelectSettingTypeSetting</b> and sets the <b>Types.Interface.SettingIndex</b> member to the value that is specified by <i>SettingIndex</i>.</p>

<p>To initialize a <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure, your driver must call one of the following functions:</p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-descriptor.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR</a>
</p>

<p><b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</b></p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-urb.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB</a>
</p>

<p>For a code example that uses <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</b>, see <a href="..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md">WdfUsbInterfaceSelectSetting</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-descriptor.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-urb.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md">WdfUsbInterfaceSelectSetting</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
