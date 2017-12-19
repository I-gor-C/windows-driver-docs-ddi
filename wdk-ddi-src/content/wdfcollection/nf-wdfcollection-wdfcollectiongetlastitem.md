---
UID: NF.wdfcollection.WdfCollectionGetLastItem
title: WdfCollectionGetLastItem function
author: windows-driver-content
description: The WdfCollectionGetLastItem method returns a handle to the last object that is in an object collection.
old-location: wdf\wdfcollectiongetlastitem.htm
old-project: wdf
ms.assetid: f90732ab-3756-46e2-8a15-e94ff82b3548
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfCollectionGetLastItem
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
req.alt-api: WdfCollectionGetLastItem
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
req.product: Windows 10 or later.
---

# WdfCollectionGetLastItem function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfCollectionGetLastItem</b> method returns a handle to the last object that is in an object collection.



## -syntax

````
WDFOBJECT WdfCollectionGetLastItem(
  _In_ WDFCOLLECTION Collection
);
````


## -parameters

### -param Collection [in]

A handle to a collection object.


## -returns
<b>WdfCollectionGetLastItem</b> returns a handle to the object that is currently at the end of the specified collection's list of objects, or <b>NULL</b> if the list is empty.

A bug check occurs if the driver supplies an invalid object handle.


## -remarks
For more information about object collections, see <a href="wdf.framework_object_collections">Framework Object Collections</a>.

The following code example obtains a handle to the last object that is in an object collection.


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
<dt>Wdfcollection.h (include Wdf.h)</dt>
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
<a href="wdf.wdfcollectiongetfirstitem">WdfCollectionGetFirstItem</a>
</dt>
<dt>
<a href="wdf.wdfcollectiongetitem">WdfCollectionGetItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCollectionGetLastItem method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

