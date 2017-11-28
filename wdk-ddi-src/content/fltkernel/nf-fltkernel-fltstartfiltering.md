---
UID: NF.fltkernel.FltStartFiltering
title: FltStartFiltering
author: windows-driver-content
description: FltStartFiltering starts filtering for a registered minifilter driver.
old-location: ifsk\fltstartfiltering.htm
old-project: ifsk
ms.assetid: fc24e764-d584-4927-942f-3b8b4b83af79
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltStartFiltering
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
req.alt-api: FltStartFiltering
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltStartFiltering function



## -description
<p><b>FltStartFiltering</b> starts filtering for a registered minifilter driver. </p>


## -syntax

````
NTSTATUS FltStartFiltering(
  _In_ PFLT_FILTER Filter
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>Opaque filter pointer returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. </p>
</dd>
</dl>

## -returns
<p><b>FltStartFiltering</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Filtering was already started for this minifilter driver. This is an error code. </p>

<p> </p>

## -remarks
<p>A minifilter driver typically calls <b>FltStartFiltering</b> from its <b>DriverEntry</b> routine after it has completed its global initialization and called <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. <b>FltStartFiltering</b> notifies the Filter Manager that the minifilter driver is ready to begin attaching to volumes and filtering I/O requests. After the minifilter driver calls this routine, the Filter Manager treats the minifilter driver as a fully active minifilter driver, presenting it with volumes to attach to, as well as I/O requests. The minifilter driver must be prepared to begin receiving these notifications and I/O requests even before <b>FltStartFiltering</b> returns. </p>

<p>A minifilter driver typically calls <b>FltStartFiltering</b> from its <b>DriverEntry</b> routine after it has completed its global initialization and called <a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>. <b>FltStartFiltering</b> notifies the Filter Manager that the minifilter driver is ready to begin attaching to volumes and filtering I/O requests. After the minifilter driver calls this routine, the Filter Manager treats the minifilter driver as a fully active minifilter driver, presenting it with volumes to attach to, as well as I/O requests. The minifilter driver must be prepared to begin receiving these notifications and I/O requests even before <b>FltStartFiltering</b> returns. </p>

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
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544305">FltRegisterFilter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltStartFiltering function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
