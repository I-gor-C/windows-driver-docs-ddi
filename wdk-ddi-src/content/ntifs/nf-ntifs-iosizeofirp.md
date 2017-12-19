---
UID: NF.ntifs.IoSizeOfIrp
title: IoSizeOfIrp macro
author: windows-driver-content
description: The IoSizeOfIrp routine determines the size in bytes for an IRP, given the number of stack locations in the IRP.
old-location: kernel\iosizeofirp.htm
old-project: kernel
ms.assetid: b7a6f903-a986-464a-9c9c-12d44f9abf6a
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoSizeOfIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSizeOfIrp
req.alt-loc: Wdm.h
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

# IoSizeOfIrp macro



## -description
The <b>IoSizeOfIrp</b> routine determines the size in bytes for an IRP, given the number of stack locations in the IRP.



## -syntax

````
USHORT IoSizeOfIrp(
  _In_ CCHAR StackSize
);
````


## -parameters

### -param StackSize [in]

Specifies the number of stack locations for the IRP. 


## -remarks
The input <i>StackSize</i> value is either that of the next-lower driver's device object or one more than that value.


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
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.iomakeassociatedirp">IoMakeAssociatedIrp</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSizeOfIrp routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

