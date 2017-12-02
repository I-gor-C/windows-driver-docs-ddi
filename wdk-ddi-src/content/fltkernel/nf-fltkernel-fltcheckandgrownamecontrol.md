---
UID: NF.fltkernel.FltCheckAndGrowNameControl
title: FltCheckAndGrowNameControl
author: windows-driver-content
description: The FltCheckAndGrowNameControl routine checks whether the buffer in a FLT_NAME_CONTROL structure is large enough to hold the specified number of bytes. If not, FltCheckAndGrowNameControl replaces it with a larger system-allocated buffer.
old-location: ifsk\fltcheckandgrownamecontrol.htm
old-project: ifsk
ms.assetid: 0a49e69e-6b6b-4f86-bd41-d1ad73e63a17
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltCheckAndGrowNameControl
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
req.alt-api: FltCheckAndGrowNameControl
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FltCheckAndGrowNameControl function



## -description
<p>The <b>FltCheckAndGrowNameControl</b> routine checks whether the buffer in a <a href="..\fltkernel\ns-fltkernel--flt-name-control.md">FLT_NAME_CONTROL</a> structure is large enough to hold the specified number of bytes. If not, <b>FltCheckAndGrowNameControl</b> replaces it with a larger system-allocated buffer. </p>


## -syntax

````
NTSTATUS FltCheckAndGrowNameControl(
  _Inout_ PFLT_NAME_CONTROL NameCtrl,
  _In_    USHORT            NewSize
);
````


## -parameters
<dl>

### -param NameCtrl [in, out]

<dd>
<p>Pointer to a <a href="..\fltkernel\ns-fltkernel--flt-name-control.md">FLT_NAME_CONTROL</a> structure containing file name information. </p>
</dd>

### -param NewSize [in]

<dd>
<p>Required size, in bytes, of the new name control buffer. </p>
</dd>
</dl>

## -returns
<p><b>FltCheckAndGrowNameControl</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is insufficient memory in the free pool to satisfy the request. </p>

<p> </p>

## -remarks
<p>Minifilter drivers must not attempt to free or replace the buffer in the <b>Name</b> member of a <a href="..\fltkernel\ns-fltkernel--flt-name-control.md">FLT_NAME_CONTROL</a> structure directly. Instead, minifilter drivers should call <b>FltCheckAndGrowNameControl</b> to obtain a larger name buffer. </p>

<p>If the size, in bytes, of the buffer in the <i>NameCtrl</i> structure is less than the value of the <i>NewSize</i> parameter, <b>FltCheckAndGrowNameControl</b> replaces it with a larger system-allocated buffer. <b>FltCheckAndGrowNameControl</b> copies the contents of the old buffer into the new one and frees the old buffer. </p>

<p>If the size, in bytes, of the buffer in the <i>NameCtrl</i> structure is greater than or equal to the value of the <i>NewSize</i> parameter, <b>FltCheckAndGrowNameControl</b> returns STATUS_SUCCESS and does not replace the buffer. </p>

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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\ns-fltkernel--flt-name-control.md">FLT_NAME_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543030">FltGetFileNameFormat</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilenameinformation.md">FltGetFileNameInformation</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilenameinformationunsafe.md">FltGetFileNameInformationUnsafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543040">FltGetFileNameQueryMethod</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCheckAndGrowNameControl routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
