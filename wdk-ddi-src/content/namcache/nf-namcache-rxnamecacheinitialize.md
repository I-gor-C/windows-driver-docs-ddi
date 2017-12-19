---
UID: NF.namcache.RxNameCacheInitialize
title: RxNameCacheInitialize function
author: windows-driver-content
description: RxNameCacheInitialize initializes a name cache (NAME_CACHE_CONTROL structure).
old-location: ifsk\rxnamecacheinitialize.htm
old-project: ifsk
ms.assetid: 2a124a6e-30ff-4c0d-9a09-8cf43e65a657
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RxNameCacheInitialize
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
req.alt-api: RxNameCacheInitialize
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

# RxNameCacheInitialize function



## -description
<b>RxNameCacheInitialize</b> initializes a name cache (NAME_CACHE_CONTROL structure).



## -syntax

````
VOID RxNameCacheInitialize(
  _In_ PNAME_CACHE_CONTROL NameCacheCtl,
  _In_ ULONG               MRxNameCacheSize,
  _In_ ULONG               MaximumEntries
);
````


## -parameters

### -param NameCacheCtl [in]

A pointer to the NAME_CACHE_CONTROL structure to initialize.


### -param MRxNameCacheSize [in]

The size, in bytes, of the network mini-redirector portion of the NAME_CACHE entry.


### -param MaximumEntries [in]

The maximum number of entries that will ever be allocated. This value prevents an errant program that opens a large number of files with bad names from using all of the paged pool memory.


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
<a href="ifsk.rxnamecacheexpireentrywithshortname">RxNameCacheExpireEntryWithShortName</a>
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
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxNameCacheInitialize function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

