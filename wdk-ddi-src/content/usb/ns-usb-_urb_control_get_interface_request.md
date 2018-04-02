---
UID: NS:usb._URB_CONTROL_GET_INTERFACE_REQUEST
title: "_URB_CONTROL_GET_INTERFACE_REQUEST"
author: windows-driver-content
description: The _URB_CONTROL_GET_INTERFACE_REQUEST structure is used by USB client drivers to retrieve the current alternate interface setting for an interface in the current configuration.
old-location: buses\_urb_control_get_interface_request.htm
old-project: usbref
ms.assetid: 64f843ba-8462-48d4-ba3a-a028bb921880
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "_URB_CONTROL_GET_INTERFACE_REQUEST, _URB_CONTROL_GET_INTERFACE_REQUEST structure [Buses], buses._urb_control_get_interface_request, usb/_URB_CONTROL_GET_INTERFACE_REQUEST, usbstrct_b0ec613c-60c0-4043-9506-5c0ede728380.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
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
-	_URB_CONTROL_GET_INTERFACE_REQUEST
product: Windows
targetos: Windows
req.typenames: 
req.product: Windows 10 or later.
---

# _URB_CONTROL_GET_INTERFACE_REQUEST structure
The <b>_URB_CONTROL_GET_INTERFACE_REQUEST</b> structure is used by USB client drivers to retrieve the current alternate interface setting for an interface in the current configuration.

## Syntax
```
struct _URB_CONTROL_GET_INTERFACE_REQUEST {
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
  UCHAR         Reserved1[4];
  USHORT        Interface;
  USHORT        Reserved2;
};
```

## Members


`Hdr`

Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be URB_FUNCTION_GET_INTERFACE, and <b>Hdr.Length</b> must equal <code>sizeof(_URB_CONTROL_GET_INTERFACE_REQUEST)</code>.

`Reserved`

Reserved. Do not use.

`Reserved0`

Reserved. Do not use.

`TransferBufferLength`

Must be 1. This member specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>. The host controller driver returns the number of bytes sent to or read from the pipe in this member.

`TransferBuffer`

Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The bus driver returns a single byte specifying the index of the current alternate setting for the interface.

`TransferBufferMDL`

Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The bus driver returns a single byte specifying the index of the current alternate setting for the interface. This MDL must be allocated from nonpaged pool.

`UrbLink`

Reserved. Do not use.

`hca`

Reserved. Do not use.

`Reserved1`

Reserved. Do not use.

`Interface`

Specifies the device-defined index of the interface descriptor being retrieved.

`Reserved2`

Reserved. Do not use.

## Remarks
The reserved members of this structure must be treated as opaque and are reserved for system use.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a>