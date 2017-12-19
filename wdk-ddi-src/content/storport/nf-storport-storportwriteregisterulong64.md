---
UID: NF.storport.StorPortWriteRegisterUlong64
title: StorPortWriteRegisterUlong64 macro
author: windows-driver-content
description: This StorPortWriteRegisterUlong64 routine writes a ULONG64 value to the specified register address.
old-location: storage\storportwriteregisterulong64.htm
old-project: storage
ms.assetid: FFBC7A27-B980-49AF-9207-237E0F0292FA
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: StorPortWriteRegisterUlong64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortWriteRegisterUlong64
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# StorPortWriteRegisterUlong64 macro



## -description
This <b>StorPortWriteRegisterUlong64</b> routine writes a <b>ULONG64</b> value to the specified register address.



## -syntax

````
 VOID StorPortWriteRegisterUlong64(
  _In_ PULONG64  Register,
  _In_ ULONG64   Value
);
````


## -parameters

### -param Register [in]

Pointer to the register where the data is written to. The register must be a mapped range in memory space


### -param Value [in]

A <b>ULONG64</b> value to write to the register.


## -remarks
The <b>StorPortWriteRegisterUlong64</b> routine is only available on the 64-bit version of Windows.


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
Available starting with Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.storportreadregisterulong64">StorPortReadRegisterUlong64</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortWriteRegisterUlong64 routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

