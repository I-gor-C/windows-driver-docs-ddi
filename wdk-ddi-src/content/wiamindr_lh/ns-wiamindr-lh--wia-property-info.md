---
UID: NS.wiamindr_lh._WIA_PROPERTY_INFO
title: WIA_PROPERTY_INFO
author: windows-driver-content
description: The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type.
old-location: image\wia_property_info.htm
old-project: image
ms.assetid: 9ab9edb8-aa37-4c28-81c9-3e41751f14ed
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIA_PROPERTY_INFO, WIA_PROPERTY_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIA_PROPERTY_INFO
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# WIA_PROPERTY_INFO structure



## -description
<p>The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type.</p>


## -syntax

````
typedef struct _WIA_PROPERTY_INFO {
  ULONG   lAccessFlags;
  VARTYPE vt;
  union {
    struct {
      LONG Min;
      LONG Nom;
      LONG Max;
      LONG Inc;
    } Range;
    struct {
      DOUBLE Min;
      DOUBLE Nom;
      DOUBLE Max;
      DOUBLE Inc;
    } RangeFloat;
    struct {
      LONG cNumList;
      LONG Nom;
      BYTE *pList;
    } List;
    struct {
      LONG   cNumList;
      DOUBLE Nom;
      BYTE   *pList;
    } ListFloat;
    struct {
      LONG cNumList;
      GUID Nom;
      GUID *pList;
    } ListGuid;
    struct {
      LONG cNumList;
      BSTR Nom;
      BSTR *pList;
    } ListBStr;
    struct {
      LONG Nom;
      LONG ValidBits;
    } Flag;
    struct {
      LONG Dummy;
    } None;
  } ValidVal;
} WIA_PROPERTY_INFO, *PWIA_PROPERTY_INFO;
````


## -struct-fields
<dl>

### -field <b>lAccessFlags</b>

<dd>
<p>Specifies the access and property attribute flags for a property. See the Microsoft Windows SDK documentation for a list of WIA property attribute flags. </p>
</dd>

### -field <b>vt</b>

<dd>
<p>Specifies the variant data type for the property. This member, which can be one of the following, controls which structure member of the <b>ValidValunion</b> is valid:</p>
<dl>
<dd>
<p>VT_UI1</p>
</dd>
<dd>
<p>VT_UI2</p>
</dd>
<dd>
<p>VT_UI4</p>
</dd>
<dd>
<p>VT_I2</p>
</dd>
<dd>
<p>VT_I4</p>
</dd>
<dd>
<p>VT_R4</p>
</dd>
<dd>
<p>VT_R8</p>
</dd>
<dd>
<p>VT_CLSID</p>
</dd>
<dd>
<p>VT_BSTR</p>
</dd>
</dl>
<p>See PROPVARIANT in the Windows SDK documentation for more information.</p>
</dd>

### -field <b>ValidVal</b>

<dd>
<dl>

### -field <b>Range</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a range of integer values. This structure contains the following members:</p>
<p><b>Min</b>, which indicates the minimum value of the property.</p>
<p><b>Max</b>, which indicates the maximum value of the property.</p>
<p><b>Nom</b>, which indicates the property's nominal value.</p>
<p><b>Inc</b>, which indicates the increment value that can be used.</p>
</dd>

### -field <b>RangeFloat</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a range of floating-point values and the property type is a <b>float</b> or <b>double</b>. This structure contains the following members:</p>
<p><b>Min</b>, which indicates the minimum value of the property.</p>
<p><b>Max</b>, which indicates the maximum value of the property.</p>
<p><b>Nom</b>, which indicates the property's nominal value.</p>
<p><b>Inc</b>, which indicates the increment value that can be used. </p>
</dd>

### -field <b>List</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a list of integer values. This structure contains the following members:</p>
<p><b>cNumList</b>, which indicates the number of elements in the array of valid values to which <b>pList</b> points.</p>
<p><b>Nom</b>, which indicates the nominal value of the property.</p>
<p><b>pList</b>, which is an array of valid values the property can be set to.</p>
</dd>

### -field <b>ListFloat</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a list of floating-point values. This structure contains the following members:</p>
<p><b>cNumList</b>, which indicates the number of elements in the array of valid values to which <b>pList</b> points.</p>
<p><b>Nom</b>, which indicates the nominal value of the property.</p>
<p><b>pList</b>, which is an array of valid values the property can be set to.</p>
</dd>

### -field <b>ListGuid</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a list of GUIDs. This structure contains the following members:</p>
<p><b>cNumList</b>, which indicates the number of elements in the array of valid values to which <b>pList</b> points.</p>
<p><b>Nom</b>, which indicates the nominal value of the property.</p>
<p><b>pList</b>, which is an array of valid values the property can be set to. </p>
</dd>

### -field <b>ListBStr</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a list of strings. This structure contains the following members:</p>
<p><b>cNumList</b>, which indicates the number of elements in the array of valid values to which <b>pList</b> points.</p>
<p><b>Nom</b>, which indicates the nominal value of the property.</p>
<p><b>pList</b>, which is an array of valid values the property can be set to.</p>
</dd>

### -field <b>Flag</b>

<dd>
<p>Is a structure that is filled when the property's valid values are specified by a bitset of flags. This structure contains the following members:</p>
<p><b>Nom</b>, which indicates the nominal value of the property.</p>
<p><b>ValidBits</b>, which is a mask indicating which bit values can be set. This member should be a bitwise OR of all possible user-defined flag values.</p>
</dd>

### -field <b>None</b>

<dd>
<p>Is a structure that is filled when the property's valid values are not given in a list, range, or bitset. This structure contains a member named <b>Dummy</b>, which indicates the property is of type NONE. </p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The WIA_PROPERTY_INFO is used by the minidriver to store information about a property of arbitrary type. This structure is also used by the <b>wiasSetItemPropAttribs</b> to set a property's valid values. The <b>lAccessFlags</b> member controls whether access to a property is read-only or read/write. This member also conveys information about the set of valid values for a property when they are defined by a list of values, a range of values, or a bitset of flags. The <b>vt</b> member contains information about the type of the property. Both members should be used to determine which member of the <b>ValidValunion</b> can be accessed. </p>

<p>For example, for a read/write property of type <b>long</b>, whose valid values are integers in the range -128 to 127, and whose nominal value is 0, <b>lAccessFlags</b> would be set to WIA_PROP_RW | WIA_PROP_RANGE, and <b>vt</b> would be set to VT_I4. <b>Range.Min</b> would be set to -128, <b>Range.Max</b> would be set to 127, and <b>Range.Inc</b> would be set to 1. <b>Range.Nom</b> would be set to 0.</p>

<p>For a different property whose valid values are defined by a list of three GUID values, <b>lAccessFlags</b> would have its WIA_PROP_LIST bit set, and <b>vt</b> would be set to VT_CLSID. <b>ListGuid.cNumList</b> would be set to 3, and the three GUIDs are <b>ListGuid.pList</b>[0], <b>ListGuid.pList</b>[1], and <b>ListGuid.pList</b>[2].</p>

<p>A property whose valid values are defined by a bitset of the values 0x01, 0x02, 0x04, and 0x08 would have the WIA_PROP_FLAG bit set in <b>lAccessFlags</b>, and <b>vt</b> would be set to VT_UI4. For such a property, the value stored in <b>Flag.ValidBits</b> would be 0x0F, the bitwise OR of the four flag values previously mentioned.</p>

<p>The following examples show how to use array data with WIA_PROPERTY_INFO and how to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549475">wiasWriteMultiple</a> to set your property values.</p>

<p>Initialization might look like the following example:</p>

<p>At run time, changing the value with <b>wiasWriteMultiple</b> might look like the following example:</p>

<p><b>Note</b>  WIA uses the COM PROPVARIANT type, VARIANT (defined in the Microsoft Windows SDK documentation), so the default is VT_VECTOR, and not VT_ARRAY (which is also supported).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549358">wiasSetItemPropAttribs</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIA_PROPERTY_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
