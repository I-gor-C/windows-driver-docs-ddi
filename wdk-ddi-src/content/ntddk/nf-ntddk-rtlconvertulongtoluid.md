---
UID: NF.ntddk.RtlConvertUlongToLuid
title: RtlConvertUlongToLuid function
author: windows-driver-content
description: The RtlConvertUlongToLuid routine converts an unsigned long integer to a locally unique identifier (LUID), which is used by the system to represent a security privilege.
old-location: kernel\rtlconvertulongtoluid.htm
old-project: kernel
ms.assetid: f3c1e2d5-8bb8-486c-a78a-3ddde6ab64bd
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: RtlConvertUlongToLuid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlConvertUlongToLuid
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
---

# RtlConvertUlongToLuid function



## -description
The <b>RtlConvertUlongToLuid</b> routine converts an unsigned long integer to a locally unique identifier (<a href="kernel.luid">LUID</a>), which is used by the system to represent a security privilege.



## -syntax

````
LUID RtlConvertUlongToLuid(
  _In_ ULONG Ulong
);
````


## -parameters

### -param Ulong [in]

Specifies the unsigned long integer to convert. 


## -returns
<b>RtlConvertUlongToLuid</b> returns the converted <a href="kernel.luid">LUID</a>.


## -remarks
<b>RtlConvertUlongToLuid</b> is used to convert a system-defined privilege value, passed as a ULONG, to a locally unique identifier (<a href="kernel.luid">LUID</a>) used by the system to represent that privilege. Drivers typically pass a LUID to <b>SeSinglePrivilegeCheck</b>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<dt>Ntddk.h (include Ntddk.h or Ntifs.h)</dt>
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
<a href="kernel.rtlconvertlongtoluid">RtlConvertLongToLuid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561842">RtlEqualLuid</a>
</dt>
<dt>
<a href="kernel.sesingleprivilegecheck">SeSinglePrivilegeCheck</a>
</dt>
<dt>
<a href="kernel.luid">LUID</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlConvertUlongToLuid routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

