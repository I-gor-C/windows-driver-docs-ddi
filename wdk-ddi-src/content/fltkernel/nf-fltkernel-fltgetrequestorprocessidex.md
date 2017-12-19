---
UID: NF.fltkernel.FltGetRequestorProcessIdEx
title: FltGetRequestorProcessIdEx function
author: windows-driver-content
description: The FltGetRequestorProcessIdEx routine returns the kernel-mode handle for the process that is associated with the thread that requested a given I/O operation.
old-location: ifsk\fltgetrequestorprocessidex.htm
old-project: ifsk
ms.assetid: e6a8b2ca-7e9d-410a-b44b-7e873b6e5833
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FltGetRequestorProcessIdEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Vista or later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetRequestorProcessIdEx
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
req.irql: <= DISPATCH_LEVEL
---

# FltGetRequestorProcessIdEx function



## -description
The <b>FltGetRequestorProcessIdEx</b> routine returns the kernel-mode handle for the process that is associated with the thread that requested a given I/O operation. 



## -syntax

````
HANDLE FltGetRequestorProcessIdEx(
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param CallbackData [in]

A pointer to an <a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a> structure that identifies the thread and the I/O operation. 


## -returns
The <b>FltGetRequestorProcessIdEx</b> routine returns the kernel-mode handle for the process that is associated with the thread that originally requested the I/O operation. If the operation is not associated with any thread, FltGetRequestorProcessIdEx returns <b>NULL</b>. 


## -remarks
The <b>FltGetRequestorProcessIdEx</b> routine returns the kernel-mode handle for the process that the requesting thread is currently attached to. This process may or may not be the same process that created the thread. 


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
Version

</th>
<td width="70%">
Available in Microsoft Vista or later versions of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.fltgetrequestorprocess">FltGetRequestorProcess</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetRequestorProcessIdEx routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

