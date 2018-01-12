---
UID: NF:wdm.FIELD_OFFSET
title: FIELD_OFFSET macro
author: windows-driver-content
description: The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type.
old-location: kernel\field_offset.htm
old-project: kernel
ms.assetid: c792d021-3c64-4341-878c-08a7e163447c
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: FIELD_OFFSET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FIELD_OFFSET
req.alt-loc: ntdef.h
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
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# FIELD_OFFSET macro



## -description
The <b>FIELD_OFFSET</b> macro returns the byte offset of a named field in a known structure type.



## -syntax

````
LONG FIELD_OFFSET(
  _In_ TYPE  Type,
  _In_ PCHAR Field
);
````


## -parameters

### -param Type [in]

Specifies the name of a known structure type containing <i>Field</i>. 


### -param Field [in]

Specifies the name of a field in a structure of type <i>Type</i>. 


## -remarks
Used by device driver writers to symbolically determine the offset of a known field in a known structure type. 


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
<dt>Ntdef.h (include Wdm.h or Ntddk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FIELD_OFFSET function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

