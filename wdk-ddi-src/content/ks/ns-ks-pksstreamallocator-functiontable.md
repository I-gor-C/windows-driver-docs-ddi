---
UID: NS.ks.PKSSTREAMALLOCATOR_FUNCTIONTABLE
title: PKSSTREAMALLOCATOR_FUNCTIONTABLE
author: windows-driver-content
description: Clients can request the function table of a given allocator by sending a KSSTREAMALLOCATOR_FUNCTIONTABLE structure in a KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE property request.
old-location: stream\ksstreamallocator_functiontable.htm
old-project: stream
ms.assetid: 0bc02fa8-41ca-4430-9dff-e98e39b4eeef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSSTREAMALLOCATOR_FUNCTIONTABLE, KSSTREAMALLOCATOR_FUNCTIONTABLE, *PKSSTREAMALLOCATOR_FUNCTIONTABLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSSTREAMALLOCATOR_FUNCTIONTABLE
req.alt-loc: ks.h
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
req.iface: 
---

# PKSSTREAMALLOCATOR_FUNCTIONTABLE structure



## -description
<p>Clients can request the function table of a given allocator by sending a KSSTREAMALLOCATOR_FUNCTIONTABLE structure in a KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE property request.</p>


## -syntax

````
typedef struct {
  PFNALLOCATOR_ALLOCATEFRAME AllocateFrame;
  PFNALLOCATOR_FREEFRAME     FreeFrame;
} KSSTREAMALLOCATOR_FUNCTIONTABLE, *PKSSTREAMALLOCATOR_FUNCTIONTABLE;
````


## -struct-fields
<dl>

### -field <b>AllocateFrame</b>

<dd>
<p>Points to a <a href="stream.kstrallocateframe">KStrAllocateFrame</a> routine.</p>
</dd>

### -field <b>FreeFrame</b>

<dd>
<p>Points to a <a href="stream.kstrfreeframe">KStrFreeFrame</a> routine.</p>
</dd>
</dl>

## -remarks
<p>This property is only supported by allocators supporting the DISPATCH_LEVEL function interface. Allocators supporting this property must be able to allocate and free frames at IRQL &lt;= DISPATCH_LEVEL.</p>

<p>Because the DISPATCH_LEVEL interface is closely associated with the IRP-based interface, acquiring the function table is likely to result in the creation of an internal notification event to allow pending I/O to be completed when frames are returned to the free list. When the handle to the allocator is closed, the function table pointers are invalid and the associated events are automatically disabled.</p>

<p>This property is only accessible from kernel-mode.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.kstrallocateframe">KStrAllocateFrame</a>
</dt>
<dt>
<a href="stream.kstrfreeframe">KStrFreeFrame</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565633">KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSSTREAMALLOCATOR_FUNCTIONTABLE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
