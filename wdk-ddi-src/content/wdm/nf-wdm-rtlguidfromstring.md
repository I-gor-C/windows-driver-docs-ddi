---
UID: NF.wdm.RtlGUIDFromString
title: RtlGUIDFromString function
author: windows-driver-content
description: The RtlGUIDFromString routine converts the given Unicode string to a GUID in binary format.
old-location: kernel\rtlguidfromstring.htm
old-project: kernel
ms.assetid: 7bdfc781-93d6-4f49-95f1-46f102908ec5
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: RtlGUIDFromString
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
req.alt-api: RtlGUIDFromString
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# RtlGUIDFromString function



## -description
The <b>RtlGUIDFromString</b> routine converts the given Unicode string to a GUID in binary format.



## -syntax

````
NTSTATUS RtlGUIDFromString(
  _In_  PCUNICODE_STRING GuidString,
  _Out_ GUID             *Guid
);
````


## -parameters

### -param GuidString [in]

Pointer to the buffered Unicode string to be converted to a GUID. 


### -param Guid [out]

Pointer to a caller-supplied variable in which the GUID is returned. 


## -returns
If the conversion succeeds, <b>RtlGUIDFromString</b> returns STATUS_SUCCESS. Otherwise, no conversion was done. 


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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
<a href="kernel.rtlstringfromguid">RtlStringFromGUID</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlGUIDFromString routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

