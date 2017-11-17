---
UID: NF.wdfrequest.WdfRequestGetFileObject
title: WdfRequestGetFileObject
author: windows-driver-content
description: The WdfRequestGetFileObject method retrieves the framework file object that is associated with a specified I/O request.
old-location: wdf\wdfrequestgetfileobject.htm
ms.assetid: 0c5a1e12-b66f-4bcb-bb9d-739b883fe9c2
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRequestGetFileObject
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, FileObjectConfigured, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfRequestGetFileObject
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestGetFileObject function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRequestGetFileObject</b> method retrieves the framework file object that is associated with a specified I/O request.</p>


## -syntax

````
WDFFILEOBJECT WdfRequestGetFileObject(
  _In_ WDFREQUEST Request
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestGetFileObject</b> returns a handle to the framework file object, if the framework has created a file object for the specified request. Otherwise, this method returns <b>NULL</b>. (A driver typically tests for a <b>NULL</b> return value only if it sets the <a href="https://msdn.microsoft.com/e0887061-eafe-4dba-bb7a-58bf949e2d08">WdfFileObjectCanBeOptional</a> bit flag in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551319">WDF_FILEOBJECT_CONFIG</a> structure.)</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfRequestGetFileObject</b> method returns <b>NULL</b> if either:</p>

<p>Your driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a> and specified a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551315">WDF_FILEOBJECT_CLASS</a> value that causes the framework to create file objects.</p>

<p>Another driver sent a read, write, or I/O control request to your driver without first sending a request type of <a href="https://msdn.microsoft.com/91c036a0-7fce-4c7d-a217-eb1c487a15d0">WdfRequestTypeCreate</a>.</p>

<p>For more information about <b>WdfRequestGetFileObject</b> and framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>.</p>

<p>The following code example obtains an I/O request's file object and then calls a driver-defined routine that obtains a pointer to the file object's context space.</p>

<p>The <b>WdfRequestGetFileObject</b> method returns <b>NULL</b> if either:</p>

<p>Your driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a> and specified a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551315">WDF_FILEOBJECT_CLASS</a> value that causes the framework to create file objects.</p>

<p>Another driver sent a read, write, or I/O control request to your driver without first sending a request type of <a href="https://msdn.microsoft.com/91c036a0-7fce-4c7d-a217-eb1c487a15d0">WdfRequestTypeCreate</a>.</p>

<p>For more information about <b>WdfRequestGetFileObject</b> and framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>.</p>

<p>The following code example obtains an I/O request's file object and then calls a driver-defined routine that obtains a pointer to the file object's context space.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
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
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546059">FileObjectConfigured</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551315">WDF_FILEOBJECT_CLASS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestGetFileObject method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
