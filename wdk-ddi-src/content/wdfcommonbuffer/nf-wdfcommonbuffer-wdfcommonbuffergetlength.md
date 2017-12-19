---
UID: NF.wdfcommonbuffer.WdfCommonBufferGetLength
title: WdfCommonBufferGetLength function
author: windows-driver-content
description: The WdfCommonBufferGetLength method returns the length of a specified common buffer.
old-location: wdf\wdfcommonbuffergetlength.htm
old-project: wdf
ms.assetid: 7ffb818d-7c58-4c84-997b-1703f480aaf0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfCommonBufferGetLength
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcommonbuffer.h
req.include-header: WdfCommonBuffer.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfCommonBufferGetLength
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

# WdfCommonBufferGetLength function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfCommonBufferGetLength</b> method returns the length of a specified common buffer. 



## -syntax

````
size_t WdfCommonBufferGetLength(
  _In_ WDFCOMMONBUFFER CommonBuffer
);
````


## -parameters

### -param CommonBuffer [in]

A handle to a common buffer object that the driver obtained by a previous call to <a href="wdf.wdfcommonbuffercreate">WdfCommonBufferCreate</a>.  


## -returns
<b>WdfCommonBufferGetLength</b> returns the length, in bytes, of the buffer that is associated with the common buffer that the <i>CommonBuffer</i> parameter specifies.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
For more information about common buffers, see <a href="wdf.using_common_buffers">Using Common Buffers</a>


The following code example obtains the length of a specified common buffer.


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
<dt>Wdfcommonbuffer.h (include WdfCommonBuffer.h)</dt>
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
<a href="wdf.wdfcommonbuffercreate">WdfCommonBufferCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCommonBufferGetLength method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

