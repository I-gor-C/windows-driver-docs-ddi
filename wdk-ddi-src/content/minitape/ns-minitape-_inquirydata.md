---
UID: NS:minitape._INQUIRYDATA
title: "_INQUIRYDATA"
author: windows-driver-content
description: The INQUIRYDATA structure is used in conjunction with the TapeMiniExtensionInit and TapeMiniVerifyInquiry routines to report SCSI inquiry data associated with a tape device.
old-location: storage\inquirydata.htm
old-project: storage
ms.assetid: 2389fb1e-b16a-4d0a-b347-8b8a0f1cf061
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PINQUIRYDATA, INQUIRYDATA, INQUIRYDATA structure [Storage Devices], PINQUIRYDATA, PINQUIRYDATA structure pointer [Storage Devices], _INQUIRYDATA, scsi/INQUIRYDATA, scsi/PINQUIRYDATA, storage.inquirydata, structs-tape_be59bcac-0d77-4186-99a6-97c34bb37793.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: minitape.h
req.include-header: Scsi.h, Minitape.h, Storport.h
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
-	scsi.h
api_name:
-	INQUIRYDATA
product: Windows
targetos: Windows
req.typenames: INQUIRYDATA, *PINQUIRYDATA, INQUIRYDATA, *PINQUIRYDATA
---

# _INQUIRYDATA structure
The INQUIRYDATA structure is used in conjunction with the <a href="..\minitape\nc-minitape-tape_extension_init_routine.md">TapeMiniExtensionInit</a> and <a href="..\minitape\nc-minitape-tape_verify_inquiry_routine.md">TapeMiniVerifyInquiry</a> routines to report SCSI inquiry data associated with a tape device.

## Syntax
````
typedef struct _INQUIRYDATA {
  UCHAR DeviceType  :5;
  UCHAR DeviceTypeQualifier  :3;
  UCHAR DeviceTypeModifier  :7;
  UCHAR RemovableMedia  :1;
  union {
    UCHAR  Versions;
    struct {
      UCHAR ANSIVersion  :3;
      UCHAR ECMAVersion  :3;
      UCHAR ISOVersion  :2;
    };
  };
  UCHAR ResponseDataFormat  :4;
  UCHAR HiSupport  :1;
  UCHAR NormACA  :1;
  UCHAR TerminateTask  :1;
  UCHAR AERC  :1;
  UCHAR AdditionalLength;
  UCHAR Reserved;
  UCHAR Addr16  :1;
  UCHAR Addr32  :1;
  UCHAR AckReqQ  :1;
  UCHAR MediumChanger  :1;
  UCHAR MultiPort  :1;
  UCHAR ReservedBit2  :1;
  UCHAR EnclosureServices  :1;
  UCHAR ReservedBit3  :1;
  UCHAR SoftReset  :1;
  UCHAR CommandQueue  :1;
  UCHAR TransferDisable  :1;
  UCHAR LinkedCommands  :1;
  UCHAR Synchronous  :1;
  UCHAR Wide16Bit  :1;
  UCHAR Wide32Bit  :1;
  UCHAR RelativeAddressing  :1;
  UCHAR VendorId[8];
  UCHAR ProductId[16];
  UCHAR ProductRevisionLevel[4];
  UCHAR VendorSpecific[20];
  UCHAR Reserved3[40];
} INQUIRYDATA, *PINQUIRYDATA;
````

## Members


`DeviceType`

Specifies the type of device. For a complete list of symbolic constants that indicate the various device types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563821">Specifying Device Types</a>.

`DeviceTypeQualifier`

Indicates whether the device is present or not. The values that this member can take are as follows:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
DEVICE_QUALIFIER_ACTIVE

</td>
<td>
The operating system supports the device, and the device is present.

</td>
</tr>
<tr>
<td>
DEVICE_QUALIFIER_NOT_ACTIVE

</td>
<td>
The operating system supports the device, but the device is not present.

</td>
</tr>
<tr>
<td>
DEVICE_QUALIFIER_NOT_SUPPORTED

</td>
<td>
The operating system does not support this device. 

</td>
</tr>
</table>

`DeviceTypeModifier`

Specifies the device type modifier, if any, as defined by SCSI. If no device type modifier exists, this member is zero.

`RemovableMedia`

Indicates, when <b>TRUE</b>, that the media is removable, and when <b>FALSE</b> that the media is not removable.

`Versions`

Indicates the version of the inquiry data standard that this data conforms to. For more information about the version values allowed in this field, see the <i>SCSI Primary Commands - 2 (SPC-2)</i> specification.

`ResponseDataFormat`

Indicates the SCSI standard that governs the response data format. The value of this member must be 2.

`HiSupport`

Indicates, when zero, that the target does not use the hierarchical addressing model to assign LUNs to logical units. A value of 1 indicates the target uses the hierarchical addressing model to assign LUNs to logical units.

`NormACA`

Indicates, when set to one, that the operating system supports setting the NACA bit to one in the control byte of the command descriptor block (CDB). A value of zero indicates that the system does not support setting the NACA bit to one. For more information about the function of the NACA bit and the control byte in a CDB, see the <i>SCSI Primary Commands - 2 (SPC-2)</i> specification.

`ReservedBit`



`AERC`

Indicates, when set to one, that the target device supports the asynchronous event reporting capability. A value of zero indicates that the target device does not support asynchronous event reports. Details of the asynchronous event reporting support are protocol-specific. For more information about asynchronous even reporting, see the <i>SCSI Primary Commands - 2 (SPC-2)</i> specification.

`AdditionalLength`

Specifies the length in bytes of the parameters of the command descriptor block (CDB).

`Reserved`

Reserved.

`SoftReset`

Indicates, when set to one, that the target device supports soft resets. A value of zero indicates that the target does not support soft resets.

`CommandQueue`

Indicates, when set to one, that the target device supports command queuing for this logical unit. However, a value of zero does not necessarily indicate that the target device does not support command queuing. The meaning of these values depends on the values present in the SCSI inquiry data. For information about the meaning of the command queuing bit, see the <i>SCSI Primary Commands - 2 (SPC-2)</i> specification.

`Reserved2`



`LinkedCommands`

Indicates, when set to one, that the operating system supports linked commands. A value of zero indicates the operating system does not support linked commands.

`Synchronous`

Indicates, when set to one, that the target supports synchronous data transfer. A value of zero indicates that the target does not support synchronous data transfer.

`Wide16Bit`

Indicates, when set to one, that the target supports 16-bit wide data transfers. A value of zero indicates that the device does not support 16-bit wide data transfers.

`Wide32Bit`

Indicates, when set to one, that the target supports 32-bit wide data transfers. A value of zero indicates that the device does not support 32-bit wide data transfers.

`RelativeAddressing`

Indicates, when set to one, that the operating system supports the relative addressing mode. A value of zero indicates the operating system does not support relative addressing.

`VendorId`

Contains eight bytes of ASCII data that identifies the vendor of the product.

`ProductId`

Contains sixteen bytes of ASCII data that indicates the product ID, as defined by the vendor. The data shall be left-aligned within this field and the unused bytes filled with ASCII blanks.

`ProductRevisionLevel`

Contains four bytes of ASCII data that indicates the product revision level, as defined by the vendor.

`VendorSpecific`

Contains 20 bytes of vendor-specific data.

`Reserved3`

Reserved.

`VersionDescriptors`



`Reserved4`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | minitape.h (include Scsi.h, Minitape.h, Storport.h) |

## See Also

<a href="..\minitape\nc-minitape-tape_verify_inquiry_routine.md">TapeMiniVerifyInquiry</a>



<a href="..\minitape\nc-minitape-tape_extension_init_routine.md">TapeMiniExtensionInit</a>