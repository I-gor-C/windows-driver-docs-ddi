---
UID : NS:usb._URB_CONTROL_GET_STATUS_REQUEST
title : _URB_CONTROL_GET_STATUS_REQUEST
author : windows-driver-content
description : The _URB_CONTROL_GET_STATUS_REQUEST structure is used by USB client drivers to retrieve status from a device, interface, endpoint, or other device-defined target.
old-location : buses\_urb_control_get_status_request.htm
old-project : usbref
ms.assetid : 6a005ff3-951f-462d-84e6-e1fd931c5afc
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _URB_CONTROL_GET_STATUS_REQUEST,
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
req.alt-api : _URB_CONTROL_GET_STATUS_REQUEST
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

# _URB_CONTROL_GET_STATUS_REQUEST structure
The _URB_CONTROL_GET_STATUS_REQUEST structure is used by USB client drivers to retrieve status from a device, interface, endpoint, or other device-defined target.

## Syntax
````
struct _URB_CONTROL_GET_STATUS_REQUEST {
  struct URB_HEADER  Hdr;
  PVOID               Reserved;
  ULONG               Reserved0;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  UCHAR               Reserved1[4];
  USHORT              Index;
  USHORT              Reserved2;
};
````

## Members

        
            `hca`

            Reserved. Do not use.
        
            `Hdr`

            Pointer to a <a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Length</b> must be <code>sizeof(_URB_CONTROL_GET_STATUS_REQUEST)</code>, and <b>Hdr.Function</b> must be one of the following values:

<dl>
<dd>URB_FUNCTION_GET_STATUS_FROM_DEVICE</dd>
<dd>URB_FUNCTION_GET_STATUS_FROM_INTERFACE</dd>
<dd>URB_FUNCTION_GET_STATUS_FROM_ENDPOINT</dd>
<dd>URB_FUNCTION_GET_STATUS_FROM_OTHER.</dd>
</dl>
        
            `Index`

            Specifies the device-defined index, returned by a successful configuration request, if the request is for an endpoint or interface. Otherwise, <b>Index</b> must be zero.
        
            `Reserved`

            Reserved. Do not use.
        
            `Reserved0`

            Reserved. Do not use.
        
            `Reserved1`

            Reserved. Do not use.
        
            `Reserved2`

            Reserved. Do not use.
        
            `TransferBuffer`

            Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The bus driver returns a single byte specifying the status for the target.
        
            `TransferBufferLength`

            Must be 2. This member specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes sent to or read from the pipe in this member.
        
            `TransferBufferMDL`

            Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The bus driver returns a single byte specifying the status for the target. This MDL must be allocated from nonpaged pool.
        
            `UrbLink`

            Reserved. Do not use.

    ## Remarks
        Drivers can use the <a href="..\usbdlib\nf-usbdlib-usbbuildgetstatusrequest.md">UsbBuildGetStatusRequest</a> service routine to format this URB.

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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_CONTROL_GET_STATUS_REQUEST structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>