---
UID: NF.wdfdevice.WdfDeviceReadFromHardware
title: WdfDeviceReadFromHardware function
author: windows-driver-content
description: The WdfDeviceReadFromHardware method is used internally by the framework. Do not use.
old-location: wdf\wdfdevicereadfromhardware.htm
old-project: wdf
ms.assetid: 3E9ECB09-39DD-4A16-B096-24AAD96D52E9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDeviceReadFromHardware
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfDeviceReadFromHardware
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceReadFromHardware function



## -description
The <b>WdfDeviceReadFromHardware</b> method is used internally by the framework. Do not use.
Instead, use the <a href="wdf.wdf_register_port_access_functions">WDF Register/Port Access Functions</a>.


## -syntax

````
SIZE_T WdfDeviceReadFromHardware(
  _In_      WDFDEVICE                       Device,
  _In_      WDF_DEVICE_HWACCESS_TARGET_TYPE Type,
  _In_      WDF_DEVICE_HWACCESS_TARGET_SIZE Size,
  _In_      PVOID                           TargetAddress,
  _Out_opt_ PVOID                           Buffer,
  _In_opt_  ULONG                           Count
);
````


## -parameters

### -param Device [in]


### -param Type [in]


### -param Size [in]


### -param TargetAddress [in]


### -param Buffer [out, optional]


### -param Count [in, optional]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.11
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wdfhwaccess.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.iwdfdevice3_readfromhardware">ReadFromHardware</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceReadFromHardware method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>