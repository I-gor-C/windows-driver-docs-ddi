---
UID: NF.fltkernel.FltRegisterFilter
title: FltRegisterFilter
author: windows-driver-content
description: FltRegisterFilter registers a minifilter driver.
old-location: ifsk\fltregisterfilter.htm
ms.assetid: 46e96f85-d368-40cd-9530-81959d20b750
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltRegisterFilter
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
ms.keywords: FltRegisterFilter
req.iface: 
---

# FltRegisterFilter function



## -description
<p><b>FltRegisterFilter</b> registers a minifilter driver. </p>


## -syntax

````
NTSTATUS FltRegisterFilter(
  _In_        PDRIVER_OBJECT   Driver,
  _In_  const FLT_REGISTRATION *Registration,
  _Out_       PFLT_FILTER      *RetFilter
);
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A pointer to the driver object for the minifilter driver. This should be the same driver object pointer that was passed as input to the minifilter driver's <b>DriverEntry</b> routine. </p>
</dd>

### -param <i>Registration</i> [in]

<dd>
<p>A pointer to a caller-allocated minifilter driver registration structure (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>). </p>
</dd>

### -param <i>RetFilter</i> [out]

<dd>
<p>A pointer to a caller-allocated variable that receives an opaque filter pointer for the caller. </p>
</dd>
</dl>

## -returns
<p><b>FltRegisterFilter</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltRegisterFilter</b> encountered a pool allocation failure. This is an error code. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One of the following: </p>

<p>The <b>Version</b> member of the <i>Registration</i> structure was not set to FLT_REGISTRATION_VERSION. </p>

<p>One of the non-NULL name-provider routines in the <i>Registration</i> structure was set to an invalid value. The <b>GenerateFileNameCallback</b>, <b>NormalizeNameComponentCallback</b>, and <b>NormalizeNameComponentExCallback</b> members of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a> point to the name-provider routines. </p>

<p>STATUS_INVALID_PARAMETER is an error code. </p><dl>
<dt><b>STATUS_FLT_NOT_INITIALIZED</b></dt>
</dl><p>The Filter Manager was not initialized when the filter tried to register. Make sure that the Filter Manager is loaded as a driver. This is an error code. </p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The filter service key is not found in the registry.</p>

<p>-or-</p>

<p>The filter instance is not registered.</p>

<p> </p>

## -remarks
<p>Every minifilter driver must call <b>FltRegisterFilter</b> from its <b>DriverEntry</b> routine to add itself to the global list of registered minifilter drivers and to provide the Filter Manager with a list of callback functions and other information about the minifilter driver. </p>

<p><b>FltRegisterFilter</b> returns an opaque filter pointer for the minifilter driver in *<i>RetFilter</i>. This pointer value uniquely identifies the minifilter driver and remains constant as long as the minifilter driver is loaded. The minifilter driver should save this pointer, because it is a required parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/ff544569">FltStartFiltering</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544606">FltUnregisterFilter</a>. </p>

<p>After calling <b>FltRegisterFilter</b>, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff544569">FltStartFiltering</a> to begin filtering I/O operations. </p>

<p>A minifilter driver can only call <b>FltRegisterFilter</b> to register itself, not another minifilter driver. </p>

<p>To unregister itself, a minifilter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff544606">FltUnregisterFilter</a>.. </p>

<p>Every minifilter driver must call <b>FltRegisterFilter</b> from its <b>DriverEntry</b> routine to add itself to the global list of registered minifilter drivers and to provide the Filter Manager with a list of callback functions and other information about the minifilter driver. </p>

<p><b>FltRegisterFilter</b> returns an opaque filter pointer for the minifilter driver in *<i>RetFilter</i>. This pointer value uniquely identifies the minifilter driver and remains constant as long as the minifilter driver is loaded. The minifilter driver should save this pointer, because it is a required parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/ff544569">FltStartFiltering</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff544606">FltUnregisterFilter</a>. </p>

<p>After calling <b>FltRegisterFilter</b>, a minifilter driver typically calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff544569">FltStartFiltering</a> to begin filtering I/O operations. </p>

<p>A minifilter driver can only call <b>FltRegisterFilter</b> to register itself, not another minifilter driver. </p>

<p>To unregister itself, a minifilter driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff544606">FltUnregisterFilter</a>.. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544811">FLT_REGISTRATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544569">FltStartFiltering</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544606">FltUnregisterFilter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltRegisterFilter function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
