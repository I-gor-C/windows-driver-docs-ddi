---
UID: NF.wdfdevice.WdfDeviceCreateDeviceInterface
title: WdfDeviceCreateDeviceInterface function
author: windows-driver-content
description: The WdfDeviceCreateDeviceInterface method creates a device interface for a specified device.
old-location: wdf\wdfdevicecreatedeviceinterface.htm
old-project: wdf
ms.assetid: cdfe1932-ee3d-41ea-8d7b-85c17c0f1722
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceCreateDeviceInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceCreateDeviceInterface
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceCreateDeviceInterface function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceCreateDeviceInterface</b> method creates a device interface for a specified device.



## -syntax

````
NTSTATUS WdfDeviceCreateDeviceInterface(
  _In_           WDFDEVICE        Device,
  _In_     const GUID             *InterfaceClassGUID,
  _In_opt_       PCUNICODE_STRING ReferenceString
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param InterfaceClassGUID [in]

A pointer to a GUID that identifies the device interface class.


### -param ReferenceString [in, optional]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that describes a reference string for the device interface. The string must not contain any path separator characters ("/" or "\").  This parameter is optional and can be <b>NULL</b>.   For more information, see the following Remarks section.


## -returns
<b>WdfDeviceCreateDeviceInterface</b> returns STATUS_SUCCESS if the operation succeeds.

For a list of other return values that <b>WdfDeviceCreateDeviceInterface</b> can return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
Drivers can use the <i>ReferenceString</i> parameter to differentiate different instances of a single interface. In other words, if a driver calls <b>WdfDeviceCreateDeviceInterface</b> twice for the same device interface class, the driver can specify a different <i>ReferenceString</i> parameter each time. When an instance of an interface is opened, the I/O manager passes the instance's reference string to the driver. The reference string is appended to the path component of the interface instance's name. The driver can then use the reference string to determine which instance of the device interface class is being opened.

For more information about device interfaces and the <b>WdfDeviceCreateDeviceInterface</b> method, see <a href="wdf.using_device_interfaces">Using Device Interfaces</a>.

The following example registers the COM port interface class for a device.


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
1.0

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
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="wdf.wdfdevicesetdeviceinterfacestate">WdfDeviceSetDeviceInterfaceState</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceCreateDeviceInterface method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

