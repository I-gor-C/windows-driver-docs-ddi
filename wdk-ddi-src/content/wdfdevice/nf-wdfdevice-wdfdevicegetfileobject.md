---
UID: NF.wdfdevice.WdfDeviceGetFileObject
title: WdfDeviceGetFileObject function
author: windows-driver-content
description: The WdfDeviceGetFileObject method returns a handle to the framework file object that is associated with a specified WDM file object.
old-location: wdf\wdfdevicegetfileobject.htm
old-project: wdf
ms.assetid: 2e56d444-4248-4f00-b712-cbb3a4869302
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceGetFileObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceGetFileObject
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceGetFileObject function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceGetFileObject</b> method returns a handle to the framework file object that is associated with a specified WDM file object.



## -syntax

````
WDFFILEOBJECT WdfDeviceGetFileObject(
  _In_ WDFDEVICE    Device,
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters

### -param Device [in]

A handle to a framework device object.


### -param FileObject [in]

A pointer to a WDM <a href="kernel.file_object">FILE_OBJECT</a> structure.


## -returns
<b>WdfDeviceGetFileObject</b> returns a handle to the framework file object that is associated with the specified WDM file object. If a framework file object was not created for the file, or if the <i>FileObject</i> pointer is invalid, the method returns <b>NULL</b>.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
For more information about framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>.

The following code example obtains a pointer to a named WDM device object and its corresponding WDM file object, if the requested access to the objects can be granted. Then, the example obtains a handle to the framework file object that is associated with the WDM file object.


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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

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
<a href="kernel.iogetdeviceobjectpointer">IoGetDeviceObjectPointer</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceGetFileObject method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

