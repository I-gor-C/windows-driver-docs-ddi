---
UID : NS:wdfusb._WDF_USB_INTERFACE_SELECT_SETTING_PARAMS
title : _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS
author : windows-driver-content
description : The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure contains selection information for a USB interface.
old-location : wdf\wdf_usb_interface_select_setting_params.htm
old-project : wdf
ms.assetid : fad8a205-8427-48c5-b4b5-b125aa9fe85c
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, *PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wdfusb.h
req.include-header : Wdfusb.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 1.0
req.umdf-ver : 2.0
req.alt-api : WDF_USB_INTERFACE_SELECT_SETTING_PARAMS
req.alt-loc : wdfusb.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, *PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS
req.product : Windows 10 or later.
---

# _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure contains selection information for a USB interface.

## Syntax
````
typedef struct _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS {
  ULONG                               Size;
  WdfUsbTargetDeviceSelectSettingType Type;
  union {
    struct {
      PUSB_INTERFACE_DESCRIPTOR InterfaceDescriptor;
    } Descriptor;
    struct {
      UCHAR SettingIndex;
    } Interface;
    struct {
      PURB Urb;
    } Urb;
  } Types;
} WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, *PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS;
````

## Members

        
            `Size`

            The size, in bytes, of this structure.
        
            `Type`

            A <a href="..\wdfusb\ne-wdfusb-_wdfusbtargetdeviceselectsettingtype.md">WdfUsbTargetDeviceSelectSettingType</a>-typed value that identifies a technique for specifying a device interface.
        
            `Types`

            

    ## Remarks
        The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure is used as input to the <a href="..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md">WdfUsbInterfaceSelectSetting</a> method. 

To initialize a <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure, your driver must call one of the following functions:


<a href="..\wdfusb\nf-wdfusb-wdf_usb_interface_select_setting_params_init_descriptor.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR</a>



<a href="..\wdfusb\nf-wdfusb-wdf_usb_interface_select_setting_params_init_setting.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</a>



<a href="..\wdfusb\nf-wdfusb-wdf_usb_interface_select_setting_params_init_urb.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB</a>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

    ## See Also

        <dl>
<dt>
<a href="..\usb\ns-usb-_urb.md">URB</a>
</dt>
<dt>
<a href="..\usbspec\ns-usbspec-_usb_interface_descriptor.md">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md">WdfUsbInterfaceSelectSetting</a>
</dt>
<dt>
<a href="..\wdfusb\ne-wdfusb-_wdfusbtargetdeviceselectsettingtype.md">WdfUsbTargetDeviceSelectSettingType</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>