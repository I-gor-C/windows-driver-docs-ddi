---
UID: NF.wdffileobject.WdfFileObjectGetRelatedFileObject
title: WdfFileObjectGetRelatedFileObject
author: windows-driver-content
description: The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object.
old-location: wdf\wdffileobjectgetrelatedfileobject.htm
ms.assetid: EB00FF6B-144B-4256-A362-D593FD4CFC98
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
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
req.dll: WUDFx02000.dll; 
TBD
req.irql: PASSIVE_LEVEL
ms.keywords: WdfFileObjectGetRelatedFileObject
req.iface: 
req.product: Windows 10 or later.
---

# WdfFileObjectGetRelatedFileObject function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WdfFileObjectGetRelatedFileObject</b> method retrieves the related file object to a framework file object.</p>


## -syntax

````
WDFFILEOBJECT WdfFileObjectGetRelatedFileObject(
  _In_ WDFFILEOBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A handle to a framework file object.</p>
</dd>
</dl>

## -returns
<p><b>WdfFileObjectGetRelatedFileObject</b> returns a handle to the related file object to a framework file object.</p>

## -remarks
<p>Use of related file objects is technology-specific. For example, <a href="NULL">kernel streaming</a> uses related file objects to represent the parent filters of child pins.</p>

<p>For more information about related file objects, see the <a href="https://msdn.microsoft.com/0ac5c19a-b3ec-4f1e-a018-2c11cc18e58d">GetRelatedFileObject</a> member of the kernel-mode <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a> structure.</p>

<p>Use of related file objects is technology-specific. For example, <a href="NULL">kernel streaming</a> uses related file objects to represent the parent filters of child pins.</p>

<p>For more information about related file objects, see the <a href="https://msdn.microsoft.com/0ac5c19a-b3ec-4f1e-a018-2c11cc18e58d">GetRelatedFileObject</a> member of the kernel-mode <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a> structure.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
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
<dt>Wdffileobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx02000.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547310">WdfFileObjectGetFileName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfFileObjectGetRelatedFileObject method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
