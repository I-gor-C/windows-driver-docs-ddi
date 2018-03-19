---
UID: NS:usb._URB_CONTROL_GET_CONFIGURATION_REQUEST
title: "_URB_CONTROL_GET_CONFIGURATION_REQUEST"
author: windows-driver-content
description: The _URB_CONTROL_GET_CONFIGURATION_REQUEST structure is used by USB client drivers to retrieve the current configuration for a device.
old-location: buses\_urb_control_get_configuration_request.htm
old-project: usbref
ms.assetid: 6f50b520-244e-4848-8696-969de82aa8ff
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "_URB_CONTROL_GET_CONFIGURATION_REQUEST, _URB_CONTROL_GET_CONFIGURATION_REQUEST structure [Buses], buses._urb_control_get_configuration_request, usb/_URB_CONTROL_GET_CONFIGURATION_REQUEST, usbstrct_77d89ae2-eb81-48f0-b399-85d39a5feb6a.xml"
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
-	_URB_CONTROL_GET_CONFIGURATION_REQUEST
product: Windows
targetos: Windows
req.typenames: 
req.product: Windows 10 or later.
---

# _URB_CONTROL_GET_CONFIGURATION_REQUEST structure
The _URB_CONTROL_GET_CONFIGURATION_REQUEST structure is used by USB client drivers to retrieve the current configuration for a device.

## Syntax
````
struct _URB_CONTROL_GET_CONFIGURATION_REQUEST {
  struct URB_HEADER  Hdr;
  PVOID               Reserved;
  ULONG               Reserved0;
  ULONG               TransferBufferLength;
  PVOID               TransferBuffer;
  PMDL                TransferBufferMDL;
  struct URB  *UrbLink;
  struct URB_HCD_AREA  hca;
  UCHAR               Reserved1[8];
};
````

## Members


`Hdr`

Pointer to a <a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a> structure that specifies the URB header information. <b>Hdr.Function</b> must be set to URB_FUNCTION_GET_CONFIGURATION.

<b>Hdr.Length</b> must equal <code>sizeof(_URB_CONTROL_GET_CONFIGURATION_REQUEST)</code>.

`Reserved`

Reserved. Do not use.

`Reserved0`

Reserved. Do not use.

`TransferBufferLength`

Must be 1. This member specifies the length, in bytes, of the buffer specified in <b>TransferBuffer</b> or described in <b>TransferBufferMDL</b>.

`TransferBuffer`

Pointer to a resident buffer for the transfer or is <b>NULL</b> if an MDL is supplied in <b>TransferBufferMDL</b>. The bus driver returns a single byte that specifies the index of the current configuration.

`TransferBufferMDL`

Pointer to an MDL that describes a resident buffer or is <b>NULL</b> if a buffer is supplied in <b>TransferBuffer</b>. The bus driver returns a single byte that specifies the index of the current configuration. This MDL must be allocated from nonpaged pool.

`UrbLink`

Reserved. Do not use.

`hca`

Reserved. Do not use.

`Reserved1`

Reserved. Do not use.

## Remarks
The reserved members of this structure must be treated as opaque and are reserved for system use.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="..\usb\ns-usb-_urb.md">URB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>



<a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a>