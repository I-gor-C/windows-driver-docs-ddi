---
UID: NS.wdfdevice._WDF_DEVICE_INTERFACE_PROPERTY_DATA
title: WDF_DEVICE_INTERFACE_PROPERTY_DATA
author: windows-driver-content
description: The WDF_DEVICE_INTERFACE_PROPERTY_DATA structure describes a device interface property.
old-location: wdf\wdf_device_interface_property_data.htm
ms.assetid: 2AC9E23B-928E-480F-A208-5A2DE92AEF4B
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_INTERFACE_PROPERTY_DATA
req.alt-loc: wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_DEVICE_INTERFACE_PROPERTY_DATA, WDF_DEVICE_INTERFACE_PROPERTY_DATA, *PWDF_DEVICE_INTERFACE_PROPERTY_DATA
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_INTERFACE_PROPERTY_DATA structure



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WDF_DEVICE_INTERFACE_PROPERTY_DATA</b> structure describes a device interface property.</p>


## -syntax

````
typedef struct _WDF_DEVICE_INTERFACE_PROPERTY_DATA {
  ULONG            Size;
  const GUID       *InterfaceClassGUID;
  PCUNICODE_STRING ReferenceString;
  const DEVPROPKEY *PropertyKey;
  LCID             Lcid;
  ULONG            Flags;
} WDF_DEVICE_INTERFACE_PROPERTY_DATA, *PWDF_DEVICE_INTERFACE_PROPERTY_DATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>InterfaceClassGUID</b>

<dd>
<p>A pointer to a GUID that identifies the device interface class.</p>
</dd>

### -field <b>ReferenceString</b>

<dd>
<p>A pointer to a <b>UNICODE_STRING</b> structure that describes a reference
    string for the device interface. This parameter is optional and can
    be NULL.</p>
</dd>

### -field <b>PropertyKey</b>

<dd>
<p>A pointer to a <b>DEVPROPKEY</b> structure that specifies the device 
    property key.</p>
</dd>

### -field <b>Lcid</b>

<dd>
<p>Specifies a locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>. The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Not currently used. Set this member to zero.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_INTERFACE_PROPERTY_DATA</b> structure is used as input to the following methods:</p>

<p>Drivers should initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn265630">WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT</a>.</p>

<p>For an example of how to use <b>WDF_DEVICE_INTERFACE_PROPERTY_DATA</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn265600">WdfDeviceAssignInterfaceProperty</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265630">WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265598">WdfDeviceAllocAndQueryInterfaceProperty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265600">WdfDeviceAssignInterfaceProperty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265607">WdfDeviceQueryInterfaceProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_INTERFACE_PROPERTY_DATA structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
