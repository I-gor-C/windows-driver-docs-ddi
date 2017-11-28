---
UID: NF.wdfchildlist.WdfChildListBeginIteration
title: WdfChildListBeginIteration
author: windows-driver-content
description: The WdfChildListBeginIteration method prepares the framework for retrieving items from a specified child list.
old-location: wdf\wdfchildlistbeginiteration.htm
old-project: wdf
ms.assetid: b81dbad8-0e03-4183-a7b3-32c75a656575
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfChildListBeginIteration
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
req.alt-api: WdfChildListBeginIteration
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfChildListBeginIteration function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListBeginIteration</b> method prepares the framework for retrieving items from a specified child list.</p>


## -syntax

````
VOID WdfChildListBeginIteration(
  _In_ WDFCHILDLIST             ChildList,
  _In_ PWDF_CHILD_LIST_ITERATOR Iterator
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child list object.</p>
</dd>

### -param <i>Iterator</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a> structure that indicates the type of child devices to be retrieved.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>After calling <b>WdfChildListBeginIteration</b>, the driver can repeatedly call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> to obtain information about each child device in the child list. </p>

<p>After the driver has finished calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>.</p>

<p>If the driver makes changes to the child list after calling <b>WdfChildListBeginIteration</b>, the framework stores all of the changes and notifies the Plug and Play (PnP) manager of the changes when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>.</p>

<p>The driver can nest calls to <b>WdfChildListBeginIteration</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>. If the driver nests calls to these methods, the framework stores all of the changes until the last call to <b>WdfChildListEndIteration</b>.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WdfChildListBeginIteration</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>.</p>

<p>After calling <b>WdfChildListBeginIteration</b>, the driver can repeatedly call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a> to obtain information about each child device in the child list. </p>

<p>After the driver has finished calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>.</p>

<p>If the driver makes changes to the child list after calling <b>WdfChildListBeginIteration</b>, the framework stores all of the changes and notifies the Plug and Play (PnP) manager of the changes when the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>.</p>

<p>The driver can nest calls to <b>WdfChildListBeginIteration</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>. If the driver nests calls to these methods, the framework stores all of the changes until the last call to <b>WdfChildListEndIteration</b>.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>For a code example that uses <b>WdfChildListBeginIteration</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551230">WDF_CHILD_LIST_ITERATOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551232">WDF_CHILD_LIST_ITERATOR_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551225">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545608">WdfChildListBeginScan</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545618">WdfChildListEndIteration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545641">WdfChildListRequestChildEject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545655">WdfChildListRetrieveNextDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfChildListBeginIteration method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
