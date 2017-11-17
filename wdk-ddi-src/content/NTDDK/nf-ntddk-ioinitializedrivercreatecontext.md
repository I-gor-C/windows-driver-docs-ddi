---
UID: NF.ntddk.IoInitializeDriverCreateContext
title: IoInitializeDriverCreateContext
author: windows-driver-content
description: The IoInitializeDriverCreateContext routine initializes a caller-allocated variable of type IO_DRIVER_CREATE_CONTEXT.
old-location: ifsk\ioinitializedrivercreatecontext.htm
ms.assetid: 1d35ed3e-d14f-43ad-9c11-38aa37e76492
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoInitializeDriverCreateContext
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
ms.keywords: IoInitializeDriverCreateContext
req.iface: 
---

# IoInitializeDriverCreateContext function



## -description
<p>The <b>IoInitializeDriverCreateContext</b> routine initializes a caller-allocated variable of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff548565">IO_DRIVER_CREATE_CONTEXT</a>.</p>


## -syntax

````
VOID IoInitializeDriverCreateContext(
   PIO_DRIVER_CREATE_CONTEXT DriverContext
);
````


## -parameters
<dl>

### -param <i>DriverContext</i> 

<dd>
<p>A pointer to a caller-allocated variable of type IO_DRIVER_CREATE_CONTEXT.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>IoInitializeDriverCreateContext</b> routine initializes a caller-allocated IO_DRIVER_CREATE_CONTEXT structure used in passing additional create parameters to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a> routines.</p>

<p>Callers of <b>IoInitializeDriverCreateContext</b> can be running at any IRQL if the <i>DriverContext</i> block is in nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

<p>Starting in Windows 10, version 1607, this routine sets the <b>SiloContext</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548565">IO_DRIVER_CREATE_CONTEXT</a> to <b>IO_USE_AMBIENT_SILO</b>.</p>

<p>The <b>IoInitializeDriverCreateContext</b> routine initializes a caller-allocated IO_DRIVER_CREATE_CONTEXT structure used in passing additional create parameters to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a> routines.</p>

<p>Callers of <b>IoInitializeDriverCreateContext</b> can be running at any IRQL if the <i>DriverContext</i> block is in nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

<p>Starting in Windows 10, version 1607, this routine sets the <b>SiloContext</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff548565">IO_DRIVER_CREATE_CONTEXT</a> to <b>IO_USE_AMBIENT_SILO</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541939">FltCreateFileEx2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548283">IoCreateFileEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoInitializeDriverCreateContext routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
