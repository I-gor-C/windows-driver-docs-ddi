---
UID: NE.wudfddi_types._WDF_PROPERTY_STORE_ROOT_CLASS
title: WDF_PROPERTY_STORE_ROOT_CLASS
author: windows-driver-content
description: The WDF_PROPERTY_STORE_ROOT_CLASS enumeration identifies the registry keys that UMDF property stores represent.
old-location: wdf\wdf_property_store_root_class.htm
ms.assetid: f26732a7-54b5-4573-ac4f-7b2b6c8db8b0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: WDF_PROPERTY_STORE_ROOT_CLASS
req.alt-loc: Wudfddi_types.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: WRITE_REGISTER_USHORT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_PROPERTY_STORE_ROOT_CLASS enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>WDF_PROPERTY_STORE_ROOT_CLASS</b> enumeration identifies the registry keys that UMDF property stores represent.</p>


## -syntax

````
typedef enum _WDF_PROPERTY_STORE_ROOT_CLASS { 
  WdfPropertyStoreRootClassHardwareKey         = 0x00,
  WdfPropertyStoreRootClassSoftwareKey         = 0x01,
  WdfPropertyStoreRootClassDeviceInterfaceKey  = 0x02,
  WdfPropertyStoreRootClassLegacyHardwareKey   = 0x03
} WDF_PROPERTY_STORE_ROOT_CLASS;
````


## -enum-fields
<dl>

### -field <a id="WdfPropertyStoreRootClassHardwareKey"></a><a id="wdfpropertystorerootclasshardwarekey"></a><a id="WDFPROPERTYSTOREROOTCLASSHARDWAREKEY"></a><b>WdfPropertyStoreRootClassHardwareKey</b>

<dd>
<p>The property store represents a device's <a href="wdf.using_the_registry_in_umdf_drivers">hardware key</a>.</p>
</dd>

### -field <a id="WdfPropertyStoreRootClassSoftwareKey"></a><a id="wdfpropertystorerootclasssoftwarekey"></a><a id="WDFPROPERTYSTOREROOTCLASSSOFTWAREKEY"></a><b>WdfPropertyStoreRootClassSoftwareKey</b>

<dd>
<p>The property store represents a driver's <a href="wdf.using_the_registry_in_umdf_drivers">software key</a>.</p>
</dd>

### -field <a id="WdfPropertyStoreRootClassDeviceInterfaceKey"></a><a id="wdfpropertystorerootclassdeviceinterfacekey"></a><a id="WDFPROPERTYSTOREROOTCLASSDEVICEINTERFACEKEY"></a><b>WdfPropertyStoreRootClassDeviceInterfaceKey</b>

<dd>
<p>The property store represents the key for an instance of a <a href="wdf.using_the_registry_in_umdf_drivers">device interface class</a>.</p>
</dd>

### -field <a id="WdfPropertyStoreRootClassLegacyHardwareKey"></a><a id="wdfpropertystorerootclasslegacyhardwarekey"></a><a id="WDFPROPERTYSTOREROOTCLASSLEGACYHARDWAREKEY"></a><b>WdfPropertyStoreRootClassLegacyHardwareKey</b>

<dd>
<p>The property store represents the <a href="wdf.using_the_registry_in_umdf_drivers">DEVICEMAP key</a>, which is used by only a few older drivers. </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_PROPERTY_STORE_ROOT_CLASS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561453">WDF_PROPERTY_STORE_ROOT</a> structure.</p>

<p>The <b>WDF_PROPERTY_STORE_ROOT_CLASS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561453">WDF_PROPERTY_STORE_ROOT</a> structure.</p>

<p>The <b>WDF_PROPERTY_STORE_ROOT_CLASS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561453">WDF_PROPERTY_STORE_ROOT</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561453">WDF_PROPERTY_STORE_ROOT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_PROPERTY_STORE_ROOT_CLASS enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
