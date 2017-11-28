---
UID: NS.smclib._VENDOR_ATTR
title: VENDOR_ATTR
author: windows-driver-content
description: The VENDOR_ATTR structure defines the data that is stored in the VendorAttr member of the SMARTCARD_EXTENSION structure. VENDOR_ATTR also holds information that identifies the smart card reader, such as the vendor name, unit number, and serial number.
old-location: smartcrd\vendor_attr.htm
old-project: smartcrd
ms.assetid: f166ced5-2d63-4e35-af77-78ca80c888d7
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: VENDOR_ATTR, VENDOR_ATTR, *PVENDOR_ATTR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VENDOR_ATTR
req.alt-loc: smclib.h
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
req.iface: 
req.product: Windows 10 or later.
---

# VENDOR_ATTR structure



## -description
<p>The VENDOR_ATTR structure defines the data that is stored in the <b>VendorAttr</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548974">SMARTCARD_EXTENSION</a> structure. VENDOR_ATTR also holds information that identifies the smart card reader, such as the vendor name, unit number, and serial number. </p>


## -syntax

````
typedef struct _VENDOR_ATTR {
  struct {
    USHORT Length;
    UCHAR  Buffer[MAXIMUM_ATTR_STRING_LENGTH];
  } VendorName;
  struct {
    USHORT Length;
    UCHAR  Buffer[MAXIMUM_ATTR_STRING_LENGTH];
  } IfdType;
  ULONG  UnitNo;
  struct {
    USHORT BuildNumber;
    UCHAR  VersionMinor;
    UCHAR  VersionMajor;
  } IfdVersion;
  struct {
    USHORT Length;
    UCHAR  Buffer[MAXIMUM_ATTR_STRING_LENGTH];
  } IfdSerialNo;
  ULONG  Reserved[25];
} VENDOR_ATTR, *PVENDOR_ATTR;
````


## -struct-fields
<dl>

### -field <b>VendorName</b>

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field <b>Length</b>

<dd>
<p>Contains the ANSI-coded name of the vendor. Because a length field is provided, no terminating <b>NULL</b> character is necessary. This member is required. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Contains the length of the ANSI-coded name of the vendor. This member is required. </p>
</dd>
</dl>
</dd>

### -field <b>IfdType</b>

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field <b>Length</b>

<dd>
<p>Contains the length of the ANSI-coded designation of the reader. This member is required. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Contains the ANSI-coded reader name. This member is required. 
</p>
</dd>
</dl>
</dd>

### -field <b>UnitNo</b>

<dd>
<p>Contains the zero-based number of this unit. Because you can have more than one reader of this kind installed, <b>UnitNo</b> can distinguish the readers. This member is required. </p>
</dd>

### -field <b>IfdVersion</b>

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field <b>BuildNumber</b>

<dd>
<p>Contains the build number of the reader driver. This member can be used for support purposes and should be maintained only if the reader allows the value to be queried. This member is optional. </p>
</dd>

### -field <b>VersionMinor</b>

<dd>
<p>Contains the minor version number of the reader driver. This member can be used for support purposes and should be maintained only if the reader allows the value to be queried. This member is optional. </p>
</dd>

### -field <b>VersionMajor</b>

<dd>
<p>Contains the major version number of the reader driver. This member can be used for support purposes and should be maintained only if the reader allows the value to be queried. This member is optional. </p>
</dd>
</dl>
</dd>

### -field <b>IfdSerialNo</b>

<dd>
<p>
      A structure with the following members:
      
     </p>
<dl>

### -field <b>Length</b>

<dd>
<p>Contains the length of the serial number, in bytes, of the connected reader. </p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>A pointer to the serial number of the connected reader. This field should only be maintained if the reader allows the serial number to be queried. This member is optional. </p>
</dd>
</dl>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>