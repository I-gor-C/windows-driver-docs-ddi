---
UID: NF.ntifs.RtlIsValidOemCharacter
title: RtlIsValidOemCharacter function
author: windows-driver-content
description: The RtlIsValidOemCharacter routine determines if the specified Unicode character can be mapped to a valid OEM character.
old-location: ifsk\rtlisvalidoemcharacter.htm
old-project: ifsk
ms.assetid: 76040e0d-a43c-4e3d-aaaa-b84fc2613603
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RtlIsValidOemCharacter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlIsValidOemCharacter
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
req.irql: PASSIVE_LEVEL
---

# RtlIsValidOemCharacter function



## -description
The <b>RtlIsValidOemCharacter</b> routine determines if the specified Unicode character can be mapped to a valid OEM character. 



## -syntax

````
BOOLEAN RtlIsValidOemCharacter(
  _Inout_ PWCHAR Char
);
````


## -parameters

### -param Char [in, out]

Pointer to the character. If the character can be mapped to a valid OEM character, this parameter receives the Unicode translation of the valid OEM character.


## -returns
<b>RtlIsValidOemCharacter</b> returns <b>TRUE</b> if the character can be mapped to a valid OEM character, <b>FALSE</b> otherwise. 


## -remarks
<b>RtlIsValidOemCharacter</b> translates the Unicode character at <i>Char</i> using the OEM code page that was installed as the current system code page at system boot time, and converts the translated character to uppercase. <b>RtlIsValidOemCharacter</b> checks that the resulting character is a valid OEM character.

For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. 


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
This routine is available on Microsoft Windows 2000 and later. 

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
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.rtloemstringtocountedunicodestring">RtlOemStringToCountedUnicodeString</a>
</dt>
<dt>
<a href="ifsk.rtloemstringtounicodestring">RtlOemStringToUnicodeString</a>
</dt>
<dt>
<a href="ifsk.rtlunicodetooemn">RtlUnicodeToOemN</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlIsValidOemCharacter routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

