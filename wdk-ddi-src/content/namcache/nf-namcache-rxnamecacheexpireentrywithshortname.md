---
UID: NF.namcache.RxNameCacheExpireEntryWithShortName
title: RxNameCacheExpireEntryWithShortName function
author: windows-driver-content
description: RxNameCacheExpireEntryWithShortName expires all of the name cache entries whose name prefix matches the given short file name.
old-location: ifsk\rxnamecacheexpireentrywithshortname.htm
old-project: ifsk
ms.assetid: 4d842454-4a59-4f82-9aeb-3dfbe9d8cd8a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxNameCacheExpireEntryWithShortName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: namcache.h
req.include-header: Namcache.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxNameCacheExpireEntryWithShortName
req.alt-loc: namcache.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
---

# RxNameCacheExpireEntryWithShortName function



## -description
<b>RxNameCacheExpireEntryWithShortName</b> expires all of the name cache entries whose name prefix matches the given short file name.


## -syntax

````
VOID RxNameCacheExpireEntryWithShortName(
  _In_ PNAME_CACHE_CONTROL NameCacheCtl,
  _In_ PUNICODE_STRING     Name
);
````


## -parameters

### -param NameCacheCtl [in]

A pointer to the NAME_CACHE_CONTROL structure to scan.

### -param Name [in]

A pointer to the Unicode string that contains the name prefix to scan for name cache entry matches to expire.

## -returns
None

## -remarks
The <b>RxNameCacheExpireEntryWithShortName</b> routine scans the active list and inserts any matching NAME_CACHE entries at the head of the free list. The <b>CaseInsensitive</b> member of the NAME_CACHE entry is used to determine whether the scan should ignore case sensitivity when matching the <i>Name</i> parameter.

Because the active list is scanned, the <b>RxNameCacheExpireEntryWithShortName</b> routine puts any non-matching entries that have expired on the free list. A <i>Name</i> value of zero length will match all entries and insert the entries on the free list.

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
Header
</th>
<td width="70%">
<dl>
<dt>Namcache.h (include Namcache.h)</dt>
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
<a href="ifsk.rxnamecacheactivateentry">RxNameCacheActivateEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecachecheckentry">RxNameCacheCheckEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecachecreateentry">RxNameCacheCreateEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecacheexpireentry">RxNameCacheExpireEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecachefetchentry">RxNameCacheFetchEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecachefinalize">RxNameCacheFinalize</a>
</dt>
<dt>
<a href="ifsk.rxnamecachefreeentry">RxNameCacheFreeEntry</a>
</dt>
<dt>
<a href="ifsk.rxnamecacheinitialize">RxNameCacheInitialize</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxNameCacheExpireEntryWithShortName function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
