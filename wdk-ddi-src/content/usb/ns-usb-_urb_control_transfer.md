---
UID : NS:usb._URB_CONTROL_TRANSFER
title : _URB_CONTROL_TRANSFER
author : windows-driver-content
description : The _URB_CONTROL_TRANSFER structure is used by USB client drivers to transfer data to or from a control pipe.
old-location : buses\_urb_control_transfer.htm
old-project : usbref
ms.assetid : ee557112-ada3-4906-a8f3-e59b59ab2bc1
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _URB_CONTROL_TRANSFER,
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
req.alt-api : _URB_CONTROL_TRANSFER
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

# _URB_CONTROL_TRANSFER structure
The <b>_URB_CONTROL_TRANSFER</b> structure is used by USB client drivers to transfer data to or from a control pipe.

## Syntax
````
struct _URB_CONTROL_TRANSFER {
  struct URB_HEADER  Hdr;
  USBD_PIPE_HANDLE    PipeHandle;
  ULONG               TransferFlags;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  UCHAR               SetupPacket[8];
};
````

## Members

        
            `hca`

            Reserved. Do not use.
        
            `Hdr`

            Pointer to a <a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be URB_FUNCTION_CONTROL_TRANSFER, and <b>Hdr.Length</b> must be <code>sizeof(_URB_CONTROL_TRANSFER)</code>.
        
            `PipeHandle`

            Handle for the control pipe.

 If target is the default control endpoint, then  <b>PipeHandle</b> must be <b>NULL</b>.  In this case, the <b>TransferFlags</b> must contain the USBD_DEFAULT_PIPE_TRANSFER flag.

If target is a non-default control endpoint, <b>PipeHandle</b> specifies an opaque handle for the control pipe. The host controller driver returns this handle when the client driver selects the device configuration with a URB of type URB_FUNCTION_SELECT_CONFIGURATION or when the client driver changes the settings for an interface with a URB of type URB_FUNCTION_SELECT_INTERFACE.
        
            `SetupPacket`

            Specifies a USB-defined request setup packet. The format of a USB request setup packet is found in the USB core specification.
        
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

    ## Remarks
        The <a href="..\usb\ns-usb-_urb_control_transfer_ex.md">URB_CONTROL_TRANSFER_EX</a> structure is identical to <b>URB_CONTROL_TRANSFER</b>, except that it provides a timeout value in the <b>Timeout</b> field.

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
<a href="..\usb\ns-usb-_urb_control_transfer_ex.md">URB_CONTROL_TRANSFER_EX</a>
</dt>
<dt>
<a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_CONTROL_TRANSFER structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>