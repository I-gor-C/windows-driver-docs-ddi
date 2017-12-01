---
UID: NF.wdfcollection.WdfCollectionGetItem
title: WdfCollectionGetItem
author: windows-driver-content
description: The WdfCollectionGetItem method returns a handle to the object that is contained in a specified object collection and associated with a specified index value.
old-location: wdf\wdfcollectiongetitem.htm
old-project: wdf
ms.assetid: 3bb6232c-b87e-4358-ba0c-8854d641bfd8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfCollectionGetItem
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
req.alt-api: WdfCollectionGetItem
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

# WdfCollectionGetItem function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfCollectionGetItem</b> method returns a handle to the object that is contained in a specified object collection and associated with a specified index value.</p>


## -syntax

````
WDFOBJECT WdfCollectionGetItem(
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
<p>A zero-based index value that identifies an object in the collection. </p>
</dd>
</dl>

## -returns
<p><b>WdfCollectionGetItem</b> returns a framework object handle, or <b>NULL</b> if the <i>Index</i> value is invalid.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Index values represent the order in which objects are added to a collection. An index value of zero represents the first object in the collection, an index value of one represents the second object, and so on, like a linked list. When the driver removes item <i>i</i> from a collection, item <i>i</i>+1 becomes item <i>i</i>. </p>

<p>For more information about object collections, see <a href="wdf.framework_object_collections">Framework Object Collections</a>.</p>

<p>For a code example that uses <b>WdfCollectionGetItem</b>, see <a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetcount.md">WdfCollectionGetCount</a>.</p>

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
<a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetfirstitem.md">WdfCollectionGetFirstItem</a>
</dt>
<dt>
<a href="..\wdfcollection\nf-wdfcollection-wdfcollectiongetlastitem.md">WdfCollectionGetLastItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCollectionGetItem method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
