---
UID : NA:prefix
ms.assetid : 40e93800-fca3-3d55-8a33-71ad08228385
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# prefix.h header



prefix.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [RxpAcquirePrefixTableLockExclusive](nf-prefix-rxpacquireprefixtablelockexclusive.md) | RxpAcquirePrefixTableLockExclusive acquires the prefix table lock exclusively. |
| [RxpAcquirePrefixTableLockShared](nf-prefix-rxpacquireprefixtablelockshared.md) | RxpAcquirePrefixTableLockShared acquires the prefix table lock shared. |
| [RxPrefixTableLookupName](nf-prefix-rxprefixtablelookupname.md) | RxPrefixTableLookupName looks up a name in a prefix table used to catalog SRV_CALL, NET_ROOT, and V_NET_ROOT names and converts the underlying pointer to a structure that contains the name. |
| [RxpReleasePrefixTableLock](nf-prefix-rxpreleaseprefixtablelock.md) | RxpReleasePrefixTableLock releases a previously acquired shared or exclusive prefix table lock. |