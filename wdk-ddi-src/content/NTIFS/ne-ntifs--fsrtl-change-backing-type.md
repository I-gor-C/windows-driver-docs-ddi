---
UID: NE.ntifs._FSRTL_CHANGE_BACKING_TYPE
title: FSRTL_CHANGE_BACKING_TYPE
author: windows-driver-content
description: The FSRTL_CHANGE_BACKING_TYPE enumeration specifies the type of cache or control area that a file object designates.
old-location: ifsk\fsrtl_change_backing_type.htm
ms.assetid: 952812f4-5d29-4d1d-ab81-dd3a76a5f04c
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FSRTL_CHANGE_BACKING_TYPE
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
req.iface: 
---

# FSRTL_CHANGE_BACKING_TYPE enumeration



## -description
<p>The FSRTL_CHANGE_BACKING_TYPE enumeration specifies the type of cache or control area that a file object designates.</p>


## -syntax

````
typedef enum _FSRTL_CHANGE_BACKING_TYPE { 
  ChangeDataControlArea   = 0,
  ChangeImageControlArea  = 1,
  ChangeSharedCacheMap    = 2
} FSRTL_CHANGE_BACKING_TYPE, *PFSRTL_CHANGE_BACKING_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ChangeDataControlArea"></a><a id="changedatacontrolarea"></a><a id="CHANGEDATACONTROLAREA"></a><b>ChangeDataControlArea</b>

<dd>
<p>The data control area of the memory manager.</p>
</dd>

### -field <a id="ChangeImageControlArea"></a><a id="changeimagecontrolarea"></a><a id="CHANGEIMAGECONTROLAREA"></a><b>ChangeImageControlArea</b>

<dd>
<p>An image control area that belongs to the memory manager.</p>
</dd>

### -field <a id="ChangeSharedCacheMap"></a><a id="changesharedcachemap"></a><a id="CHANGESHAREDCACHEMAP"></a><b>ChangeSharedCacheMap</b>

<dd>
<p>The shared cache map of the cache manager.</p>
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
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545749">FsRtlChangeBackingFileObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSRTL_CHANGE_BACKING_TYPE enumeration%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
