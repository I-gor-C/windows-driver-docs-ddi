---
UID: NS.hidpi._HIDP_VALUE_CAPS
title: HIDP_VALUE_CAPS
author: windows-driver-content
description: The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a usage range).
old-location: hid\hidp_value_caps.htm
old-project: hid
ms.assetid: 37084f3a-f57e-45bb-a364-157b3d155394
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HIDP_VALUE_CAPS, HIDP_VALUE_CAPS, *PHIDP_VALUE_CAPS
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
req.alt-api: HIDP_VALUE_CAPS
req.alt-loc: hidpi.h
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
req.iface: 
---

# HIDP_VALUE_CAPS structure



## -description
<p>The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a <a href="hid.hid_usages#usage_range#usage_range">usage range</a>).</p>


## -syntax

````
typedef struct _HIDP_VALUE_CAPS {
  USAGE   UsagePage;
  UCHAR   ReportID;
  BOOLEAN IsAlias;
  USHORT  BitField;
  USHORT  LinkCollection;
  USAGE   LinkUsage;
  USAGE   LinkUsagePage;
  BOOLEAN IsRange;
  BOOLEAN IsStringRange;
  BOOLEAN IsDesignatorRange;
  BOOLEAN IsAbsolute;
  BOOLEAN HasNull;
  UCHAR   Reserved;
  USHORT  BitSize;
  USHORT  ReportCount;
  USHORT  Reserved2[5];
  ULONG   UnitsExp;
  ULONG   Units;
  LONG    LogicalMin;
  LONG    LogicalMax;
  LONG    PhysicalMin;
  LONG    PhysicalMax;
  union {
    struct {
      USAGE  UsageMin;
      USAGE  UsageMax;
      USHORT StringMin;
      USHORT StringMax;
      USHORT DesignatorMin;
      USHORT DesignatorMax;
      USHORT DataIndexMin;
      USHORT DataIndexMax;
    } Range;
    struct {
      USAGE  Usage;
      USAGE  Reserved1;
      USHORT StringIndex;
      USHORT Reserved2;
      USHORT DesignatorIndex;
      USHORT Reserved3;
      USHORT DataIndex;
      USHORT Reserved4;
    } NotRange;
  };
} HIDP_VALUE_CAPS, *PHIDP_VALUE_CAPS;
````


## -struct-fields
<dl>

### -field UsagePage

<dd>
<p>Specifies the usage page of the usage or usage range.</p>
</dd>

### -field ReportID

<dd>
<p>Specifies the report ID of the HID report that contains the usage or usage range.</p>
</dd>

### -field IsAlias

<dd>
<p>Indicates, if <b>TRUE</b>, that the usage is member of a set of aliased usages. Otherwise, if <b>IsAlias</b> is <b>FALSE</b>, the value has only one usage.</p>
</dd>

### -field BitField

<dd>
<p>Contains the data fields (one or two bytes) associated with an input, output, or feature main item.</p>
</dd>

### -field LinkCollection

<dd>
<p>Specifies the index of the <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> in a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> link collection array that contains the usage or usage range. If <b>LinkCollection</b> is zero, the usage or usage range is contained in the top-level collection.</p>
</dd>

### -field LinkUsage

<dd>
<p>Specifies the usage of the link collection that contains the usage or usage range. If <b>LinkCollection</b> is zero, <b>LinkUsage</b> specifies the usage of the top-level collection.</p>
</dd>

### -field LinkUsagePage

<dd>
<p>Specifies the usage page of the link collection that contains the usage or usage range. If <b>LinkCollection</b> is zero, <b>LinkUsagePage</b> specifies the usage page of the top-level collection.</p>
</dd>

### -field IsRange

<dd>
<p>Specifies, if <b>TRUE</b>, that the structure describes a usage range. Otherwise, if <b>IsRange</b> is <b>FALSE</b>, the structure describes a single usage.</p>
</dd>

### -field IsStringRange

<dd>
<p>Specifies, if <b>TRUE</b>, that the usage or usage range has a set of string descriptors. Otherwise, if <b>IsStringRange</b> is <b>FALSE</b>, the usage or usage range has zero or one string descriptor.</p>
</dd>

### -field IsDesignatorRange

<dd>
<p>Specifies, if <b>TRUE</b>, that the usage or usage range has a set of designators. Otherwise, if <b>IsDesignatorRange</b> is <b>FALSE</b>, the usage or usage range has zero or one designator.</p>
</dd>

### -field IsAbsolute

<dd>
<p>Specifies, if <b>TRUE</b>, that the usage or usage range provides absolute data. Otherwise, if <b>IsAbsolute</b> is <b>FALSE</b>, the value is the change in state from the previous value.</p>
</dd>

### -field HasNull

<dd>
<p>Specifies, if <b>TRUE</b>, that the usage supports a <b>NULL</b> value, which indicates that the data is not valid and should be ignored. Otherwise, if <b>HasNull</b> is <b>FALSE</b>, the usage does not have a <b>NULL</b> value.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field BitSize

<dd>
<p>Specifies the size, in bits, of a usage's data field in a report. If <b>ReportCount</b> is greater than one, each usage has a separate data field of this size.</p>
</dd>

### -field ReportCount

<dd>
<p>Specifies the number of usages that this structure describes.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field UnitsExp

<dd>
<p>Specifies the usage's exponent, as described by the USB HID standard.</p>
</dd>

### -field Units

<dd>
<p>Specifies the usage's units, as described by the USB HID Standard.</p>
</dd>

### -field LogicalMin

<dd>
<p>Specifies a usage's signed lower bound.</p>
</dd>

### -field LogicalMax

<dd>
<p>Specifies a usage's signed upper bound.</p>
</dd>

### -field PhysicalMin

<dd>
<p>Specifies a usage's signed lower bound after scaling is applied to the logical minimum value.</p>
</dd>

### -field PhysicalMax

<dd>
<p>Specifies a usage's signed upper bound after scaling is applied to the logical maximum value.</p>
</dd>

### -field Range

<dd>
<p>Specifies, if <b>IsRange</b> is <b>TRUE</b>, information about a usage range. Otherwise, if <b>IsRange</b> is <b>FALSE</b>, <b>NotRange</b> contains information about a single usage. 
</p>
<dl>

### -field UsageMin

<dd>
<p>Indicates the inclusive lower bound of usage range whose inclusive upper bound is specified by <b>Range.UsageMax</b>.</p>
</dd>

### -field UsageMax

<dd>
<p>Indicates the inclusive upper bound of a usage range whose inclusive lower bound is indicated by <b>Range.UsageMin</b>.</p>
</dd>

### -field StringMin

<dd>
<p>Indicates the inclusive lower bound of a range of string descriptors (specified by string minimum and string maximum items) whose inclusive upper bound is indicated by <b>Range.StringMax</b>.
</p>
</dd>

### -field StringMax

<dd>
<p>Indicates the inclusive upper bound of a range of string descriptors (specified by string minimum and string maximum items) whose inclusive lower bound is indicated by <b>Range.StringMin</b>.</p>
</dd>

### -field DesignatorMin

<dd>
<p>Indicates the inclusive lower bound of a range of designators (specified by designator minimum and designator maximum items) whose inclusive lower bound is indicated by <b>Range.DesignatorMax</b>.</p>
</dd>

### -field DesignatorMax

<dd>
<p>Indicates the inclusive upper bound of a range of designators (specified by designator minimum and designator maximum items) whose inclusive lower bound is indicated by <b>Range.DesignatorMin</b>.</p>
</dd>

### -field DataIndexMin

<dd>
<p>Indicates the inclusive lower bound of a sequential range of <a href="https://msdn.microsoft.com/84577544-515a-4fdc-86e5-518182c6c461">data indices</a> that correspond, one-to-one and in the same order, to the usages specified by the usage range <b>Range.UsageMin</b> to <b>Range.UsageMax</b>.</p>
</dd>

### -field DataIndexMax

<dd>
<p>Indicates the inclusive upper bound of a sequential range of data indices that correspond, one-to-one and in the same order, to the usages specified by the usage range <b>Range.UsageMin</b> to <b>Range.UsageMax</b>.</p>
</dd>
</dl>
</dd>

### -field NotRange

<dd>
<p>Specifies, if <b>IsRange</b> is <b>FALSE</b>, information about a single usage. Otherwise, if <b>IsRange</b> is <b>TRUE</b>, <b>Range</b> contains information about a usage range.</p>
<dl>

### -field Usage

<dd>
<p>Indicates a <a href="hid.hid_usages#usage_id#usage_id">usage ID</a>.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field StringIndex

<dd>
<p>Indicates a string descriptor ID for the usage specified by <b>NotRange.Usage</b>.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field DesignatorIndex

<dd>
<p>Indicates a designator ID for the usage specified by <b>NotRange.Usage</b>.</p>
</dd>

### -field Reserved3

<dd>
<p>Reserved for internal system use.</p>
</dd>

### -field DataIndex

<dd>
<p>Indicates the data index of the usage specified by <b>NotRange.Usage</b>.</p>
</dd>

### -field Reserved4

<dd>
<p>Reserved for internal system use.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Clients obtain a <a href="https://msdn.microsoft.com/d447dda6-a1e5-4e57-b06f-f79f8662c236">value capability array</a> by calling <a href="..\hidpi\nf-hidpi-hidp-getvaluecaps.md">HidP_GetValueCaps</a> or <a href="..\hidpi\nf-hidpi-hidp-getspecificvaluecaps.md">HidP_GetSpecificValueCaps</a>. These routines return an array of HIDP_VALUE_CAPS structures in a caller-allocated buffer. The required buffer length is specified in the <a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a> structure returned by <a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>. </p>

<p>For information about the capabilities of HID control values, see <a href="https://msdn.microsoft.com/228fab4f-ff90-43c5-bc68-26b29e8a7dd6">Collection Capability</a> and <a href="https://msdn.microsoft.com/d447dda6-a1e5-4e57-b06f-f79f8662c236">Value Capability Arrays</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getbuttoncaps.md">HidP_GetButtonCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getspecificbuttoncaps.md">HidP_GetSpecificButtonCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getspecificvaluecaps.md">HidP_GetSpecificValueCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getusagevalue.md">HidP_GetUsageValue</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getusagevaluearray.md">HidP_GetUsageValueArray</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getvaluecaps.md">HidP_GetValueCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HIDP_VALUE_CAPS structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
