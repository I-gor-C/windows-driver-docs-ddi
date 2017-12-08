---
UID: NE.wdfusb._WdfUsbTargetDeviceSelectSettingType
title: _WdfUsbTargetDeviceSelectSettingType
author: windows-driver-content
description: The WdfUsbTargetDeviceSelectSettingType enumeration defines techniques for specifying an alternate setting for a USB interface.
old-location: wdf\wdfusbtargetdeviceselectsettingtype.htm
old-project: wdf
ms.assetid: 3bbe3da6-f069-4965-ae60-2d755d7557c1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _WdfUsbTargetDeviceSelectSettingType, WdfUsbTargetDeviceSelectSettingType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetDeviceSelectSettingType
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
req.irql: <=DISPATCH_LEVEL  (See Remarks section.)
req.product: Windows 10 or later.
---

# _WdfUsbTargetDeviceSelectSettingType enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfUsbTargetDeviceSelectSettingType</b> enumeration defines techniques for specifying an alternate setting for a USB interface.


## -syntax

````
typedef enum _WdfUsbTargetDeviceSelectSettingType { 
  WdfUsbInterfaceSelectSettingTypeDescriptor  = 0x10,
  WdfUsbInterfaceSelectSettingTypeSetting     = 0x11,
  WdfUsbInterfaceSelectSettingTypeUrb         = 0x12
} WdfUsbTargetDeviceSelectSettingType;
````


## -enum-fields

### -field WdfUsbInterfaceSelectSettingTypeDescriptor

Specify an interface's alternate setting by providing a <a href="buses.usb_interface_descriptor">USB_INTERFACE_DESCRIPTOR</a> structure.

### -field WdfUsbInterfaceSelectSettingTypeSetting

Specify an interface's alternate setting by providing a setting index value.

### -field WdfUsbInterfaceSelectSettingTypeUrb

Specify an interface's alternate setting by providing a <a href="buses.urb">URB</a>.

## -remarks
The <b>WdfUsbTargetDeviceSelectSettingType</b> enumeration is used in the <a href="wdf.wdf_usb_interface_select_setting_params">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure.

## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="buses.urb">URB</a>
</dt>
<dt>
<a href="buses.usb_interface_descriptor">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="wdf.wdf_usb_interface_select_setting_params">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceSelectSettingType enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
