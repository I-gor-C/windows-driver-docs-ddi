---
UID : NS:usb._URB_CONTROL_VENDOR_OR_CLASS_REQUEST
title : _URB_CONTROL_VENDOR_OR_CLASS_REQUEST
author : windows-driver-content
description : The _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target.
old-location : buses\_urb_control_vendor_or_class_request.htm
old-project : usbref
ms.assetid : 3d355489-cc70-4fa1-b08f-08ccf84f5490
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _URB_CONTROL_VENDOR_OR_CLASS_REQUEST,
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : usb.h
req.include-header : Usb.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : _URB_CONTROL_VENDOR_OR_CLASS_REQUEST
req.alt-loc : usb.h
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
req.typenames : 
req.product : Windows 10 or later.
---

# _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure
The <b>_URB_CONTROL_VENDOR_OR_CLASS_REQUEST</b> structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target.

## Syntax
````
struct _URB_CONTROL_VENDOR_OR_CLASS_REQUEST {
  struct URB_HEADER  Hdr;
  PVOID               Reserved;
  ULONG               TransferFlags;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  UCHAR               RequestTypeReservedBits;
  UCHAR               Request;
  USHORT              Value;
  USHORT              Index;
  USHORT              Reserved1;
};
````

## Members

        
            `hca`

            Reserved. Do not use.
        
            `Hdr`

            Pointer to a <a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be one of URB_FUNCTION_CLASS_XXX or URB_FUNCTION_VENDOR_XXX GET_STATUS, and <b>Hdr.Length</b> must be <code>sizeof(_URB_CONTROL_VENDOR_OR_CLASS_REQUEST)</code>.
        
            `Index`

            Specifies the device-defined index, returned by a successful configuration request, if the request is for an endpoint or interface. Otherwise, <b>Index</b> must be zero.
        
            `Request`

            Specifies the USB or vendor-defined request code for the device, interface, endpoint, or other device-defined target.
        
            `RequestTypeReservedBits`

            Reserved. Do not use.
        
            `Reserved`

            
        
            `Reserved1`

            Reserved. Do not use.
        
            `TransferBuffer`

            Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The contents of this buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified this buffer will contain data read from the device on return from the host controller driver. Otherwise, this buffer contains driver-supplied data for transfer to the device.
        
            `TransferBufferLength`

            Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes sent to or read from the pipe in this member.
        
            `TransferBufferMDL`

            Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The contents of the buffer depend on the value of <b>TransferFlags</b>. If USBD_TRANSFER_DIRECTION_IN is specified, the described buffer will contain data read from the device on return from the host controller driver. Otherwise, the buffer contains driver-supplied data for transfer to the device. This MDL must be allocated from nonpaged pool.
        
            `TransferFlags`

            Specifies zero, one, or a combination of the following flags:



<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `UrbLink`

            Reserved. Do not use.
        
            `Value`

            Specifies a value, specific to <b>Request</b>, that becomes part of the USB-defined setup packet for the target. This value is defined by the creator of the code used in <b>Request</b>.

    ## Remarks
        Drivers can use the <b>UsbBuildVendorRequest</b> service routine format this URB.

The reserved members of this structure must be treated as opaque and are reserved for system use.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usb.h (include Usb.h) |

    ## See Also

        <dl>
<dt>
<a href="..\usb\ns-usb-_urb.md">URB</a>
</dt>
<dt>
<a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>