---
UID: NS:hidpi._HIDP_VALUE_CAPS
title: "_HIDP_VALUE_CAPS"
author: windows-driver-content
description: The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a usage range).
old-location: hid\hidp_value_caps.htm
old-project: hid
ms.assetid: 37084f3a-f57e-45bb-a364-157b3d155394
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PHIDP_VALUE_CAPS, HIDP_VALUE_CAPS, HIDP_VALUE_CAPS structure [Human Input Devices], PHIDP_VALUE_CAPS, PHIDP_VALUE_CAPS structure pointer [Human Input Devices], _HIDP_VALUE_CAPS, hid.hidp_value_caps, hidpi/HIDP_VALUE_CAPS, hidpi/PHIDP_VALUE_CAPS, hidstrct_cbe30aff-5a6a-40d4-9621-b8d93ebb1948.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hidpi.h
req.include-header: Hidpi.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	hidpi.h
api_name:
-	HIDP_VALUE_CAPS
product: Windows
targetos: Windows
req.typenames: HIDP_VALUE_CAPS, *PHIDP_VALUE_CAPS
---

# _HIDP_VALUE_CAPS structure
The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a <a href="https://msdn.microsoft.com/84fed314-3554-4291-b51c-734d874a4bab">usage range</a>).

## Syntax
```
typedef struct _HIDP_VALUE_CAPS {
  USAGE   UsagePage;
  UCHAR   ReportID;
  BOOLEAN IsAlias;
  USHORT  BitField;
  USHORT  LinkCollection;
  USAGE   LinkUsage;
  USAGE   LinkUsagePage;
  BOOLEAN IsRange;
  BOOLEAN IsStringRange;
  BOOLEAN IsDesignatorRange;
  BOOLEAN IsAbsolute;
  BOOLEAN HasNull;
  UCHAR   Reserved;
  USHORT  BitSize;
  USHORT  ReportCount;
  USHORT  Reserved2[5];
  ULONG   UnitsExp;
  ULONG   Units;
  LONG    LogicalMin;
  LONG    LogicalMax;
  LONG    PhysicalMin;
  LONG    PhysicalMax;
  union {
    struct {
      USAGE  UsageMin;
      USAGE  UsageMax;
      USHORT StringMin;
      USHORT StringMax;
      USHORT DesignatorMin;
      USHORT DesignatorMax;
      USHORT DataIndexMin;
      USHORT DataIndexMax;
    } Range;
    struct {
      USAGE  Reserved1;
      USAGE  Usage;
      USHORT StringIndex;
      USHORT Reserved2;
      USHORT DesignatorIndex;
      USHORT Reserved3;
      USHORT DataIndex;
      USHORT Reserved4;
    } NotRange;
  };
} HIDP_VALUE_CAPS, *PHIDP_VALUE_CAPS;
```

## Members


`UsagePage`

Specifies the usage page of the usage or usage range.

`ReportID`

Specifies the report ID of the HID report that contains the usage or usage range.

`IsAlias`

Indicates, if <b>TRUE</b>, that the usage is member of a set of aliased usages. Otherwise, if <b>IsAlias</b> is <b>FALSE</b>, the value has only one usage.

`BitField`

Contains the data fields (one or two bytes) associated with an input, output, or feature main item.

`LinkCollection`

Specifies the index of the <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> in a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> link collection array that contains the usage or usage range. If <b>LinkCollection</b> is zero, the usage or usage range is contained in the top-level collection.

`LinkUsage`

Specifies the usage of the link collection that contains the usage or usage range. If <b>LinkCollection</b> is zero, <b>LinkUsage</b> specifies the usage of the top-level collection.

`LinkUsagePage`

Specifies the usage page of the link collection that contains the usage or usage range. If <b>LinkCollection</b> is zero, <b>LinkUsagePage</b> specifies the usage page of the top-level collection.

`IsRange`

Specifies, if <b>TRUE</b>, that the structure describes a usage range. Otherwise, if <b>IsRange</b> is <b>FALSE</b>, the structure describes a single usage.

`IsStringRange`

Specifies, if <b>TRUE</b>, that the usage or usage range has a set of string descriptors. Otherwise, if <b>IsStringRange</b> is <b>FALSE</b>, the usage or usage range has zero or one string descriptor.

`IsDesignatorRange`

Specifies, if <b>TRUE</b>, that the usage or usage range has a set of designators. Otherwise, if <b>IsDesignatorRange</b> is <b>FALSE</b>, the usage or usage range has zero or one designator.

`IsAbsolute`

Specifies, if <b>TRUE</b>, that the usage or usage range provides absolute data. Otherwise, if <b>IsAbsolute</b> is <b>FALSE</b>, the value is the change in state from the previous value.

`HasNull`

Specifies, if <b>TRUE</b>, that the usage supports a <b>NULL</b> value, which indicates that the data is not valid and should be ignored. Otherwise, if <b>HasNull</b> is <b>FALSE</b>, the usage does not have a <b>NULL</b> value.

`Reserved`

Reserved for internal system use.

`BitSize`

Specifies the size, in bits, of a usage's data field in a report. If <b>ReportCount</b> is greater than one, each usage has a separate data field of this size.

`ReportCount`

Specifies the number of usages that this structure describes.

`Reserved2`

Reserved for internal system use.

`UnitsExp`

Specifies the usage's exponent, as described by the USB HID standard.

`Units`

Specifies the usage's units, as described by the USB HID Standard.

`LogicalMin`

Specifies a usage's signed lower bound.

`LogicalMax`

Specifies a usage's signed upper bound.

`PhysicalMin`

Specifies a usage's signed lower bound after scaling is applied to the logical minimum value.

`PhysicalMax`

Specifies a usage's signed upper bound after scaling is applied to the logical maximum value.

## Remarks
Clients obtain a <a href="https://msdn.microsoft.com/d447dda6-a1e5-4e57-b06f-f79f8662c236">value capability array</a> by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff539754">HidP_GetValueCaps</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff539737">HidP_GetSpecificValueCaps</a>. These routines return an array of HIDP_VALUE_CAPS structures in a caller-allocated buffer. The required buffer length is specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a> structure returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539715">HidP_GetCaps</a>. 

For information about the capabilities of HID control values, see <a href="https://msdn.microsoft.com/228fab4f-ff90-43c5-bc68-26b29e8a7dd6">Collection Capability</a> and <a href="https://msdn.microsoft.com/d447dda6-a1e5-4e57-b06f-f79f8662c236">Value Capability Arrays</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidpi.h (include Hidpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539707">HidP_GetButtonCaps</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539715">HidP_GetCaps</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539733">HidP_GetSpecificButtonCaps</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539737">HidP_GetSpecificValueCaps</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539748">HidP_GetUsageValue</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539750">HidP_GetUsageValueArray</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539754">HidP_GetValueCaps</a>