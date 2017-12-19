---
UID: NF.ntifs.PsGetProcessExitTime
title: PsGetProcessExitTime function
author: windows-driver-content
description: The PsGetProcessExitTime routine returns the exit time for the current process.
old-location: ifsk\psgetprocessexittime.htm
old-project: ifsk
ms.assetid: 2d98e2f5-0dc4-4490-a039-eb57f0e5fa87
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: PsGetProcessExitTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetProcessExitTime
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <=DISPATCH_LEVEL
---

# PsGetProcessExitTime function



## -description
The <b>PsGetProcessExitTime</b> routine returns the exit time for the current process.



## -syntax

````
LARGE_INTEGER PsGetProcessExitTime(
   VOID 
);
````


## -parameters

### -param  

None


## -returns
<b>PsGetProcessExitTime</b> returns the exit time for the current process, in system time format. 


## -remarks
System time is a count of 100-nanosecond intervals since January 1, 1601. System time is typically updated approximately every ten milliseconds. This value is computed for the GMT time zone. To adjust this value for the local time zone, use <b>ExSystemTimeToLocalTime</b>.

For more information about converting time values, see <a href="kernel.data_conversions">Data Conversions</a>. 


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
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.exsystemtimetolocaltime">ExSystemTimeToLocalTime</a>
</dt>
<dt>
<a href="kernel.kequerysystemtime">KeQuerySystemTime</a>
</dt>
<dt>
<a href="ifsk.psisthreadterminating">PsIsThreadTerminating</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PsGetProcessExitTime routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

