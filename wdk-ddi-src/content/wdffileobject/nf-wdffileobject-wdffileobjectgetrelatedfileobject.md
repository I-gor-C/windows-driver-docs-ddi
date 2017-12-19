---
UID: NF.wdffileobject.WdfFileObjectGetRelatedFileObject
title: WdfFileObjectGetRelatedFileObject function
author: windows-driver-content
description: The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object.
old-location: wdf\wdffileobjectgetrelatedfileobject.htm
old-project: wdf
ms.assetid: EB00FF6B-144B-4256-A362-D593FD4CFC98
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfFileObjectGetRelatedFileObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdffileobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WdfFileObjectGetRelatedFileObject
req.alt-loc: WUDFx02000.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WUDFx02000.lib
req.dll: WUDFx02000.dll; TBD
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfFileObjectGetRelatedFileObject function



## -description
<p class="CCE_Message">[Applies to UMDF only]

The <b>WdfFileObjectGetRelatedFileObject</b> method retrieves the related file object to a framework file object.



## -syntax

````
WDFFILEOBJECT WdfFileObjectGetRelatedFileObject(
  _In_ WDFFILEOBJECT FileObject
);
````


## -parameters

### -param FileObject [in]

A handle to a framework file object.


## -returns
<b>WdfFileObjectGetRelatedFileObject</b> returns a handle to the related file object to a framework file object.


## -remarks
Use of related file objects is technology-specific. For example, <a href="https://msdn.microsoft.com/dcd28218-b3bf-4e5d-b1a7-6910103afb96">kernel streaming</a> uses related file objects to represent the parent filters of child pins.

For more information about related file objects, see the <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> member of the kernel-mode <a href="kernel.file_object">FILE_OBJECT</a> structure.


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
Minimum support

</th>
<td width="70%">
Windows 8.1

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
<dt>Wdffileobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx02000.dll; </dt>
<dt>TBD</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdffileobjectgetfilename">WdfFileObjectGetFileName</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFileObjectGetRelatedFileObject method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

