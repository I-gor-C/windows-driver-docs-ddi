---
UID: NF.wdfcollection.WdfCollectionRemoveItem
title: WdfCollectionRemoveItem
author: windows-driver-content
description: The WdfCollectionRemoveItem method removes a specified object from an object collection, based on a specified index value.
old-location: wdf\wdfcollectionremoveitem.htm
old-project: wdf
ms.assetid: 03fde4a7-a4d1-4045-ac0c-6a37f2367b9d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfCollectionRemoveItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcollection.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfCollectionRemoveItem
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfCollectionRemoveItem function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfCollectionRemoveItem</b> method removes a specified object from an object collection, based on a specified index value. </p>


## -syntax

````
VOID WdfCollectionRemoveItem(
  _In_ WDFCOLLECTION Collection,
  _In_ ULONG         Index
);
````


## -parameters
<dl>

### -param <i>Collection</i> [in]

<dd>
<p>A handle to a collection object.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>A zero-based index that identifies the object to remove. </p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Index values represent the order in which objects are added to a collection. An index value of zero represents the first object that was added to the collection, an index value of one represents the second object, and so on. </p>

<p>When <b>WdfCollectionRemoveItem</b> removes an object from a collection, it decrements the object's reference count. </p>

<p>For more information about object collections, see <a href="wdf.framework_object_collections">Framework Object Collections</a>
</p>

<p>For a code example that uses <b>WdfCollectionRemoveItem</b>, see <a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetfirstitem.md">WdfCollectionGetFirstItem</a>.</p>

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
<dt>Wdfcollection.h (include Wdf.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfcollection\nf-wdfcollection-wdfcollectionremove.md">WdfCollectionRemove</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCollectionRemoveItem method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
