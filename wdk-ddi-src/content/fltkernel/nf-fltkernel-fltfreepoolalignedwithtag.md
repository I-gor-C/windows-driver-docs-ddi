---
UID: NF.fltkernel.FltFreePoolAlignedWithTag
title: FltFreePoolAlignedWithTag
author: windows-driver-content
description: The FltFreePoolAlignedWithTag routine frees a cache-aligned buffer that was allocated by a previous call to FltAllocatePoolAlignedWithTag.
old-location: ifsk\fltfreepoolalignedwithtag.htm
old-project: ifsk
ms.assetid: 295a34e4-734e-41ba-bf2e-378333c14e2c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltFreePoolAlignedWithTag
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltFreePoolAlignedWithTag
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: See Remarks section.
req.iface: 
---

# FltFreePoolAlignedWithTag function



## -description
<p>The <b>FltFreePoolAlignedWithTag</b> routine frees a cache-aligned buffer that was allocated by a previous call to <a href="..\fltkernel\nf-fltkernel-fltallocatepoolalignedwithtag.md">FltAllocatePoolAlignedWithTag</a>. </p>


## -syntax

````
VOID FltFreePoolAlignedWithTag(
  _In_ PFLT_INSTANCE Instance,
  _In_ PVOID         Buffer,
  _In_ ULONG         Tag
);
````


## -parameters
<dl>

### -param Instance [in]

<dd>
<p>Opaque instance pointer for a caller-owned minifilter driver instance that is attached to the volume. Must be the same instance pointer as the one used in the call to <a href="..\fltkernel\nf-fltkernel-fltallocatepoolalignedwithtag.md">FltAllocatePoolAlignedWithTag</a>. </p>
</dd>

### -param Buffer [in]

<dd>
<p>Address of the block of pool memory to be freed. </p>
</dd>

### -param Tag [in]

<dd>
<p>Tag used to mark the pool block. Must be the same tag as the one used in the call to <a href="..\fltkernel\nf-fltkernel-fltallocatepoolalignedwithtag.md">FltAllocatePoolAlignedWithTag</a>. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The memory that the <i>Buffer</i> parameter points to must not be accessed after it is freed by <b>FltFreePoolAlignedWithTag</b>. </p>

<p>The caller of <b>FltFreePoolAlignedWithTag</b> can be running at IRQL DISPATCH_LEVEL if a <b>NonPaged</b><i>XxxPoolType</i> value was specified when the memory was allocated. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocatepoolalignedwithtag.md">FltAllocatePoolAlignedWithTag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltFreePoolAlignedWithTag routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
