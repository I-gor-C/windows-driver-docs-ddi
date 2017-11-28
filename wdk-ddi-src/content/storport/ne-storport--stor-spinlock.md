---
UID: NE.storport._STOR_SPINLOCK
title: STOR_SPINLOCK
author: windows-driver-content
description: The STOR_SPINLOCK enumeration is used to specify the type of a spinlock.
old-location: storage\stor_spinlock.htm
old-project: storage
ms.assetid: 73e5e994-4133-4651-bb94-1d21386be1cd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: storport.h
req.include-header: Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STOR_SPINLOCK
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
req.iface: 
req.product: Windows 10 or later.
---

# STOR_SPINLOCK enumeration



## -description
<p>The STOR_SPINLOCK enumeration is used to specify the type of a spinlock.</p>


## -syntax

````
typedef enum _STOR_SPINLOCK { 
  DpcLock        = 1,
  StartIoLock    = 2,
  InterruptLock  = 3
} STOR_SPINLOCK;
````


## -enum-fields
<dl>

### -field <a id="DpcLock"></a><a id="dpclock"></a><a id="DPCLOCK"></a><b>DpcLock</b>

<dd>
<p>Indicates a DPC spinlock. </p>
</dd>

### -field <a id="StartIoLock"></a><a id="startiolock"></a><a id="STARTIOLOCK"></a><b>StartIoLock</b>

<dd>
<p>Indicates a StartIo spinlock.  </p>
</dd>

### -field <a id="InterruptLock"></a><a id="interruptlock"></a><a id="INTERRUPTLOCK"></a><b>InterruptLock</b>

<dd>
<p>Indicates an Interrupt spinlock.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567025">StorPortAcquireSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STOR_SPINLOCK enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
