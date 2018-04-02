---
UID: NS:hidport._HID_DESCRIPTOR
title: "_HID_DESCRIPTOR"
author: windows-driver-content
description: The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device.
old-location: hid\hid_descriptor.htm
old-project: hid
ms.assetid: 80a6a5d8-b13a-418d-a4bd-941d3a913c1e
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PHID_DESCRIPTOR, HID_DESCRIPTOR, HID_DESCRIPTOR structure [Human Input Devices], PHID_DESCRIPTOR, PHID_DESCRIPTOR structure pointer [Human Input Devices], _HID_DESCRIPTOR, hid.hid_descriptor, hidport/HID_DEVICE_ATTRIBUTES, hidport/PHID_DESCRIPTOR, hidstrct_07b2c0af-449d-484e-8aa8-9d7e3909d113.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidport.h
req.include-header: Hidport.h
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
-	hidport.h
api_name:
-	HID_DESCRIPTOR
product:
- Windows
targetos: Windows
req.typenames: HID_DESCRIPTOR, *PHID_DESCRIPTOR
---

# _HID_DESCRIPTOR structure
The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device.

## Syntax
```
typedef struct _HID_DESCRIPTOR {
  UCHAR                     bLength;
  UCHAR                     bDescriptorType;
  USHORT                    bcdHID;
  UCHAR                     bCountry;
  UCHAR                     bNumDescriptors;
  struct {
    UCHAR  bReportType;
    USHORT wReportLength;
  } _HID_DESCRIPTOR_DESC_LIST;
  _HID_DESCRIPTOR_DESC_LIST DescriptorList[1];
} *PHID_DESCRIPTOR, HID_DESCRIPTOR;
```

## Members


`bLength`



`bDescriptorType`



`bcdHID`



`bCountry`



`bNumDescriptors`



`_HID_DESCRIPTOR_DESC_LIST`



`DescriptorList`



## Remarks
The HID class driver uses an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439622">IOCTL_HID_GET_DEVICE_DESCRIPTOR</a> request to obtain a device's HID descriptor from a HID minidriver.

For information about HID descriptors, see the Universal Serial Bus (USB) standard<i> Device Class Definition for Human Interface Devices (HID)</i> located at the <a href="http://www.usb.org/home">USB Implementers Forum website</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidport.h (include Hidport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439622">IOCTL_HID_GET_DEVICE_DESCRIPTOR</a>