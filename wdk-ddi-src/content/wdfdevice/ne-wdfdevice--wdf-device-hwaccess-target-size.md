---
UID: NE.wdfdevice._WDF_DEVICE_HWACCESS_TARGET_SIZE
title: WDF_DEVICE_HWACCESS_TARGET_SIZE
author: windows-driver-content
description: The WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration is used internally by the framework. Do not use.
old-location: wdf\wdf_device_hwaccess_target_size.htm
old-project: wdf
ms.assetid: C675431E-6213-4FA8-86DB-65FE6EE90853
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_DEVICE_HWACCESS_TARGET_TYPE
req.alt-loc: wdfdevice.h,wudfddi_types.h
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
req.product: Windows 10 or later.
---

# WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>WDF_DEVICE_HWACCESS_TARGET_SIZE</b> enumeration is used internally by the framework. Do not use.</p>


## -syntax

````
typedef enum __WDF_IO_TARGET_STATE { 
  WdfDeviceHwAccessTargetSizeInvalid  = 0,
  WdfDeviceHwAccessTargetSizeUchar    = 1,
  WdfDeviceHwAccessTargetSizeUshort   = 2,
  WdfDeviceHwAccessTargetSizeUlong    = 3,
  WdfDeviceHwAccessTargetSizeUlong64  = 4,
  WdfDeviceHwAccessTargetSizeMaximum  = 5
} WDF_DEVICE_HWACCESS_TARGET_TYPE, *PWDF_DEVICE_HWACCESS_TARGET_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfDeviceHwAccessTargetSizeInvalid"></a><a id="wdfdevicehwaccesstargetsizeinvalid"></a><a id="WDFDEVICEHWACCESSTARGETSIZEINVALID"></a><b>WdfDeviceHwAccessTargetSizeInvalid</b>

<dd></dd>

### -field <a id="WdfDeviceHwAccessTargetSizeUchar"></a><a id="wdfdevicehwaccesstargetsizeuchar"></a><a id="WDFDEVICEHWACCESSTARGETSIZEUCHAR"></a><b>WdfDeviceHwAccessTargetSizeUchar</b>

<dd></dd>

### -field <a id="WdfDeviceHwAccessTargetSizeUshort"></a><a id="wdfdevicehwaccesstargetsizeushort"></a><a id="WDFDEVICEHWACCESSTARGETSIZEUSHORT"></a><b>WdfDeviceHwAccessTargetSizeUshort</b>

<dd></dd>

### -field <a id="WdfDeviceHwAccessTargetSizeUlong"></a><a id="wdfdevicehwaccesstargetsizeulong"></a><a id="WDFDEVICEHWACCESSTARGETSIZEULONG"></a><b>WdfDeviceHwAccessTargetSizeUlong</b>

<dd></dd>

### -field <a id="WdfDeviceHwAccessTargetSizeUlong64"></a><a id="wdfdevicehwaccesstargetsizeulong64"></a><a id="WDFDEVICEHWACCESSTARGETSIZEULONG64"></a><b>WdfDeviceHwAccessTargetSizeUlong64</b>

<dd></dd>

### -field <a id="WdfDeviceHwAccessTargetSizeMaximum"></a><a id="wdfdevicehwaccesstargetsizemaximum"></a><a id="WDFDEVICEHWACCESSTARGETSIZEMAXIMUM"></a><b>WdfDeviceHwAccessTargetSizeMaximum</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wudfddi_types.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561319">UMDF Structures and Enumeration Types</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
