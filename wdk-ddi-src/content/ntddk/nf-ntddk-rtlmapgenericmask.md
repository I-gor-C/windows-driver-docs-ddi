---
UID: NF.ntddk.RtlMapGenericMask
title: RtlMapGenericMask function
author: windows-driver-content
description: The RtlMapGenericMask routine determines the nongeneric access rights specified by an ACCESS_MASK.
old-location: kernel\rtlmapgenericmask.htm
old-project: kernel
ms.assetid: dd3a5f87-21a9-4186-bb74-a49e6751622e
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlMapGenericMask
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlMapGenericMask
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
req.irql: <= APC_LEVEL
---

# RtlMapGenericMask function



## -description
The <b>RtlMapGenericMask</b> routine determines the nongeneric access rights specified by an ACCESS_MASK.



## -syntax

````
VOID RtlMapGenericMask(
  _Inout_ PACCESS_MASK     AccessMask,
  _In_    PGENERIC_MAPPING GenericMapping
);
````


## -parameters

### -param AccessMask [in, out]

Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> variable. The routine updates this to contain only those access rights that are not also granted by any GENERIC_<i>XXX</i> access rights originally specified the variable. The routine also clears any GENERIC_<i>XXX</i> bits that are set. 


### -param GenericMapping [in]

Pointer to a <a href="kernel.generic_mapping">GENERIC_MAPPING</a> structure that describes the specific access rights that correspond to each generic access right. 


## -returns
None


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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.generic_mapping">GENERIC_MAPPING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlMapGenericMask routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

