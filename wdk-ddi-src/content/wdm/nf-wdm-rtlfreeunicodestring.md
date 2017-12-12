---
UID: NF.wdm.RtlFreeUnicodeString
title: RtlFreeUnicodeString function
author: windows-driver-content
description: The RtlFreeUnicodeString routine releases storage that was allocated by RtlAnsiStringToUnicodeString or RtlUpcaseUnicodeString.
old-location: kernel\rtlfreeunicodestring.htm
old-project: kernel
ms.assetid: 505e2ab7-13c3-4cdd-90ba-a37bb38fe160
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: RtlFreeUnicodeString
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
req.alt-api: RtlFreeUnicodeString
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

# RtlFreeUnicodeString function



## -description
The <b>RtlFreeUnicodeString</b> routine releases storage that was allocated by <b>RtlAnsiStringToUnicodeString</b> or <b>RtlUpcaseUnicodeString</b>.



## -syntax

````
VOID RtlFreeUnicodeString(
  _Inout_ PUNICODE_STRING UnicodeString
);
````


## -parameters

### -param UnicodeString [in, out]

Pointer to the Unicode string buffer previously allocated by <b>RtlAnsiStringToUnicodeString</b> or <b>RtlUpcaseUnicodeString</b>. 


## -returns
None


## -remarks
This routine does not release the ANSI string buffer passed to <b>RtlAnsiStringToUnicodeString</b>. 


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
<a href="kernel.rtlansistringtounicodestring">RtlAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="kernel.rtlupcaseunicodestring">RtlUpcaseUnicodeString</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlFreeUnicodeString routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

