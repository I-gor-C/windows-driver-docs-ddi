---
UID: NF.wdm.RtlFreeAnsiString
title: RtlFreeAnsiString function
author: windows-driver-content
description: The RtlFreeAnsiString routine releases storage that was allocated by RtlUnicodeStringToAnsiString.
old-location: kernel\rtlfreeansistring.htm
old-project: kernel
ms.assetid: ca46be9e-31f6-4118-8958-4eb2c8450e8c
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlFreeAnsiString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlFreeAnsiString
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
req.irql: <=APC_LEVEL
req.product: Windows 10 or later.
---

# RtlFreeAnsiString function



## -description
The <b>RtlFreeAnsiString</b> routine releases storage that was allocated by <b>RtlUnicodeStringToAnsiString</b>.



## -syntax

````
VOID RtlFreeAnsiString(
  _Inout_ PANSI_STRING AnsiString
);
````


## -parameters

### -param AnsiString [in, out]

Pointer to the ANSI string buffer previously allocated by <b>RtlUnicodeStringToAnsiString</b>. 


## -returns
None


## -remarks
This routine does not release the Unicode string buffer passed to <b>RtlUnicodeStringToAnsiString</b>. 


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
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
&lt;=APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlunicodestringtoansistring">RtlUnicodeStringToAnsiString</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlFreeAnsiString routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

