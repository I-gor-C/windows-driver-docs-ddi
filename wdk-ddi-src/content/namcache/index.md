---
UID : NA:namcache
ms.assetid : c527b3d1-92c4-3901-8854-46f3a1d6612b
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# namcache.h header



namcache.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [RxNameCacheActivateEntry](nf-namcache-rxnamecacheactivateentry.md) | RxNameCacheActivateEntry takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the name cache entry on the active list. |
| [RxNameCacheCheckEntry](nf-namcache-rxnamecachecheckentry.md) | RxNameCacheCheckEntry checks a name cache entry for validity. A valid entry means that the lifetime has not expired and the MRxContext parameter passes the equality check. |
| [RxNameCacheCreateEntry](nf-namcache-rxnamecachecreateentry.md) | RxNameCacheCreateEntry allocates and initializes a NAME_CACHE structure with the given name string. |
| [RxNameCacheExpireEntry](nf-namcache-rxnamecacheexpireentry.md) | RxNameCacheExpireEntry puts a NAME_CACHE entry on the free list for recycling. |
| [RxNameCacheExpireEntryWithShortName](nf-namcache-rxnamecacheexpireentrywithshortname.md) | RxNameCacheExpireEntryWithShortName expires all of the name cache entries whose name prefix matches the given short file name. |
| [RxNameCacheFetchEntry](nf-namcache-rxnamecachefetchentry.md) | RxNameCacheFetchEntry looks for a match with a specified name string for a NAME_CACHE entry. |
| [RxNameCacheFinalize](nf-namcache-rxnamecachefinalize.md) | RxNameCacheFinalize releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheFreeEntry](nf-namcache-rxnamecachefreeentry.md) | RxNameCacheFreeEntry releases the storage for a NAME_CACHE entry and decrements the count of the NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheInitialize](nf-namcache-rxnamecacheinitialize.md) | RxNameCacheInitialize initializes a name cache (NAME_CACHE_CONTROL structure). |