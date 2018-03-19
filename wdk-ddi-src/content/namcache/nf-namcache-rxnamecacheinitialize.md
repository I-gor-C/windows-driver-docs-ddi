---
UID: NF:namcache.RxNameCacheInitialize
title: RxNameCacheInitialize function
author: windows-driver-content
description: RxNameCacheInitialize initializes a name cache (NAME_CACHE_CONTROL structure).
old-location: ifsk\rxnamecacheinitialize.htm
old-project: ifsk
ms.assetid: 2a124a6e-30ff-4c0d-9a09-8cf43e65a657
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RxNameCacheInitialize, RxNameCacheInitialize function [Installable File System Drivers], ifsk.rxnamecacheinitialize, namcache/RxNameCacheInitialize, rxref_1a97be61-3797-49f0-ad90-e426e43505c1.xml
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	namcache.h
api_name:
-	RxNameCacheInitialize
product: Windows
targetos: Windows
req.typenames: VIDEO_STREAM_INIT_PARMS, *LPVIDEO_STREAM_INIT_PARMS
---


# RxNameCacheInitialize function
<b>RxNameCacheInitialize</b> initializes a name cache (NAME_CACHE_CONTROL structure).

## Syntax

````
VOID RxNameCacheInitialize(
  _In_ PNAME_CACHE_CONTROL NameCacheCtl,
  _In_ ULONG               MRxNameCacheSize,
  _In_ ULONG               MaximumEntries
);
````

## Parameters

`NameCacheCtl`

A pointer to the NAME_CACHE_CONTROL structure to initialize.

`MRxNameCacheSize`

The size, in bytes, of the network mini-redirector portion of the NAME_CACHE entry.

`MaximumEntries`

The maximum number of entries that will ever be allocated. This value prevents an errant program that opens a large number of files with bad names from using all of the paged pool memory.


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | namcache.h (include Namcache.h) |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="..\namcache\nf-namcache-rxnamecachefetchentry.md">RxNameCacheFetchEntry</a>



<a href="..\namcache\nf-namcache-rxnamecacheexpireentrywithshortname.md">RxNameCacheExpireEntryWithShortName</a>



<a href="..\namcache\nf-namcache-rxnamecachecreateentry.md">RxNameCacheCreateEntry</a>



<a href="..\namcache\nf-namcache-rxnamecacheexpireentry.md">RxNameCacheExpireEntry</a>



<a href="..\namcache\nf-namcache-rxnamecachecheckentry.md">RxNameCacheCheckEntry</a>



<a href="..\namcache\nf-namcache-rxnamecacheactivateentry.md">RxNameCacheActivateEntry</a>



<a href="..\namcache\nf-namcache-rxnamecachefinalize.md">RxNameCacheFinalize</a>



<a href="..\namcache\nf-namcache-rxnamecachefreeentry.md">RxNameCacheFreeEntry</a>