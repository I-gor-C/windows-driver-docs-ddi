---
UID: NF.ntddk.PsGetProcessCreateTimeQuadPart
title: PsGetProcessCreateTimeQuadPart function
author: windows-driver-content
description: The PsGetProcessCreateTimeQuadPart routine returns a LONGLONG value that represents the time at which the process was created.
old-location: kernel\psgetprocesscreatetimequadpart.htm
old-project: kernel
ms.assetid: d202b6d9-9964-4c95-acd3-f641e8f9d879
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PsGetProcessCreateTimeQuadPart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetProcessCreateTimeQuadPart
req.alt-loc: Ntoskrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: Ntoskrnl.exe
req.irql: Any level
---

# PsGetProcessCreateTimeQuadPart function



## -description
The <b>PsGetProcessCreateTimeQuadPart</b> routine returns a LONGLONG value that represents the time at which the process was created. 


## -syntax

````
LONGLONG PsGetProcessCreateTimeQuadPart(
  _In_ PEPROCESS Process
);
````


## -parameters

### -param Process [in]

A pointer to the EPROCESS structure that represents the process. Drivers can use the <a href="kernel.psgetcurrentprocess">PsGetCurrentProcess</a> and <a href="kernel.obreferenceobjectbyhandle">ObReferenceObjectByHandle</a> routines to obtain a pointer to the EPROCESS structure for a process. 

## -returns
<b>PsGetProcessCreateTimeQuadPart</b> returns the process creation time, in 100-nanosecond intervals, since January 1, 1601. The return value is the same as the value that the <a href="kernel.kequerysystemtime">KeQuerySystemTime</a> routine returns when the process was created. (Note that if the system time is changed, the value that <b>PsGetProcessCreateTimeQuadPart</b> returns is unaffected.) 

## -remarks


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
Available in Windows XP and later versions of Windows. 
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.kequerysystemtime">KeQuerySystemTime</a>
</dt>
<dt>
<a href="kernel.obreferenceobjectbyhandle">ObReferenceObjectByHandle</a>
</dt>
<dt>
<a href="kernel.psgetcurrentprocess">PsGetCurrentProcess</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PsGetProcessCreateTimeQuadPart routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
