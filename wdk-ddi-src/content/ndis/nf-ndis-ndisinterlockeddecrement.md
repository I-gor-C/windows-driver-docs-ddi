---
UID: NF.ndis.NdisInterlockedDecrement
title: NdisInterlockedDecrement macro
author: windows-driver-content
description: The NdisInterlockedDecrement function decrements a caller-supplied variable of type LONG as an atomic operation.
old-location: netvista\ndisinterlockeddecrement.htm
old-project: netvista
ms.assetid: cf425cd6-88e6-479f-a5c7-364ae896145d
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisInterlockedDecrement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInterlockedDecrement (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInterlockedDecrement (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInterlockedDecrement
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
---

# NdisInterlockedDecrement macro



## -description
The 
  <b>NdisInterlockedDecrement</b> function decrements a caller-supplied variable of type LONG as an atomic
  operation.



## -syntax

````
LONG NdisInterlockedDecrement(
  [in] PLONG Addend
);
````


## -parameters

### -param Addend [in]

A pointer to the variable to be decremented.


## -remarks
<b>NdisInterlockedDecrement</b> can safely be used on variables in pageable memory.

<b>NdisInterlockedDecrement</b> is atomic only with respect to other 
    <b>NdisInterlocked<i>Xxx</i></b> calls.


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
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/495776f3-8ad4-46ee-8809-4edf01fd5038">NdisInterlockedDecrement (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInterlockedDecrement (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<a href="netvista.ndisinterlockedincrement">NdisInterlockedIncrement</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInterlockedDecrement macro%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

