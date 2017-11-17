---
UID: NF.wdfchildlist.WdfChildListRequestChildEject
title: WdfChildListRequestChildEject
author: windows-driver-content
description: The WdfChildListRequestChildEject method informs the framework that a specified device is about to be ejected from its docking station.
old-location: wdf\wdfchildlistrequestchildeject.htm
ms.assetid: d7729edf-e92d-4707-83e2-fece90daeacf
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfChildListRequestChildEject
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
ms.keywords: WdfChildListRequestChildEject
req.iface: 
req.product: Windows 10 or later.
---

# WdfChildListRequestChildEject function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListRequestChildEject</b> method informs the framework that a specified device is about to be ejected from its docking station.</p>


## -syntax

````
BOOLEAN WdfChildListRequestChildEject(
  _In_ WDFCHILDLIST                                 ChildList,
  _In_ PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a child list object.</p>
</dd>

### -param <i>IdentificationDescription</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>WdfChildListRequestChildEject</b> returns <b>TRUE</b> if the operation succeeds. If an input parameter is invalid, or if the framework cannot find the device in the child list, the method returns <b>FALSE</b>.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.
</p>

## -remarks
<p>A bus driver can call <b>WdfChildListRequestChildEject</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548817">WdfPdoRequestEject</a> to report that the driver has detected an attempt to eject one of its enumerated child devices from the device's docking station. For example, the driver might detect that a user has pushed an eject button. </p>

<p>If the driver is using dynamic bus enumeration and if the device's identification description is available, the driver can call <b>WdfChildListRequestChildEject</b>. If the framework device object for the device's PDO is available, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548817">WdfPdoRequestEject</a>. </p>

<p>The <b>WdfChildListRequestChildEject</b> method's <i>IdentificationDescription</i> parameter identifies the device that is being ejected. The device must be a member of the child list that the <i>ChildList</i> parameter represents.</p>

<p>The framework uses the identification description to locate the device in the child list.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For more information about ejectable devices, see <a href="wdf.supporting_ejectable_devices">Supporting Ejectable Devices</a>.</p>

<p>For a code example that uses <b>WdfChildListRequestChildEject</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>.</p>

<p>A bus driver can call <b>WdfChildListRequestChildEject</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548817">WdfPdoRequestEject</a> to report that the driver has detected an attempt to eject one of its enumerated child devices from the device's docking station. For example, the driver might detect that a user has pushed an eject button. </p>

<p>If the driver is using dynamic bus enumeration and if the device's identification description is available, the driver can call <b>WdfChildListRequestChildEject</b>. If the framework device object for the device's PDO is available, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548817">WdfPdoRequestEject</a>. </p>

<p>The <b>WdfChildListRequestChildEject</b> method's <i>IdentificationDescription</i> parameter identifies the device that is being ejected. The device must be a member of the child list that the <i>ChildList</i> parameter represents.</p>

<p>The framework uses the identification description to locate the device in the child list.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For more information about ejectable devices, see <a href="wdf.supporting_ejectable_devices">Supporting Ejectable Devices</a>.</p>

<p>For a code example that uses <b>WdfChildListRequestChildEject</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551223">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548817">WdfPdoRequestEject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListRequestChildEject method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
