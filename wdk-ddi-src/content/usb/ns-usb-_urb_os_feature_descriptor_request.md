---
UID: NS:usb._URB_OS_FEATURE_DESCRIPTOR_REQUEST
title: "_URB_OS_FEATURE_DESCRIPTOR_REQUEST"
author: windows-driver-content
description: The _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device.
old-location: buses\_urb_os_feature_descriptor_request.htm
old-project: usbref
ms.assetid: 9ff62523-e9e3-4f32-802f-6fee0082d925
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "_URB_OS_FEATURE_DESCRIPTOR_REQUEST, _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure [Buses], buses._urb_os_feature_descriptor_request, usb/_URB_OS_FEATURE_DESCRIPTOR_REQUEST"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	usb.h
api_name:
-	_URB_OS_FEATURE_DESCRIPTOR_REQUEST
product:
- Windows
targetos: Windows
req.typenames: 
req.product: Windows 10 or later.
---

# _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure
The <b>_URB_OS_FEATURE_DESCRIPTOR_REQUEST</b> structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device.

## Syntax
```
struct _URB_OS_FEATURE_DESCRIPTOR_REQUEST {
  _URB_HEADER   Hdr;
  struct        _URB_HEADER;
  PVOID         Reserved;
  ULONG         Reserved0;
  ULONG         TransferBufferLength;
  PVOID         TransferBuffer;
  PMDL          TransferBufferMDL;
  _URB          *UrbLink;
  struct        _URB;
  _URB_HCD_AREA hca;
  struct        _URB_HCD_AREA;
  UCHAR  : 5    Recipient;
  UCHAR  : 3    Reserved1;
  UCHAR         Reserved2;
  UCHAR         InterfaceNumber;
  UCHAR         MS_PageIndex;
  USHORT        MS_FeatureDescriptorIndex;
  USHORT        Reserved3;
};
```

## Members


`Hdr`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must URB_FUNCTION_GET_MS_FEATURE_DESCRIPTOR.
<b>Hdr.Length</b> must be <code>sizeof(_URB_OS_FEATURE_DESCRIPTOR_REQUEST)</code>.

`Reserved`



`Reserved0`



`TransferBufferLength`

Specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes read in this member.  Current implementation of this function limits the maximum MS OS Feature Descriptor size to 4 Kilobytes.

`TransferBuffer`

Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>.

`TransferBufferMDL`

Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. This MDL must be allocated from nonpaged pool.

`UrbLink`

Reserved. Do not use.

`hca`



`Recipient`

Specifies whether the recipient is the USB device or an interface on the USB device.  One of the following values must be specified:

<ul>
<li>0 indicates that the USB device is the recipient of the request.
</li>
<li>1 indicates that a USB interface is the recipient of the request. 
</li>
<li>2 indicates that a USB endpoint is the recipient of the request. 
</li>
</ul>

`Reserved1`



`Reserved2`



`InterfaceNumber`

Indicates the interface number that is the recipient of the request, if the <b>Recipient</b> member value is 1. Must be set to 0 if the USB device is the recipient.

`MS_PageIndex`

Must be set to 0. Page index of the 64K page of the MS OS Feature Descriptor to be returned.  Current implementation only supports a maximum descriptor size of 4K.

`MS_FeatureDescriptorIndex`

Index for MS OS Feature Descriptor to be requested.

`Reserved3`



## Remarks
The reserved members of this structure must be treated as opaque and are reserved for system use.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later operating systems. Available in Windows XP and later operating systems. |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a>