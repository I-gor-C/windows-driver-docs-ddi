---
UID: NC.fltkernel.PFLT_GET_OPERATION_STATUS_CALLBACK
title: PFLT_GET_OPERATION_STATUS_CALLBACK
author: windows-driver-content
description: A minifilter driver can register a routine of type PFLT_GET_OPERATION_STATUS_CALLBACK as the minifilter driver's OperationStatusCallback routine.
old-location: ifsk\PFLT_GET_OPERATION_STATUS_CALLBACK.htm
old-project: ifsk
ms.assetid: f3fedf69-260c-4117-b302-db3ce6b182a0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available in Windows 2000 SP4 and earlier operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OperationStatusCallback
req.alt-loc: FltKernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IXpsPartIterator
---

# PFLT_GET_OPERATION_STATUS_CALLBACK callback



## -description
<p>A minifilter driver can register a routine of type <i>PFLT_GET_OPERATION_STATUS_CALLBACK</i> as the minifilter driver's OperationStatusCallback routine.

</p>


## -prototype

````
PFLT_GET_OPERATION_STATUS_CALLBACK OperationStatusCallback;

VOID OperationStatusCallback(
  _In_     PCFLT_RELATED_OBJECTS   FltObjects,
  _In_     PFLT_IO_PARAMETER_BLOCK IopbSnapshot,
  _In_     NTSTATUS                OperationStatus,
  _In_opt_ PVOID                   RequesterContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>FltObjects</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a> structure that contains opaque pointers for the objects related to the current operation.</p>
</dd>

### -param <i>IopbSnapshot</i> [in]

<dd>
<p>A pointer to the data structure containing parameters from the IO Request Packet for the operation. </p>
</dd>

### -param <i>OperationStatus</i> [in]

<dd>
<p>The NTSTATUS value of the I/O operation generating the callback. </p>
</dd>

### -param <i>RequesterContext</i> [in, optional]

<dd>
<p>An optional pointer to a minifilter driver-provided context information of the requester passed from <a href="https://msdn.microsoft.com/library/windows/hardware/ff544346">FltRequestOperationStatusCallback</a>. </p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>A minifilter driver can register a routine of type <i>PFLT_GET_OPERATION_STATUS_CALLBACK</i> as the minifilter driver's OperationStatusCallback routine. 

</p>

<p>Most minifilter drivers never need to register a routine of type <i>PFLT_GET_OPERATION_STATUS_CALLBACK</i>. Normally, a minifilter driver only calls this routine to determine whether a requested opportunistic lock was granted. 
</p>

<p>A minifilter driver can register a routine of type <i>PFLT_GET_OPERATION_STATUS_CALLBACK</i> as the minifilter driver's OperationStatusCallback routine. 

</p>

<p>Most minifilter drivers never need to register a routine of type <i>PFLT_GET_OPERATION_STATUS_CALLBACK</i>. Normally, a minifilter driver only calls this routine to determine whether a requested opportunistic lock was granted. 
</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available in Windows 2000 SP4 and earlier operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>FltKernel.h (include FltKernel.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544638">FLT_IO_PARAMETER_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544816">FLT_RELATED_OBJECTS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544346">FltRequestOperationStatusCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_GET_OPERATION_STATUS_CALLBACK routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
