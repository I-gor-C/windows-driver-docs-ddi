# Declarations in the namcache header
This header Namcache contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxNameCacheFinalize function](nf-namcache-rxnamecachefinalize.md) | RxNameCacheFinalize releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheActivateEntry function](nf-namcache-rxnamecacheactivateentry.md) | RxNameCacheActivateEntry takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the name cache entry on the active list. |
| [RxNameCacheExpireEntryWithShortName function](nf-namcache-rxnamecacheexpireentrywithshortname.md) | RxNameCacheExpireEntryWithShortName expires all of the name cache entries whose name prefix matches the given short file name. |
| [RxNameCacheOpSaved function](nf-namcache-rxnamecacheopsaved.md) | TBD |
| [RxNameCacheExpireEntry function](nf-namcache-rxnamecacheexpireentry.md) | RxNameCacheExpireEntry puts a NAME_CACHE entry on the free list for recycling. |
| [RxNameCacheInitialize function](nf-namcache-rxnamecacheinitialize.md) | RxNameCacheInitialize initializes a name cache (NAME_CACHE_CONTROL structure). |
| [RxNameCacheFetchEntry function](nf-namcache-rxnamecachefetchentry.md) | RxNameCacheFetchEntry looks for a match with a specified name string for a NAME_CACHE entry. |
| [RxNameCacheFreeEntry function](nf-namcache-rxnamecachefreeentry.md) | RxNameCacheFreeEntry releases the storage for a NAME_CACHE entry and decrements the count of the NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure. |
| [RxNameCacheCreateEntry function](nf-namcache-rxnamecachecreateentry.md) | RxNameCacheCreateEntry allocates and initializes a NAME_CACHE structure with the given name string. |
| [RxNameCacheCheckEntry function](nf-namcache-rxnamecachecheckentry.md) | RxNameCacheCheckEntry checks a name cache entry for validity. A valid entry means that the lifetime has not expired and the MRxContext parameter passes the equality check. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NAME_CACHE structure](ns-namcache--name-cache~r1.md) | TBD |
| [NAME_CACHE structure](ns-namcache--name-cache.md) | TBD |
| [MRX_NAME_CACHE_ structure](ns-namcache--mrx-name-cache-~r1.md) | TBD |
| [MRX_NAME_CACHE_ structure](ns-namcache--mrx-name-cache-.md) | TBD |
| [NAME_CACHE_CONTROL_ structure](ns-namcache--name-cache-control-.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RX_NC_CHECK_STATUS enumeration](ne-namcache--rx-nc-check-status.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
