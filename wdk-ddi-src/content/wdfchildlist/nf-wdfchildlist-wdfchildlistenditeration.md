---
UID: NF.wdfchildlist.WdfChildListEndIteration
title: WdfChildListEndIteration function
author: windows-driver-content
description: The WdfChildListEndIteration method processes modifications to a specified child list.
old-location: wdf\wdfchildlistenditeration.htm
old-project: wdf
ms.assetid: f8dc1d77-d0c5-4112-939d-221955012de1
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfChildListEndIteration
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfChildListEndIteration
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

# WdfChildListEndIteration function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfChildListEndIteration</b> method processes modifications to a specified child list. 


## -syntax

````
VOID WdfChildListEndIteration(
  _In_ WDFCHILDLIST             ChildList,
  _In_ PWDF_CHILD_LIST_ITERATOR Iterator
);
````


## -parameters

### -param ChildList [in]

The same handle to a framework child-list object that the driver previously specified to <a href="wdf.wdfchildlistbeginiteration">WdfChildListBeginIteration</a>.

### -param Iterator [in]

A pointer to the same caller-allocated <a href="wdf.wdf_child_list_iterator">WDF_CHILD_LIST_ITERATOR</a> structure that the driver previously supplied to <b>WdfChildListEndIteration</b>.

## -returns
None.

A system bug check occurs if the driver supplies an invalid object handle.


## -remarks
If the driver has made multiple calls to <a href="wdf.wdfchildlistbeginiteration">WdfChildListBeginIteration</a> or <a href="wdf.wdfchildlistbeginscan">WdfChildListBeginScan</a>, the framework does not process modifications to the child list until the driver has made a corresponding number of calls to <b>WdfChildListEndIteration</b> and <a href="wdf.wdfchildlistendscan">WdfChildListEndScan</a>.

For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.

For a code example that uses <b>WdfChildListEndIteration</b>, see <a href="wdf.wdfchildlistretrievenextdevice">WdfChildListRetrieveNextDevice</a>.

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
<dt>Wdfchildlist.h (include Wdf.h)</dt>
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
<a href="wdf.wdf_child_list_iterator">WDF_CHILD_LIST_ITERATOR</a>
</dt>
<dt>
<a href="wdf.wdfchildlistbeginiteration">WdfChildListBeginIteration</a>
</dt>
<dt>
<a href="wdf.wdfchildlistbeginscan">WdfChildListBeginScan</a>
</dt>
<dt>
<a href="wdf.wdfchildlistendscan">WdfChildListEndScan</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListEndIteration method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
