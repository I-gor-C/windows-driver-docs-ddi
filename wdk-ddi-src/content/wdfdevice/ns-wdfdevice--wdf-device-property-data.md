---
UID: NS.wdfdevice._WDF_DEVICE_PROPERTY_DATA
title: WDF_DEVICE_PROPERTY_DATA
author: windows-driver-content
description: The WDF_DEVICE_PROPERTY_DATA structure describes a device property.
old-location: wdf\wdf_device_property_data.htm
ms.assetid: C49562C0-D8B6-4BAE-96EB-4005D9EB19DE
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_PROPERTY_DATA
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
ms.keywords: WDF_DEVICE_PROPERTY_DATA, WDF_DEVICE_PROPERTY_DATA, *PWDF_DEVICE_PROPERTY_DATA
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_PROPERTY_DATA structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_PROPERTY_DATA</b> structure describes a device property.</p>


## -syntax

````
typedef struct _WDF_DEVICE_PROPERTY_DATA {
  ULONG            Size;
  const DEVPROPKEY *PropertyKey;
  LCID             Lcid;
  ULONG            Flags;
} WDF_DEVICE_PROPERTY_DATA, *PWDF_DEVICE_PROPERTY_DATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>PropertyKey</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that specifies the device 
    property key.</p>
</dd>

### -field <b>Lcid</b>

<dd>
<p>Specifies a locale identifier. Set this parameter either to a language-specific LCID value or to <b>LOCALE_NEUTRAL</b>. The <b>LOCALE_NEUTRAL</b> LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to <b>LOCALE_SYSTEM_DEFAULT</b> or <b>LOCALE_USER_DEFAULT</b>. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Set to  <b>PLUGPLAY_PROPERTY_PERSISTENT</b> if this property value is being set by <a href="https://msdn.microsoft.com/library/windows/hardware/dn265601">WdfDeviceAssignProperty</a>. Otherwise, set this member to zero.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_PROPERTY_DATA</b> structure is used as input to the following methods:</p>

<p>Drivers should initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn265633">WDF_DEVICE_PROPERTY_DATA_INIT</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.13</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265633">WDF_DEVICE_PROPERTY_DATA_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265599">WdfDeviceAllocAndQueryPropertyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265601">WdfDeviceAssignProperty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265608">WdfDeviceQueryPropertyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265612">WdfFdoInitAllocAndQueryPropertyEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265613">WdfFdoInitQueryPropertyEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_PROPERTY_DATA structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
