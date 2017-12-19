---
UID: NF.wdfiotarget.WdfIoTargetWdmGetTargetFileObject
title: WdfIoTargetWdmGetTargetFileObject function
author: windows-driver-content
description: The WdfIoTargetWdmGetTargetFileObject method returns a pointer to the Windows Driver Model (WDM) file object that is associated with a specified remote I/O target.
old-location: wdf\wdfiotargetwdmgettargetfileobject.htm
old-project: wdf
ms.assetid: e3131dde-95fc-447c-9451-5c8af074ed24
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfIoTargetWdmGetTargetFileObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfiotarget.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfIoTargetWdmGetTargetFileObject
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
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfIoTargetWdmGetTargetFileObject function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfIoTargetWdmGetTargetFileObject</b> method returns a pointer to the Windows Driver Model (WDM) file object that is associated with a specified remote I/O target.



## -syntax

````
PFILE_OBJECT WdfIoTargetWdmGetTargetFileObject(
  _In_ WDFIOTARGET IoTarget
);
````


## -parameters

### -param IoTarget [in]

A handle to a remote I/O target object. This handle was obtained from a previous call to <a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>.


## -returns
<b>WdfIoTargetWdmGetTargetFileObject</b> returns a pointer to a WDM <a href="kernel.file_object">FILE_OBJECT</a> structure.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
The pointer that the <b>WdfIoTargetWdmGetTargetFileObject</b> method returns is valid until the driver calls <a href="wdf.wdfiotargetclose">WdfIoTargetClose</a> or <a href="wdf.wdfiotargetcloseforqueryremove">WdfIoTargetCloseForQueryRemove</a>, or until the remote I/O target object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the remote I/O target object, and if the object is deleted before the remote I/O target is closed, the pointer is valid until the <i>EvtCleanupCallback</i> function returns.

If the driver attempts to access the WDM device object after it has been removed, the driver can cause the system to crash.  The <a href="http://go.microsoft.com/fwlink/p/?linkid=251907">toastmon</a> sample demonstrates how the driver can provide an <a href="..\wdfiotarget\nc-wdfiotarget-evt_wdf_io_target_query_remove.md">EvtIoTargetQueryRemove</a> callback function so that it is notified if the I/O target is removed.

For more information about <b>WdfIoTargetWdmGetTargetFileObject</b>, see <a href="wdf.obtaining_information_about_a_general_i_o_target">Obtaining Information About a General I/O Target</a>. 

For more information about I/O targets, see <a href="wdf.using_i_o_targets">Using I/O Targets</a>.

The following code example obtains a pointer to the WDM file object that is associated with a remote I/O target.


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
<dt>Wdfiotarget.h (include Wdf.h)</dt>
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
&lt;=DISPATCH_LEVEL

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
<a href="kernel.file_object">FILE_OBJECT</a>
</dt>
<dt>
<a href="wdf.wdfiotargetcreate">WdfIoTargetCreate</a>
</dt>
<dt>
<a href="wdf.wdfiotargetwdmgettargetdeviceobject">WdfIoTargetWdmGetTargetDeviceObject</a>
</dt>
<dt>
<a href="wdf.wdfiotargetwdmgettargetfilehandle">WdfIoTargetWdmGetTargetFileHandle</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoTargetWdmGetTargetFileObject method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

